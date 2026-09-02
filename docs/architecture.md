# Architecture

## Why Dawn, why a fork

Michele's brief: "make it look like shopsmithco.com." That site runs on CommentSold (React SPA, `s3.commentsold.com/webstore-builds`), so there is no Liquid theme to reuse. Dawn 16 gives us Online Store 2.0 JSON templates, the theme editor, predictive search, cart drawer, facets, and WCAG-minded markup for free. We restyle it rather than rebuild it — every pixel Michele sees is ours, every behavior underneath is Shopify-maintained.

Rule of thumb: **never edit Dawn's CSS files.** Overrides live in `assets/beau-bou.css`; new sections get their own `assets/section-*.css`. That keeps a future Dawn upstream merge realistic.

## Design tokens

Set in `layout/theme.liquid` from theme settings so Michele can tune them in the editor without code:

| CSS var | Source setting | Default |
| --- | --- | --- |
| `--font-heading-family` | `type_header_font` | Playfair Display 400 |
| `--font-body-family` | `type_body_font` | Poppins 400 |
| `--font-accent-family/style/weight` | `type_accent_font` (new) | Playfair Display italic |
| `--nav-letter-spacing` | `nav_letter_spacing` (new) | 0.12em |
| `--display-letter-spacing` | `display_letter_spacing` (new) | 0.30em |

Color schemes (`settings_data.json → color_schemes`):

| Scheme | Name | Use |
| --- | --- | --- |
| scheme-1 | Paper `#FFFFFF` / ink `#2B2B2B` / button `#6A6A6A` | Default everywhere (matches reference) |
| scheme-2 | Linen `#F6F3EE` | Alternate band backgrounds |
| scheme-3 | Peacock `#0F5F66` | Brand strip — the one bold accent, pulled from the peacock in Michele's logo |
| scheme-4 | Ink `#111111` | Sold-out badge, dark CTAs |
| scheme-5 | Blush `#F2E4E1` | Seasonal / sale banners |

## Utility classes (assets/beau-bou.css)

- `.bb-display` — uppercase, wide-tracked serif. The Smith + Co. "J E W E L R Y  +  A C C E S S O R I E S" look.
- `.bb-accent` — accent font (italic/script feel) for "by Michele"-style lines.
- `.bb-frame` — 1px ink border with 0.6rem inset padding; hover zooms the image slightly (motion-safe).
- `.bb-eyebrow` — small tracked label.

## Header

`logo_position: middle-left`, dropdown menus, inline menu allowed to wrap to two rows (reference has a two-row nav). New `show_inline_search` renders `snippets/header-inline-search.liquid` on ≥990px and hides Dawn's modal search icon there; mobile keeps the icon. Localization selectors are off (single-market store).

## Homepage (templates/index.json)

1. `hero-logo` — framed wide image, logo overlay (upload transparent PNG of the peacock logo), tagline, accent, CTA → `new-arrivals`
2. `featured-collection` "Shop What's New" — desktop slider, portrait cards, quick-add → `new-arrivals`
3. `category-tiles` ×2 — Swimsuits / Dresses / Gowns, then Tops / Bottoms / Jewelry + Accessories
4. `brand-strip` — Peacock scheme, scrolling ribbon, statement, three value cards, Shop All
5. `featured-collection` "Sale" → `sale`
6. `visit-our-store` — storefront photo, address, hours, Get Directions, phone, "In-store pickup available"

Sections read images/captions/links from the assigned collection and only need overrides when Michele wants a different photo.

## Collection page

Vertical facets (sidebar), 4 columns desktop / 2 mobile, portrait ratio, secondary image on hover, quick-add, 24 per page. Badge: white box, black tracked "SALE", soft shadow, bottom-right.

## Fonts

Shopify-hosted (no Google Fonts call): `playfair_display_n4`, `playfair_display_i4`, `poppins_n4`. Swap in the editor under Theme settings → Typography. If Michele wants the logo's exact serif, upload it as a custom font via a small `@font-face` block in `beau-bou.css` and set `type_header_font` to a system fallback.

## Not included (by decision)

- Products, collections, pages, menus, policies — see `docs/handoff.md` for the checklist.
- Apps (reviews, loyalty "3% credit back" like the reference) — recommend Shopify's own **Shop** app + a loyalty app once revenue justifies it.
