# Be-YOU-tiful Boutique: images for Michele's store

Everything the website shows, ready to upload to Michele's Shopify store (xapm2f-fr). Upload the files
**before** installing the theme, so the homepage photos appear as soon as the theme is in.

## 1-files → Content → Files

Select every file in `1-files` and upload them in one go: **Content → Files → Upload files**.

- **Keep the filenames exactly as they are.** The theme finds each photo by its name.
- After uploading, add the alt text from `3-looks/looks.csv` to the try-on photos (click a file → Alt text).
  It helps Google and screen readers.

What's in there: the storefront hero (desktop and phone), the logos (black and white lockups, favicon),
the four brand logos, the join-the-list graphic, the category photos, the 13 try-on photos used by the
Looks, the Highlights photo, and the About / Visit Us store photos.

## 2-collection-images → each collection's image

Each file is named after its collection (`dresses.webp`, `baby-toddler.webp`, …).

1. Create the collection if it isn't there yet (title and rule in `collection-images.csv`).
2. Open it: **Products → Collections → (name) → Collection image → Add image**, pick the matching file.
3. Paste the alt text from `collection-images.csv` (Edit image → Alt text).

Collections with no photo yet: New Arrivals, Swimsuits, Gowns, Sale, Clearance, and the three brand
collections. They show their products' photos once products are added.

## 3-looks → Content → Metaobjects → Look

**First, the definition.** The theme reads metaobjects of type **`look`** (singular). In Settings → Custom data →
Metaobjects → Add definition, name it **Look**; the type under the name must read `Type: look`. A definition named
"Looks" gets type `looks`, and the theme ignores it (Highlights then falls back to the bundled sample photos).
Fields, with these labels: Title (single line text), Image (Image file), Pieces (list of products), Goes with (list
of products), Caption (multi-line text), Video (Video file). Turn on Active-draft status and Publish entries as web
pages.

Then, for each row in `looks.csv`: **Add entry** → Title, Image (pick the file named in `image_file`), Status
**Active**. Pieces and Goes with stay empty until Michele's products are in the store; the look page shows the
sold-out message until then.

**Create the definition before uploading the theme.** Shopify drops `templates/metaobject/look.json` from a theme
zip when the `look` type doesn't exist yet, and every look page then 404s. If that happened, re-add the template in
Online Store → Edit code → templates → New file `metaobject/look.json` (copy it from this repo, swapping in the
store's own collection and links).

Done on Michele's store (xapm2f-fr) on 2026-10-19: Look definition plus all 13 entries, and the look page template
re-added after the upload dropped it.

## Not images (moved separately)

The theme itself, pages, menus, page and collection search listings, and policies. See the full site kit
(`bash scripts/build-site-kit.sh`) and `docs/handoff.md`.
