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

Hours format for the structured data, one line per range: `Mo 11:00-16:00`, `Tu-Fr 10:00-17:00`,
`Sa 10:00-16:00`, `Su 10:00-15:00`.

## In the store (not in this repo)

- **Search listing titles + descriptions** on every page (About, Visit Us, Contact, Shipping & Returns, Shop
  the Look, Size Guide, Questions) and all 22 collections. Edit under each page/collection → Search engine
  listing. They name the boutique, Punta Gorda and XXS–2X, and the brief's area (Port Charlotte, North Port,
  Englewood, Fort Myers, Cape Coral) is in the structured data.
- **Shipping & Returns page** (`/pages/shipping-returns`), linked in the footer and from Questions.

## Still to do by hand

1. **Google Business Profile:** it still shows "264-A W Marion Ave", Monday 10–5 and Sunday 11–3. Change it
   to 264 W Marion Ave and Mon 11–4 · Tue–Fri 10–5 · Sat 10–4 · Sun 10–3, so Google sees the same name,
   address, phone and hours everywhere.
2. **Homepage title** (Online Store → Preferences): e.g. "Women's Boutique in Punta Gorda, FL | Be-YOU-tiful
   Boutique by Michele". It's "Be-YOU-Tiful Boutique – Punta Gorda, FL" now. The API can't set it.
3. **Policies** (Settings → Policies): Refund and Shipping still say "264-A"; Contact information lists
   Amber's phone and email. Paste from `docs/policies/PASTE-INTO-SHOPIFY.md`. The API connection can't edit
   policies.
4. **Products:** when real products go in, give each a clear title, a description, and alt text on photos.
5. **Search Console:** once the domain is live on Michele's store, verify it and submit `/sitemap.xml`.
