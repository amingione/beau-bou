# beau-bou

Shopify Online Store 2.0 theme for **Be-YOU-tiful Boutique by Michele** (Punta Gorda, FL). Forked from Shopify Dawn 16.0.0 and restyled to match the client's reference site, [shopsmithco.com](https://shopsmithco.com): white ground, Poppins body, wide-tracked serif display labels, hairline black frames, flat gray buttons, sidebar-filtered collection grid with white SALE badges.

> The reference site is **not** a Shopify store (it's a CommentSold webstore), so nothing was copied — the look is recreated natively in Liquid on Dawn's accessible, fast base so Michele gets the theme editor, Shopify checkout, and app compatibility.

## Quick start

```bash
npm i -g @shopify/cli          # once
shopify auth login             # once per machine
npm run dev                    # hot-reload preview on Amber's boutique test store (v0m0hb-x3)
npm run check                  # theme-check (gate is "error"; 11 upstream Dawn warnings are known)
npm run push:client            # upload an UNPUBLISHED theme to Michele's store (xapm2f-fr)
npm run package                # zip for manual upload: Online Store → Themes → Add theme → Upload zip
```

Zsh shortcuts: `source scripts/aliases.zsh` → `bb-dev`, `bb-check`, `bb-push`, `bb-zip`, `bb-preview`.

## What's custom (vs. stock Dawn)

| Area | Change |
| --- | --- |
| `config/settings_data.json` | Preset **Be-YOU-tiful**: Playfair Display headings, Poppins body, Playfair italic accent; 5 color schemes, approved by Amber 2026-09-25 (the live theme is the source of truth): light gray `#f1f1f1`, white, teal `#5B93A0`, charcoal `#272727`, slate `#3f494a`; accent teal `#0f5f66`. The earlier iridescent-pastel palette is retired. Square corners, flat gray buttons, drawer cart; markdown badges read Clearance, or Sale for `sale`-tagged event items |
| `config/settings_schema.json` | Theme info; new settings `type_accent_font`, `nav_letter_spacing`, `display_letter_spacing` |
| `layout/theme.liquid` | Loads accent font, exposes `--font-accent-*`, `--nav-letter-spacing`, `--display-letter-spacing`; loads `beau-bou.css` |
| `assets/beau-bou.css` | All global overrides (nav, buttons, cards, badges, facets, footer) + `.bb-display` / `.bb-accent` / `.bb-frame` utilities |
| `sections/header.liquid` + `snippets/header-inline-search.liquid` | Always-visible desktop search field (setting `show_inline_search`) |
| `sections/hero-logo.liquid` | Framed hero image with centered logo overlay + tagline + accent line + CTA |
| `sections/hero-looks.liquid` + `snippets/hero-looks-stage.liquid` + `assets/hero-looks.js` + `snippets/look-card.liquid` | Legacy runway experiment retained in source; it is not in the current homepage template. See [`docs/looks.md`](docs/looks.md) before reusing it. |
| `sections/shop-styles.liquid` + `snippets/shop-styles-post.liquid` + `assets/shop-styles.js` | **Shop Styles** homepage grid of looks — photo or try-on video. Clicking opens a post with featured pieces and cart actions; the individual Look page remains available. See [`docs/looks.md`](docs/looks.md) |
| `templates/metaobject/look.json` + `sections/main-look.liquid` | LTK-style **shop this look** page per outfit: photo/video left, pieces + goes-with grids right, share, more looks |
| `sections/category-tiles.liquid` | Hairline-framed collection tiles with wide-tracked serif captions (the Smith + Co. signature) |
| `sections/brand-strip.liquid` | Peacock-scheme statement band with scrolling ribbon (XXS–2X, swimwear to formal wear) and value cards |
| `sections/visit-our-store.liquid` | Framed storefront photo + address, hours rows, Get Directions (auto Google Maps link), phone |
| `templates/index.json` | Homepage settings and section order: cover hero → collections → What's New → Shop Styles → brands → promise → sale → visit |
| `templates/collection.json` | Vertical (sidebar) filters, 4-col portrait grid, quick-add, 24/page |
| `sections/header-group.json`, `footer-group.json` | Announcement copy; footer = mailing list, Help menu, Get in touch, Store hours, social, payment icons |

Full section reference and client handoff checklist live in [`docs/`](docs/).

## Repo layout

```
assets/       CSS/JS/SVG — ours are beau-bou.css + section-*.css
config/       settings_schema.json (editor UI), settings_data.json (current values)
layout/       theme.liquid, password.liquid
locales/      Dawn translations (untouched)
sections/     Liquid sections + header/footer group JSON
snippets/     partials
templates/    JSON templates (index, collection, product, …)
docs/         architecture, sections, collections, handoff, preview mock
scripts/      aliases.zsh, cutouts.py (rembg runway cutouts), looks/seed-looks.ts (metaobject seeding)
```

## License

Dawn is MIT-licensed by Shopify (see `LICENSE.md`). Custom work © LaunchWell Brands, delivered to the client under the project agreement.

## Current store and theme (2026-11-02)

**`xapm2f-fr` is Michele's store** at shopbeyoutifulboutique.com. Its published theme is `be-you-tiful-boutique-theme` (ID `157452402844`). **`v0m0hb-x3` is Amber's boutique test store**; `kw59hc-k1` is an older development store and is not the current target. The owner theme was installed on October 19. This repo is the source for theme changes; a local commit does not update Michele's published theme. Preview and target any later upload deliberately.

The November 2 owner editor shows an About page with Michele's story and a separate Kind words block. The current store details are 264 W Marion Ave, Punta Gorda, FL 33950 · (941) 369-1628 · beyoutifulboutiquebymichele@gmail.com. Amber confirmed hours on November 2: **Mon–Fri 10–5 · Sat 10–4 · Sun 11–3**. Keep the About, Contact, Visit Us, homepage, footer, structured data, and pickup/shipping copy aligned. See [`docs/pages/about.md`](docs/pages/about.md), [`docs/seo.md`](docs/seo.md), and [`docs/handoff.md`](docs/handoff.md) for the content and launch checks.
