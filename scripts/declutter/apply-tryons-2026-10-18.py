#!/usr/bin/env python3
"""Homepage "Shop Our Highlights": Amber's polished try-ons (2026-10-18).

The looks themselves are Look metaobjects in the store (7 new ones made from photos-in/looks-haul, the
4 older runway-cutout Looks set to Draft). This script only swaps the section's Extra photo blocks:
the 6 raw selfie try-ons go, and the second fit of the tropical bell-sleeve dress is added, linking to
that dress's look page. Keeps Shopify's comment header. Idempotent.

Run from the repo root:  python3 scripts/declutter/apply-tryons-2026-10-18.py
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
sec = data["sections"]["shop_styles"]

sec["blocks"] = {
    "tropical_second_fit": {
        "type": "photo",
        "settings": {
            "image": "shopify://shop_images/beyoutiful-tryon-tropical-bell-sleeve-shift-dress-b.webp",
            "title": "",
            "link": "/pages/looks/tropical-bell-sleeve-dress",
        },
    }
}
sec["block_order"] = ["tropical_second_fit"]

(ROOT / REL).write_text(header + json.dumps(data, indent=2, ensure_ascii=False) + "\n")
print("shop_styles extra photos:", sec["block_order"])
