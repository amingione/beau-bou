# Looks — fashion runway + shop-this-look pages

Last updated: 2026-09-21

## Current revision — 2026-09-21

[VERIFIED] Amber rejected the first rendered runway: the standalone cutouts, oversized empty stage, and peacock stacked above the outfits did not meet the intended feature quality. Do not restore that presentation or describe it as approved based on the earlier concept approval.

[OBSERVED] A newer client source set exists at `~/LocalStorm/Work/Be-YOU-tiful Boutique/beyoutiful-try-ons/`. Selected portrait sources are 1536×2048, substantially better than the old 414px thumbnails. Original files remain untouched. The theme uses four 900px WebP deployment assets (`assets/beyoutiful-runway-*.webp`), sourced from try-on-01 (orange floral dress), try-on-03 (navy/white maxi), try-on-08 (blue blouse), and try-on-02 (blue/green dress).

[TESTING] The revised draft uses framed photographs around a compact central peacock/title, content-sized section height, and container-responsive columns. The peacock stays between the photo panels even in the Shopify sidebar preview and on phones. Compact previous/play-pause/next controls replace the oversized text button; previous/next stops autoplay so the selected photos remain stable. Verified in the Shopify draft at 390px, 780px, and 1440px: three columns, no horizontal overflow, both active photos loaded at 900px source width. Previous/next changed both panels and updated the counter; keyboard Enter worked. Console showed only the Shopify custom-pixel sandbox warning. The new layout still awaits Amber's visual acceptance. Existing Contact fallbacks remain until published look entries and product associations are available.

## Approved runway placement — 2026-09-21

[SUPERSEDED — rendered execution rejected; placement remains valid] Amber approved the concept of a separate fashion-show section directly beneath the existing cover hero, with different outfit slideshows left/right and a stationary standalone holographic peacock in the center. Ivory ground with a lavender sheen, five-second synchronized transitions, and soft floor shadows. On phones the peacock sits above the two outfit panels. This supersedes the earlier choice to use the runway itself as the homepage hero.

[VERIFIED] The saved Shopify draft homepage was pulled before editing; its cover hero and other sections were preserved. The new `runway` instance reuses `hero-looks`; its editor label is **Fashion runway**. A Presentation setting retains the older dark editorial appearance as an option. Source photos are unchanged. The selected cutouts and peacock have deployment copies in theme assets so the section works before the Files/metaobject import. Image pickers override bundled cutouts.

[VERIFIED] Pause/play applies to both sides. Reduced motion starts paused; manual pause survives tab/hover changes. Keyboard focus on an outfit stops rotation. Inactive outfits cannot receive focus, and removing the section in the theme editor cleans up its timer and listeners.

[VERIFIED] Draft verification on 2026-09-21: desktop three-column runway and Shopify phone preview rendered with all three images. Play/Pause and synchronized outfit changes were exercised. New-store `/looks/<handle>` links returned 404 because the look entries are not published there yet; manual cards now resolve a published metaobject URL when present and otherwise link to Contact labeled **Ask about this look**. This is the current empty-content state, not a completed shoppable catalog. Michele still supplies product associations and pricing.

[VERIFIED] Final checks: Shopify theme check passed (zero errors, nine existing warnings); JavaScript syntax and seven motion/lifecycle cases passed. Desktop and phone screenshots showed no clipping. The fallback outfit link opened the Contact form. Chrome console showed Shopify preview preload/custom-pixel warnings and analytics collection failure, with no runway-script error observed. Browser-extension calls timed out, so visual QA used the native Chrome surface through CUA. Draft theme ID: `192212107628`; not published.

### Change log
- 2026-09-21: recorded rejection of the cutout stage and rebuilt the draft with higher-resolution framed portraits, compact controls, and columns based on component width. Pending visual acceptance.
- 2026-09-21: recorded Amber's approved below-hero runway design, preserved the saved cover hero, added playback/accessibility support and safe unpublished-look links.

## Earlier implementation reference

The description below records the earlier hero layout; the approved placement and controls above take precedence.

The home-page hero is the silver-blue holographic logo center stage with an outfit slideshow either
side. Both sides crossfade to their next outfit **on the same beat** (5s default) while showing
different looks; no controls, no indicators, no copy. Every outfit is a **Look**: a Shopify
metaobject with its own page at `/looks/<handle>` laid out like LTK / LikeToKnowIt — photo left,
"Shop this look" pieces right, "Goes with it" pieces below, more looks at the bottom.

Michele never touches code: **Content → Metaobjects → Look → Add entry** and it appears in the
slideshow and gets a page.

```
docs/images/photos-in/tops:bottoms:outfitStyles/*.webp     styled photos (Facebook/Google/phone)
        │  scripts/cutouts.py  (rembg → trim → 3:4 canvas → ground shadow)
        ▼
docs/images/photos-in/looks/*-cutout.webp                   transparent runway cutouts
docs/looks/looks.json                                       manifest: title, caption, pieces, featured, sort
        │  scripts/looks/seed-looks.ts  (definition → Files → metaobjects)
        ▼
Shopify  ─ Content › Metaobjects › Look  ─▶  sections/hero-looks.liquid    (home page)
                                          ─▶  templates/metaobject/look.json → sections/main-look.liquid  (/looks/<handle>)
```

## Files

| File | Role |
| --- | --- |
| `sections/hero-looks.liquid` | Hero: logo center (optional link, optional single button — blank by default), left + right slideshow stages. Settings: look source, full-body only, max looks, seconds per look, transition (crossfade / slide), transition length, outfit height, floor line, pause on hover, captions. Manual `look` blocks are the fallback when no metaobjects exist. |
| `snippets/hero-looks-stage.liquid` | One side. Splits looks odd/even across the two sides and stacks them as slides; slide 1 is visible before JS runs. |
| `assets/hero-looks.js` | One ticker per section advances **every** stage at the same instant → left and right stay in sync. Pauses on hover/focus and hidden tab; preloads the next image; re-inits on theme-editor section load. |
| `snippets/look-card.liquid` + `assets/component-look-card.css` | One clickable cutout: figure, soft floor, hover caption "Shop the look / Title". Whole card is the link. Shared with the look page's "More looks" grid. |
| `assets/section-hero-looks.css` | Layout (mobile: logo top, stages side by side), crossfade with a settle-in scale, slide variant, `prefers-reduced-motion` → plain fade. |
| `templates/metaobject/look.json` | Page template for the `look` metaobject type. |
| `sections/main-look.liquid` + `assets/section-main-look.css` | The look page: sticky photo/video, badge, byline, caption, share (Facebook / Pinterest / Text / Copy link), pieces grid with quick-add, goes-with grid, "Shop all" CTA, empty-state "Ask about this look", "More looks" runway. |
| `scripts/cutouts.py` | Background removal + runway prep. Re-runnable; skips outputs newer than their source. |
| `scripts/looks/seed-looks.ts` | Store setup + sync from the manifest. Idempotent (upsert by handle). |
| `docs/looks/looks.json` | The manifest. Hand-edit titles, captions, `pieces`/`goes_with` (product handles), `featured`, `sort`, and `overrides` for the full-body heuristic. |

## Look metaobject (`type: look`)

| Key | Type | Notes |
| --- | --- | --- |
| `title` | single line | Display name; also the SEO title |
| `image` | file (image) | The styled photo — shown on the look page |
| `cutout` | file (image) | Transparent runway cutout — shown in the hero. Falls back to `image` |
| `video` | file (video) | Optional try-on clip; replaces the photo on the look page |
| `caption` | multi line | Michele's note (sizes worn, occasion); also the SEO description |
| `pieces` | list of products | "Shop this look" |
| `goes_with` | list of products | "Goes with it" — pairs well, not in the photo |
| `featured` | boolean | Off = hidden from the runway (page still live) |
| `full_body` | boolean | Off for waist-up cutouts; hero setting "Full-body looks only" honours it |
| `sort` | integer | Lower first (the rails read entries in the order Shopify returns them; keep `sort` for future ordering) |

Capabilities: publishable, Online Store pages under `/looks`, renderable (SEO from `title`/`caption`),
storefront `PUBLIC_READ`. Theme reads it as `shop.metaobjects.look.values` and `metaobject` on the page.

## Workflow

```zsh
bb-cutouts              # python3 scripts/cutouts.py        — new photos → cutouts + manifest rows
bb-cutouts --force      # redo all (after editing overrides)
bb-looks-seed           # node scripts/looks/seed-looks.ts  — needs SHOPIFY_STORE + SHOPIFY_ADMIN_TOKEN
bb-looks-seed --dry     # print the plan
bb-looks-seed --skip-files   # metaobjects only, reuse files already in the store
```

1. Drop styled photos into `docs/images/photos-in/tops:bottoms:outfitStyles/` (named `beyoutiful-<what-she-is-wearing>.webp`).
2. `bb-cutouts`. Check `docs/images/photos-in/looks/`. If the heuristic got full-body vs waist-up wrong, add the handle to `overrides` in the manifest and re-run with `--force`.
3. Edit `docs/looks/looks.json`: titles, captions, product handles for `pieces` / `goes_with`.
4. `bb-looks-seed` against the target store (token from a custom app with `write_metaobject_definitions, write_metaobjects, write_files, read_products`). Or do the same three steps through the Shopify MCP — the mutations are the ones in the script.
5. Theme editor → Home → **Hero looks**: logo = `beyoutiful-logo-holographic-silver-blue.webp`, source = automatic.

### Photo quality
The Facebook thumbnails are 414×414. The cutout pipeline upsamples 2× before segmenting, which holds
up at the default 46vh card height but goes soft on retina. When Michele sends originals, drop them in
under the same names and run `bb-cutouts --force`; nothing else changes.

### Waist-up shots
Detected by how wide the subject is along its bottom edge (feet are narrow, a cropped torso is wide).
Waist-up cutouts get a soft fade at the crop line instead of a ground shadow and `full_body: false`.
Manual corrections live in `overrides`.

## Design notes
- **Full bleed (2026-09-20):** the hero runs edge to edge under the header with a dark photographic backdrop (setting *Background photo*, *Darken* 65%, *Blur*, *Focal point*, *Minimum height* 80vh) — styled after a moody editorial hero. With no photo it falls back to a deep-plum iridescent gradient. Scheme-4 (midnight plum) so captions/floor read light. Current backdrop `beyoutiful-hero-backdrop-mannequins.webp` is a 414px display shot upsampled + blurred 6px — a placeholder until Michele sends a hi-res in-store shot (2400px+ wide, moody, no logo in frame).
- Logo: `Be-YOU-tiful Boutique Logo Holographic Redesign-2.png` (silver-blue lockup, 1394×922) → `docs/images/photos-in/01_Logo-holo/beyoutiful-logo-holographic-silver-blue.webp` (trimmed, lossless). The rainbow version was judged too busy; it stays in `01_Logo-holo/` if Michele wants to compare.
- Hero is logo-only — no tagline, accent line, or hint. A single button setting exists and is blank.
- Sync: one `setInterval` per section calls `advance()` on all stages; each stage keeps its own index, so sides never show the same outfit at the same time (odd looks left, even looks right).
- Mobile: logo on top, the two stages side by side underneath at 60% height, still in sync.
- The runway/marquee v1 (`hero-runway`) is parked in `_to_delete/hero-runway-v1/` — delete once v3 is approved.

## Palette (2026-09-20 — "soft iridescent pastels")
No stark white, no green. `config/settings_data.json` color schemes: **scheme-1** ivory `#FBF8F5` · **scheme-2** blush-lavender mist `#F3EDF3` · **scheme-3** lavender `#DCD4EC` (was peacock green) · **scheme-4** midnight plum `#2E2A33` · **scheme-5** blush `#F5E4EA`. Text everywhere charcoal-plum `#2E2A33`; primary buttons dusty lavender `#6E5F86`. Tokens in `assets/beau-bou.css`: `--bb-ink`, `--bb-accent` (replaced every hard-coded `#0f5f66`), `--bb-hairline` (soft plum), `--bb-holo` (iridescent gradient, for ribbons/accents).
- The pre-existing **Shop the Look (live)** page (`page.shop-the-look`) is the live-stream/try-on version and stays as is; look pages are the evergreen per-outfit version. They can cross-link: put the live page in the hero CTA when a stream is scheduled.
