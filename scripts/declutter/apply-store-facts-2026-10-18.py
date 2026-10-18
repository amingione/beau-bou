#!/usr/bin/env python3
"""Store facts, corrected by Amber 2026-10-18. Idempotent; run from the repo root.

  Address: 264 W Marion Ave, Punta Gorda, FL 33950 (no "-A")
  Hours:   Mon 11AM–4PM · Tue–Fri 10AM–5PM · Sat 10AM–4PM · Sun 10AM–3PM
  Phone:   (941) 369-1628      Sizes: XXS–2X

Touches live theme files, the policy builder and the current docs. Dated records (meeting packets,
QA pass, contract transcription, client-portal decisions) stay as written: they record what was true
on their date.

  python3 scripts/declutter/apply-store-facts-2026-10-18.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FILES = [
    *sorted((ROOT / "sections").glob("*.liquid")),
    *sorted((ROOT / "sections").glob("*.json")),
    *sorted((ROOT / "templates").rglob("*.json")),
    *sorted((ROOT / "snippets").glob("*.liquid")),
    ROOT / "config/settings_schema.json",
    ROOT / "config/settings_data.json",
    ROOT / "scripts/build-policies.py",
    ROOT / "scripts/placeholders.py",
    *sorted((ROOT / "docs/policies").rglob("*.md")),
    *sorted((ROOT / "docs/policies/downloads/src").glob("*.html")),
    ROOT / "docs/handoff.md",
    ROOT / "docs/launch/claude-code-launch-prompt.md",
    ROOT / "docs/preview/index.html",
    ROOT / "docs/preview/artifact.html",
    ROOT / "README.md",
]

RULES: list[tuple[re.Pattern[str], str]] = [
    # 264-A W Marion → 264 W Marion (Amber, 2026-10-18: no "-A")
    (re.compile(r"\b264-A W(est)? Marion"), r"264 W\1 Marion"),
    # Sunday 11–3 → 10–3, in the formats the theme and docs use
    (re.compile(r"(Sunday(?::\s*</strong>|</strong>:?|:)?\s*)11AM – 3PM"), r"\g<1>10AM – 3PM"),
    (re.compile(r'("days": "Sunday",\s*"hours": ")11AM – 3PM'), r"\g<1>10AM – 3PM"),
    (re.compile(r"Sun 11–3"), "Sun 10–3"),
    (re.compile(r"Sunday 11–3"), "Sunday 10–3"),
    (re.compile(r"Sunday 11 ?(?:am|AM) ?– ?3 ?(?:pm|PM)"), "Sunday 10AM – 3PM"),
]

changed = []
for f in FILES:
    if not f.exists():
        continue
    text = f.read_text()
    new = text
    for pat, rep in RULES:
        new = pat.sub(rep, new)
    # multi-line JSON: "days": "Sunday", newline, "hours": "11AM – 3PM"
    new = re.sub(r'("days": "Sunday",\s*\n\s*"hours": ")11AM – 3PM', r"\g<1>10AM – 3PM", new)
    if new != text:
        f.write_text(new)
        changed.append(str(f.relative_to(ROOT)))
print("\n".join(changed) or "no changes")
