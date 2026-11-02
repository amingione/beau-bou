# SEO (mobile + desktop)

Amber asked for all the on-page SEO possible on 2026-10-18. What's in place, and where it lives.

## In the theme

| What | Where | Notes |
| --- | --- | --- |
| Page titles | `layout/theme.liquid` | Adds "– Be-YOU-tiful Boutique" once, unless the title already names the boutique. |
| Meta description | `layout/theme.liquid` | Each page's own description, else Theme settings → Search & social listing → Default description. |
| Share image (Facebook, Messages) | `snippets/meta-tags.liquid` | The page's image, else Shopify's social sharing image, else **Default share image** (theme setting). 1200px, https. |
| Local business data | `snippets/bb-local-business-schema.liquid` | `ClothingStore` structured data: name, address, phone, map pin, hours, areas served, Facebook/Instagram/TikTok/Google. On the homepage, About, Visit Us and Contact. Edit under **Store details for Google** in Theme settings. |
| Organization + site search | `sections/header.liquid` | Dawn's built-in structured data. |
| Google profile link | `sections/visit-our-store.liquid` | "Reviews on Google" button; link from Store details for Google (or a per-section override). |
| Alt text | `sections/page-hero.liquid` + file alt text | Hero falls back to the heading; images used on the site have alt text in Content → Files. |
| Canonical URL, sitemap, robots.txt | Shopify | Automatic (`/sitemap.xml`, `/robots.txt`). |

Hours confirmed by Amber on 2026-11-02. Enter one line per range in Theme settings → Store details for Google:
`Mo-Fr 10:00-17:00`, `Sa 10:00-16:00`, `Su 11:00-15:00`.

## In the store (not in this repo)

- **Search listing titles + descriptions** on every page (About, Visit Us, Contact, Shipping & Returns, Shop
  the Look, Size Guide, Questions) and the owner-store collections. Edit under each page/collection → Search engine
  listing. They name the boutique, Punta Gorda and XXS–2X, and the brief's area (Port Charlotte, North Port,
  Englewood, Fort Myers, Cape Coral) is in the structured data.
- **Shipping & Returns page** (`/pages/shipping-returns`), linked in the footer and from Questions.

## Still to do by hand

1. **Google Business Profile:** verify the current listing against 264 W Marion Ave and Mon–Fri 10–5 · Sat 10–4 · Sun 11–3. The October 18 audit found the old `264-A` address there; its current status needs a fresh check.
2. **Pickup settings:** Michele's published Shipping policy was corrected and saved on November 2; Contact information and Refund policy were checked and current. Compare any separate pickup settings or notifications with the confirmed hours. A theme commit does not update those store settings.
3. **Products:** give each real product a clear title, description, and photo alt text.
4. **Search Console:** verify the domain and submit `/sitemap.xml` when the storefront is ready for indexing.
