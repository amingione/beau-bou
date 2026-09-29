# Signed contract + Michele's handwritten decisions

Photos of the signed packet (iPhone HEIC, taken 2026-09-21). This file transcribes every handwritten answer and records what was done on the site. The `docs/` folder does **not** sync to the Shopify theme.

## Proposal (signed)
$1,000 flat ($500 deposit · $500 at launch). Launch target **October 15, 2026**. Includes: Smith + Co.–style theme; homepage (hero, What's New, six category tiles, "Every body. Every occasion." band, Sale row, Visit Our Store); category + product pages; About, Contact, Visit Us, Shipping & Returns, Privacy pages; mobile-first; vector logo + favicon + social images; store setup (local pickup, shipping rates, payments, tax, policies, domain); footer email signup, Facebook + Google Business Profile linked; first 12 products loaded together; 30 days post-launch support.

## Website Decisions — handwritten answers
| # | Question | Michele's answer | Status (2026-09-28) |
|---|---|---|---|
| 1 | Approve homepage design | ✓ Yes, build it | Done |
| 2 | Teal accent band | ✓ Love it, keep it | Done (brand strip unchanged; top promo bar is one shade deeper teal for text contrast) |
| 3 | Logo | (blank) | Rebuilt vector in use |
| 4 | Shop categories | **Gowns crossed out.** Add: **Baby/Toddler, Jackets, Kids boys/girls.** Side note "Brands": **Samuel Dong, Frank Lyman, Dolcezza, Silver** | Collections created (Jackets, Baby & Toddler, Kids — all by product type; Samuel Dong, Frank Lyman, Dolcezza — by vendor) and published. Main menu: categories under **Shop All**, brands under **Shop Brands**. Homepage Gowns tile → **Jackets**. All "gowns" copy removed. Gowns collection is empty and off every menu/tile; unpublish it in admin (the API connection may not unpublish). **"Silver" not added — confirm the brand (Silver Jeans Co.?).** |
| 5 | Sizes | "XS–3X" + wrote **XXS** | **Updated 2026-09-29: XXS–2X** site-wide (theme + About + Questions pages). "Gowns" wording → **Formal Wear** |
| 6 | Best sellers to feature | "Thinking on" | Waiting on Michele |
| 7 | Shipping or pickup | **Both** (pickup + flat-rate shipping; no amount written) | Amber set it to carrier-calculated (dynamic) rates instead of a flat fee — USPS/UPS for standard, FedEx for overnight, all priced by weight/distance. Questions page + shipping policy text updated. Done. |
| 8 | Ways to pay | **✓ Add pay-in-4 installments**; PayPal crossed out | **On hold on purpose:** Amber is deliberately not enabling Shop Pay Installments or any other payment/financing method yet — the store is still in her own Shopify account and will transfer to Michele's account first, so it gets set up under Michele's login from the start. |
| 9 | Returns | **7 days, tag on item & receipt · excludes final sale (clearance)** · "open 7 days a wk" | Questions page updated. Refund + shipping policy text ready in `docs/policies/` — **paste into Settings → Policies** (connection lacks policy permission) |
| 10 | Store hours & announcement bar | ✓ "Change to"; wrote hours near Sun–Mon ("11-3", "10-5") + open 7 days | Confirmed 2026-09-28: **Sunday 11–3**. Site-wide hours now Mon 11–4 · Tue–Fri 10–5 · Sat 10–4 · **Sun 11–3**. Announcement: "Get 20% off your first online order!" |
| 11 | Website address | shopbeyoutiful.com crossed out | shopbeyoutifulboutique.com in use |
| 12 | Social links | Instagram: "have broke, look @ new"; TikTok **@beyoutiful.boutiq64** (hard to read) | Done — Facebook, Instagram (@michelensmginer) and TikTok (@beyoutiful.boutiq64) are all set in Theme settings → Social media and live in the footer. |
| 13 | Email list | "*Reg price items* — one time 20% off / Rewards options" | Welcome code: **20% off the entire order**, email subscribers, once per customer. Amber confirmed 2026-09-28 it is **not** limited to regular-price items. |
| 14 | About page story | "Will write and send" | Waiting on Michele |

## Meeting sheet (not filled in)
- Address: **264 W Marion Ave, Punta Gorda, FL 33950** (corrected 2026-09-29 — no "-A"; replaces the 2026-09-28 "264-A"). Made consistent across theme, pages and policy text (store contact details in Settings → Store details still need it — admin only).
- Name for About/agreement, Aundrea's role, Shopify signup email — blank.

## Other notes on the packet (not website scope)
"New owners has contact"; "November — Allegiant — book w/ chamber — $1000.00"; "The Parrot" on the back of the proposal. One photo is a proposal page printed on Procell Therapies letterhead (reused paper).

## Still in Shopify admin (can't be done from the repo or the API connection)
1. ~~**Settings → Policies**: paste `docs/policies/refund-policy.md` and `shipping-policy.md`~~ — done 2026-09-28 (Shipping and Terms of Service pasted in; Privacy already had the boutique's contact info).
2. **Settings → Store details**: store email/phone → the boutique's (currently Amber's).
3. **Settings → Payments**: turn on Shop Pay Installments (pay-in-4) — **intentionally on hold** until the store transfers to Michele's own Shopify account.
4. ~~**Settings → Shipping and delivery**: set the flat U.S. rate~~ — not applicable; Amber set carrier-calculated (dynamic) rates instead, USPS/UPS by weight and distance.
5. **Products → Collections → Gowns**: unpublish (or delete) — it's empty (the API mutation is blocked by a safety policy; needs a manual click in admin).
