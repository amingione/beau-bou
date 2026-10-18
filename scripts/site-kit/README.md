# Be-YOU-tiful Boutique — complete site kit

A Shopify **theme zip holds only the design** (templates, sections, styles, scripts and a few bundled photos).
Photos you pick in the theme editor live in the store's **Files**, and products, looks, pages and menus are store
data — so they ship separately in this kit. Follow the steps in order on the new store.

| In this kit | What it is |
|---|---|
| `1-theme/Be-YOU-tiful-Boutique-theme.zip` | The theme. **Online Store → Themes → Add theme → Upload zip file** |
| `2-store-files/` | Every photo/logo the theme points to (hero, category tiles, visit-our-store, logos, favicon, look photos). **Content → Files → Upload files** — select them all. Keep the filenames exactly as they are; the theme finds them by name. |
| `4-looks/looks.json` | Shop Styles looks (title, photo, pieces). Create them under **Content → Metaobjects → Look**, or run `scripts/looks/seed-looks.ts` from the repo with an Admin API token. |
| `5-policies/` | Refund, shipping, terms and contact text for **Settings → Policies** |

## Install order
1. **Upload the store files first** (step 2), then the theme (step 1) — the homepage photos appear as soon as both are in.
2. Import products (step 3). The CSV pulls each product photo from its URL during import.
3. Create collections the homepage uses (automated, by product type): New Arrivals, Dresses, Tops, Bottoms, Jackets, Swimsuits, Jewelry + Accessories, Handbags, Baby & Toddler, Kids, Sale, Clearance. Handles must match (`dresses`, `tops`, …).
4. Pages: About, Contact, Visit Us, Questions, Size Guide, Shop the Look — create each and choose the template with the same name (Online Store → Pages → Theme template).
5. Menus: Navigation → Main menu (Home, Shop All ▸ categories, Shop Brands, New Arrivals, Clearance, Visit Us ▸ Contact).
6. Looks (step 4). Until you add any, the Shop Styles grid shows four bundled sample looks.
7. Theme editor → check header logo, favicon and the homepage; re-pick any image that shows as empty.

## Notes
- The 18 `TEST —` products were archived on 2026-10-18 and are no longer in the kit; import Michele's real inventory instead.
- **Images only:** `bash scripts/site-kit/build-image-export.sh "<folder>"` downloads every image the site uses, sorted into Files / collection images / Looks, with upload steps (`scripts/site-kit/IMAGE-EXPORT.md`).
- Rebuild this kit any time from the repo: `bash scripts/build-site-kit.sh` (output: `dist/`).
