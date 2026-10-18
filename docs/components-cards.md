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

## Product cards (added 2026-10-18)

Amber wanted the cards on the **product** grids too, not only the collection list and category tiles.
Card A (37:391) now has a product version: `snippets/card-product-boutique.liquid`.

- **Switch:** Theme settings → Product cards → **Product card style** (`product_card_style`): Theme default /
  Boutique. Set to Boutique. `layout/theme.liquid` loads `component-bb-cards.css` when it's on.
- **Where it shows:** `snippets/card-product.liquid` hands off to the boutique card in every grid **without
  quick add**: collection pages, search, the homepage product rows, related products. Look pages
  (`main-look`, `shop-the-look`) sell pieces in place with quick add on, so they keep the default card with
  its add-to-cart. Horizontal cards on the product page also keep the default card.
- **Collection pages:** quick add was turned off (`templates/collection.json`), per Amber: tap the card to
  open the product.
- **Card:** right-aligned name (2 lines max) and price above a rounded photo in the grid's own ratio
  (portrait by default), second photo on hover when the section allows it. The Figma dark banner shows
  only for **Sale** ("Was $X") or **Sold out**, and the price line carries the same information for screen readers.
