#!/usr/bin/env python3
"""Homepage: "Shop the brands we carry" logo grid (2026-10-18), after the Collections carousel.

Brands from Michele's contract: Samuel Dong, Frank Lyman, Dolcezza, Silver. The first three have
collections; Silver links to Shopify's vendor page. Logos show as wordmarks until files are uploaded
(Theme editor → Brand logos → each Brand → Logo). Keeps Shopify's comment header. Idempotent.

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
    ("samuel_dong", "Samuel Dong", "samuel-dong", ""),
    ("frank_lyman", "Frank Lyman", "frank-lyman", ""),
    ("dolcezza", "Dolcezza", "dolcezza", ""),
    ("silver", "Silver", "", "/collections/vendors?q=Silver"),
]
existing = s.get("brands", {}).get("blocks", {})
s["brands"] = {
    "type": "brand-logos",
    "blocks": {
        key: {
            "type": "brand",
            "settings": {
                "name": name,
                # keep a logo someone already uploaded in the editor
                "logo": existing.get(key, {}).get("settings", {}).get("logo", ""),
                "collection": handle,
                "link": link,
            },
        }
        for key, name, handle, link in brands
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
