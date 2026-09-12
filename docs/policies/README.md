# Store policies

Text for Shopify **Settings → Policies** on Michele's store (Refund/Shipping, Privacy, Terms). Not applied to Amber's dev store `kw59hc-k1` — policies there belong to another business.

Apply by hand in admin, or via Admin API `shopPolicyUpdate` with `type: REFUND_POLICY | PRIVACY_POLICY | TERMS_OF_SERVICE` and the HTML of each file. The theme footer links to `/policies/refund-policy`, `/policies/privacy-policy`, `/policies/terms-of-service`.
