# Boutique collections and navigation

This records the **September 20 test-store setup** in `v0m0hb-x3`. Michele's owner store is `xapm2f-fr`; its boutique theme was published October 19, and its page templates are assigned. The owner-store menu and collection state is summarized in [handoff.md](handoff.md), and should be read in Shopify before changing live navigation. The table below is historical test-store configuration, not an instruction to recreate it on Michele's store.

| Collection | Handle | Membership rule |
| --- | --- | --- |
| New Arrivals | `new-arrivals` | Tag includes `new` |
| Sale | `sale` | Tag includes `sale`. Reserved for sale events. |
| Clearance | `clearance` | Price is reduced (compare-at above price) **and** tag is not `sale`. Created 2026-09-25. |
| Dresses | `dresses` | Product type equals `Dresses` |
| Gowns | `gowns` | Product type equals `Gowns` |
| Tops | `tops` | Product type equals `Tops` |
| Bottoms | `bottoms` | Product type equals `Bottoms` |
| Handbags | `handbags` | Product type equals `Handbags` |
| Jewelry + Accessories | `jewelry-accessories` | Product type equals `Jewelry + Accessories` |
| Swimsuits | `swimsuits` | Product type equals `Swimsuits` |
| Shop All | `all` | Shopify’s built-in all-products route |

Use those exact Product type names. A product can appear in its category, New Arrivals and Sale (or Clearance) at the same time. Any markdown is Clearance by default; tag `sale` only for a sale event and remove it afterwards. A product is never in both Sale and Clearance. Remove `new` or `sale` tags when appropriate. The Sale collection does not alter prices; the owner sets Price and Compare-at price. The original setup created no product records. On September 21, Amber authorized eighteen fictional test products; their exact types and `new`/`sale` tags now populate these collections. See [handoff.md](handoff.md#test-catalog--september-21-2026).

The existing empty Home page collection was preserved. The category listing `/collections` is linked from the main menu. The theme’s category tiles refer to Dresses, Gowns, Tops, Bottoms, Jewelry + Accessories and Handbags; featured sections use New Arrivals and Clearance (switch the homepage row's collection to Sale during an event).

## Test-store main menu (`main-menu`, historical)

- Home → `/`
- Shop All → `/collections/all`
- Contact → `/pages/contact`
- New Arrivals → `/collections/new-arrivals`
- Shop by Category → `/collections`
- Clearance → `/collections/clearance` (was Sale → `/collections/sale` until 2026-09-25; add a Sale link back during events)
- Visit Us → `/pages/visit-us`

## Test-store footer menu (`footer`, historical)

Search, Your Privacy Choices, Size Guide, Questions, Visit Us, About, Contact. Shopify policy links are displayed separately by the footer when those policies are saved.

## Initial test-store pages and template assignment (historical)

| Page handle | Custom template | Current state |
| --- | --- | --- |
| `about` | `about` | Created, visible, Default page until theme launch |
| `visit-us` | `visit-us` | Created, visible, Default page until theme launch |
| `questions` | `faq` | Created, visible, Default page until theme launch |
| `size-guide` | `size-guide` | Created, visible, Default page until theme launch |
| `contact` | `contact` | Existing page; preserve |
| `shop-the-look` | `shop-the-look` | Visible; four-look gallery renders in the draft through Default page until theme launch |

Michele's owner store now runs the published boutique theme, with About, Visit Us, Questions, Size Guide, Shop the Look and Contact assigned to their matching custom templates as recorded on October 19. See [handoff.md](handoff.md) for current owner-store status and product-field and app instructions.
