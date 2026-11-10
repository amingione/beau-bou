# SEO (mobile + desktop)

Amber asked for all the on-page SEO possible on 2026-10-18. This table describes the local theme repository; the
November 5 schema corrections below have not been applied to the active Shopify theme as of the November 10 check.

## In the theme

| What | Where | Notes |
| --- | --- | --- |
| Page titles | `layout/theme.liquid` | Adds "– Be-YOU-tiful Boutique" once, unless the title already names the boutique. |
| Meta description | `layout/theme.liquid` | Each page's own description, else Theme settings → Search & social listing → Default description. |
| Share image (Facebook, Messages) | `snippets/meta-tags.liquid` | The page's image, else Shopify's social sharing image, else **Default share image** (theme setting). 1200px, https. |
| Local business data | `snippets/bb-local-business-schema.liquid` | `ClothingStore` structured data: name, address, phone, numeric map pin, hours and `OpeningHoursSpecification`, storefront photo, areas served, and social/Google profiles. On the homepage, About, Visit Us and Contact. Edit under **Store details for Google** in Theme settings. |
| Organization + site search | `sections/header.liquid` | Store identity uses a stable homepage URL and the same `/#store` ID as `ClothingStore`; empty social links are omitted. Homepage `WebSite` data points to the same store. On the homepage, `MerchantReturnPolicy` links the published Shopify refund policy when present. The policy has a clearance exception, so no universal return window is asserted in schema. |
| Breadcrumbs | `layout/theme.liquid` | Two-step `BreadcrumbList` for products, collections and standard pages; three steps for Shop the Look detail pages through the parent gallery. |
| Product data | `sections/main-product.liquid` and `sections/featured-product.liquid` | Shopify's native `product | structured_data` supplies product and offer details. An unconfigured Featured product placeholder emits no Product JSON-LD. |
| Google profile link | `sections/visit-our-store.liquid` | "Reviews on Google" button; link from Store details for Google (or a per-section override). |
| Visit Us directions | `sections/map-embed.liquid` | The local file has a compact address and directions fallback. The active theme still uses Google's `q=...&output=embed` URL; its map rendered in the November 10 preview. Keep the active map unless a fresh preview shows a failure. |
| Alt text | `sections/page-hero.liquid` + file alt text | Hero falls back to the heading; images used on the site have alt text in Content → Files. |
| Canonical URL, sitemap, robots.txt | Shopify | Automatic (`/sitemap.xml`, `/robots.txt`). |

Hours confirmed by Amber on 2026-11-02. Enter one line per range in Theme settings → Store details for Google:
`Mo-Fr 10:00-17:00`, `Sa 10:00-16:00`, `Su 11:00-15:00`.

## In the store (not in this repo)

- **Search listing titles + descriptions** exist on the main pages (About, Visit Us, Contact, Shipping & Returns,
  Shop the Look, Size Guide, Questions). The Visit Us listing was corrected on November 5 to Monday–Friday 10–5,
  Saturday 10–4 and Sunday 11–3. Twelve populated collections received assortment-specific descriptions and
  search listings on November 5: Dresses, Tops, Jewelry & Accessories, Handbags, Baby & Toddler, Toys,
  Formal Wear, Drinkware, Bottoms, Kids, Girls and Samuel Dong. Other collections still need review.
- **Shipping & Returns page** (`/pages/shipping-returns`), linked in the footer and from Questions.

## Verified theme status (November 10, 2026)

- The active theme is `157452402844` (`be-you-tiful-boutique-theme`). Its store-detail settings and displayed
  About, Contact, Visit Us, homepage, and footer hours agree with Amber's confirmed Monday–Friday 10–5,
  Saturday 10–4, Sunday 11–3 schedule. The active Visit Us map rendered in the preview.
- The November 5 schema corrections in `layout/theme.liquid`, `sections/header.liquid`,
  `snippets/bb-local-business-schema.liquid`, and `sections/featured-product.liquid` remain local only. The
  Shopify CLI's current login cannot read this store, and the connected Shopify tool blocks writes to a live
  theme. Re-read the four live files before any future upload. The active About template also has different
  image and caption settings from this repository; do not upload that template wholesale.
- The November 5 store and launch findings below are a dated snapshot. Recheck product publication, payments,
  taxes, Search Console, and editor drafts before treating those findings as current.

## Verified launch controls (November 10, 2026)

- Shopify Preferences briefly showed Private mode off despite the theme preview bar saying password protected.
  Private mode was restored and saved without changing the existing password. A fresh anonymous request to
  `/pages/about` redirected to `/password`.
- The curated store has 149 Active products, all assigned to Online Store. Shopify Payments still requests
  setup. The US tax page says not collecting, and Florida shows action required. US shipping services and
  store pickup are configured; the six published policies are present.
- Google & YouTube is installed but still asks to connect a Google account. The Work Google account did not
  show a Boutique Search Console property or Business Profile owner controls. The Maps listing still shows
  `264-A W Marion Ave` and no website, although its regular hours match the store.
- The embedded EPOS pilot screen loads in Michele's Shopify admin. It shows outbound inventory sync paused,
  zero approved variant mappings, and zero approved location mappings. API connectivity and a successful poll
  do not establish stock synchronization; a physically verified item and real counter sale/refund are required.

## Launch and search visibility status (November 5, 2026)

- Amber intentionally keeps the Online Store password protected during prelaunch. Do not remove the password
  as an SEO fix. Anonymous product and page URLs redirect to `/password`, and `/sitemap.xml` returns 404;
  indexing of the intended pages is deferred until Amber chooses to launch.
- All 121 products in this audit have **Active** product status. Shopify's separate Online Store publication
  currently includes zero products; this is a channel setting, not a contradiction of Active status. Do not
  change product status or publish products as part of an SEO audit. On November 5, custom search titles and
  descriptions were added to 105 active products; 115 of 121 now have both fields. The six remaining listings
  have conflicting color, size, or image details that need product-level correction before SEO text is safe.
  All 784 active-product images now have alt text. The descriptions of images on the six disputed products
  describe only what is visible in the image; they do not assert disputed size, color, stock or manufacturer
  identifiers.
- Twenty-five collections are assigned to Online Store, but ten contain no products. The Swimsuits collection
  currently has no swimsuits; both Jackets collections contain the same three products. Resolve membership and
  duplicate URLs before optimizing these pages. New Arrivals has an unsaved editor draft, so leave it untouched.
- The ten optimized collections with collection images received factual alt text on November 5. Dresses and
  Samuel Dong have no collection image.
- `www.shopbeyoutifulboutique.com` was connected in Shopify on November 5; HTTPS and redirect to the primary
  apex domain were verified. The primary domain was not changed.
- Shopify Payments still shows **Complete setup**. US Taxes and duties shows **Not collecting**, with Florida
  marked **Action required** because its physical-presence threshold was met in September 2026. Checkout and
  tax readiness need Michele's review before a launch decision; the storefront password and product
  publication remain under Amber's control.
- Shopify confirms the installed be-you-tiful app has all 23 requested permissions, including Locations.
  Its live inventory bridge still reports `syncMode: paused`, no outbound writes and no verified variant
  mappings; permissions alone do not establish inventory sync.
- The connected Google Search Console account does not show this domain. Google & YouTube has zero published
  products, and its feed diagnostics could not be verified because its admin panel was blank.
- Local schema corrections in `sections/header.liquid`, `layout/theme.liquid`, and
  `snippets/bb-local-business-schema.liquid` are in the repository only. The Visit Us directions fallback is
  also local only; at the November 5 review, the active theme showed a blank map panel. The November 10 preview
  showed the map working. The active theme had a separate unsaved New Arrivals editor draft at this review;
  do not overwrite or save unrelated editor work during SEO work.

## Still to do by hand

1. **Google Business Profile and local citations:** on November 5, Google Maps and Waze still displayed
   `264-A W Marion Ave`, though their phone and weekly hours matched the store. Google Maps showed no website;
   Yahoo still showed the former `1133 Bal Harbor Blvd`. Correct the owner listing and citations using Michele's
   authorized Google account; the currently signed-in Work account had no owner controls for this business.
2. **Pickup settings:** Michele's published Shipping policy was corrected and saved on November 2; Contact information and Refund policy were checked and current. Compare any separate pickup settings or notifications with the confirmed hours. A theme commit does not update those store settings.
3. **Products and collections:** publish only the curated products that are ready for online sale, complete their
   factual search listings and image alt text, and resolve empty or miscategorized collections.
4. **Search Console:** verify the domain in Michele's Google account and submit `/sitemap.xml` after the storefront
   is public and the sitemap responds. Review Merchant listings and Core Web Vitals reports after real pages crawl.
