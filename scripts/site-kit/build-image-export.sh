#!/usr/bin/env bash
# Image export for moving the site to Michele's store (xapm2f-fr).
# Downloads every image the site uses from the test store's CDN, sorted by where it goes:
#   1-files/              → Content → Files (keep filenames; the theme finds them by name)
#   2-collection-images/  → each collection's image (Products → Collections → <name> → Image)
#   3-looks/looks.csv     → Content → Metaobjects → Look (title + image; the photos are in 1-files)
# Usage: bash scripts/site-kit/build-image-export.sh "<output dir>"     Docs: scripts/site-kit/README.md
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OUT="${1:?usage: build-image-export.sh <output dir>}"
mkdir -p "$OUT"/{1-files,2-collection-images,3-looks}
fail=0
grep -v '^\s*#' "$ROOT/scripts/site-kit/store-files.txt" | grep -v '^\s*$' | while read -r url; do
  f="$(basename "$url")"
  curl -fsSL -m 60 "$url" -o "$OUT/1-files/$f" || { echo "  ! not found: $f"; rm -f "$OUT/1-files/$f"; }
done
cp "$ROOT/docs/client-portal/brand/png/favicon-512.png" "$OUT/1-files/beyoutiful-favicon-512.png" 2>/dev/null || echo "  ! favicon not in repo"
tail -n +2 "$ROOT/scripts/site-kit/collection-images.csv" | python3 -c '
import csv,sys,subprocess,os
out=sys.argv[1]
for h,t,rule,f,alt,url in csv.reader(sys.stdin):
    dest=os.path.join(out,"2-collection-images",h+os.path.splitext(f)[1])
    r=subprocess.run(["curl","-fsSL","-m","60",url,"-o",dest])
    if r.returncode: print("  ! not found:",url)
' "$OUT"
cp "$ROOT/scripts/site-kit/collection-images.csv" "$OUT/2-collection-images/"
cp "$ROOT/scripts/site-kit/looks.csv" "$OUT/3-looks/"
cp "$ROOT/scripts/site-kit/IMAGE-EXPORT.md" "$OUT/README.md"
echo "✓ $(ls "$OUT/1-files" | wc -l | tr -d ' ') files, $(ls "$OUT/2-collection-images" | grep -vc csv) collection images → $OUT"
