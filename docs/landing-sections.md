# Homepage landing sections (from Figma, 2026-10-18)

Source: Figma "Fashion Website Landing Page (Community)", file `MNPjk3erCuTMe588rPIOga`.
The Figma text and photos were examples. Everything shown on the site comes from the store
(Looks, collections, Michele's own graphic) or from the theme editor. Theme fonts (Playfair / Poppins)
replace the Figma Inter.

| Figma node | What it is on the site | Code |
| --- | --- | --- |
| 1:612 "Name of brand goes here" | **Announcements**: text left, picture right, rotating | `sections/announcement-spotlight.liquid`, `assets/section-announcement-spotlight.css`, `assets/announcement-spotlight.js` |
| 1:159 "Shop our highlights" | **Shop Styles → Highlights layout**: intro + button left, try-on looks right | `sections/shop-styles.liquid` (layout `highlights`), `assets/section-shop-styles-highlights.css`, `assets/icon-quick-view.svg` |
| 1:135 "Collections" | **Collections carousel**: gray band, square tiles, one button | `sections/collection-carousel.liquid`, `assets/section-collection-carousel.css` |

Both swipeable rows share `assets/bb-scroller.js` + `assets/component-bb-scroller.css` +
`snippets/bb-scroller-buttons.liquid` (prev/next buttons that disable at the ends, hidden on phones).

Homepage order: hero → Announcements → Shop Our Highlights → Collections → Shop What's New → teal band →
Clearance → Visit Our Store. The old Shop by Category grid (`tiles_1`) is hidden, not deleted. Turn it back
on in the theme editor if wanted. The Collections carousel can also use the category card instead of squares.

## Announcements

One block per announcement. Use it for the mailing list, a brand Michele carries, or an event.

- **Picture**: wide photos fill the right half. For graphics with words in them, turn on **Show the whole
  picture** so nothing gets cropped, and set the background color to match the graphic's edges.
- **Email sign-up** (optional, per block): Shopify's newsletter form. New addresses land in Customers with
  email marketing on. The thank-you line is editable.
- **Link** (optional): the underlined link under the text, e.g. "Shop the brand" → the brand's collection.
- Two or more blocks rotate together (text and picture), every *Seconds per announcement*. They pause on
  hover or keyboard focus and have a pause button. They never rotate for visitors with reduced motion on.
  Dots appear only when there is more than one.

Live now: one block, Michele's "All new, all the time / join the list" graphic
(`beyoutiful-join-the-list-announcement.webp` in Files) with the sign-up form.

## Shop Our Highlights (Shop Styles, Highlights layout)

Same section and same Looks as before (Content → Metaobjects → Look). Only the layout is new.

- Each card shows the look photo, the "Shop the look" label, the look name, and "N pieces · from $X". The
  price is the lowest available piece. **Quick view** opens the existing shop-this-look pop-up, where every
  piece can be added to the cart, plus "View full look page".
- The Extra photo blocks fill in after the Looks, up to *Grid and highlights: looks to show*.
- Label text and color are settings. The default color is the Figma red `#e60023`, which gives white text
  4.8:1 contrast. Keep any replacement that dark.
- The button on the left goes to `/pages/shop-the-look` (the full LTK-style page).

## Collections carousel

One block per collection. A block's picture wins; with it blank the tile uses the collection's own picture;
with neither it shows just the name on charcoal (no placeholder drawing). Names sit on a 42% dark scrim, so
white text stays at 3:1+ even over a white photo (large-text AA).

Category photos (2026-10-18) come from `photos-in/categories` on Amber's Mac, converted to 1600px WebP and
uploaded to Files as `beyoutiful-category-*.webp` with alt text. Each one is also set as its collection's image,
so the /collections page matches.

| Tile | Collection | Photo |
| --- | --- | --- |
| Dresses | `dresses` | dresses |
| Tops | `tops` | tops (denim top) |
| Bottoms | `bottoms` | bottoms (white pants outfit) |
| Jumpsuits | `jumpsuits` (new) | jumpers |
| Jackets | `jackets` | jackets |
| Shoes | `shoes` (new) | shoes |
| Handbags | `handbags` | bags |
| Hats | `hats` (new) | hats (straw sun hat) |
| Jewelry + Accessories | `jewelry-accessories` | jewelry |
| Drinkware | `drinkware` (new) | drinkware |
| Swimsuits | `swimsuits` | none yet |
| Kids | `kids` | kids-toys (plush) |
| Little Girls | `little-girls` (new) | little-girls |
| Toys | `toys` (new) | kids-toys-alt (beach set) |
| Baby & Toddler | `baby-toddler` | none yet |

The six new collections are manual, published to the Online Store, and empty until products are added.
Pants, shorts and shirts photos weren't given their own collections: pants and shorts belong under Bottoms,
shirts under Tops. Those photos, plus `bottoms-alt`, `hat` (caps) and `gowns`, are converted but unused.
Gowns stays out per Michele's contract.

## Re-apply the homepage setup

```bash
python3 scripts/declutter/apply-landing-sections-2026-10-18.py   # idempotent; keeps Shopify's comment header
```

## Gotcha found on the way

Shopify rejects a section whose select option label is over **50 characters**. The upload API accepts the
file, then silently keeps the old version. Theme Check doesn't flag it. Check a file's `checksumMd5` after
any upload.
