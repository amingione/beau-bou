#!/usr/bin/env python3
"""Homepage: Figma landing sections (2026-10-18).

Adds Announcements (mailing-list slide first) under the hero, switches Shop Styles to the
Highlights layout, adds the Collections carousel, and hides (does not delete) the old
Shop by Category grid. Keeps Shopify's comment header. Idempotent.

Run from the repo root:  python3 scripts/declutter/apply-landing-sections-2026-10-18.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REL = "templates/index.json"


def load() -> tuple[str, dict]:
    text = (ROOT / REL).read_text()
    m = re.match(r"(\s*/\*.*?\*/\s*)", text, flags=re.S)
    header = m.group(1) if m else ""
    return header, json.loads(text[len(header):])


header, data = load()
s = data["sections"]

# ---------- Announcements (Figma 1:612) ----------
s["announcements"] = {
    "type": "announcement-spotlight",
    "blocks": {
        "join_list": {
            "type": "slide",
            "settings": {
                "image": "shopify://shop_images/beyoutiful-join-the-list-announcement.webp",
                "show_whole_image": True,
                "media_bg": "#e6e6e6",  # matches the paper texture in Michele's graphic
                "eyebrow": "",
                "heading": "Join the list",
                "text": "<p>Be the first to know when new pieces land at the boutique.</p>",
                "show_signup": True,
                "signup_button": "Join the list",
                "signup_success": "You're on the list. Thank you!",
                "link_label": "Shop new arrivals",
                "link": "/collections/new-arrivals",
            },
        }
    },
    "block_order": ["join_list"],
    "settings": {
        "label": "Announcements",
        "autoplay_seconds": 7,
        "height": 520,
        "color_scheme": "scheme-2",
        "padding_top": 0,
        "padding_bottom": 0,
    },
}

# ---------- Shop Styles → Highlights (Figma 1:159) ----------
s["shop_styles"]["settings"].update(
    {
        "layout": "highlights",
        "heading": "Shop Our Highlights",
        "intro": "<p>Try-on looks styled right here in the boutique. Tap one to shop every piece, plus a few that pair with it.</p>",
        "badge_label": "Shop the look",
        "badge_color": "#e60023",
        "button_label": "Shop the pieces",
        "button_link": "/pages/shop-the-look",
        "max_looks": 10,
        "color_scheme": "scheme-2",
        "padding_top": 60,
        "padding_bottom": 60,
    }
)

# ---------- Collections carousel (Figma 1:135) ----------
# Pictures reuse the old category grid's photos; collections without one show just the name.
tile_images = {
    k: b["settings"].get("image", "")
    for k, b in s.get("tiles_1", {}).get("blocks", {}).items()
}
handles = ["dresses", "tops", "bottoms", "jackets", "handbags", "jewelry-accessories", "swimsuits", "kids", "baby-toddler"]
s["collections"] = {
    "type": "collection-carousel",
    "blocks": {
        h: {"type": "collection", "settings": {"collection": h, "image": tile_images.get(h, ""), "label": "", "link": ""}}
        for h in handles
    },
    "block_order": handles,
    "settings": {
        "heading": "Collections",
        "tile_style": "square",
        "card_button_label": "Shop now",
        "button_label": "Shop all",
        "button_link": "/collections",
        "color_scheme": "scheme-1",
        "padding_top": 60,
        "padding_bottom": 60,
    },
}

# The carousel replaces the Shop by Category grid on the homepage; keep it, hidden.
if "tiles_1" in s:
    s["tiles_1"]["disabled"] = True

order = ["hero", "announcements", "shop_styles", "collections", "whats_new", "brand", "sale", "visit"]
data["order"] = order + [k for k in data["order"] if k not in order]

(ROOT / REL).write_text(header + json.dumps(data, indent=2, ensure_ascii=False) + "\n")
print("applied:", " → ".join(data["order"]))
