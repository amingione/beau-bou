# Clean pass — logo-forward, easy to navigate (2026-10-16)

Michele's feedback: logos should be more prominent where they're placed, the site has to be easy to
navigate, and it has to be clean. She hates busy. (Background in radio-station marketing, so she reads
branding critically and spots templated or AI-looking design.)

## What was wrong (measured on the live `beau-bou/main` theme, store `v0m0hb-x3`)

| Area | Before |
| --- | --- |
| Header logo | Wordmark only (no peacock), in a 2000×2000 canvas that was ~50% empty padding. At the 100px setting the visible artwork was ~52px wide. "by Michele" was unreadable. |
| Header | Seven menu items wrapped onto two lines ("Visit Us" dropped to row two). A boxed search field sat next to a second search icon. |
| Hero | Logo at ~320px visible, competing with a tagline, the faith line and a button. A 15% white overlay greyed the photo, and a double hairline frame boxed it in. |
| Frames | Solid black 1px frames with an inner inset around the hero, every category tile and the Visit section, so the page read as a stack of boxes. |
| Tracking | Display labels at 0.30em letter-spacing ("S H O P  S T Y L E S"), the most templated-looking element on the page. |
| Repetition | "Accept yourself as you were designed by God" appeared twice on the homepage (hero and teal band). The Shop the Look banner and the Shop Styles carousel both opened `/pages/shop-the-look`. The teal band stacked a scrolling ribbon, an eyebrow, a headline, an accent line, three boxed value cards and a button, and the value cards repeated "XXS – 2X" three ways. |
| Product rows | 8 products (two rows) with an "Add to cart" / "Choose options" button on every card. |

## What changed

**Logo**
- New files in Shopify → Content → Files: `beyoutiful-lockup-black-trim.png` and `beyoutiful-lockup-white-trim.png`. These are Michele's real peacock lockup, tight-cropped (see `docs/client-portal/brand/README.md`).
- Header: logo centered on its own row (`top-center`) at 220px desktop / 136px mobile. That is about 4× the previous visible size, with the peacock included.
- Hero (desktop): same lockup at 600px, centered in the photo's white space. No overlay, frame or glow. One button.
- Hero (phones/tablets, under 990px): the cover photo is a wide collage, and no narrow crop clears both the window's peacock decal and the mannequins. Below 990px the logo stands alone on white (72vw, max 440px) with the button. The photo's Files focal point (~92% x, on the mannequins) is written inline by `image_tag`, which is why a plain `object-position` override did nothing.
- Footer: white knockout of the same lockup leads the teal footer, above one short line of copy.

**Navigation** (Shopify → Content → Menus; store data, not theme files)
- Main menu: `New Arrivals · Shop ▾ · Brands ▾ · Shop the Look · Clearance · Visit Us`. It fits one line.
  - Removed "Home" (the logo is the home link) and the duplicate "New Arrivals" inside the Shop dropdown.
  - "Visit Us" is a direct link now. A dropdown holding only Contact was an extra click for nothing.
  - "Shop the Look" was only reachable from homepage banners. It's now top level.
- Footer menu reordered: Contact, Visit Us, About, Size Guide, Questions, Search, Your Privacy Choices.
- Inline search box removed; the search icon opens Dawn's search modal.

**Homepage** (`templates/index.json`): hero → Shop Styles → Shop by Category (one 6-tile grid) → Shop What's New (4) → teal band → Clearance (4) → Visit Our Store.
- The two tile sections were merged into one grid with one aspect ratio. Tiles are photo + caption, with no box.
- The Shop the Look banner is hidden, not deleted (`"disabled": true`). Re-enable it in the theme editor if wanted.
- Teal band (approved by Michele, "Love it, keep it") keeps the color, statement, faith line and Shop All button. The ribbon, eyebrow and three value cards were removed.
- Product cards: no per-card buttons on the homepage, one row each. Quick add still works on collection pages.

**Global** (`config/settings_data.json`, `assets/beau-bou.css`)
- Frames: `--bb-hairline` is now `rgba(43,43,43,.14)` and the inset is `0`. Every framed element (look pages, size guide, map) calms down together.
- Display tracking 30 → 14, nav tracking 12 → 10. Hover lift on cards off.

## Where it's staged

- Preview theme **`clean-pass preview 2026-10-16`** (`#193257603436`), a duplicate of live `beau-bou/main` with these files applied. Open it from Online Store → Themes → … → Preview.
- Git branch `clean-pass-2026-10-16`. Merging it to `main` deploys to the live theme through the GitHub sync.
- Menus and the two logo files are store data and are **already live**. On the live theme today, the header `logo` setting still points at the old wordmark file, so the live header changes only after the merge.

## Rollback

Everything theme-side is one commit. To undo it: `git revert <sha> && git push` (the GitHub ↔ Shopify sync redeploys).
Menus are store data. The prior main menu was: Home · Shop All ▾ (Shop All, New Arrivals, Dresses, Tops, Bottoms,
Jackets, Swimsuits, Jewelry + Accessories, Handbags, Baby & Toddler, Kids) · Shop Brands ▾ · New Arrivals ·
Clearance · Visit Us ▾ (Contact).

## Re-apply / tweak

```bash
python3 scripts/declutter/apply-2026-10-16.py   # idempotent JSON edits (keeps Shopify's comment header)
python3 scripts/declutter/trim-logo.py docs/client-portal/brand/png-source/beyoutiful-lockup-black-source.png docs/client-portal/brand/beyoutiful-lockup
```

## Domain warning (found 2026-10-16)

`shopbeyoutifulboutique.com` is **not** attached to the store that holds this build (`v0m0hb-x3`). It
serves a third store, `xapm2f-fr`, running an old image-less copy of the theme ("be-you-tiful-boutique-theme-1-2-0":
placeholder art, default Home/Catalog/Contact menu, old "264-A" address and "XXS–3X"). The real build is at
`shopbe-you-tifulboutique.myshopify.com`. Before launch, either move the domain to `v0m0hb-x3` or transfer that
store's ownership to Michele and remove the domain from `xapm2f-fr`. Check what Michele has been looking at.

## Update 2026-10-18: storefront hero restored

Amber didn't want the storefront photo taken out of the hero. It's back, with the peacock logo bigger *on* the storefront:

- Desktop: `beyoutiful-storefront-hero-desktop.webp` (1672×941). Phones (≤749px): `beyoutiful-storefront-hero-mobile-1080.webp` (1080×1080). Both are in Shopify Files with alt text, and both have the holographic logo already in the artwork.
- The hero section has a new **Phone image** setting (`image_mobile`), served through a `<picture>` source, so phones get the square artwork instead of a crop of the wide one.
- `content_below_image` is on: the artwork shows uncropped and edge to edge, and the Shop What's New button sits under it. The overlaid black logo, heading, tagline and accent are cleared, since the logo is in the image.
- Removed the rule that hid the photo below 990px and showed a logo on white.
- Re-apply: `python3 scripts/declutter/apply-storefront-hero-2026-10-18.py` (idempotent).
- The desktop artwork is 1672px wide, so on large or retina screens it's slightly soft. A 2400px+ export would sharpen it.
