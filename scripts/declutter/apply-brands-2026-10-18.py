#!/usr/bin/env python3
"""Homepage: "Shop the brands we carry" logo grid (2026-10-18), after the Collections carousel.

Brands from Michele's contract: Samuel Dong, Frank Lyman, Dolcezza, Silver (Silver Jeans Co.). The first
three have collections; Silver links to Shopify's vendor page. Each uses its official logo, recolored black. Keeps Shopify's comment header. Idempotent.

Run from the repo root:  python3 scripts/declutter/apply-brands-2026-10-18.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REL = "templates/index.json"

text = (ROOT / REL).read_text()
m = re.match(r"(\s*/\*.*?\*/\s*)", text, flags=re.S)
header = m.group(1) if m else ""
data = json.loads(text[len(header):])
s = data["sections"]

brands = [
    # key, name, collection, link, logo (official logos from each brand's site, recolored black;
    # uploaded to Content → Files 2026-10-18, sources in photos-in/brand-logos/source)
    ("samuel_dong", "Samuel Dong", "samuel-dong", "", "beyoutiful-brand-samuel-dong.png"),
    ("frank_lyman", "Frank Lyman", "frank-lyman", "", "beyoutiful-brand-frank-lyman.png"),
    ("dolcezza", "Dolcezza", "dolcezza", "", "beyoutiful-brand-dolcezza.png"),
    ("silver", "Silver Jeans Co.", "", "/collections/vendors?q=Silver%20Jeans", "beyoutiful-brand-silver-jeans.png"),
]
existing = s.get("brands", {}).get("blocks", {})
s["brands"] = {
    "type": "brand-logos",
    "blocks": {
        key: {
            "type": "brand",
            "settings": {
                "name": name,
                # a logo picked in the editor wins over the default file
                "logo": existing.get(key, {}).get("settings", {}).get("logo") or f"shopify://shop_images/{logo}",
                "collection": handle,
                "link": link,
            },
        }
        for key, name, handle, link, logo in brands
    },
    "block_order": [b[0] for b in brands],
    "settings": {
        "heading": "Shop the brands we carry",
        "black_logos": True,
        "color_scheme": "scheme-2",
        "padding_top": 60,
        "padding_bottom": 60,
    },
}

order = [k for k in data["order"] if k != "brands"]
order.insert(order.index("collections") + 1, "brands")
data["order"] = order

(ROOT / REL).write_text(header + json.dumps(data, indent=2, ensure_ascii=False) + "\n")
print("applied:", " → ".join(data["order"]))
