#!/usr/bin/env python3
"""Tight-crop a transparent logo and emit a white knockout of it.

Usage:
  python3 scripts/declutter/trim-logo.py \
    docs/client-portal/brand/png-source/beyoutiful-lockup-black-source.png \
    docs/client-portal/brand/beyoutiful-lockup

Writes <prefix>-black-trim.png and <prefix>-white-trim.png.
Requires Pillow (pip install pillow).
"""
from __future__ import annotations

import sys
from PIL import Image

ALPHA_FLOOR = 24   # ignore near-invisible antialias haze when finding the bounds
MARGIN = 0.02      # breathing room, as a share of the longest side


def main(src: str, prefix: str) -> None:
    im = Image.open(src).convert("RGBA")
    mask = im.getchannel("A").point(lambda v: 255 if v > ALPHA_FLOOR else 0)
    box = mask.getbbox()
    if box is None:
        raise SystemExit("source has no visible pixels")
    pad = int(max(box[2] - box[0], box[3] - box[1]) * MARGIN)
    crop = im.crop((
        max(0, box[0] - pad), max(0, box[1] - pad),
        min(im.width, box[2] + pad), min(im.height, box[3] + pad),
    ))
    crop.save(f"{prefix}-black-trim.png", optimize=True)

    white = Image.new("L", crop.size, 255)
    Image.merge("RGBA", (white, white, white, crop.getchannel("A"))).save(
        f"{prefix}-white-trim.png", optimize=True
    )
    print(f"{crop.width}x{crop.height} -> {prefix}-black-trim.png, {prefix}-white-trim.png")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    main(sys.argv[1], sys.argv[2])
