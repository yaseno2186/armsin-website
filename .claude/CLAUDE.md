# Armsin Digital Media — Portfolio Site

## Purpose
Client-facing portfolio/landing site for Armsin Digital Media, a 
digital products studio based in Germany, targeting local shops, 
restaurants, and small businesses — reach is Germany-wide (open to 
clients globally), not limited to one town. Offering spans websites, 
apps, photography, and systems/automation, not websites alone.

## Tech constraints
- Plain HTML/CSS/JS only — no frameworks, no build tools, no npm.
- Single-page site OR simple multi-page (index.html, impressum.html, 
  datenschutz.html) — keep the file structure flat.
- Must be mobile-first and responsive (most visitors will check on phone).
- Fast-loading — no heavy libraries, minimal JS.
- Code must stay simple enough for a non-technical person to edit 
  text later without breaking anything.

## Language
All visible content in German (target audience: German local business 
owners). Code comments can be in English.

## Design system
**Repainted 2026-09-05 at the founder's explicit request** ("make it more
programming style") — full site-wide light→dark recolor, retro-terminal/CRT
direction, chosen from 3 named options. Supersedes the original light
"paper" palette below; see `.tastemaker/style-lock.md` and
`.tastemaker/decisions.log` for the contrast math and rationale.

- Background: #0A0E0C (page bg + hero/nav/footer chrome — whole site is
  dark now, not just a few accent sections)
- Surface: #131E17 (elevated cards, forms, booking frame)
- Secondary: #0F1A14 (alternate section backgrounds — Services, Booking)
- Text: #D6E8DD (primary text, green-tinted white)
- Text (dim): rgba(214, 232, 221, 0.68) (secondary/muted text)
- Accent: #39D97A (phosphor-green — CTA buttons, links, highlights, use
  sparingly, only for actions — replaces the old burnt-orange #C1592B)
- On-accent: #06120B (near-black text for use on the bright accent fill)
- Amber: #E0A458 (rare CRT-amber highlight, used sparingly)
- Headline font: 'JetBrains Mono' (Google Fonts) — changed from 'Fraunces'
  by a separate concurrent session on 2026-09-05; kept as-is since it fits
  the new terminal direction
- Body font: 'Inter' (Google Fonts) — unchanged
- Keep generous whitespace, avoid clutter — calm and trustworthy still
  applies, just expressed through a terminal/developer register now
  instead of the original warm-editorial one.

<details>
<summary>Original light palette (superseded, kept for reference)</summary>

- Ink: #1C2530 (headlines, nav, footer bg)
- Paper: #FAF6F0 (page background)
- Accent: #C1592B (CTA buttons, links, highlights)
- Secondary: #2F4A3E (alternate section backgrounds)
- Neutral text: #6E6A63 (body copy, subtext)
- Headline font: 'Fraunces' (Google Fonts)
</details>

## Pages / sections needed
1. Hero — clear one-line value proposition + CTA button ("Kostenlosen 
   Check anfragen" or similar), no stock-photo cliché feel
2. Services — 4 short cards: Websites, Apps, Fotografie, Systeme &amp; 
   Automatisierung (adjust based on actual offering)
3. Why us — 2-3 short trust points (schnell, unkompliziert, lokal, 
   fair kalkuliert — no fake reviews/testimonials since we have none yet)
4. Contact — simple form (name, email, message) + direct email/phone, 
   no backend needed yet, just mailto: or a note that form submission 
   needs a backend later
5. Footer — Impressum link, Datenschutz link, business name

## Legal requirement
Site needs a proper Impressum page (German legal requirement for 
any commercial website) — flag this if I don't have the content 
ready, don't invent placeholder legal text.

## What NOT to do
- No fake testimonials or fake client logos (I have zero real 
  clients yet — be honest in copy, focus on the offer itself)
- No generic stock "hero image of people high-fiving"
- No overly salesy language — tone should match: direct, practical, 
  no fluff (see my Marketing project instructions)