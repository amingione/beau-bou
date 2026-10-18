#!/usr/bin/env bash
# Build the complete Be-YOU-tiful site kit: theme zip + store Files + collection images list + looks + policies.
# Usage: bash scripts/build-site-kit.sh      → dist/Be-YOU-tiful-Boutique-site-kit.zip
# Needs: Shopify CLI (npx), curl, zip. Docs: scripts/site-kit/README.md
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/dist"
KIT="$OUT/Be-YOU-tiful-Boutique-site-kit"
NAME="Be-YOU-tiful-Boutique-site-kit.zip"

rm -rf "$KIT" "$OUT/$NAME"
mkdir -p "$KIT"/{1-theme,2-store-files,3-collection-images,4-looks,5-policies}

echo "→ Packaging theme"
( cd "$ROOT" && npx -y @shopify/cli@3 theme package --path . >/dev/null )
mv "$ROOT"/*.zip "$KIT/1-theme/Be-YOU-tiful-Boutique-theme.zip"

echo "→ Downloading store files"
grep -v '^\s*#' "$ROOT/scripts/site-kit/store-files.txt" | grep -v '^\s*$' | while read -r url; do
  file="$(basename "${url%%\?*}")"
  curl -fsSL "$url" -o "$KIT/2-store-files/$file" || echo "  ! failed: $file"
done
# Favicon referenced by settings but kept in the repo's brand folder, not store Files.
cp "$ROOT/docs/client-portal/brand/png/favicon-512.png" "$KIT/2-store-files/beyoutiful-favicon-512.png"

echo "→ Products, looks, policies"
# TEST products were archived 2026-10-18; collection images and looks come from the image export manifests
cp "$ROOT/scripts/site-kit/collection-images.csv" "$KIT/3-collection-images/"
cp "$ROOT/scripts/site-kit/looks.csv" "$KIT/4-looks/"
cp "$ROOT/docs/policies/PASTE-INTO-SHOPIFY.md" "$KIT/5-policies/"
cp "$ROOT/scripts/site-kit/README.md" "$KIT/README.md"

( cd "$OUT" && zip -qr "$NAME" "$(basename "$KIT")" )
rm -rf "$KIT"
echo "✓ $OUT/$NAME ($(du -h "$OUT/$NAME" | cut -f1))"
