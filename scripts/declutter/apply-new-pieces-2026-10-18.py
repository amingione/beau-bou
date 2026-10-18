#!/usr/bin/env python3
"""Homepage updates for Amber's "new pieces" photos (2026-10-18).

- Shop Our Highlights shows up to 14 looks (13 Looks now: 7 from looks-haul + 6 from "new peices").
- Collections row: Baby & Toddler tile uses beyoutiful-category-baby-toddler.webp (the soft baby books),
  set on the tile itself so it carries over to Michele's store with the theme.
Keeps Shopify's comment header. Idempotent.

  python3 scripts/declutter/apply-new-pieces-2026-10-18.py
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

ss = data["sections"]["shop_styles"]["settings"]
ss["max_looks"] = 14
ss["carousel_count"] = 16

tiles = data["sections"]["collections"]["blocks"]
if "baby-toddler" in tiles:
    tiles["baby-toddler"]["settings"]["image"] = "shopify://shop_images/beyoutiful-category-baby-toddler.webp"

(ROOT / REL).write_text(header + json.dumps(data, indent=2, ensure_ascii=False) + "\n")
print("max_looks", ss["max_looks"], "| baby-toddler tile:", tiles.get("baby-toddler", {}).get("settings", {}).get("image"))
