# beau-bou

Shopify Online Store 2.0 theme for **Be-YOU-tiful Boutique by Michele** (Punta Gorda, FL). Forked from Shopify Dawn 16.0.0 and restyled to match the client's reference site, [shopsmithco.com](https://shopsmithco.com): white ground, Poppins body, wide-tracked serif display labels, hairline black frames, flat gray buttons, sidebar-filtered collection grid with white SALE badges.

> The reference site is **not** a Shopify store (it's a CommentSold webstore), so nothing was copied — the look is recreated natively in Liquid on Dawn's accessible, fast base so Michele gets the theme editor, Shopify checkout, and app compatibility.

## Quick start

```bash
npm i -g @shopify/cli          # once
shopify auth login             # once per machine
npm run dev                    # hot-reload preview on the dev store (kw59hc-k1)
npm run check                  # theme-check (gate is "error"; 11 upstream Dawn warnings are known)
npm run push:client            # upload as UNPUBLISHED theme to Michele's store (set handle in shopify.theme.toml)
npm run package                # zip for manual upload: Online Store → Themes → Add theme → Upload zip
```

Zsh shortcuts: `source scripts/aliases.zsh` → `bb-dev`, `bb-check`, `bb-push`, `bb-zip`, `bb-preview`.

## What's custom (vs. stock Dawn)

| Area | Change |
| --- | --- |
| `config/settings_data.json` | Preset **Be-YOU-tiful**: Playfair Display headings, Poppins body, Playfair italic accent; 5 color schemes — soft iridescent pastels: Ivory, Blush-lavender mist, Lavender, Midnight plum, Blush (see `docs/looks.md` › Palette); square corners, flat gray buttons, drawer cart, white SALE badge |
| `config/settings_schema.json` | Theme info; new settings `type_accent_font`, `nav_letter_spacing`, `display_letter_spacing` |
| `layout/theme.liquid` | Loads accent font, exposes `--font-accent-*`, `--nav-letter-spacing`, `--display-letter-spacing`; loads `beau-bou.css` |
| `assets/beau-bou.css` | All global overrides (nav, buttons, cards, badges, facets, footer) + `.bb-display` / `.bb-accent` / `.bb-frame` utilities |
| `sections/header.liquid` + `snippets/header-inline-search.liquid` | Always-visible desktop search field (setting `show_inline_search`) |
| `sections/hero-logo.liquid` | Framed hero image with centered logo overlay + tagline + accent line + CTA |
| `sections/hero-looks.liquid` + `snippets/hero-looks-stage.liquid` + `assets/hero-looks.js` + `snippets/look-card.liquid` | **Hero looks** (current home hero): silver-blue holographic logo center stage, an outfit slideshow either side that crossfades in sync while showing different looks; no controls, no copy. Every outfit links to its `/looks/<handle>` page. Reads `look` metaobjects; manual blocks as fallback. See [`docs/looks.md`](docs/looks.md) |
| `templates/metaobject/look.json` + `sections/main-look.liquid` | LTK-style **shop this look** page per outfit: photo/video left, pieces + goes-with grids right, share, more looks |
| `sections/category-tiles.liquid` | Hairline-framed collection tiles with wide-tracked serif captions (the Smith + Co. signature) |
| `sections/brand-strip.liquid` | Peacock-scheme statement band with scrolling ribbon (XS–3X, swim to gowns) and value cards |
| `sections/visit-our-store.liquid` | Framed storefront photo + address, hours rows, Get Directions (auto Google Maps link), phone |
| `templates/index.json` | Homepage wired: hero looks → What's New slider → 2×3 category tiles → brand strip → Sale slider → Visit |
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

## Build state (2026-09-12)

Design approved by Michele. Theme v1.1 is on Amber's dev store `kw59hc-k1` (unpublished) with the full page set — About, Visit Us, Contact, Questions, Size Guide, **Shop the Look** (live/try-on video + shoppable rail) — 12 sample products, 10 collections, brand placeholders in every image slot. See `docs/store/README.md` (what's in the store and how it got there), `docs/images/README.md` (placeholder → real photo swap), `docs/policies/` (policy text for Michele's store).
