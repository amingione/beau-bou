# About page

The November 2 owner theme editor supplied the story layout in `templates/page.about.json`. It uses two custom
editor blocks: **Our story** (`blocks/ai_gen_block_de2e383.liquid`) and **Kind words**
(`blocks/ai_gen_block_f9eedc1.liquid`). The page order is hero → story → family and lifestyle album → promise →
store tour arrival → Facebook review strip → store tour discoveries → store visit/hours → Kind words. The hero
and promise retain Michele's faith line, "Accept yourself as you were designed by God." The story block carries
her first-person copy, photos, pull quote and attribution; the Kind words block is a separate Google review
carousel with three excerpts from the owner editor. The Facebook strip and Google carousel remain distinct.
The active theme was saved and read back on November 2; the local template remains separate from Shopify's
page body.

## Family album and store tour

The photo source folder is `~/LocalStorm/Workspace/In Progress/Be-YOU-tiful Boutique/photos-in/about-page/`.
Eight family and lifestyle photos form a compact, sideways-scrolling lookbook rail at every screen width. The
separate store tour has eight stops in two matching horizontal rails around the review strip, moving from the
storefront and windows through clothing, fragrance, accessories and gifts. Photos remain fully visible inside
bounded cards, with on-page previous/next controls and keyboard navigation. The story lead, page hero and
storefront visit photos are also size-limited so they do not dominate the page. Captions and alt text describe
what is visible without
assigning family relationships to the people pictured. The closing album note thanks customers for their visits,
stories and trust.

The theme section is `sections/about-photo-journal.liquid`, with styles in
`assets/section-about-photo-journal.css`. Its photo blocks are editable in Shopify. Fourteen selected photos were
uploaded to Shopify Files for this page; two existing store photos were reused. Duplicate source photos and four
short product clips were not placed in the page. No source photos were removed or changed.

## Source

Michele wrote the story herself (sent through Amber, 2026-10-18). The site version is lightly edited for
punctuation and paragraph breaks only. Her words, facts and first-person voice are unchanged. The edits:

- "SC" → "South Carolina"; "my Airforce daughter" → "my daughter in the Air Force"; "covid shut down" → "COVID shutdown"
- Ellipses turned into sentences; "Love and kindness" lowercased mid-sentence, and used as the heading
- "from size xxs to 2x" → "in sizes XXS to 2X" (matches the rest of the site)

## Keep in mind

- On November 2, an older Shopify theme-editor session showed pending removal of the About, Visit Us and
  homepage templates. Its pending state was saved as a **draft only** rollout named
  `Recovery - unsaved boutique editor 2026-11-02`, with a note not to launch it. The refreshed editor showed a
  disabled Save button, and all three active templates remained intact. Do not launch that recovery rollout.
- "Over the last 7 years" will go stale. Update it each year, or change it to "Since 2020" if Michele prefers.
- The Shopify page body (Online Store → Pages → About) held older short text at the October 18 review. This
  custom template does not display it. Check the body before switching to Default or reusing it for a search
  listing; update it in Michele's store only after checking the current admin value.
- The Kind words excerpts and names came from the owner editor. Check their provenance and the current Google
  review link as a follow-up; the carousel is already on Michele's active theme.

## Facebook reviews (section **reviews**)

Three of the 16 Facebook recommendations (100% recommend), picked and sent by Amber on 2026-10-18 from
facebook.com/MicheleMonksEnsmingerMansfield. Each one shows the reviewer's first name, the same as the old
Google quotes did. "Show 5 stars" is off because Facebook recommendations don't have a star rating.

| Name | Posted | Edits to the original |
| --- | --- | --- |
| Tonya | Aug 20, 2021 | First letters capitalized; the dress-shoes sentence cut (marked with …) |
| Judith | Dec 2, 2021 | "Michelle" → "Michele" (her name's spelling); "Love !!!" → "Love!!!" |
| Annette | Jan 25, 2024 | Commas added for readability; no words changed |

The section shows no dates. If a reviewer asks to be taken off, delete her block in the theme editor.
