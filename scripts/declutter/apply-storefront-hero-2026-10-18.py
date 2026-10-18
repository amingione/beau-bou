#!/usr/bin/env python3
"""Storefront hero (2026-10-18).

Amber's call: keep the storefront photo with the peacock logo on it, logo bigger.
The logo is part of the artwork, so the overlaid logo, heading, tagline and accent
are cleared; the image shows uncropped with the button below it. Phones get the
square 1080x1080 version via the section's image_mobile setting.

Idempotent. Run from anywhere:  python3 scripts/declutter/apply-storefront-hero-2026-10-18.py
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

data["sections"]["hero"]["settings"].update(
    {
        "image": "shopify://shop_images/beyoutiful-storefront-hero-desktop.webp",
        "image_mobile": "shopify://shop_images/beyoutiful-storefront-hero-mobile-1080.webp",
        "content_below_image": True,  # uncropped artwork, button underneath
        "logo": "",                   # logo is already in the artwork
        "heading": "",
        "tagline": "",
        "accent": "",
        "show_frame": False,
        "full_width": True,
        "padding_top": 0,
        "padding_bottom": 0,
    }
)

(ROOT / REL).write_text(header + json.dumps(data, indent=2, ensure_ascii=False) + "\n")
print("applied")
