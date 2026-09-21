#!/usr/bin/env python3
"""
cutouts.py — turn styled outfit photos into runway-ready cutouts.

  photos-in/tops:bottoms:outfitStyles/*.webp  →  photos-in/looks/<name>-cutout.webp
                                              →  docs/looks/looks.json (manifest, merged — hand edits survive)

Pipeline per image: 2× Lanczos upsample (the FB thumbnails are 414px) → rembg
(isnet-general-use) → alpha trim → tight bottom-aligned canvas → soft ground shadow
(full-body) or a faded crop line (waist-up; detected by bottom-edge width, overridable).
Transparent WebP out. Re-runnable: skips outputs newer than their source unless --force.

Usage:
  python3 scripts/cutouts.py                # process everything new
  python3 scripts/cutouts.py --force        # redo all
  python3 scripts/cutouts.py --only blue    # substring filter
Requires: pip install rembg onnxruntime pillow
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "docs/images/photos-in/tops:bottoms:outfitStyles"
OUT = ROOT / "docs/images/photos-in/looks"
MANIFEST = ROOT / "docs/looks/looks.json"

MIN_RATIO = 0.42               # canvas w:h never narrower than this (≈ a standing figure)
FIGURE_HEIGHT = 0.90           # figure fills 90% of canvas height
UPSCALE = 2                    # FB thumbnails are 414px; segment at 828px
SHADOW = True


def titleize(stem: str) -> str:
    s = re.sub(r"^beyoutiful-", "", stem)
    s = re.sub(r"-(cutout|store-model|mirror-selfie|model)$", "", s)
    words = s.split("-")
    fixes = {"t": "T-", "shirt": "Shirt"}
    out = []
    skip = False
    for i, w in enumerate(words):
        if skip:
            skip = False
            continue
        if w == "t" and i + 1 < len(words) and words[i + 1] == "shirt":
            out.append("T-Shirt")
            skip = True
        else:
            out.append(w.capitalize())
    return " ".join(out)


def ground_shadow(size: tuple[int, int], figure_box: tuple[int, int, int, int]) -> Image.Image:
    """Soft ellipse under the feet — sells the 'standing on a runway' read."""
    W, H = size
    x0, y0, x1, y1 = figure_box
    fw = x1 - x0
    sh = Image.new("L", (W, H), 0)
    from PIL import ImageDraw
    d = ImageDraw.Draw(sh)
    cx = (x0 + x1) // 2
    ry = max(6, int(fw * 0.09))
    rx = int(fw * 0.42)
    d.ellipse((cx - rx, y1 - ry, cx + rx, y1 + ry), fill=140)
    sh = sh.filter(ImageFilter.GaussianBlur(radius=max(4, fw * 0.06)))
    layer = Image.new("RGBA", (W, H), (20, 20, 24, 0))
    layer.putalpha(sh)
    return layer


def process(src: Path, dst: Path, session, force_full: bool | None = None) -> dict:
    from rembg import remove

    im = Image.open(src).convert("RGB")
    if UPSCALE > 1:
        im = im.resize((im.width * UPSCALE, im.height * UPSCALE), Image.LANCZOS)
    cut = remove(im, session=session, post_process_mask=True).convert("RGBA")

    # trim to alpha bbox (ignore faint halo)
    alpha = cut.getchannel("A").point(lambda a: 255 if a > 24 else 0)
    bbox = alpha.getbbox()
    if not bbox:
        raise RuntimeError(f"no subject found in {src.name}")
    # Full-body vs waist-up: measure how wide the subject is along its bottom edge.
    # Feet/ankles are narrow (< ~45% of the figure's width); a torso cut by the frame is wide.
    cut = cut.crop(bbox)
    a_np = cut.getchannel("A")
    band = a_np.crop((0, max(0, cut.height - 6), cut.width, cut.height)).point(lambda v: 255 if v > 24 else 0)
    band_bbox = band.getbbox()
    bottom_w = (band_bbox[2] - band_bbox[0]) if band_bbox else 0
    touches_edge = bbox[3] >= im.height * 0.985
    full_body = (bottom_w / cut.width) < 0.45 or not touches_edge
    if force_full is not None:
        full_body = force_full
    if not full_body:
        # fade the crop line out instead of faking a floor under it
        fade_px = max(24, int(cut.height * 0.14))
        a = cut.getchannel("A")
        grad = Image.linear_gradient("L").resize((cut.width, fade_px))  # 0 → 255 top→bottom
        grad = grad.point(lambda v: 255 - v)                            # 255 → 0
        mask = Image.new("L", cut.size, 255)
        mask.paste(grad, (0, cut.height - fade_px))
        from PIL import ImageChops
        cut.putalpha(ImageChops.multiply(a, mask))

    # canvas hugs the figure: width = figure + room for the ground shadow, never narrower than
    # MIN_RATIO of the height. The runway cards size themselves to this aspect, so tight = dense.
    fig_h = cut.height
    H = int(fig_h / FIGURE_HEIGHT)
    W = max(int(cut.width * 1.28), int(H * MIN_RATIO))
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    x = (W - cut.width) // 2
    y = H - cut.height - int(H * 0.04)
    if SHADOW and full_body:
        canvas.alpha_composite(ground_shadow((W, H), (x, y, x + cut.width, y + cut.height)))
    canvas.alpha_composite(cut, (x, y))

    dst.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(dst, "WEBP", quality=90, method=6)
    return {"width": W, "height": H, "full_body": full_body}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only", default="")
    args = ap.parse_args()

    from rembg import new_session
    session = new_session("isnet-general-use")

    manifest: dict = {"looks": []}
    if MANIFEST.exists():
        manifest = json.loads(MANIFEST.read_text())
    by_handle = {l["handle"]: l for l in manifest["looks"]}
    # Hand overrides for the full-body heuristic: {"overrides": {"<handle>": {"full_body": true}}}
    overrides: dict = manifest.setdefault("overrides", {})

    srcs = sorted(p for p in SRC.glob("*.webp") if args.only in p.name)
    done = 0
    for src in srcs:
        handle = re.sub(r"^beyoutiful-", "", src.stem)
        dst = OUT / f"{src.stem}-cutout.webp"
        fresh = dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime
        if fresh and not args.force:
            info = None
        else:
            info = process(src, dst, session, overrides.get(handle, {}).get("full_body"))
            done += 1
            print(f"✔ {dst.name} {info['width']}×{info['height']} {'full-body' if info['full_body'] else 'waist-up'}")
        entry = by_handle.get(handle) or {
            "handle": handle,
            "title": titleize(src.stem),
            "caption": "",
            "pieces": [],
            "goes_with": [],
            "featured": True,
            "sort": len(by_handle) + 1,
        }
        entry["source"] = str(src.relative_to(ROOT))
        entry["cutout"] = str(dst.relative_to(ROOT))
        if info is not None:
            entry["full_body"] = info["full_body"]
        by_handle[handle] = entry

    manifest["looks"] = sorted(by_handle.values(), key=lambda l: l["sort"])
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"{done} processed · {len(manifest['looks'])} looks in {MANIFEST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
