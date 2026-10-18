#!/usr/bin/env python3
"""Homepage order (Amber, 2026-10-18): Shop What's New right under the hero with the logo,
Announcements last, just above the footer. Hidden sections keep their place at the end.
Keeps Shopify's comment header. Idempotent.

  python3 scripts/declutter/apply-home-order-2026-10-18.py
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

WANT = ["hero", "whats_new", "shop_styles", "collections", "brands", "brand", "sale", "visit", "announcements"]
order = [k for k in WANT if k in data["sections"]]
order += [k for k in data["order"] if k not in order]  # anything else (hidden sections) after
data["order"] = order
(ROOT / REL).write_text(header + json.dumps(data, indent=2, ensure_ascii=False) + "\n")
print(" → ".join(order))
