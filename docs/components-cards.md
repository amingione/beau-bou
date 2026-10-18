# Boutique cards (from Figma, 2026-10-18)

Source: Figma "10 Product Cards (Community)", file `a8D9PKsYgZQSIIEq4gTD8d`.
Type uses the theme fonts (Playfair Display / Poppins) instead of the mixed community fonts in the file; sizes,
radii, colors, spacing and the shadow follow the Figma values.

| Card | Figma node | Snippet | Used by |
| --- | --- | --- | --- |
| Category card: photo, gold tag pill, frosted panel with name + small line + pill button | `37:211` | `snippets/card-category.liquid` | **Category tiles** section → *Tile style: Card* (homepage "Shop by Category") |
| Collection card: title + small line over a rounded photo, optional dark banner with gold headline | `37:391` | `snippets/card-collection-drop.liquid` | All-collections page → *Card style: Boutique card*; **Collection cards** section (add anywhere) |

Styles for both live in `assets/component-bb-cards.css`. The banner background is the Figma asset itself,
`assets/card-drop-overlay.svg` (266×63, #262626 at reduced opacity), shown at its native size.

## Editing in the theme editor

**Category tiles → Tile style: Card.** Each tile gets three extra fields:
- *Tag*: the gold pill (e.g. "Clearance"). Blank hides it.
- *Subtitle*: the small line under the name (e.g. "All clearance items are final sale"). Blank hides it.
- *Button label*: defaults to "Shop now" (e.g. "Last chance").

On phones with 2 columns the card scales down: smaller radius, compact panel, subtitle hidden.

**Collection card.** Title, photo, link and the small line come from the collection:
- The small line shows the item count ("12 styles"), or **"Coming soon"** when the collection is empty.
- *Banner headline* / *Banner small line* (Collection cards section only) add the dark strip over the photo,
  e.g. a new collection name and a drop date. Blank means no banner.
- Text is right-aligned, as in the Figma design.

## Re-apply

`python3 scripts/declutter/apply-figma-cards-2026-10-18.py` sets the homepage tiles and the /collections page to
the new cards (idempotent).

## Product cards (added 2026-10-18, redone same day)

Amber tried Card A on the product grids and turned it down. She sent a minimal reference instead, and the
product card now follows it: `snippets/card-product-boutique.liquid` + `assets/component-bb-product-card.css`.
The collection-list and category cards above are unchanged (`component-bb-cards.css` is back to its main version).

- **Look:** light-gray photo tile (`#f5f5f5`), portrait 4:5 by default (or the grid's square/adapt ratio),
  no card box and no rounded corners. Small square tag top-left: **SOLD OUT**, or for a markdown **SALE** (tagged `sale`) / **CLEARANCE** (everything else, via `snippets/markdown-badge-label.liquid`, same as the product page), white on warm brown
  `#6e4f45` (8:1 contrast; override with `--bb-pcard-tag-bg`). Name below in the heading serif (Playfair,
  2 lines max), price in Poppins, the old price struck through in `#767676` when on sale. Hover: second photo
  if the section allows it, otherwise a slight zoom (skipped for reduced motion), and the name underlines.
- **Switch:** Theme settings → Product cards → **Product card style** (`product_card_style`): Theme default /
  Boutique (minimal). Set to Boutique. `layout/theme.liquid` loads `component-bb-product-card.css` only when it's on.
- **Where it shows:** `snippets/card-product.liquid` hands off to the boutique card in every grid **without
  quick add**: collection pages, search, the homepage product rows, related products. Look pages
  (`main-look`, `shop-the-look`) sell pieces in place with quick add on, so they keep the default card with
  its add-to-cart. Horizontal cards on the product page also keep the default card.
- **Collection pages:** quick add is off (`templates/collection.json`): tap the card to open the product.
- **Kept from the default card:** the `<product-component>` wrapper (product view analytics still fire),
  the store's "show currency codes" setting, "From" for products whose variants vary in price, and
  screen-reader labels for sale and regular price, and star ratings when the section's "Show product rating" is on and a reviews app fills `reviews.rating`.
