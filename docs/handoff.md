# Client handoff checklist — Be-YOU-tiful Boutique by Michele

Store facts (from Google Business Profile + Facebook, verified 2026-09-02):

- 264-A W Marion Ave, Punta Gorda, FL 33950 · (941) 369-1628 · beyoutifulboutiquebymichele@gmail.com
- Hours: Tue–Fri 10–5 · Sat 10–4 · Sun–Mon closed · In-store pickup offered
- Tagline: "Unique Boutique with affordable prices…from swimsuits to gowns. Size XS to 3X."
- Faith line: "Accept yourself as you were designed by God"
- Facebook: facebook.com/MicheleMonksEnsmingerMansfield (2.1K followers, 16 reviews, 100% recommend)
- Logo: black circle, white serif "Be-YOU-tiful Boutique", script "by Michele", white peacock. Get the original from Michele (Canva/printer file) — the FB avatar is 480px and too small for the hero.

## 1. Store setup (Michele or Amber, ~30 min)

- [ ] Shopify store created on Michele's email; Amber added as **collaborator** (Settings → Users)
- [ ] Settings → Store details: name, address above, phone, timezone America/New_York, USD
- [ ] Settings → Shipping & delivery: **Local pickup** enabled for the Marion Ave location (hours above)
- [ ] Settings → Payments: Shopify Payments; enable Shop Pay; consider Sezzle/Afterpay (reference offers Sezzle)
- [ ] Settings → Policies: generate Refund, Privacy, Terms, Shipping (theme footer links to these)
- [ ] Settings → Customer accounts: **New customer accounts** on (header account icon)
- [ ] Domain: buy `beyoutifulboutique.com` (or similar) via Shopify or point Michele's registrar

## 2. Theme install

- [ ] `npm run push:client` (after setting the store handle in `shopify.theme.toml`) **or** `npm run package` → upload zip in Online Store → Themes **or** the no-login API path in `docs/store/README.md` (zip → Files → `themeCreate`). After any zip import, diff the theme's file list against the zip — Shopify drops files that fail validation without telling you.
- [ ] Theme settings → Logo: upload transparent PNG (≥ 600px wide); Favicon: the circle logo
- [ ] Theme settings → Social: Facebook URL; add Instagram when she has one
- [ ] Create collections + menus exactly as `docs/collections.md` (already scripted once on the dev store — see `docs/store/README.md`; menus must be handles `beau-bou-main` / `beau-bou-footer`)
- [ ] Upload the image set to Files first (`docs/images/`), same filenames — templates already point at `shopify://shop_images/beyoutiful-*`
- [ ] Pages: about, visit-us, questions, size-guide, shop-the-look, contact with the matching template suffixes
- [ ] Policies from `docs/policies/` (Settings → Policies)
- [ ] Homepage: open editor, assign photos to **Hero**, six **Category tiles**, **Visit our store** (pull from Facebook album with Michele's permission — screenshots are not print quality; ask for originals)
- [ ] Announcement bar copy confirmed with Michele (current: pickup + XS–3X)
- [ ] Preview on phone: nav drawer, search, cart drawer, checkout

## 3. Content Michele owns

- [ ] Products: title, price, compare-at (for SALE badge), **Product type** (drives category collections), sizes as variants XS–3X, 2+ photos each
- [ ] About page copy (her story, faith line)
- [ ] Contact page live (`page.contact` template)
- [ ] Mailing list: Shopify Email is free to 10k sends/mo — footer form already collects subscribers

## 4. Launch

- [ ] Publish theme
- [ ] Remove password page
- [ ] Google Business Profile → add website URL; Facebook page → Shop button → website
- [ ] Submit sitemap in Search Console (`/sitemap.xml`)
- [ ] Add store to LaunchWell monitoring

## Support notes

- Theme editor covers 95% of changes. Code changes → this repo → `npm run push:client` (stays unpublished until published in admin).
- Dawn updates: compare against `Shopify/dawn` releases; only `layout/theme.liquid` and `sections/header.liquid` carry hand edits — everything else custom is additive.
