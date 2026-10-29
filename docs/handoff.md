## October 29 live catalog/discount update

- Added 80 internal boutique SKUs, resolved eight repeated-SKU variants, and filled 71 missing shipping weights with approved estimates. All 266 draft variants now have unique SKUs and nonzero weights. Estimated weights are tagged `weight-estimate-review` and must be weighed before launch.
- [Full current SKU/weight export](store/launch-catalog-2026-10-29.csv), [repair audit](store/catalog-repairs-2026-10-29.csv), [remaining weight checks](store/launch-catalog-issues-2026-10-29.csv).
- Live welcome discount now targets the 155-product regular-price eligibility collection. 20%, $100 minimum, email subscribers, one use/customer and combination settings verified unchanged.
- Eligibility is a maintained snapshot. Remove products before markdowns; refresh via the app's `sync:newsletter --apply` script before selling changed/new products. Any product with a discounted variant is excluded in full. Automatic refresh and checkout acceptance tests are NOT complete.
- EPOS V4 continues to return 401 despite matching configured credentials. Outbound inventory/order/customer handlers and a documented Love Loyalty external-POS bridge remain unimplemented. See the app repo `docs/EPOSNOW_SYNC.md` for the exact access blocker and unsent vendor question draft.
- These catalog and discount changes are LIVE. Local app/theme source has not been pushed or deployed by this follow-up. No products were activated and the storefront password remains a launch gate.

# Launch readiness update — October 29, 2026

Current authorization: Shopify owns the curated catalog; EPOS inventory must sync both ways. Keep the storefront password until all pilot and checkout gates pass. Love Loyalty owns rewards; no separate rewards engine or points reset. Newsletter offer: one-time 20% off regular-priced items, $100 minimum, once per customer.

## Local changes (not published)

- CLI environment `client` now targets `xapm2f-fr`; `dev` targets boutique test store `v0m0hb-x3`. FAS is excluded.
- `npm run push:client` / `push:dev` use a fixed-target wrapper and create unpublished themes only. Direct CLI calls can bypass this wrapper; always verify the store.
- Homepage Look URL corrected to `/pages/look/…`; test-product fallback removed in favor of `/collections/all`; Look collection reconciled to the owner’s live `new-arrivals`.
- Announcement wording now states the regular-price-only, one-time email signup offer. This copy does NOT configure or enforce a checkout discount.
- Theme check passes with 11 pre-existing warnings. Owner live JSON settings and the Mixologie editorial spotlight block have been reconciled into the local repo; no theme was pushed.

## Current blockers / owner session

App work and technical evidence are recorded in the existing `beau-bou-app/docs/EPOSNOW_SYNC.md`. The old import is retired in local code; replacement supports previews/mapping approvals and held webhook receipts only. Product/inventory/customer/order writes and rewards integration are not complete. EPOS V4 reads returned 401 using both local and production credentials. The production app’s expired Shopify token was successfully renewed through its existing refresh flow; authenticated owner-store reads now work.

Current owner catalog: 155 draft products / 266 draft variants, 7 archived variants, zero active products. SKU and missing-weight repairs are complete as recorded above; 71 weights are estimates requiring physical checks. All draft variants are inventory tracked, have product media, and have positive prices; quantities are not yet reconciled with EPOS or physical stock.

The live newsletter discount is restricted to the regular-price eligibility collection. Subscriber eligibility, one use per customer, $100 minimum, and no combinations are preserved. Collection maintenance and checkout tests remain required; see the limitations above. The app still needs the locally added `read_locations` scope granted before location-name reads.

Remaining checks: full owner catalog and opening physical stock, active EPOS API device/location, Love Loyalty rules and supported EPOS bridge, Faire inventory ownership, actual newsletter discount/automation and mixed-cart repeat-use tests, payment/shipping/pickup/tax/notification settings, Look product links, mobile/desktop checkout, refunds/restocks, failure recovery, and a reconciled trading day.

The owner screenshot confirms be-you-tiful, Love Loyalty, and Faire installed. Older installation and test-catalog notes below are historical, not proof of current account settings.

---

# Client handoff checklist — Be-YOU-tiful Boutique by Michele

## Current owner workflow — September 21, 2026

**Scope confirmed by Amber:** Michele owns products, prices, variants, photos and inventory. Our work is the reusable boutique templates, app configuration, navigation and collection structure. Catalog entry is not a prerequisite for completing that setup. On September 21, Amber explicitly authorized a separate fictional catalog for testing; the details below do not replace Michele’s responsibility for real merchandise.

**Stores (confirmed by Amber 2026-10-18):** `v0m0hb-x3` (`shopbe-you-tifulboutique.myshopify.com`) is **Amber's test store**, used to preview the theme and app before handing them to Michele. Its published theme is `beau-bou/main` (`192420839788`), synced from GitHub `main` (Amber published it 2026-10-18; before that the live theme was `clean-pass preview 2026-10-16`, `193257603436`). **`xapm2f-fr` is Michele's own store**, and `shopbeyoutifulboutique.com` is connected there, correctly. **Since 2026-10-19 Michele's store runs the finished theme** (`be-you-tiful-boutique-theme`, uploaded zip) as its live theme; see "Michele's store (xapm2f-fr) setup status" below. Don't reinstall or re-publish it; later theme changes go through this repo. (A 2026-10-16 note claiming the domain needed to move to `v0m0hb-x3` was wrong and has been removed.) **Update 2026-09-25:** `shopify theme list -s v0m0hb-x3` shows `be-you-tiful-1-2-0` (`192212107628`) as **[live]** and Horizon unpublished, but `https://shopbeyoutifulboutique.com` still redirects to `/password`, so nothing is public. (Earlier notes below that say "draft" or "Horizon live" predate this.) Do not modify the old `kw59hc-k1` development store.

### Adding a product

1. Enter title, description, photos, price and inventory. Use the **Default product** template.
2. Use option names **Size** and **Color** consistently. Set the real variants and stock for each item.
3. Set **Product type** to one of the exact category names in [collections.md](collections.md). Collections populate automatically. Add tag `new` for New Arrivals. **Markdowns are Clearance automatically:** set a compare-at price above the price and the product shows a **Clearance** badge and joins the Clearance collection, no tag needed. **"Sale" is only for sale events:** add tag `sale` to the event's products and they show a **Sale** badge and move from Clearance to the Sale collection; remove the tag when the event ends. Tags never change prices; Michele controls the actual price and compare-at price.
4. Complete the pinned **Fit notes** and **Materials care** fields near the bottom of the product editor. Both are rich text, displayed by the boutique product template and hidden when blank. Never infer fabric composition or care instructions from photos.
5. Optionally choose a published brand-specific **Size guide** page. This replaces the general guide link for that product; otherwise the template uses `/pages/size-guide`.
6. Choose **Complementary products** (pinned by Search & Discovery) to populate **Complete the look**. These must be eligible, available products before Shopify returns recommendations.

### Managing Shop the Look

Open **Content → Metaobjects → Look**, choose an outfit, and select **every featured outfit item** under **Pieces**: garments, shoes, jewelry and bags actually being shown off. Each product gets its own photo, price, size options and cart action. This is a curated product list, not automatic image recognition. Optional **Goes with** products are separate recommendations and appear below. Photo, title and caption belong to that outfit entry. Keep entries Active to show their pages. The four homepage photos already link to matching Look pages; the homepage Shop the Look banner opens the gallery. Products and prices remain Michele's responsibility. See [looks.md](looks.md) for current routing and theme details.

### Test catalog — September 21, 2026

**2026-10-18: all 18 TEST products archived** (gone from the storefront; delete them in Products → Archived when ready).

Imported **18 test products / 55 variants / 18 images** into `v0m0hb-x3` using [client-test-products.csv](store/client-test-products.csv). Source photos came from the local boutique assets and remain untouched. Titles begin `TEST —`, handles begin `test-`, SKUs begin `BB-TEST-`, and all products have `test-product`, `sample`, and `new` tags. Descriptions explicitly identify fictional prices, sizes and copy. Prices range from $16 to $78; three products have compare-at prices and the `sale` tag.

Eleven clothing products have S/M/L/XL variants; sandals have test sizes 6–10; the handbag and jewelry use One Size. Six supporting products were added after Amber clarified that a look must break down the complete outfit. Their isolated photos are AI-generated test illustrations based on visible pieces in the local outfit photos, not verified retail photography. Local assets are `docs/images/placeholders/test-*.png`; details and mapping are in [looks.md](looks.md). Inventory is untracked for cart testing. Products are Active and published to Online Store only. This is store-level catalog data, shared across themes; the store remains password protected and the boutique theme remains a draft.

All four Look entries now reference matching test products under Pieces, plus complementary test products under Goes with. Before launch, replace those references with Michele’s real merchandise, then filter Products by tag `test-product` and archive the eighteen samples. Keep the original photos in Files because the theme and Look entries also use them. The older `store/sample-products.json` belongs to the previous development store, not this import.

Verified in the boutique draft: Shop All shows twelve products, New Arrivals and Sale populate, and Orange Blossom Midi Dress size M / Orange adds to the cart at $64. The test cart item was removed afterward. No checkout or order was submitted.

### Apps and built-in tools

- **Shopify Search & Discovery is installed.** Availability and Price filters were already present. Product type was added; empty filter values are now hidden. Sold-out search results remain at the end. Size and Color filter sources are not offered until products with those options exist. After the first catalog entries: Apps → Search & Discovery → Filters → Add filter → Size / Color.
- **Shopify Messaging** was already installed. No campaigns or customer messages were sent.
- The theme includes size/color selectors, swatches, quick-add, cart, sale badges, related products, contact form, newsletter signup and app-block support. No paid plugin was added. Reviews, wishlist, back-in-stock alerts and chat are optional additions to decide from actual operating needs.

### Completed setup

- Nine automated collections created in the new store; exact rules are in [collections.md](collections.md).
- Created visible **Size Guide**, **Visit Us**, **About**, and **Questions** pages with useful editable body content. Existing Contact and Your Privacy Choices pages preserved. Shop the Look, Make it Yours is now visible at `/pages/shop-the-look`, with four outfit pages at `/pages/looks/<handle>` in the boutique draft.
- Main menu now includes Home, Shop All, Contact, New Arrivals, Shop by Category, Sale, Visit Us. Footer includes Search, Your Privacy Choices, Size Guide, Questions, Visit Us, About, Contact. Header uses `main-menu`; footer uses `footer`.
- Product template now has Boutique product details and Complete the look blocks. Policy links read the store’s saved shipping/refund policies. Removed unconfirmed delivery times and return promises. Removed invented numeric chart presets from the size-guide section.
- Four changed theme files uploaded successfully to the draft only: `sections/main-product.liquid`, `templates/product.json`, `sections/size-guide.liquid`, `sections/footer-group.json`. Homepage, hero, colors and outfit work were not overwritten.

### Final launch work

- Shopify currently lists only the live Horizon theme’s page templates in page administration. When the boutique theme is published, assign About → `about`, Visit Us → `visit-us`, Questions → `faq`, Size Guide → `size-guide`, Contact → `contact`, Shop the Look → `shop-the-look`. The first four pages currently use Default page and already have real body content. Custom size-guide preview was verified in the draft.
- Preserve and reconcile the theme editor’s existing unsaved design session before publishing. Look metaobject/hero work is tracked separately in [looks.md](looks.md); do not broad-push unrelated local files.
- Michele must confirm shipping, pickup and returns terms in Shopify settings. Do not copy unapproved sample policy wording into the live store.
- Activate Size/Color filters now that sample options exist, then repeat variant/cart/checkout checks with actual merchandise before launch. Archive the explicitly authorized test catalog first.

### Verification

- Shopify accepted all four targeted theme files; draft remained unpublished.
- Theme Check: zero errors in deployable theme files; nine upstream warnings. Whole-folder check also sees four errors and 49 warnings inside the existing `_to_delete/hero-runway-v1` archive, which is outside Shopify’s theme directories. Those archive files were not changed or uploaded.
- Authenticated Chrome preview: custom size-guide template renders, sizing accordion expands (`aria-expanded=true`), mobile layout inspected, footer links rendered; no captured console errors. Mobile preview reset. The September 21 test catalog now verifies quick-add and cart behavior; checkout and real-inventory validation remain launch work.
- Brand preflight consulted the global brand index and this project’s source docs. No boutique-specific global brand entry exists; this handoff records the confirmed ownership and setup decisions.

---

Store facts (from Google Business Profile + Facebook, verified 2026-09-02):

- 264 W Marion Ave, Punta Gorda, FL 33950 · (941) 369-1628 · beyoutifulboutiquebymichele@gmail.com
- Hours (open 7 days since 2026-09-25): Mon 11–4 · Tue–Fri 10–5 · Sat 10–4 · Sun 10–3 · In-store pickup offered
- Tagline: "Unique Boutique with affordable prices…from swimwear to formal wear. Size XXS to 2X. (Updated 2026-09-29: was "swimsuits to gowns … 3X".)"
- Faith line: "Accept yourself as you were designed by God"
- Facebook: facebook.com/MicheleMonksEnsmingerMansfield (2.1K followers, 16 reviews, 100% recommend)
- Logo: black circle, white serif "Be-YOU-tiful Boutique", script "by Michele", white peacock. Get the original from Michele (Canva/printer file) — the FB avatar is 480px and too small for the hero.

## Michele's store (xapm2f-fr) setup status — 2026-10-19

Done in her admin (Claude, via Chrome, Amber's request):
- Theme `be-you-tiful-boutique-theme` (uploaded zip) is the live theme. All 52 site files are in Content → Files.
- Look definition **Look** (type `look`) plus 13 Active entries. An empty "Looks" (type `looks`) definition Amber made first is still there; delete it when convenient.
- Look pages (`/pages/look/<handle>`, all 13 return 200): the uploaded zip had dropped `templates/metaobject/look.json`, because Shopify skips a metaobject template whose type doesn't exist yet when the theme goes in. All 13 pages 404'd until the template was re-added in Edit code. Her copy points "Shop all new arrivals" to `new-arrivals` and the sold-out button to `/collections/all` (the repo copy points to test-store handles).
- Homepage Highlights: the extra tropical photo block now uses her `…-shift-dress-b.jpg` (the zip referenced a `.webp` her store doesn't have) and links to `/pages/look/tropical-bell-sleeve-dress`.
- Pages (all Visible, with search listings): About (`about`), Visit Us (`visit-us`), Questions (`faq`), Size Guide (`size-guide`), Shop the Look (`shop-the-look`), Shipping & Returns (default), Contact (`contact`).
- Shipping & Returns page, Refund policy and Shipping policy use the approved wording from `docs/policies/PASTE-INTO-SHOPIFY.md` (no USPS-only, 1–2 day, free-shipping-threshold, swimwear/jewelry final-sale or store-credit claims; Michele never confirmed those). **The test store's Shipping & Returns page still has those unconfirmed lines.**
- Main menu: Shop (her 15 collections + Shop All) · Brands (Samuel Dong, Frank Lyman, Dolcezza, Silver Jeans Co. via `/collections/vendors?q=`) · Shop the Look · About · Visit Us · Contact. Footer: About, Visit Us, Contact, Shipping & Returns, Size Guide, Questions, Your Privacy Choices.
- Location renamed "Be-YOU-tiful Boutique" with 264 W Marion Ave, Punta Gorda FL 33950 and (941) 369-1628; Pickup in store on.
- Preferences: homepage title and meta description set.
- Collections added: New Arrivals (tag `new`), Sale (tag `sale`), Dresses (type Dresses), Jumpsuits (type Jumpsuits), Clearance (compare-at price is set, excluding tag `sale`). They fill in as products are added.

Still Michele's/Amber's to do: finish Shopify Payments setup (Shop Pay, pay-in-4); register for Florida sales tax (Shopify flags it now that the location is in FL); her store has Formal Wear instead of Gowns (keep or rename); remove the password page at launch.

## 1. Store setup (Michele or Amber, ~30 min)

- [ ] Shopify store created on Michele's email; Amber added as **collaborator** (Settings → Users)
- [x] Settings → Store details: name, address above, phone, timezone America/New_York, USD *(done in xapm2f-fr 2026-10-19)*
- [x] Settings → Shipping & delivery: **Local pickup** enabled for the Marion Ave location (hours above) *(done in xapm2f-fr 2026-10-19)*
- [ ] Settings → Payments: Shopify Payments; enable Shop Pay; consider Sezzle/Afterpay (reference offers Sezzle)
- [x] Settings → Policies: generate Refund, Privacy, Terms, Shipping (theme footer links to these) *(done in xapm2f-fr 2026-10-19)*
- [ ] Settings → Customer accounts: **New customer accounts** on (header account icon)
- [x] Domain: `shopbeyoutifulboutique.com` is connected to Michele's store `xapm2f-fr` (correct; nothing to move)
- [x] Handoff: install the finished theme (and the app, if used) on Michele's store `xapm2f-fr` *(done in xapm2f-fr 2026-10-19)*

## 2. Theme install

- [x] *(done 2026-10-19: zip uploaded to xapm2f-fr and published; the app is not installed there)* `npm run push:client` (after setting the store handle in `shopify.theme.toml`) **or** `npm run package` → upload zip in Online Store → Themes **or** the no-login API path in `docs/store/README.md` (zip → Files → `themeCreate`). After any zip import, diff the theme's file list against the zip — Shopify drops files that fail validation without telling you.
- [ ] Theme settings → Logo: upload transparent PNG (≥ 600px wide); Favicon: the circle logo
- [ ] Theme settings → Social: Facebook URL; add Instagram when she has one
- [x] *(menus and the missing New Arrivals, Dresses, Sale, Clearance, Jumpsuits collections done in xapm2f-fr 2026-10-19)* Create collections + menus exactly as `docs/collections.md` (already scripted once on the dev store — see `docs/store/README.md`; current new-store menus use `main-menu` / `footer`)
- [x] Upload the image set to Files first (`docs/images/`), same filenames — templates already point at `shopify://shop_images/beyoutiful-*` *(done in xapm2f-fr 2026-10-19)*
- [x] Pages: about, visit-us, questions, size-guide, shop-the-look, contact with the matching template suffixes *(done in xapm2f-fr 2026-10-19)*
- [x] Policies from `docs/policies/` (Settings → Policies) *(done in xapm2f-fr 2026-10-19)*
- [ ] Homepage: open editor, assign photos to **Hero**, six **Category tiles**, **Visit our store** (pull from Facebook album with Michele's permission — screenshots are not print quality; ask for originals)
- [ ] Announcement bar copy confirmed with Michele (current: pickup + XXS–2X)
- [ ] Preview on phone: nav drawer, search, cart drawer, checkout

## 3. Content Michele owns

- [ ] Products: title, price, compare-at (for the Clearance badge; tag `sale` only for sale events), **Product type** (drives category collections), sizes as variants XXS–2X, 2+ photos each
- [x] About page copy (her story, faith line): Michele's story is in `templates/page.about.json` → Our story (2026-10-18; see `docs/pages/about.md`)
- [ ] Contact page live (`page.contact` template)
- [ ] Mailing list: the footer form collects subscribers; review current Shopify Messaging pricing before sending campaigns

## 4. Launch

- [x] Publish theme *(done in xapm2f-fr 2026-10-19)*
- [ ] Remove password page
- [ ] Google Business Profile → add website URL; Facebook page → Shop button → website
- [ ] Submit sitemap in Search Console (`/sitemap.xml`)
- [ ] Add store to LaunchWell monitoring

## Support notes

- Theme editor covers 95% of changes. Code changes → this repo → `npm run push:client` (stays unpublished until published in admin).
- Dawn updates: compare against `Shopify/dawn` releases; only `layout/theme.liquid` and `sections/header.liquid` carry hand edits — everything else custom is additive.

## Launch preparation — 2026-09-20

- [VERIFIED] Test store: `v0m0hb-x3` (Amber's, for previewing before handoff). Michele's own store is `xapm2f-fr`, with domain `shopbeyoutifulboutique.com` (corrected 2026-10-18). Store was private, with Horizon as its only installed theme at inspection. The custom v1.1 theme remains in development store `kw59hc-k1`.
- [DECIDED] Amber requested completion today and supplied LIKEtoKNOW.it references for the page reached from a homepage banner. References are in `docs/images/inspo- banner routed page/`. The homepage now links to `/pages/shop-the-look`, retaining the shoppable outfit/video section.
- [VERIFIED] Restored 75 missing local theme files from the September 18 Shopify export, preserving four locally differing templates. Rebuilt the empty theme settings schema from official Shopify Dawn v16.0.0 and restored the three boutique-specific styling controls.
- [VERIFIED] Prepared `be-you-tiful-1.2.0.zip`; final Shopify Theme Check returned zero errors and nine warnings in upstream Dawn code. Browser rendering and mobile interactions remain untested until import.
- [VERIFIED] Theme now references descriptive WebP photos, preserves the full branded cover on mobile, and suppresses example cards for empty featured collections. Draft copy no longer promises unconfirmed shipping times, returns terms, gift cards, or a live-stream schedule. Unverified review section remains disabled.
- [VERIFIED] The new store had no products. Real prices, variants, inventory, and confirmed fulfillment/return terms are still required for online sales. Requested this information from Amber; no response received yet.
- [VERIFIED] New store had Contact and Your Privacy Choices pages. About, Visit Us, Questions, Size Guide, and Shop the Look still need creation and template assignment after import, along with collections and menus.
- [VERIFIED 15:45] Imported `be-you-tiful-1-2-0` as draft theme `192212107628` in `v0m0hb-x3`. Native Chrome picker succeeded where extension uploads returned “Not allowed.” Uploaded the 10 distinct WebPs referenced by the theme; Files count increased from 23 to 33. Temporary upload copies were removed after source hash verification.
- [VERIFIED] Connected homepage hero, six category images, Shop the Look banner, and boutique image using the editor; all 10 rendered homepage image elements (including logo) loaded successfully. Inspected at 1440px and 390px; mobile document width equaled viewport (390px), no captured preview console errors. Full shopping flow is not validated.
- [VERIFIED] Store visibility changed to Public during the session; Horizon remains the live theme. This agent has not published a theme or changed visibility.
- [VERIFIED] Existing menus are Main menu (Home, Catalog, Contact), Footer menu (Search, Your Privacy Choices), and Customer account main menu. Header was connected to Main menu in the editor; a later partial CLI upload restored the old group configuration, so local header now uses `main-menu`. A subsequent header-only CLI push succeeded and the preview navigation shows Home, Catalog, Contact.
- [BLOCKED] Shop the Look page content is entered in an open admin tab but NOT saved: Shopify reports “Title is required” despite the populated field. No new pages have been created. Retain the tab for recovery; do not duplicate the page blindly.
- [VERIFIED] Shopify CLI login succeeded. A settings/templates-only push completed partially; index.json and templates/metaobject/look.json were rejected because new `hero-runway` / `main-look` sections were not in the uploaded draft.
- [COORDINATION] New runway/look files and docs were added locally concurrently (15:31–15:39), outside this task’s edits. Preserve them; do not perform a broad push until their owner confirms readiness. The uploaded ZIP remains the earlier stable snapshot. Amber has been asked whether another agent is working on this theme.
- [PENDING] Create/assign pages, collections, and complete menus; confirm real products/prices/sizes/inventory and fulfillment/return terms; verify interactions and checkout before publishing. Preview: https://shopbeyoutifulboutique.com/?preview_theme_id=192212107628

- [VERIFIED 15:49] Mobile menu opens/closes with Home, Catalog, Contact; search dialog opens/closes; empty-cart drawer opens/closes. Preview console captured zero errors. Temporary viewport overrides were reset. Checkout/product flow remains blocked by absent catalog.
