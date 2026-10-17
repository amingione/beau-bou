# Brand assets — Be-YOU-tiful Boutique by Michele

## Live logos (use these) — updated 2026-10-16

The site uses Michele's real logo (peacock + "Be-YOU-tiful Boutique by Michele" lockup), not the traces below.

| File | Where it's live | Shopify Files name |
| --- | --- | --- |
| `beyoutiful-lockup-black-trim.png` (1416×859, transparent) | Theme settings → Logo (header, 220px desktop / 136px mobile) and the homepage hero (600px) | `beyoutiful-lockup-black-trim.png` |
| `beyoutiful-lockup-white-trim.png` (1416×859, transparent) | Footer brand block on the teal band (Theme settings → Brand information → Image) | `beyoutiful-lockup-white-trim.png` |
| `png-source/beyoutiful-lockup-black-source.png` | Original from Michele's logo folder (1800×1200, padded). Re-export from here. | `black-logo.png` |

The trims are the source lockup cropped to its artwork plus a 2% margin, so the theme's width setting
equals the logo's visible width. The white file is a pixel-exact knockout of the black lockup (same
composition). `png-source/beyoutiful-lockup-white-source.png` is a different arrangement
(peacock on the right, black outline) and is not used on the site.

Regenerate: `python3 scripts/declutter/trim-logo.py` (see docs/design-clean-pass.md).

## Legacy traces (do not use as the logo)

Vectorized 2026-09-02 from the only available source: the 480px Facebook page avatar
(`source-facebook-avatar-480.png`). Pipeline: 4× cubic upscale → threshold → speck cleanup →
potrace (optimized curves) → hand-wrapped SVG with a tight viewBox.

**Quality note:** the didone hairline serifs in "Be-YOU-tiful Boutique" are at the limit of a
480px source. Web use (header, hero, favicon, social, OG) is clean. For print, signage, or
embroidery, get Michele's original file (Canva / her printer) and re-export from that.

## Files

| File | Use |
| --- | --- |
| `beyoutiful-logo-black.svg` | Header + hero over light photos (theme `assets/`) |
| `beyoutiful-logo-white.svg` | Over the Peacock band / dark photos (theme `assets/`) |
| `beyoutiful-logo-peacock.svg` | Accent uses — packaging, email header |
| `beyoutiful-badge-black.svg` | Circle badge = FB avatar recreated; favicon source (theme `assets/`) |
| `beyoutiful-badge-peacock.svg` / `-white.svg` | Alt badges for social |
| `png/beyoutiful-logo-*-{600,1200,2400}.png` | Upload to Theme settings → Logo (use 1200) |
| `png/beyoutiful-badge-*-{512,1024,2048}.png` | Social avatars |
| `png/favicon-{32,180,512}.png` | Theme settings → Favicon (512); 180 = Apple touch |
| `png/og-image-1200x630.png` | Default social share image (Online Store → Preferences) |
| `png/social-square-peacock-1080.png` | Instagram/Facebook post tile |

All SVGs carry `role="img"` + `aria-label`; fills are literal so they render identically in any host.
To recolor, change the `fill` on the `<g>`.
