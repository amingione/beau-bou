# Collections & menus the theme expects

Create these **empty** collections in Michele's store before pushing the theme so the homepage tiles and sliders resolve. Handles must match exactly (Shopify derives the handle from the title; edit the URL handle field if it differs).

| Title | Handle | Used by |
| --- | --- | --- |
| New Arrivals | `new-arrivals` | Hero CTA, "Shop What's New" slider |
| Swimsuits | `swimsuits` | Category tile |
| Dresses | `dresses` | Category tile |
| Gowns | `gowns` | Category tile |
| Tops | `tops` | Category tile |
| Bottoms | `bottoms` | Category tile |
| Jewelry + Accessories | `jewelry-accessories` | Category tile |
| Sale | `sale` | "Sale" slider |
| Shop All | `all` | Built-in Shopify collection — nothing to create |

Suggested automated rules (Products → Collections → Automated):

- **New Arrivals**: Product tag equals `new` (Michele tags new drops; remove tag after 30 days) — or Created date within last 30 days once Shopify supports it in your plan.
- **Sale**: Compare-at price is greater than 0.
- Category collections: Product type equals the category name — then Michele only sets **Product type** when adding an item.

## Menus (Navigation)

**main-menu** (header) — mirrors the reference's two-row nav, sized for a boutique:

```
What's New            → /collections/new-arrivals
Best Sellers          → /collections/all?sort_by=best-selling
Swimsuits             → /collections/swimsuits
Dresses + Gowns       → /collections/dresses
  ├ Dresses           → /collections/dresses
  └ Gowns             → /collections/gowns
Tops                  → /collections/tops
Bottoms               → /collections/bottoms
Jewelry + Accessories → /collections/jewelry-accessories
Shop All              → /collections/all
SALE!                 → /collections/sale
Visit Us              → /pages/visit
```

**footer** menu (Help):

```
Contact Us          → /pages/contact
About Us            → /pages/about
Shipping & Returns  → /policies/refund-policy
Privacy Policy      → /policies/privacy-policy
```

## Pages

- `contact` — use template `page.contact` (Dawn contact form). Prefill heading "Any questions?"
- `about` — Michele's story; the FB intro line "Accept yourself as you were designed by God" belongs here.
- `visit` — add the **Visit our store** section via the editor (Add section → Visit our store).
