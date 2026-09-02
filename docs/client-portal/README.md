# Client portal — Assembly (LaunchWell workspace)

Built 2026-09-02 in the Assembly desktop app. Michele's contact showed **Active** at 12:36 PM Sep 2 (it was Inactive at 11:00 AM) — verify whether an invite/magic link went out — Amber reviews, then invites from CRM → Michele Mansfield → ⋯ → Share magic link.

## What exists in Assembly

**CRM → Company:** Be-YOU-tiful Boutique by Michele · Contact: Michele Mansfield · beyoutifulboutiquebymichele@gmail.com (last name inferred from the Facebook URL — confirm). Custom fields: Phone number (941) 369-1628 · Address 264-A W Marion Ave, Punta Gorda, FL 33950 · Store hours Tue–Fri 10–5 · Sat 10–4 · Sun–Mon closed.

**Client Studio → Project:** *Be-YOU-tiful Boutique Shopify Website* · Phase: Client review · Launch target: Oct 15, 2026 · Progress 40% · Service: Custom Website Design & Development (In progress) · LaunchWell workflow applied.

| Section | Contents |
| --- | --- |
| What's happening now / Next from client | Design done → review preview, answer decisions, upload photos, upload original logo |
| Project brief (client-editable) | All 14 fields prefilled from the brief: business summary, goals, audience, CTA, products, differentiators, reference site, desired pages, features, domain options, existing site, social, hours/address, notes |
| Milestone checklist | Discovery complete ✓ |
| Progress updates | Week 1 — Design complete (visible to client) |
| Client requests | 7 LaunchWell defaults + **Answer the 14 Website Decisions** + **Upload your 10 photos (see Photo Shot List)** — both created with *Notify the client* OFF |
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

## Before inviting Michele

1. Confirm surname.
2. Read the auto-posted welcome message in Messages (Assembly's default) — edit if it doesn't sound like you.
3. Optionally tick "Content requests sent" once you notify her.
4. CRM → contact ⋯ → Email magic link.
