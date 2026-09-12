#!/usr/bin/env python3
"""
Swap Michele's real photos into the theme's image slots.

1. Drop her photos into docs/images/photos-in/ (any filenames).
2. Edit docs/images/photo-map.json — one line per slot: which incoming file
   fills which slot. Unmapped slots keep their placeholder.
3. Run:  python3 scripts/swap-photos.py            → writes docs/images/final/
         python3 scripts/swap-photos.py --upload   → also prints the Shopify
            Files upload plan (stagedUploadsCreate input JSON) for the MCP flow.

Output files use the SAME filenames the theme already references
(shopify://shop_images/beyoutiful-<slot>.jpg), so re-uploading them to Files
with duplicateResolutionMode: REPLACE updates every page with no template edits.

Crops are smart-centered (entropy-free, plain center crop with a top bias for
portraits so heads don't get clipped). Adjust `bias` per slot in the map if needed.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
IN = ROOT / "docs/images/photos-in"
OUT = ROOT / "docs/images/final"
MAP = ROOT / "docs/images/photo-map.json"

# slot -> (width, height)
SLOTS: dict[str, tuple[int, int]] = {
    "hero-storefront": (2400, 1000),
    "tile-swimsuits": (1200, 1380),
    "tile-dresses": (1200, 1380),
    "tile-gowns": (1200, 1380),
    "tile-tops": (1200, 1380),
    "tile-bottoms": (1200, 1380),
    "tile-jewelry-accessories": (1200, 1380),
    "storefront-marion-ave": (1200, 1500),
    "michele-portrait": (1200, 1500),
    "shop-the-look-poster": (1200, 1500),
    **{f"collection-{s}": (2400, 800) for s in ["new-arrivals", "swimsuits", "dresses", "gowns", "tops", "bottoms", "jewelry-accessories", "sale", "live-picks"]},
}


def crop_fit(img: Image.Image, size: tuple[int, int], bias: float = 0.4) -> Image.Image:
    """Cover-crop to `size`; bias 0 = top, 0.5 = center, 1 = bottom (vertical only)."""
    img = ImageOps.exif_transpose(img).convert("RGB")
    tw, th = size
    scale = max(tw / img.width, th / img.height)
    img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
    left = (img.width - tw) // 2
    top = round((img.height - th) * bias)
    return img.crop((left, top, left + tw, top + th))


def main() -> None:
    if not MAP.exists():
        MAP.write_text(json.dumps({slot: {"file": "", "bias": 0.4} for slot in SLOTS}, indent=2) + "\n")
        print(f"Wrote starter map → {MAP}. Fill in `file` for each slot, then re-run.")
        return
    mapping = json.loads(MAP.read_text())
    OUT.mkdir(parents=True, exist_ok=True)
    plan = []
    for slot, spec in mapping.items():
        if slot not in SLOTS or not spec.get("file"):
            continue
        src = IN / spec["file"]
        if not src.exists():
            print(f"!! {slot}: {src.name} not found in photos-in/")
            continue
        out = OUT / f"beyoutiful-{slot}.jpg"
        crop_fit(Image.open(src), SLOTS[slot], float(spec.get("bias", 0.4))).save(out, quality=88, optimize=True, progressive=True)
        plan.append({"resource": "IMAGE", "filename": out.name, "mimeType": "image/jpeg", "httpMethod": "POST", "fileSize": str(os.path.getsize(out))})
        print(f"✓ {slot:32s} ← {src.name}")
    if "--upload" in sys.argv:
        print("\nstagedUploadsCreate input:\n" + json.dumps({"input": plan}, indent=1))
        print("\nThen fileCreate each with duplicateResolutionMode: REPLACE and the same filename.")


if __name__ == "__main__":
    main()
