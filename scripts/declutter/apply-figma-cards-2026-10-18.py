#!/usr/bin/env python3
"""Turn on the Figma cards (2026-10-18). Idempotent.

- Homepage "Shop by Category" (tiles_1) -> Card style (Figma node 37:211)
- All-collections page (/collections) -> Boutique card (Figma node 37:391)
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def edit(rel: str, fn) -> None:
    text = (ROOT / rel).read_text()
    m = re.match(r"(\s*/\*.*?\*/\s*)", text, flags=re.S)
    header = m.group(1) if m else ""
    data = json.loads(text[len(header):])
    fn(data)
    (ROOT / rel).write_text(header + json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print("updated", rel)


def home(d: dict) -> None:
    d["sections"]["tiles_1"]["settings"]["tile_style"] = "card"


def list_collections(d: dict) -> None:
    d["sections"]["main"]["settings"]["card_style"] = "drop"


edit("templates/index.json", home)
edit("templates/list-collections.json", list_collections)
