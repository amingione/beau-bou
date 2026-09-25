# Boutique collections and navigation

Created in `v0m0hb-x3` on September 20, 2026. Michele enters products and prices; these collections automatically organize her catalog.

| Collection | Handle | Membership rule |
| --- | --- | --- |
| New Arrivals | `new-arrivals` | Tag includes `new` |
| Sale | `sale` | Tag includes `sale` |
| Dresses | `dresses` | Product type equals `Dresses` |
| Gowns | `gowns` | Product type equals `Gowns` |
| Tops | `tops` | Product type equals `Tops` |
| Bottoms | `bottoms` | Product type equals `Bottoms` |
| Handbags | `handbags` | Product type equals `Handbags` |
| Jewelry + Accessories | `jewelry-accessories` | Product type equals `Jewelry + Accessories` |
| Swimsuits | `swimsuits` | Product type equals `Swimsuits` |
| Shop All | `all` | Shopify’s built-in all-products route |

Use those exact Product type names. A product can appear in its category, New Arrivals and Sale at the same time. Remove `new` or `sale` tags when appropriate. The Sale collection does not alter prices; the owner sets Price and Compare-at price. The original setup created no product records. On September 21, Amber authorized eighteen fictional test products; their exact types and `new`/`sale` tags now populate these collections. See [handoff.md](handoff.md#test-catalog--september-21-2026).

The existing empty Home page collection was preserved. The category listing `/collections` is linked from the main menu. The theme’s category tiles refer to Dresses, Gowns, Tops, Bottoms, Jewelry + Accessories and Handbags; featured sections use New Arrivals and Sale.

## Main menu (`main-menu`)

- Home → `/`
- Shop All → `/collections/all`
- Contact → `/pages/contact`
- New Arrivals → `/collections/new-arrivals`
- Shop by Category → `/collections`
- Sale → `/collections/sale`
- Visit Us → `/pages/visit-us`

## Footer menu (`footer`)

Search, Your Privacy Choices, Size Guide, Questions, Visit Us, About, Contact. Shopify policy links are displayed separately by the footer when those policies are saved.

## Pages and template assignment

| Page handle | Custom template | Current state |
| --- | --- | --- |
| `about` | `about` | Created, visible, Default page until theme launch |
| `visit-us` | `visit-us` | Created, visible, Default page until theme launch |
| `questions` | `faq` | Created, visible, Default page until theme launch |
| `size-guide` | `size-guide` | Created, visible, Default page until theme launch |
| `contact` | `contact` | Existing page; preserve |
| `shop-the-look` | `shop-the-look` | Visible; four-look gallery renders in the draft through Default page until theme launch |

Only the live theme’s templates appear in Shopify’s page assignment menu. Assign the boutique templates after publishing the boutique theme. Until then, the four created pages have editable body content, and custom templates can be inspected through the draft theme editor. See [handoff.md](handoff.md) for product-field and app instructions.
