#!/usr/bin/env node
/**
 * seed-looks.ts — push docs/looks/looks.json into a Shopify store.
 *
 *   1. Ensures the `look` metaobject definition exists (pages at /looks/<handle>).
 *   2. Uploads each look's styled photo + runway cutout (+ the hero logo) to Files.
 *   3. Upserts one `look` metaobject per manifest entry (idempotent by handle).
 *
 * Runs on plain Node ≥ 22.18 (type-stripping, no build step):
 *   SHOPIFY_STORE=v0m0hb-x3 SHOPIFY_ADMIN_TOKEN=shpat_… node scripts/looks/seed-looks.ts
 *   … --only blue          substring filter on handle
 *   … --skip-files         reuse files already in the store (matched by filename)
 *   … --dry                print the plan, change nothing
 *
 * Token: Settings → Apps → Develop apps → create app → Admin API scopes
 *   write_metaobject_definitions, write_metaobjects, write_files, read_products
 * Docs: docs/looks.md
 */

import { readFile, stat } from "node:fs/promises";
import { basename, resolve } from "node:path";
import { fileURLToPath } from "node:url";

// ---------- types ----------
interface LookEntry {
  handle: string;
  title: string;
  caption: string;
  pieces: string[];
  goes_with: string[];
  featured: boolean;
  full_body?: boolean;
  sort: number;
  source: string;
  cutout: string;
}
interface Manifest {
  looks: LookEntry[];
  overrides?: Record<string, { full_body?: boolean }>;
  logo?: string;
}
interface StagedTarget {
  url: string;
  resourceUrl: string;
  parameters: { name: string; value: string }[];
}
interface UserError {
  field?: string[] | null;
  message: string;
}
interface GraphQLResponse<T> {
  data?: T;
  errors?: { message: string }[];
}

// ---------- config ----------
const ROOT = resolve(fileURLToPath(import.meta.url), "../../..");
const STORE = process.env.SHOPIFY_STORE;
const TOKEN = process.env.SHOPIFY_ADMIN_TOKEN;
const API = "2025-07";
const args = new Set(process.argv.slice(2));
const only = (() => {
  const i = process.argv.indexOf("--only");
  return i > -1 ? process.argv[i + 1] ?? "" : "";
})();
const DRY = args.has("--dry");
const SKIP_FILES = args.has("--skip-files");

if (!STORE || !TOKEN) {
  console.error("Set SHOPIFY_STORE (e.g. v0m0hb-x3) and SHOPIFY_ADMIN_TOKEN.");
  process.exit(1);
}

// ---------- graphql ----------
async function gql<T>(query: string, variables: Record<string, unknown> = {}): Promise<T> {
  const res = await fetch(`https://${STORE}.myshopify.com/admin/api/${API}/graphql.json`, {
    method: "POST",
    headers: { "Content-Type": "application/json", "X-Shopify-Access-Token": TOKEN as string },
    body: JSON.stringify({ query, variables }),
  });
  const json = (await res.json()) as GraphQLResponse<T>;
  if (json.errors?.length) throw new Error(json.errors.map((e) => e.message).join("; "));
  if (!json.data) throw new Error("empty response");
  return json.data;
}

function assertNoErrors(errors: UserError[] | undefined, ctx: string): void {
  if (errors && errors.length) throw new Error(`${ctx}: ${errors.map((e) => `${(e.field ?? []).join(".")} ${e.message}`).join(" | ")}`);
}

// ---------- 1. definition ----------
const DEFINITION = {
  name: "Look",
  type: "look",
  description: "A styled outfit for the home-page runway and its /looks/<handle> shop-this-look page. Created by the beau-bou theme (docs/looks.md).",
  displayNameKey: "title",
  access: { storefront: "PUBLIC_READ" },
  capabilities: {
    publishable: { enabled: true },
    onlineStore: { enabled: true, data: { urlHandle: "looks", createRedirects: true } },
    renderable: { enabled: true, data: { metaTitleKey: "title", metaDescriptionKey: "caption" } },
  },
  fieldDefinitions: [
    { key: "title", name: "Title", type: "single_line_text_field", required: true },
    { key: "image", name: "Styled photo", type: "file_reference", description: "The original photo of the outfit on a person or mannequin.", validations: [{ name: "file_type_options", value: '["Image"]' }] },
    { key: "cutout", name: "Runway cutout", type: "file_reference", description: "Background-removed version for the home-page runway (scripts/cutouts.py).", validations: [{ name: "file_type_options", value: '["Image"]' }] },
    { key: "video", name: "Video (optional)", type: "file_reference", description: "Try-on clip. Plays on the look page instead of the photo.", validations: [{ name: "file_type_options", value: '["Video"]' }] },
    { key: "caption", name: "Caption", type: "multi_line_text_field", description: "Michele's note about the look — sizes worn, occasion, styling tip." },
    { key: "pieces", name: "Pieces in the look", type: "list.product_reference", description: "Every product being worn." },
    { key: "goes_with", name: "Goes with it", type: "list.product_reference", description: "Pieces that pair with the outfit but aren't in the photo." },
    { key: "featured", name: "Show on home-page runway", type: "boolean", capabilities: { adminFilterable: { enabled: true } } },
    { key: "full_body", name: "Full-body cutout", type: "boolean", description: "Off for waist-up shots (the runway can skip them).", capabilities: { adminFilterable: { enabled: true } } },
    { key: "sort", name: "Sort order", type: "number_integer", description: "Lower numbers first on the runway." },
  ],
};

async function ensureDefinition(): Promise<void> {
  const existing = await gql<{ metaobjectDefinitionByType: { id: string } | null }>(
    `{ metaobjectDefinitionByType(type: "look") { id } }`,
  );
  if (existing.metaobjectDefinitionByType) {
    console.log("✔ look definition exists", existing.metaobjectDefinitionByType.id);
    return;
  }
  if (DRY) return void console.log("· would create look definition");
  const r = await gql<{ metaobjectDefinitionCreate: { metaobjectDefinition: { id: string } | null; userErrors: UserError[] } }>(
    `mutation($definition: MetaobjectDefinitionCreateInput!) { metaobjectDefinitionCreate(definition: $definition) { metaobjectDefinition { id } userErrors { field message } } }`,
    { definition: DEFINITION },
  );
  assertNoErrors(r.metaobjectDefinitionCreate.userErrors, "definition");
  console.log("✔ created look definition", r.metaobjectDefinitionCreate.metaobjectDefinition?.id);
}

// ---------- 2. files ----------
async function existingFileIds(filenames: string[]): Promise<Map<string, string>> {
  const map = new Map<string, string>();
  for (const name of filenames) {
    const stem = name.replace(/\.[a-z0-9]+$/i, "");
    const r = await gql<{ files: { nodes: { id: string; image?: { url: string } | null }[] } }>(
      `query($q: String!) { files(first: 5, query: $q) { nodes { id ... on MediaImage { image { url } } } } }`,
      { q: `filename:${stem}` },
    );
    const hit = r.files.nodes.find((n) => n.image?.url.includes(`/${stem}.`) || n.image?.url.includes(`/${stem}_`));
    if (hit) map.set(name, hit.id);
  }
  return map;
}

async function uploadFiles(paths: string[]): Promise<Map<string, string>> {
  const byName = new Map<string, string>();
  if (!paths.length) return byName;
  const input = await Promise.all(
    paths.map(async (p) => ({
      filename: basename(p),
      mimeType: "image/webp",
      resource: "FILE",
      httpMethod: "POST",
      fileSize: String((await stat(p)).size),
    })),
  );
  const staged = await gql<{ stagedUploadsCreate: { stagedTargets: StagedTarget[]; userErrors: UserError[] } }>(
    `mutation($input: [StagedUploadInput!]!) { stagedUploadsCreate(input: $input) { stagedTargets { url resourceUrl parameters { name value } } userErrors { field message } } }`,
    { input },
  );
  assertNoErrors(staged.stagedUploadsCreate.userErrors, "stagedUploadsCreate");

  const targets = staged.stagedUploadsCreate.stagedTargets;
  for (const [i, target] of targets.entries()) {
    const form = new FormData();
    for (const p of target.parameters) form.append(p.name, p.value);
    form.append("file", new Blob([await readFile(paths[i])], { type: "image/webp" }), basename(paths[i]));
    const res = await fetch(target.url, { method: "POST", body: form });
    if (!res.ok) throw new Error(`upload ${basename(paths[i])} → ${res.status}`);
  }

  const created = await gql<{ fileCreate: { files: { id: string }[]; userErrors: UserError[] } }>(
    `mutation($files: [FileCreateInput!]!) { fileCreate(files: $files) { files { id } userErrors { field message } } }`,
    {
      files: targets.map((t, i) => ({
        originalSource: t.resourceUrl,
        contentType: "IMAGE",
        filename: basename(paths[i]),
        alt: basename(paths[i]).replace(/^beyoutiful-/, "").replace(/\.webp$/, "").replace(/-/g, " "),
        duplicateResolutionMode: "REPLACE",
      })),
    },
  );
  assertNoErrors(created.fileCreate.userErrors, "fileCreate");
  created.fileCreate.files.forEach((f, i) => byName.set(basename(paths[i]), f.id));
  console.log(`✔ uploaded ${byName.size} files`);
  return byName;
}

// ---------- 3. products by handle ----------
async function productIds(handles: string[]): Promise<Map<string, string>> {
  const map = new Map<string, string>();
  for (const h of new Set(handles)) {
    const r = await gql<{ productByHandle: { id: string } | null }>(`query($h: String!) { productByHandle(handle: $h) { id } }`, { h });
    if (r.productByHandle) map.set(h, r.productByHandle.id);
    else console.warn(`  ! product not found: ${h}`);
  }
  return map;
}

// ---------- 4. upsert looks ----------
async function upsertLook(look: LookEntry, files: Map<string, string>, products: Map<string, string>): Promise<void> {
  const fullBody = look.full_body ?? true;
  const fields: { key: string; value: string }[] = [
    { key: "title", value: look.title },
    { key: "caption", value: look.caption ?? "" },
    { key: "featured", value: String(look.featured) },
    { key: "full_body", value: String(fullBody) },
    { key: "sort", value: String(look.sort) },
    { key: "pieces", value: JSON.stringify(look.pieces.map((h) => products.get(h)).filter(Boolean)) },
    { key: "goes_with", value: JSON.stringify(look.goes_with.map((h) => products.get(h)).filter(Boolean)) },
  ];
  const img = files.get(basename(look.source));
  const cut = files.get(basename(look.cutout));
  if (img) fields.push({ key: "image", value: img });
  if (cut) fields.push({ key: "cutout", value: cut });

  if (DRY) return void console.log(`· would upsert look/${look.handle} (${fields.length} fields)`);
  const r = await gql<{ metaobjectUpsert: { metaobject: { id: string; handle: string } | null; userErrors: UserError[] } }>(
    `mutation($handle: MetaobjectHandleInput!, $metaobject: MetaobjectUpsertInput!) { metaobjectUpsert(handle: $handle, metaobject: $metaobject) { metaobject { id handle } userErrors { field message } } }`,
    {
      handle: { type: "look", handle: look.handle },
      metaobject: { fields, capabilities: { publishable: { status: "ACTIVE" } } },
    },
  );
  assertNoErrors(r.metaobjectUpsert.userErrors, `look/${look.handle}`);
  console.log(`✔ /looks/${r.metaobjectUpsert.metaobject?.handle}`);
}

// ---------- main ----------
async function main(): Promise<void> {
  const manifest = JSON.parse(await readFile(resolve(ROOT, "docs/looks/looks.json"), "utf8")) as Manifest;
  const looks = manifest.looks.filter((l) => l.handle.includes(only));
  console.log(`${looks.length} looks → ${STORE}${DRY ? " (dry run)" : ""}`);

  await ensureDefinition();

  const wanted = [
    ...looks.flatMap((l) => [resolve(ROOT, l.source), resolve(ROOT, l.cutout)]),
    ...(manifest.logo ? [resolve(ROOT, manifest.logo)] : []),
  ];
  let files = new Map<string, string>();
  if (SKIP_FILES) {
    files = await existingFileIds(wanted.map((p) => basename(p)));
    console.log(`✔ matched ${files.size}/${wanted.length} existing files`);
  } else if (!DRY) {
    files = await uploadFiles(wanted);
  }

  const products = await productIds(looks.flatMap((l) => [...l.pieces, ...l.goes_with]));
  for (const look of looks) await upsertLook(look, files, products);
  console.log("done · open the theme editor → Hero runway reads these automatically");
}

main().catch((e: unknown) => {
  console.error(e instanceof Error ? e.message : e);
  process.exit(1);
});
