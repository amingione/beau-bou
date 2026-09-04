# Client portal — Assembly (LaunchWell workspace)

Built 2026-09-02 in the Assembly desktop app. Michele's contact showed **Active** at 12:36 PM Sep 2 (it was Inactive at 11:00 AM) — verify whether an invite/magic link went out — Amber reviews, then invites from CRM → Michele Mansfield → ⋯ → Share magic link.

## What exists in Assembly

**CRM → Company:** Be-YOU-tiful Boutique by Michele · Contact: Michele Mansfield · beyoutifulboutiquebymichele@gmail.com (last name inferred from the Facebook URL — confirm). Custom fields: Phone number (941) 369-1628 · Address 264-A W Marion Ave, Punta Gorda, FL 33950 · Store hours Tue–Fri 10–5 · Sat 10–4 · Sun–Mon closed.

**Client Studio → Project:** *Be-YOU-tiful Boutique Shopify Website* · Phase: Client review · Launch target: Oct 15, 2026 · Progress 40% · Service: Custom Website Design & Development (In progress) · LaunchWell workflow applied.

### 2026-09-03 simplification (after Michele & Aundrea reported "couldn't find the design or files / didn't know what to do next")

- Deleted the 7 generic LaunchWell requests (Services & product copy, Domain, Project Brief, Testimonials, Legal, etc.) and the two verbose originals.
- Requests are now exactly three, numbered, Notify OFF: **Step 1 of 3 — Look at your website design and tell me yes or no** · **Step 2 of 3 — Answer 14 quick questions (about 15 minutes)** · **Step 3 of 3 — Send me 10 photos from your phone**. Completed requests kept: Photos (reply: FB photos link) and Logo files (reply: "wrong address but right logo image").
- "What's happening now" / "Next from the client" rewritten in plain words pointing at Step 1/2/3 and Messages.
- Progress update **START HERE — Your portal in 3 steps** posted, visible to client.
- New PDF `Be-YOU-tiful_Portal_Guide.pdf` (source `portal-guide.html`) — one page, hand to them by text/email or upload to Files.

| Section | Contents |
| --- | --- |
| What's happening now / Next from client | Plain-words intro → Step 1 approve, Step 2 answer 14 questions, Step 3 send 10 photos; "tap Messages if confused" |
| Project brief (client-editable) | All 14 fields prefilled from the brief: business summary, goals, audience, CTA, products, differentiators, reference site, desired pages, features, domain options, existing site, social, hours/address, notes |
| Milestone checklist | Discovery complete ✓ |
| Progress updates | Week 1 — Design complete (visible to client) |
| Client requests | Step 1 of 3 · Step 2 of 3 · Step 3 of 3 (see simplification note above) + two completed client replies |
| Approvals | **Homepage design v1** — Awaiting review, PDF attached |
| Content vault | Logos & brand files: Logo pack zip · Downloads: Homepage preview PDF, Website Decisions PDF, Photo Shot List PDF (all visible to client) |
| Onboarding checklist | Company & contact confirmed ✓ · Launch target set ✓ |
| Internal notes | CommentSold finding, store ownership, surname caveat, do-not-invite |

## Source files (this folder)

- `Be-YOU-tiful_Website_Decisions.pdf` — 14 plain-English choices, each with the default we'd pick (`decisions.html` is the source; render with Playwright)
- `Be-YOU-tiful_Photo_Shot_List.pdf` — 10 phone shots mapped to portal categories (`shotlist.html`)
- `Be-YOU-tiful_Homepage_Preview.pdf` — full-page desktop render of `docs/preview/index.html` (1440px)
- `Be-YOU-tiful_Homepage_Preview_Mobile.pdf` / `.png` — phone render (390px, iPhone-class viewport)
- `Be-YOU-tiful_Mobile_Screens.png` — four phone frames at a glance (hero, tiles, promise band, visit/footer)
- `Be-YOU-tiful_Logo_Pack.zip` — zip of `docs/brand/`
- `Be-YOU-tiful_Website_Proposal.pdf` — $1,000 flat proposal, $500/$500 payment split, Oct 15 launch target, 14-day validity (`proposal.html` is the source)

Regenerate PDFs: `python3 -c "from playwright.sync_api import sync_playwright; ..."` — see session notes; any headless Chromium `page.pdf(format='Letter', print_background=True)` works.

- `Be-YOU-tiful_Portal_Guide.pdf` — one-page "Your portal in 3 steps" for Michele & Aundrea (`portal-guide.html`)

## Open items for Amber

1. Both contacts (Michele Mansfield, Aundrea Pedigo) are already **Active** — they have portal access.
2. Michele's reply on the Logo files request: *"wrong address but right logo image"*. Address on file is 264-A W Marion Ave; Facebook shows 264 West Marion Ave. Confirm the correct one with her and fix CRM → Custom fields → Address.
3. Confirm surname "Mansfield" (inferred from the Facebook URL).
4. Text or email them `Be-YOU-tiful_Portal_Guide.pdf` with the portal link; optionally upload it to Files as well.
5. Mobile PDF/screens and the proposal are not yet in the Content vault — upload when convenient.

## Print booklet (2026-09-04)

`Be-YOU-tiful_Website_Booklet.pdf` — 15 Letter pages for the in-person visit: cover · how to use / contents · portal guide · design desktop + phone · 14 decisions (tickable) · shot list · proposal (sign page 13) · "Today's meeting" checklist (address, name, domain, Shopify email, deposit) · from-here-to-launch + contact. Contact on the back page: buildwith@launchwellbrands.com (phone left off — add in `booklet.html` if wanted).

Rebuild: render `booklet.html` with Playwright (`prefer_css_page_size=True`) to `_booklet_wrap.pdf`, then merge with pypdf in this order: wrap 1–2, Portal Guide, wrap 3–4, Decisions, Shot List, Proposal, wrap 5–6. `desk-a.png`/`desk-b.png` are the top/bottom halves of `Be-YOU-tiful_Homepage_Preview.png`.
Print: Letter, double-sided, flip on long edge, staple top-left or 3-hole punch.
