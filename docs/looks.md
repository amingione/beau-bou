# Looks — hero slideshows + shop-this-look pages

Last updated: 2026-11-02

## Michele's owner store — new looks, 2026-11-02

The active owner store is `xapm2f-fr` (theme `157452402844`). Amber supplied 35 outfit photos under
`~/LocalStorm/Workspace/In Progress/Be-YOU-tiful Boutique/photos-in/looks-haul/Final Images/`.
Seven clear outfit presentations use one full-length hero each; the other angles remain in the source
folder for product identification. The 13 previous Look entries are **Draft** and their Files are
retained for recovery. The seven entries below are **Active**. The homepage retains its Facebook
reel after the outfit photos; the old tropical Extra photo block was removed from Shop Styles.

| Active Look handle | Hero source within `Final Images/` | Visible pieces and exact catalog matches |
| --- | --- | --- |
| `white-top-black-drawstring-pants` | `black pants-white shirt/IMG_7763.jpeg` | Fitted white seamed top; black wide-leg drawstring pants; black double-buckle sandals; **Cork Sling Bag** in alternate views (`gid://shopify/Product/9321226371228`, Draft). The top, pants, and sandals have no confirmed catalog match. |
| `embroidered-bird-kimono-black-pants` | `black pants-white shirt/IMG_7767.JPG` | Black fringed kimono with floral embroidery and a blue bird on the back; the same white top and black pants; black sandals. No confirmed catalog match. The catalog's `Denim Flower Jacket: Black` is a different garment. |
| `heart-tee-rivir-stud-jeans` | `blue jeans w jewels-white heart shirt/IMG_7754.JPG` | White tee with a pink heart; **Rivir Stud Jeans** (`gid://shopify/Product/9298882953372`, Draft); blue wedge sandals and blue accessories. The tee, sandals, and accessories have no confirmed catalog match. |
| `colorful-pants-duo` | `colorful pants-duo/IMG_7789.JPG` | Left: cropped white floral-embroidered jacket, peach pants, blue sandals. Right: longer white zip jacket with colorful patches, aqua pants, pink sandals. None has a confirmed catalog match. |
| `jellyfish-print-off-shoulder-dress` | `jellyfish dress/IMG_7784.JPG` | White off-shoulder jellyfish-print dress and tan wedge sandals. Neither has a confirmed catalog match. |
| `blue-white-floral-palazzo-pants-duo` | `blue floral pants - white shirt/IMG_7778.JPG` | Both women wear **Blue/White Plazzo Pant** (`gid://shopify/Product/9298888392860`, Draft). One wears a loose white flutter-sleeve top; the other a fitted side-ruched white top. Neither top or the jewelry has a confirmed catalog match. |
| `pink-top-floral-tulle-skirt` | `floral skirt-pink shirt/IMG_7770.JPG` | Dusty-pink glitter-dot side-tie top, layered pastel floral tulle skirt, floral wedges, pink earrings. None has a confirmed catalog match. |

The three confirmed product associations are stored in the Looks' `pieces` fields. All three products
are Draft, have no Online Store publication date or URL, and are **not yet purchasable**. The theme
counts and renders only published product references, so visitors see the photo, a description of
the pieces, and an availability inquiry. When products are activated and published, their cards can
appear without rematching the Look. Do not link visually similar catalog garments as substitutes.

The live Look definition has `title`, `image`, `pieces`, `goes_with`, `caption`, and `video` only. Its
Online Store URL is `/pages/look/<handle>`; use `look.system.url` in Liquid. The older test-store
seed manifest and instructions below are historical and must not be run against the owner store.

## New pieces — 2026-10-18 (later)

From `photos-in/new peices` (Amber's edits, boutique-background versions): 6 more Active Looks:
`abstract-print-jacket-navy-maxi`, `cutwork-jeans`, `orange-pink-printed-maxi`,
`pink-print-tee-charcoal-pants`, `red-ruffle-top-jeans`, `red-ruffle-top-white-lace-pants`
(files `beyoutiful-tryon-*.webp`). Highlights now shows up to 14 looks
(`scripts/declutter/apply-new-pieces-2026-10-18.py`). The baby books photo is the Baby & Toddler collection
image (`beyoutiful-category-baby-toddler.webp`). The product-only shots (lace pants on hangers, puzzle,
sandals) and the studio versions stay in the folder for the real products.

## Try-on photos swapped — 2026-10-18

Amber didn't want the old runway cutouts or raw selfie try-ons on the site. Her polished try-ons
(`photos-in/looks-haul`: blurred background, 9:16) replace them.

- **Store (test store `v0m0hb-x3`):** 7 new Look entries, each with its own image, all **Active**:
  `abstract-print-moto-jacket`, `black-floral-ruched-maxi`, `striped-patchwork-tank-dress`,
  `navy-botanical-jumpsuit`, `tropical-bell-sleeve-dress`, `coral-puff-sleeve-mini`, `white-lace-fit-flare`.
  Files are `beyoutiful-tryon-*.webp` in Content → Files, with alt text. The 4 older Looks
  (`orange-floral-dress`, `navy-white-maxi`, `blue-ruffle-blouse`, `blue-green-dress`) are set to
  **Draft**: hidden, not deleted.
- **Theme:** Highlights' Extra photo blocks (6 raw `try-on-*.jpg`) are replaced by one: the second fit of
  the tropical dress (`…-shift-dress-b.webp`), linking to that dress's look page. Run
  `python3 scripts/declutter/apply-tryons-2026-10-18.py` to re-apply.
- **Not linked yet:** the new Looks have no **Pieces** or **Goes with** products, because the real
  products aren't in the store. Until they are, each look page shows the template's empty state:
  "We Sold Out! / When it's gone, it's GONE!" with the "Limited Summer Collection" badge. Amber chose to keep
  that wording (2026-10-18).
  Link the pieces under Content → Metaobjects → Look once the products exist.

## Shop Styles grid + pop-up — 2026-09-28

Amber picked **Option D** from the design canvas: keep the live header and hero, and replace the homepage runway slideshow with a LIKEtoKNOW.it-style grid.

| Piece | File |
| --- | --- |
| Section (grid, filters, `<dialog>`) | `sections/shop-styles.liquid` |
| Opened look ("post") | `snippets/shop-styles-post.liquid` |
| Behavior | `assets/shop-styles.js` (`<shop-styles>` custom element) |
| Styles | `assets/section-shop-styles.css` |
| Homepage wiring | `templates/index.json` → `shop_styles` (replaces `runway`) |

**How it works**
- Grid = every `look` metaobject with a photo or video (skips `featured = false`), masonry columns like the LTK feed. Tiles show a ▶ + "Try-on video" chip when the look has a **Video**, and "N pieces" when **Pieces** are linked.
- Click a tile → pop-up with the photo/video left and **Shop the pic** right: each piece has price, a size/option picker when it has variants, and a + button; "Add all N to cart" adds every available piece. Adds go through `/cart/add.js` and refresh Dawn's cart drawer (falls back to `/cart`).
- Prev/next arrows (and ← → keys) move between looks; Esc or the backdrop closes; video pauses on close; focus returns to the tile.
- **The look page stays.** Each tile is a real link to `/pages/looks/<handle>` (no JS, or ⌘/Ctrl-click, opens it), and the pop-up has a "View full look page" link.
- Looks with no pieces show the "Ask about this look" message/button (section settings).
- Filter pills (All / Try-on videos / Photos) appear once any look has a video.

**Adding a try-on video:** Content → Metaobjects → Look → entry → **Video (optional)** (field already in the definition). The Styled photo is used as the grid poster; without one, Shopify's video preview frame is used.

The old `hero-looks` section is untouched and still available in the theme editor if the runway is ever wanted back.

## Current revision — 2026-09-21

### Complete outfit breakdown — September 21

**Owner clarification:** A Look represents multiple individually shoppable items being shown off, not just the main garment with unrelated recommendations. Every featured item belongs in `Pieces`; `Goes with` is optional styling outside the photo. The owner curates these associations in Content → Metaobjects → Look; the template does not automatically recognize products in images.

The test catalog now contains 18 products / 55 variants. Six additions are tagged `outfit-piece` plus `test-product`, `sample`, `new`. The existing CSV was extended and imported with overwrite disabled, preserving the original twelve products. Active products publish to Online Store only; the boutique theme remains unpublished.

| Look | Pieces (individual prices and cart controls) |
| --- | --- |
| `blue-ruffle-blouse` | Coastal Blue Ruffle Blouse $42; Aqua & White Beaded Necklace $22; Medium Wash Straight-Leg Jeans $48; Textured Gold-Tone Stud Earrings $18 |
| `navy-white-maxi` | Harbor Bloom Maxi Dress $72; Delicate Gold-Tone Bracelet $16; Fine Gold-Tone Chain Necklace $18 |
| `orange-floral-dress` | Orange Blossom Midi Dress $64; Delicate Gold-Tone Bracelet $16; White Strappy Flat Sandals $38 |
| `blue-green-dress` | Palm Garden Printed Dress $58; Delicate Gold-Tone Bracelet $16; White Strappy Flat Sandals $38 |

The accessory images are explicitly generated **test illustrations**, inspired by the visible pieces rather than verified matches to retail inventory. No handbag is being carried in these four photos; the floral crossbody remains a separate recommendation. Do not present the generated shoes or jewelry as authenticated product photography. Michele must replace samples, pictures and associations before launch.

Generated with built-in image generation and saved locally in `docs/images/placeholders/`: `test-sandals.png`, `test-jeans.png`, `test-beaded-necklace.png`, `test-fine-chain-necklace.png`, `test-bracelet.png`, `test-earrings.png`. Originals remain untouched. These six PNGs were uploaded to the test store (`v0m0hb-x3`) Files and referenced in `docs/store/client-test-products.csv`.

Prompt set: one isolated square product on a white studio background, centered with generous margin and subtle shadow, no text/logo/person/collage; preserve the visible reference styling as closely as possible, for a clearly fictional Shopify test catalog. Specific targets: white flat multi-strap sandals from the blue-green dress photo (not wedges); medium-wash jeans from the blue blouse photo (unseen lower legs interpreted as straight-leg and disclosed); aqua/white necklace and small gold-tone textured studs from the blue blouse photo; fine plain chain necklace and delicate phone-wrist bracelet from the navy maxi photo. No claims about metal purity, materials or exact retail specifications.

The template now displays the number of pieces and keeps isolated accessory images fully visible. Theme Check passed: zero errors, eleven existing unrelated warnings. Only the main Look section and its stylesheet were uploaded to draft `192212107628`. Fresh storefront verification showed four pieces on the blue look and three on each dress look. All new product images loaded. The aqua necklace added independently at $22 and was removed after the test; sandal sizes 6–10 and jeans sizes S–XL appeared in quick-shop. Phone viewport measured 487 CSS pixels under the browser’s current scaling, matching document width with no overflow; desktop was also inspected. No captured console errors. Temporary viewport reset.

### Product cards and sharing controls — September 21

Amber requested shoppable items with prices instead of the empty inquiry box, and icons instead of text sharing links. A fresh navy Look render confirmed the linked Harbor Bloom dress at $72 with size selection and cart controls; the older screenshot showed the pre-import empty state. Verified size S / Navy / White adds at $72, then removed the test cart item. All four looks use their linked test catalog products.

Sharing now uses the theme’s Facebook, Pinterest, message and copy SVGs in 44px controls, with accessible names, tooltips and visible keyboard focus. Copy shows a checkmark and announces success without replacing the icon markup. Only `sections/main-look.liquid` and `assets/section-main-look.css` were uploaded to the unpublished boutique theme. Theme Check passed with zero errors and eleven existing unrelated warnings. Desktop and 390px phone previews verified four 44px icon controls, working copy/checkmark feedback, and no horizontal overflow; no captured console errors.

### Shop the Look routing — verified September 21

The new store now has a `look` metaobject definition with Title, Image, Pieces (product list), Caption, and Goes with (product list). Entries are Active with web pages enabled. Four entries match the current slideshow: `orange-floral-dress`, `navy-white-maxi`, `blue-ruffle-blouse`, and `blue-green-dress`. Their canonical routes are `/pages/looks/<handle>`; always render `look.system.url` rather than guessing routes.

The existing page (ID `712517419372`) is now Visible at `/pages/shop-the-look`; its original body content is preserved. The draft's default page section recognizes that handle and renders `snippets/look-gallery.liquid`, so the gallery works before the boutique theme becomes live. `page.shop-the-look.json` uses that same section. The live-video `shop-the-look` section remains available separately.

Each slideshow card opens its own Look template, not Contact. The homepage banner opens the four-look gallery. Breadcrumbs and More looks link between them. The four original WebP photos are also in Shopify Files and attached to the entries. Michele adds actual catalog products to **Content → Metaobjects → Look → [outfit] → Pieces** and optional **Goes with**. Amber subsequently authorized twelve fictional test products on September 21; all four entries now have matching Pieces and complementary Goes with products. See [handoff.md](handoff.md#test-catalog--september-21-2026) and [the import CSV](store/client-test-products.csv). Replace the test references before launch. When no pieces are linked, the detail template shows the outfit photo and an availability inquiry.

Verified by clicking all four slideshow cards and the homepage banner in draft `192212107628`; desktop and 390px detail/gallery render with loaded images and no horizontal overflow. Theme check: zero errors, eleven warnings in unrelated existing files. Browser console: only Shopify's custom-pixel sandbox warning. Theme remains unpublished. This supersedes the Contact fallback described in the earlier revision notes below.


[VERIFIED] Amber rejected the first rendered runway: the standalone cutouts, oversized empty stage, and peacock stacked above the outfits did not meet the intended feature quality. Do not restore that presentation or describe it as approved based on the earlier concept approval.

[OBSERVED] A newer client source set exists at `~/LocalStorm/Work/Be-YOU-tiful Boutique/beyoutiful-try-ons/`. Selected portrait sources are 1536×2048, substantially better than the old 414px thumbnails. Original files remain untouched. The theme uses four 900px WebP deployment assets (`assets/beyoutiful-runway-*.webp`), sourced from try-on-01 (orange floral dress), try-on-03 (navy/white maxi), try-on-08 (blue blouse), and try-on-02 (blue/green dress).

[TESTING] The revised draft uses framed photographs around a compact central peacock/title, content-sized section height, and container-responsive columns. The peacock stays between the photo panels even in the Shopify sidebar preview and on phones. Compact previous/play-pause/next controls replace the oversized text button; previous/next stops autoplay so the selected photos remain stable. Verified in the Shopify draft at 390px, 780px, and 1440px: three columns, no horizontal overflow, both active photos loaded at 900px source width. Previous/next changed both panels and updated the counter; keyboard Enter worked. Console showed only the Shopify custom-pixel sandbox warning. The new layout still awaits Amber's visual acceptance. Contact fallbacks were replaced by the individual Look pages described above.

## Approved runway placement — 2026-09-21

[SUPERSEDED — rendered execution rejected; placement remains valid] Amber approved the concept of a separate fashion-show section directly beneath the existing cover hero, with different outfit slideshows left/right and a stationary standalone holographic peacock in the center. Ivory ground with a lavender sheen, five-second synchronized transitions, and soft floor shadows — a same-session visual experiment, not a Michele-stated preference (see the Palette note below; corrected 2026-09-28). On phones the peacock sits above the two outfit panels. This supersedes the earlier choice to use the runway itself as the homepage hero.

[VERIFIED] The saved Shopify draft homepage was pulled before editing; its cover hero and other sections were preserved. The new `runway` instance reuses `hero-looks`; its editor label is **Fashion runway**. A Presentation setting retains the older dark editorial appearance as an option. Source photos are unchanged. The selected cutouts and peacock have deployment copies in theme assets so the section works before the Files/metaobject import. Image pickers override bundled cutouts.

[VERIFIED] Pause/play applies to both sides. Reduced motion starts paused; manual pause survives tab/hover changes. Keyboard focus on an outfit stops rotation. Inactive outfits cannot receive focus, and removing the section in the theme editor cleans up its timer and listeners.

[VERIFIED] Draft verification on 2026-09-21: desktop three-column runway and Shopify phone preview rendered with all three images. Play/Pause and synchronized outfit changes were exercised. New-store `/looks/<handle>` links returned 404 because the look entries are not published there yet; manual cards now resolve a published metaobject URL when present and otherwise link to Contact labeled **Ask about this look**. That was the initial empty-content state, superseded by the routing fix above. Michele still supplies product associations and pricing.

[VERIFIED] Final checks: Shopify theme check passed (zero errors, nine existing warnings); JavaScript syntax and seven motion/lifecycle cases passed. Desktop and phone screenshots showed no clipping. The fallback outfit link opened the Contact form. Chrome console showed Shopify preview preload/custom-pixel warnings and analytics collection failure, with no runway-script error observed. Browser-extension calls timed out, so visual QA used the native Chrome surface through CUA. Draft theme ID: `192212107628`; not published.

### Change log
- 2026-09-25: the four live looks already use try-on-01, -02, -03 and -08 (900×1200 WebP in `assets/`). Shortlisted ten more full-body try-ons as `docs/looks/looks-next.json` with 900×1200 WebP in `docs/images/looks-next/` (not in Shopify yet; needs Amber's picks, then product links). Contact sheets in `docs/meeting/photo-audit_*.jpg`.
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

## Palette (2026-09-20, reverted 9/26) — "soft iridescent pastels" experiment
[CORRECTED 2026-09-28] This was a same-session dev experiment, never a client request or a locked decision — Michele never stated or approved an ivory/lavender/blush direction, then or since. At the time, `config/settings_data.json` color schemes were briefly set to: scheme-1 ivory `#FBF8F5` · scheme-2 blush-lavender mist `#F3EDF3` · scheme-3 lavender `#DCD4EC` (was peacock green) · scheme-4 midnight plum `#2E2A33` · scheme-5 blush `#F5E4EA`, with tokens in `assets/beau-bou.css` (`--bb-ink`, `--bb-accent`, `--bb-hairline`, `--bb-holo`). It was reverted by commit `e57ac0c` ("retire the pastel palette") and the live theme has used grays/white with teal (peacock) as the accent ever since — confirmed unchanged again 2026-09-28 directly against the live Shopify theme. Kept here only as a historical note; do not treat this section as a live or approved direction.
- `page.shop-the-look` now renders the look gallery. The **Shop the look (live)** section remains available for a separate live-stream page.

## Homepage carousel (2026-09-29)
The homepage **Shop Styles** section now runs as an auto-scrolling carousel (Layout → Carousel): 10 tiles, no buttons, loops continuously and pauses on hover/focus or while a look is open. Visitors who set "reduce motion" get a swipeable row instead.
- Tiles fill in this order: published looks → **Extra photo** blocks (theme editor → Shop Styles → Add block) → bundled samples.
- Settings: *Tiles in carousel* (4–20, default 10), *Seconds per loop* (20–120, default 50).
- The Shop the Look page uses the same section with Layout → Grid (filters + full pop-ups).
