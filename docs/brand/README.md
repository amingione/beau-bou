# Brand assets — Be-YOU-tiful Boutique by Michele

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
