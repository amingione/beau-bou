# Dev store build — kw59hc-k1 (Amber's store, not Michele's)

State as of 2026-09-12. Everything below was created through the Shopify Admin GraphQL API (Shopify MCP) — no CLI login needed. Repeat the same steps on Michele's store when it exists; nothing here is store-specific except IDs.

## Theme
| | |
| --- | --- |
| Theme | **Beau Bou — Be-YOU-tiful v1.1** · `gid://shopify/OnlineStoreTheme/190695505993` · role UNPUBLISHED |
| How it got there | `shopify theme package` → zip uploaded to Files (staged upload, `FILE`) → `themeCreate(source: <cdn zip url>)`. ~30 s processing. |
| Superseded | `zz DELETE ME — Beau Bou v1.0 (superseded)` (`190695342153`) — delete in admin; `themeDelete` is blocked for the MCP. |
| Preview | `https://kw59hc-k1.myshopify.com/?preview_theme_id=190695505993` (storefront password page will show first) |

**Why v1.1 exists:** Shopify silently drops theme files that fail validation on zip import. v1.0 lost `sections/category-tiles.liquid` (a `"default": ""` on a text setting is invalid) and therefore `templates/index.json` (referenced a missing section). Always diff `theme.files` against the zip after `themeCreate`.

**Image references:** settings/templates written via the API keep `shopify://shop_images/<file>` as a *string* — Liquid's `image_url` then throws "invalid url input". Every image-consuming section in this theme (header logo, password logo, favicon, hero-logo, category-tiles, visit-our-store, page-hero, image-with-text, shop-the-look poster) resolves that with:

```liquid
assign bb_image = section.settings.image
if bb_image != blank and bb_image.src == blank
  assign bb_fname = bb_image | remove: 'shopify://shop_images/'
  assign bb_image = images[bb_fname]
endif
```
Saving once in the theme editor also normalises them; the fallback means we never depend on it.

## Files (Settings → Content → Files)
47 images, all prefixed `beyoutiful-`: 43 placeholders from `scripts/placeholders.py` (see `docs/images/README.md`) + logo black/white 1200, favicon 512, OG 1200×630. IDs in `docs/store/file-ids.json`. CDN base `https://cdn.shopify.com/s/files/1/0987/4348/4489/files/`.

## Catalog
- **12 sample products** (`docs/store/sample-products.json`) via `productSet` (synchronous, 6 per call). Sizes XS–3X (or One Size), untracked inventory, `inventoryPolicy: CONTINUE`, tags drive collections, all tagged `sample`. Published to Online Store.
- **10 smart collections**: new-arrivals (tag new) · best-sellers (tag best-seller) · swimsuits/dresses/gowns/tops/bottoms (product type) · jewelry-accessories (type Jewelry OR Accessories) · sale (tag sale) · live-picks (tag live-picks). Each has a banner image.
- Delete everything tagged `sample` before Michele loads real inventory: `search_products "tag:sample"` → archive/delete.

## Pages (templateSuffix → template)
about → `page.about` · visit-us → `page.visit-us` · questions → `page.faq` (handle `faq` was taken on this store) · size-guide → `page.size-guide` · shop-the-look → `page.shop-the-look` · contact (pre-existing page) → `page.contact`.

## Menus
`beau-bou-main` (header) and `beau-bou-footer` — theme header/footer groups reference these handles, so the store's existing `main-menu`/`footer` (House of Rose) are untouched.

## Not done on the dev store, on purpose
Policies (store-level, would overwrite Amber's other business) — text lives in `docs/policies/`. Shipping/pickup/payments settings — Michele's store only.
