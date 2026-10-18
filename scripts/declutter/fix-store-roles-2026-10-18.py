#!/usr/bin/env python3
"""Correct the store-role claims (Amber, 2026-10-18).

v0m0hb-x3 = Amber's TEST store (preview the theme/app before handing to Michele).
xapm2f-fr = Michele's OWN store; shopbeyoutifulboutique.com is connected there, correctly.
The 2026-10-16 "domain warning" had this backwards. One-shot; asserts every target exists.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

FIXES = {
    "README.md": [(
        "Client store is `v0m0hb-x3` (served at shopbe-you-tifulboutique.myshopify.com; **shopbeyoutifulboutique.com is attached to a different store, `xapm2f-fr`**, verified 2026-10-16, see docs/design-clean-pass.md); the published theme is `beau-bou/main` (`192420839788`), synced from this repo's `main` branch through Shopify's GitHub integration (verified 2026-10-16) but the storefront is still password protected, so nothing is public yet.",
        "Stores: **`xapm2f-fr` is Michele's own store** and has her domain, shopbeyoutifulboutique.com (correctly connected). **`v0m0hb-x3` is Amber's test store** (shopbe-you-tifulboutique.myshopify.com), used to preview the theme and app before handing them to Michele. On the test store, the published theme is `beau-bou/main` (`192420839788`), synced from this repo's `main` branch through Shopify's GitHub integration; the storefront is password protected. Michele's store still runs an older theme copy (`be-you-tiful-boutique-theme-1-2-0`) until the finished theme is handed over.",
    )],
    "docs/launch/claude-code-launch-prompt.md": [(
        "store `v0m0hb-x3` (primary domain shopbe-you-tifulboutique.myshopify.com; shopbeyoutifulboutique.com currently points at a different store, `xapm2f-fr`, verified 2026-10-16)",
        "installed on Amber's **test** store `v0m0hb-x3` (shopbe-you-tifulboutique.myshopify.com). Michele's own store is `xapm2f-fr`, where shopbeyoutifulboutique.com is correctly connected; install the app there at handoff",
    )],
    "docs/handoff.md": [
        (
            "**Correct store:** `v0m0hb-x3` (served at `shopbe-you-tifulboutique.myshopify.com`). **Correction 2026-10-16:** `shopbeyoutifulboutique.com` is attached to a different store, `xapm2f-fr` (old image-less theme copy), not to `v0m0hb-x3`. Move the domain before launch; see [design-clean-pass.md](design-clean-pass.md). The live theme is now `beau-bou/main` (`192420839788`), synced from GitHub `main`.",
            "**Stores (confirmed by Amber 2026-10-18):** `v0m0hb-x3` (`shopbe-you-tifulboutique.myshopify.com`) is **Amber's test store**, used to preview the theme and app before handing them to Michele. Its published theme is `beau-bou/main` (`192420839788`), synced from GitHub `main`. **`xapm2f-fr` is Michele's own store**, and `shopbeyoutifulboutique.com` is connected there, correctly. Michele's store still runs an older theme copy (`be-you-tiful-boutique-theme-1-2-0`); the finished theme goes there at handoff. (A 2026-10-16 note claiming the domain needed to move to `v0m0hb-x3` was wrong and has been removed.)",
        ),
        (
            "- [ ] Domain: move `shopbeyoutifulboutique.com` from store `xapm2f-fr` to `v0m0hb-x3` (Settings → Domains), then verify",
            "- [x] Domain: `shopbeyoutifulboutique.com` is connected to Michele's store `xapm2f-fr` (correct; nothing to move)\n- [ ] Handoff: install the finished theme (and the app, if used) on Michele's store `xapm2f-fr`",
        ),
        (
            "- [VERIFIED] New client store: `v0m0hb-x3`; domain: `shopbeyoutifulboutique.com`.",
            "- [VERIFIED] Test store: `v0m0hb-x3` (Amber's, for previewing before handoff). Michele's own store is `xapm2f-fr`, with domain `shopbeyoutifulboutique.com` (corrected 2026-10-18).",
        ),
    ],
    "docs/looks.md": [(
        "were uploaded to the client store Files",
        "were uploaded to the test store (`v0m0hb-x3`) Files",
    )],
    "docs/rewards-program/Epos_Shopify_Product_Sync_Guide_2026-09-28.html": [(
        "(store handle v0m0hb-x3; the shopbeyoutifulboutique.com domain still has to be moved onto it, corrected 2026-10-16)",
        "(Michele's own store: handle xapm2f-fr, domain shopbeyoutifulboutique.com; v0m0hb-x3 is Amber's test store, corrected 2026-10-18)",
    )],
}

for rel, pairs in FIXES.items():
    p = ROOT / rel
    s = p.read_text()
    for old, new in pairs:
        assert old in s, f"{rel}: target not found: {old[:60]}"
        s = s.replace(old, new)
    p.write_text(s)
    print("fixed", rel)

# Replace the wrong "Domain warning" section in the design doc
p = ROOT / "docs/design-clean-pass.md"
s = p.read_text()
start = s.index("## Domain warning (found 2026-10-16)")
end = s.index("## Update 2026-10-18", start)
s = s[:start] + """## Stores (corrected 2026-10-18)

- `v0m0hb-x3` (`shopbe-you-tifulboutique.myshopify.com`) is **Amber's test store**. Everything in this pass was built and previewed there.
- `xapm2f-fr` is **Michele's own store**, and `shopbeyoutifulboutique.com` is connected to it, correctly. It still runs an older theme copy until handoff.
- An earlier version of this section said the domain had to move to `v0m0hb-x3`. That was wrong. Nothing needs to move; at handoff, the finished theme goes to `xapm2f-fr`.

""" + s[end:]
p.write_text(s)
print("fixed docs/design-clean-pass.md")
