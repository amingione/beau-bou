#!/usr/bin/env python3
"""
Generate the on-brand placeholder image set for Be-YOU-tiful Boutique.

Every slot the theme needs gets a styled, correctly-sized image so the store
reads as finished in preview. When Michele's real photos arrive, drop them in
docs/images/photos-in/ and run `scripts/swap-photos.py` — same filenames, same
slots, nothing else changes.

Usage:  python3 scripts/placeholders.py [out_dir]   (default docs/images/placeholders)
"""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC = HERE / "assets-src"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "docs/images/placeholders"
OUT.mkdir(parents=True, exist_ok=True)

INK = (43, 43, 43)
PAPER = (255, 255, 255)
LINEN = (246, 243, 238)
PEACOCK = (15, 95, 102)
BLUSH = (241, 226, 221)
HAIR = (26, 26, 26)

PF = str(SRC / "PlayfairDisplay-Regular.ttf")
PFI = str(SRC / "PlayfairDisplay-Italic.ttf")
POP = "/usr/share/fonts/truetype/google-fonts/Poppins-Regular.ttf"
POPM = "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"

BADGE_BLACK = Image.open(SRC / "badge-black.png").convert("RGBA")
BADGE_WHITE = Image.open(SRC / "badge-white.png").convert("RGBA")


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def tracked(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, fill, tracking: float, anchor_center=True):
    """Draw letter-spaced text (PIL has no tracking). Returns width."""
    widths = [draw.textlength(ch, font=fnt) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = xy[0] - total / 2 if anchor_center else xy[0]
    y = xy[1]
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += w + tracking
    return total


def linen_texture(img: Image.Image, strength: int = 6) -> Image.Image:
    """Very faint diagonal hairlines — reads as fabric, not as a pattern."""
    w, h = img.size
    tex = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(tex)
    step = 14
    for x in range(-h, w, step):
        d.line([(x, 0), (x + h, h)], fill=(0, 0, 0, strength), width=1)
    return Image.alpha_composite(img.convert("RGBA"), tex)


def frame(draw: ImageDraw.ImageDraw, size: tuple[int, int], inset: int, color=HAIR, width: int = 2):
    w, h = size
    draw.rectangle([inset, inset, w - inset, h - inset], outline=color, width=width)


def card(
    name: str,
    size: tuple[int, int],
    label: str,
    sub: str = "",
    bg=LINEN,
    ink=INK,
    badge: Image.Image | None = None,
    badge_scale: float = 0.22,
    eyebrow: str = "Be-YOU-tiful Boutique",
    watermark: bool = False,
):
    w, h = size
    img = Image.new("RGBA", size, bg + (255,))
    img = linen_texture(img, 7 if bg != PEACOCK else 10)
    d = ImageDraw.Draw(img)

    if watermark:
        b = (badge or BADGE_BLACK).copy()
        bw = int(w * 0.6)
        b = b.resize((bw, int(b.height * bw / b.width)), Image.LANCZOS)
        alpha = b.split()[3].point(lambda a: a * 0.045)
        b.putalpha(alpha)
        img.alpha_composite(b, (int((w - bw) / 2), int((h - b.height) / 2)))
        d = ImageDraw.Draw(img)

    inset = int(min(w, h) * 0.035)
    frame(d, size, inset, color=ink if bg != PEACOCK else PAPER)

    # badge
    if badge is not None and not watermark:
        bw = int(min(w, h) * badge_scale)
        b = badge.resize((bw, int(badge.height * bw / badge.width)), Image.LANCZOS)
        img.alpha_composite(b, (int((w - bw) / 2), int(h * 0.30 - b.height / 2)))
        d = ImageDraw.Draw(img)

    # eyebrow
    ey = font(POPM, int(min(w, h) * 0.022))
    tracked(d, (w / 2, h * 0.555 if badge is not None else h * 0.40), eyebrow.upper(), ey, ink, tracking=ey.size * 0.32)

    # label — shrink to fit 80% of the width, wrap to two lines if still too wide
    ly = h * 0.60 if badge is not None else h * 0.45
    ry = ly
    if label:
        lines = [label.upper()]
        size = int(min(w, h) * 0.095)
        while True:
            lf = font(PF, size)
            widest = max(sum(d.textlength(c, font=lf) for c in ln) + lf.size * 0.22 * (len(ln) - 1) for ln in lines)
            if widest <= w * 0.80 or size <= int(min(w, h) * 0.05):
                break
            if len(lines) == 1 and " " in label and size < int(min(w, h) * 0.08):
                words = label.upper().split()
                mid = len(words) // 2
                lines = [" ".join(words[:mid]), " ".join(words[mid:])]
                continue
            size -= 2
        y = ly
        for ln in lines:
            tracked(d, (w / 2, y), ln, lf, ink, tracking=lf.size * 0.22)
            y += lf.size * 1.3
        ry = y + lf.size * 0.25
        d.line([(w * 0.44, ry), (w * 0.56, ry)], fill=ink, width=2)

    # sub (italic accent)
    if sub:
        sf = font(PFI, int(min(w, h) * 0.038))
        d.text((w / 2, ry + sf.size * 0.8), sub, font=sf, fill=ink, anchor="ma")

    img.convert("RGB").save(OUT / f"{name}.jpg", quality=88, optimize=True, progressive=True)
    return OUT / f"{name}.jpg"


def main() -> None:
    made: list[Path] = []

    # Hero background (logo is overlaid by the theme; keep this quiet)
    made.append(card("hero-storefront", (2400, 1000), "", "", bg=LINEN, watermark=True, eyebrow=""))

    # Category tiles — portrait 1 / 1.15 (theme ratio), 1200 x 1380
    tiles = [
        ("tile-swimsuits", "Swimsuits", "Beach day to boat day", LINEN, INK, BADGE_BLACK),
        ("tile-dresses", "Dresses", "Brunch to date night", PAPER, INK, BADGE_BLACK),
        ("tile-gowns", "Gowns", "Gala, prom, mother of the bride", PEACOCK, PAPER, BADGE_WHITE),
        ("tile-tops", "Tops", "The piece you'll reach for", LINEN, INK, BADGE_BLACK),
        ("tile-bottoms", "Bottoms", "Denim, skirts, linen", PAPER, INK, BADGE_BLACK),
        ("tile-jewelry-accessories", "Jewelry + Accessories", "Finish the look", BLUSH, INK, BADGE_BLACK),
    ]
    for name, label, sub, bg, ink, badge in tiles:
        made.append(card(name, (1200, 1380), label, sub, bg=bg, ink=ink, badge=badge))

    # Storefront / About
    made.append(card("storefront-marion-ave", (1200, 1500), "264 W Marion Ave", "Historic downtown Punta Gorda", bg=PAPER, badge=BADGE_BLACK, eyebrow="Visit our store"))
    made.append(card("michele-portrait", (1200, 1500), "Michele", "Owner · stylist · your biggest fan", bg=LINEN, badge=BADGE_BLACK, eyebrow="Meet"))
    made.append(card("shop-the-look-poster", (1200, 1500), "Try-on Thursdays", "Live at 7PM on Facebook", bg=PEACOCK, ink=PAPER, badge=BADGE_WHITE, eyebrow="Shop the look"))

    # Collection banners 2400 x 800
    for slug, label, sub in [
        ("new-arrivals", "What's New", "Fresh this week"),
        ("swimsuits", "Swimsuits", "XXS – 2X · mix and match"),
        ("dresses", "Dresses", "Casual to cocktail"),
        ("gowns", "Gowns", "Special occasion, no special-occasion price"),
        ("tops", "Tops", "Blouses, tees, tanks"),
        ("bottoms", "Bottoms", "Denim, skirts, linen pants"),
        ("jewelry-accessories", "Jewelry + Accessories", "Earrings, totes, hats"),
        ("sale", "Sale", "Last chance, final sale"),
        ("live-picks", "Live Picks", "Everything from this week's live"),
    ]:
        made.append(card(f"collection-{slug}", (2400, 800), label, sub, bg=LINEN if slug != "sale" else PAPER, badge=None, eyebrow="Be-YOU-tiful Boutique"))

    # Sample products 1200 x 1500 (two angles: front + detail)
    products = [
        ("coral-tie-front-swim-set", "Coral Tie-Front Swim Set", "Swimsuits", LINEN),
        ("palm-breeze-maxi-dress", "Palm Breeze Maxi Dress", "Dresses", PAPER),
        ("marion-ave-linen-blouse", "Marion Ave Linen Blouse", "Tops", LINEN),
        ("harbor-nights-sequin-gown", "Harbor Nights Sequin Gown", "Gowns", PEACOCK),
        ("sunset-stripe-one-piece", "Sunset Stripe One-Piece", "Swimsuits", PAPER),
        ("charlotte-harbor-wrap-dress", "Charlotte Harbor Wrap Dress", "Dresses", LINEN),
        ("gold-leaf-drop-earrings", "Gold Leaf Drop Earrings", "Jewelry", BLUSH),
        ("emerald-satin-gown", "Emerald Satin Gown", "Gowns", PEACOCK),
        ("fishermen-village-wide-leg-pant", "Fishermen's Village Wide-Leg Pant", "Bottoms", LINEN),
        ("peacock-print-kimono", "Peacock Print Kimono", "Tops", PAPER),
        ("gilchrist-park-denim-skirt", "Gilchrist Park Denim Skirt", "Bottoms", LINEN),
        ("straw-market-tote", "Straw Market Tote", "Accessories", BLUSH),
    ]
    for slug, title, cat, bg in products:
        ink = PAPER if bg == PEACOCK else INK
        badge = BADGE_WHITE if bg == PEACOCK else BADGE_BLACK
        made.append(card(f"product-{slug}-1", (1200, 1500), title, cat, bg=bg, ink=ink, badge=badge, badge_scale=0.16, eyebrow="Photo coming soon"))
        made.append(card(f"product-{slug}-2", (1200, 1500), "Detail", title, bg=PAPER if bg != PAPER else LINEN, ink=INK, badge=None, eyebrow=cat))

    print(f"{len(made)} images → {OUT}")


if __name__ == "__main__":
    main()
