#!/usr/bin/env python3
"""Logo-forward, low-clutter pass (2026-10-16).

Edits the theme-editor JSON in place while keeping Shopify's auto-generated
comment header, so the GitHub <-> Shopify sync accepts the files untouched
otherwise. Idempotent: running it twice produces the same files.

Run from the repo root:  python3 scripts/declutter/apply-2026-10-16.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOGO_BLACK = "shopify://shop_images/beyoutiful-lockup-black-trim.png"
LOGO_WHITE = "shopify://shop_images/beyoutiful-lockup-white-trim.png"


def load(rel: str) -> tuple[str, dict]:
    text = (ROOT / rel).read_text()
    m = re.match(r"(\s*/\*.*?\*/\s*)", text, flags=re.S)
    header = m.group(1) if m else ""
    return header, json.loads(text[len(header):])


def save(rel: str, header: str, data: dict) -> None:
    (ROOT / rel).write_text(header + json.dumps(data, indent=2, ensure_ascii=False) + "\n")


# ---------- Global theme settings ----------
h, data = load("config/settings_data.json")
cur = data["current"]
cur.update(
    {
        "logo": LOGO_BLACK,          # full peacock lockup, tight crop (was wordmark-only with 50% padding)
        "logo_width": 220,            # desktop; mobile is capped in beau-bou.css
        "brand_image": LOGO_WHITE,    # footer brand block on the teal band
        "brand_image_width": 220,
        "brand_headline": "",
        "brand_description": "<p>Swimwear to formal wear. Women's XXS to 2X, plus kids and baby. Downtown Punta Gorda.</p>",
        "display_letter_spacing": 14,  # was 30: ultra-wide tracking read as templated
        "nav_letter_spacing": 10,
        "animations_hover_elements": "none",
    }
)
save("config/settings_data.json", h, data)

# ---------- Header ----------
h, data = load("sections/header-group.json")
hdr = data["sections"]["header"]["settings"]
hdr.update(
    {
        "logo_position": "top-center",      # logo owns the top row, menu sits on one line beneath
        "mobile_logo_position": "center",
        "show_inline_search": False,         # the boxed search field duplicated the search icon
        "show_line_separator": True,
        "padding_top": 12,
        "padding_bottom": 8,
    }
)
save("sections/header-group.json", h, data)

# ---------- Footer: white logo leads ----------
h, data = load("sections/footer-group.json")
ft = data["sections"]["footer"]
ft["blocks"]["brand"] = {"type": "brand_information", "settings": {"show_social": False}}
ft["block_order"] = ["brand"] + [b for b in ft["block_order"] if b != "brand"]
save("sections/footer-group.json", h, data)

# ---------- Homepage ----------
h, data = load("templates/index.json")
s = data["sections"]

hero = s["hero"]["settings"]
hero.update(
    {
        "logo": LOGO_BLACK,
        "logo_width": 600,
        "tagline": "",                 # logo + one button; faith line lives in the teal band
        "accent": "",
        "content_position": "center",
        "overlay_opacity": 0,          # the photo already has a white center made for the logo
        "show_frame": False,
        "padding_top": 0,
        "padding_bottom": 0,
    }
)

# One category grid instead of two stacked sections
tiles = s["tiles_1"]
tiles["blocks"].update(s["tiles_2"]["blocks"])
tiles["block_order"] = ["dresses", "tops", "jackets", "bottoms", "jewelry-accessories", "handbags"]
tiles["settings"].update({"title": "Shop by Category", "image_ratio": "1 / 1.15", "padding_top": 36, "padding_bottom": 36})
del s["tiles_2"]

# Product rows: one row, no per-card buttons
for key in ("whats_new", "sale"):
    s[key]["settings"].update({"products_to_show": 4, "quick_add": "none", "enable_desktop_slider": False, "heading_size": "h2"})

# Redundant with Shop Styles (both open /pages/shop-the-look); kept, just hidden
s["shop_the_look_banner"]["disabled"] = True

# Teal band: statement + accent + one button
brand = s["brand"]
brand["settings"].update({"show_ribbon": False, "eyebrow": "", "padding_top": 64, "padding_bottom": 64})
brand["blocks"] = {}
brand["block_order"] = []

data["order"] = ["hero", "shop_styles", "tiles_1", "whats_new", "brand", "sale", "visit", "shop_the_look_banner"]
save("templates/index.json", h, data)

print("applied")
