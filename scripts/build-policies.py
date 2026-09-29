#!/usr/bin/env python3
"""Build downloadable copies of the store policies (PDF + Word) from docs/policies/downloads/src/*.html.

Usage:  pip install python-docx htmldocx && python3 scripts/build-policies.py
Output: docs/policies/downloads/  (one .pdf and .docx per policy, All-Policies.pdf, Be-YOU-tiful-Policies.zip)
PDFs are printed with headless Chromium (CHROME env var, default /opt/pw-browsers/chromium).
"""
import html
import os
import pathlib
import re
import subprocess
import tempfile
import zipfile

from docx import Document
from docx.shared import Pt, RGBColor
from htmldocx import HtmlToDocx

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "docs/policies/downloads/src"
OUT = ROOT / "docs/policies/downloads"
CHROME = os.environ.get("CHROME", "/opt/pw-browsers/chromium")
STORE = "Be-YOU-tiful Boutique by Michele"
FOOTER = "264 W Marion Ave, Punta Gorda, FL 33950 · (941) 369-1628 · beyoutifulboutiquebymichele@gmail.com"
TEAL = "#3d7b88"

CSS = f"""
@page {{ size: Letter; margin: 0.8in 0.9in; }}
body {{ font: 11pt/1.55 Georgia, 'Times New Roman', serif; color: #1c1c1c; }}
header {{ border-bottom: 2px solid {TEAL}; padding-bottom: 10px; margin-bottom: 22px; }}
.store {{ font: 600 9pt/1 Helvetica, Arial, sans-serif; letter-spacing: .14em; text-transform: uppercase; color: {TEAL}; }}
h1 {{ font: 400 24pt/1.2 Georgia, serif; margin: 8px 0 0; }}
h2 {{ font: 700 12pt/1.3 Helvetica, Arial, sans-serif; margin: 20px 0 6px; }}
p, li {{ margin: 0 0 9px; }}
a {{ color: {TEAL}; }}
footer {{ margin-top: 28px; padding-top: 10px; border-top: 1px solid #ddd; font: 8.5pt/1.4 Helvetica, Arial, sans-serif; color: #666; }}
.page {{ page-break-after: always; }} .page:last-child {{ page-break-after: auto; }}
"""


def title_of(path: pathlib.Path) -> str:
    return re.sub(r"^\d+-", "", path.stem).replace("-", " ").title()


def page(title: str, body: str) -> str:
    return (f'<section class="page"><header><div class="store">{STORE}</div><h1>{html.escape(title)}</h1></header>'
            f'{body}<footer>{FOOTER}</footer></section>')


def pdf(markup: str, dest: pathlib.Path) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as tmp:
        tmp.write(f"<!doctype html><meta charset=utf-8><style>{CSS}</style>{markup}")
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={dest}", f"file://{tmp.name}"], check=True, capture_output=True)
    os.unlink(tmp.name)


def docx(title: str, body: str, dest: pathlib.Path) -> None:
    doc = Document()
    doc.styles["Normal"].font.name = "Georgia"
    doc.styles["Normal"].font.size = Pt(11)
    eyebrow = doc.add_paragraph().add_run(STORE.upper())
    eyebrow.font.size, eyebrow.font.bold = Pt(9), True
    eyebrow.font.color.rgb = RGBColor(0x3D, 0x7B, 0x88)
    doc.add_heading(title, level=1)
    HtmlToDocx().add_html_to_document(body, doc)
    doc.add_paragraph().add_run(FOOTER).font.size = Pt(8.5)
    doc.save(dest)


def main() -> None:
    sources = sorted(SRC.glob("*.html"))
    made, pages = [], []
    for src in sources:
        title, body, name = title_of(src), src.read_text(), re.sub(r"^\d+-", "", src.stem)
        pages.append(page(title, body))
        for ext, build in ((".pdf", lambda d: pdf(page(title, body), d)), (".docx", lambda d: docx(title, body, d))):
            dest = OUT / f"{name}{ext}"
            build(dest)
            made.append(dest)
    combined = OUT / "All-Policies.pdf"
    pdf("".join(pages), combined)
    made.append(combined)
    bundle = OUT / "Be-YOU-tiful-Policies.zip"
    with zipfile.ZipFile(bundle, "w", zipfile.ZIP_DEFLATED) as z:
        for f in made:
            z.write(f, f"Be-YOU-tiful-Policies/{f.name}")
    for f in made + [bundle]:
        print(f"✓ {f.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
