# Style Lock — Armsin Digital Media

## Source
**Superseded 2026-09-05** — see "Retro-terminal repaint" section below for the current, active palette. This section is kept for history only; do not build against it.

~~Palette and fonts are given by the client brief (`.claude/CLAUDE.md`), not generated.~~

## Color contract (superseded — see repaint section below)

| Role | Token | Hex |
|---|---|---|
| Ink | `--ink` | #1C2530 |
| Paper | `--paper` | #FAF6F0 |
| Accent | `--accent` | #C1592B |
| Secondary | `--secondary` | #2F4A3E |
| Neutral text | `--neutral` | #6E6A63 |
| White | `--white` | #FFFFFF |

(original hand-calculated contrast notes omitted here — see git-free history via `.tastemaker/decisions.log` if needed; the tokens themselves no longer exist in style.css)

## Retro-terminal repaint (2026-09-05) — ACTIVE palette

User request: "change the color palette of the whole website, make it more Programming style." Presented 3 named directions (Retro terminal/CRT, GitHub Dark, VS Code Dark+ syntax) with hex previews; user picked **Retro terminal/CRT**, reasoning it fits the site's existing terminal-cursor logo and retro-PC 3D hero better than a generic dev-tool look.

This is a full light→dark repaint, not a hex swap. The old `--ink`/`--paper` tokens did double duty as both a background AND a text color depending on context (e.g. `--ink` was both "dark hero/nav/footer background" and "primary text color on the old light page"). Under an all-dark theme those two roles diverge, so they were split into separate tokens rather than reusing the old names with flipped meanings.

| Role | Token | Hex | Was |
|---|---|---|---|
| Background | `--bg` | #0A0E0C | page bg + hero/nav/footer chrome, now unified (whole site is dark, not just a few accent sections) |
| Surface | `--surface` | #131E17 | elevated cards/forms/booking-frame fill |
| Surface 2 | `--surface-2` | #0E1512 | recessed fill for inputs nested in a `--surface` card |
| Secondary | `--secondary` | #0F1A14 | alternate section bg (Services, Booking) |
| Text | `--text` | #D6E8DD | primary text everywhere (was `--ink`'s text role + `--paper`'s light-text-on-dark role, unified) |
| Text dim | `--text-dim` | rgba(214,232,221,0.68) | secondary/muted text (was `--neutral` + `--paper-dim`) |
| Accent | `--accent` | #39D97A | phosphor green, was burnt-orange #C1592B |
| Accent dark | `--accent-dark` | #2BB863 | accent hover-darken |
| On-accent | `--on-accent` | #06120B | dark text for use ON the bright accent fill (buttons/badges) |
| Amber | `--amber` | #BA5629 | **updated 2026-09-06** — was a guessed generic CRT-amber #E0A458; now the *measured* orange from the real logo asset (`assets/logo/armsin-wordmark.png`'s terminal-cursor bar, via `extract_palette.py`, ≈9% share, `#ba5629`). Second terminal color, used more deliberately now (see 2026-09-06 pass below), still never for CTA fills — green stays the only "action" color. |
| Amber dark | `--amber-dark` | #9A4620 | amber hover-darken, same lightness-step relationship as accent/accent-dark |

**Contrast (hand-calculated, WCAG relative luminance — Python/`check_contrast.py` unavailable this session):**
- `--text` on `--bg` — ≈15.2:1
- `--text` on `--surface` — ≈13.4:1
- `--text` on `--secondary` — ≈13.95:1
- `--text-dim` on `--bg` — ≈10.7:1
- `--accent` on `--bg` (icons/links/accent text) — ≈10.5:1
- `--on-accent` on `--accent` (button labels/badges) — ≈10.5:1
- **Caught and fixed:** white text on the new accent green measured ≈1.8:1 (fails badly) — this is exactly the kind of thing that looks fine as a "brand color" but fails once assigned a text role, per the anti-slop checklist's contrast-floor warning. Introduced `--on-accent` specifically for this and swapped every button/badge that used to say `color: var(--white)` on an accent fill.

**2026-09-06 — logo-orange rebalance (`check_contrast.py --matrix` this time, Python now available):** re-ran the full matrix with `--amber`/accent role = `#BA5629`. Full results in `decisions.log`; summary — `bg/accent` 4.12, `accent/on-primary` 4.05, `text/accent` 3.69, `surface/accent` 3.63 — all **UI-safe (≥3.0) but not text-safe (≥4.5)**. This is why every new orange placement below is icons/borders/badge-fills-with-bold-short-labels/decorative — never small body text or a primary CTA fill.

**Known limitation, disclosed rather than hidden:** the Google Calendar booking iframe (`index.html`/`ablauf.html` `.booking-frame`) is cross-origin content — Google's own embed renders with its own white background regardless of this site's theme. Only the frame around it (`--surface`) is dark. Not fixable from this codebase.

**Assets recolored to match:** all `assets/icons/*.svg` (stroke `#1C2530`→`#D6E8DD`, `#C1592B`→`#39D97A`) and `assets/images/process-*.svg` + `hero-illustration.svg` (accent + a few structural fills remapped). A handful of the hero illustration's minor secondary tones (`#182028`, `#7FBF9A`, `#A9A49B`, `#E4DCD0`) were left untouched — they either already fit the new dark-green theme or are minor enough shading details that a blind remap risked breaking internal contrast without visual verification. The `assets/3d/hero-pc.js` / `hero-scene.js` 3D scene's hardcoded colors were updated to match (case/screen texture/rim light). `assets/logo/*.png` were **not** recolored — they're raster files with the old light-cream color baked in; `.nav-logo`'s circle backing is hardcoded to `#FAF6F0` to match rather than clashing with a now-differently-themed CSS token.

**Not touched:** the headline font (JetBrains Mono) and the "Warum Armsin" section — both landed from a separate, concurrent session editing this project, not from this repaint.

## Type

- Headline: **JetBrains Mono** (Google Fonts) — changed from Fraunces by a concurrent session on 2026-09-05, kept as-is (fits the new terminal direction)
- Body: **Inter** (Google Fonts)
- Loaded via standard `<link>` to Google Fonts (this is a real static site, not a sandboxed artifact — no CDN allowlist restriction applies)

## Spacing scale

`--space-1: 8px, --space-2: 16px, --space-3: 24px, --space-4: 32px, --space-6: 48px, --space-8: 64px, --space-12: 96px, --space-16: 128px`

- Hero (pivotal section): `--space-16` vertical padding desktop, `--space-8` mobile
- Services (secondary section): `--space-12` vertical padding desktop, `--space-6` mobile
- Card internal padding: `--space-6` (24px) minimum, ≤ gap between cards (gap = `--space-4`/32px desktop) — internal ≤ external, per spacing rule

## Structure (Step 2.5)

- **Screen type:** Marketing narrative (local-business landing page)
- **Macrostructure:** Simplified Feature Stack — Hero → Services (3-card grid) → [Why us → Contact → Footer, not yet built]
- **Nav archetype:** Minimal sticky header — wordmark text + single CTA button, no link list (single-page site, short scroll)
- **Hero archetype:** Centered text, single custom SVG illustration below/beside copy (no stock photo — explicitly banned in brief)
- **Services archetype:** 3-column card grid (1-column stack on mobile), icon-top cards, no pricing, no fake links yet
- First build in this project — no prior `.tastemaker/log.json` to rotate against.

## Assets

- **Logo (real, user-supplied — asset > spec):** `logo/armsin-terminal-{light,dark,icon}.png` — a monospace "armsin" wordmark with an orange terminal-cursor bar. Cropped a tight transparent-background wordmark to `assets/logo/armsin-wordmark.png` for the header (light.png's canvas included a "DIGITAL MEDIA" subtitle not needed at header scale). `armsin-icon.png` (transparent corners, opaque paper-colored rounded square) used directly as favicon/apple-touch-icon — no cropping needed, already square. `armsin-terminal-dark.png` copied to `assets/logo/armsin-wordmark-dark.png` for potential future dark-surface use (not currently wired in — footer still uses plain text, out of scope for this pass).
- **This discovery changed the hero illustration's direction:** the real logo is a monospace/terminal identity, not a literal-storefront one. The hero SVG's storefront/house motif was replaced with a terminal/code-lines motif (content-line bars + a blinking orange cursor rect, same proportions as the logo's cursor bar) so the hero now visually rhymes with the real brand mark instead of contradicting it.
- Service icons: still 3 hand-coded line-style SVGs (`assets/icons/`) — unaffected by the logo update.
- **Honesty note:** the logo is a real user-supplied asset, not generated. The hero illustration is still hand-authored SVG (no illustration library / Openverse fetch — no Python/network this session), now redesigned around the real logo's terminal-cursor motif with a small CSS-in-SVG blink animation (gated by `prefers-reduced-motion` inside the SVG's own `<style>`).

## Motion

- GSAP skipped deliberately — CLAUDE.md explicitly requires "minimal JS," "no heavy libraries," and code simple enough for a non-technical editor. Using plain CSS transitions + a small vanilla `IntersectionObserver` (~15 lines) for scroll reveals, gated by `prefers-reduced-motion`.
- **Reference-informed additions (see `reference-board.md`, added 2026-09-05):** numbered section labels (e.g. "01 — Websites") applied **site-wide** (not just Services) as a consistent editorial structure device; a light CSS-only hover lift/tilt (`transform: translateY/rotate` on `:hover`, no JS) for cards; a multi-line, deliberately-broken headline treatment in the Hero (break the value-prop across 2-3 short lines instead of one long sentence); mobile layouts that genuinely simplify (flatten/calm) rather than just shrink the desktop version; optionally one dark full-bleed section using existing `--secondary`/`--ink` tokens as a mood break between sections. Explicitly rejected: device-shell/tabbed UI, CRT/pixel-dissolve transitions, magnetic 3D tilt, audio cues, WebGL/real-time 3D hero — all need a real animation/3D library or bespoke JS the brief forbids.
- **CRT scanline field (added 2026-09-05, `.trust`/`.process` backgrounds):** a faint static scanline texture (`repeating-linear-gradient`, 1px/3px, `--wash` token) plus one thin light band that sweeps top-to-bottom (`transform: translateY`, not `top`) — green on `.trust`, amber on `.process`, opposite direction/duration per section. Replaced a first attempt using two blurred, drifting radial-gradient "blob" circles, which the user rejected as "very bad" — that pattern is the same one already removed from the hero in the anti-slop pass below (gate 14, "not the default gradient"/drifting-blob decoration). **Do not reintroduce blurred drifting gradient blobs anywhere on this site** — if a section wants ambient background motion, reach for on-theme CRT material (scanlines, a scan sweep, static noise/vignette) instead, and re-check this file's anti-slop history before adding any new decorative background shape.

## Logo-orange rebalance (2026-09-06)

User request: "make the website more Programming style retro computer Programs with the green (retro monitors) and orange (from the logo)." The dark CRT-green repaint from 2026-09-05 was already active; this pass extends the *orange* half of that two-tone terminal identity, which had previously been used in only a handful of one-off spots (see the amber token history above).

- **Grounded the color for real:** ran `.claude/skills/tastemaker/scripts/extract_palette.py` on the actual logo files in `assets/logo/`. The wordmark's cursor bar measured `#ba5629` (≈9% pixel share) — this replaced the old guessed `#E0A458` amber as the `--amber` token's value (see Color contract above). `armsin-icon.png` did not contain the cursor bar at a large enough scale to register as a dominant color, so `armsin-wordmark.png`/`armsin-wordmark-dark.png` were the useful sources.
- **Found and fixed a second stale orange:** `.nav-logo`'s background circle in an earlier state of this file had been hand-set to a hardcoded `#C1592B` (the *pre-repaint* brand orange, from before the 2026-09-05 dark recolor) — a guess, not the measured value, and not tokenized. By the time this pass ran, a concurrent edit to this file had already removed that background rule entirely (nav-logo now just shows the raster image at full size with no circle backing) — no fix needed there any more, noted here only so a future session doesn't go looking for it.
- **Extended orange usage, all within the UI-safe (not text-safe) contrast tier the matrix above sets:**
  - `.process-num` step badges (`index.html` "So arbeite ich" rail) now alternate green/orange (`nth-child(even)` → `--amber`) instead of all four being green — reads as the classic green+amber terminal pairing running down the rail, not orange used only once in isolation.
  - `.btn-ghost` hover state (secondary/ghost buttons site-wide, including the hero's ghost CTA) — border + wash now `--amber`/`--amber-wash` instead of `--text`/`--wash`. Primary buttons (`.btn-primary`) are untouched — green stays the only color that means "the action," per CLAUDE.md's "use sparingly, only for actions" rule; orange marks the *secondary* interactive tier instead.
  - `.process::after`'s scan-sweep glow (already amber-colored) now reads off `--amber-glow` instead of a hardcoded `rgba(224, 164, 88, ...)` — same visual role, now tokenized and using the corrected hue.
  - `.retro-pc-led` (hero PC power LED) and `.code-line-amber` (one of the two floating code-window accent lines) already referenced `--amber` — no code change needed, but both now render the corrected, real-logo orange automatically.
- **Deliberately left alone:** service/process SVG icons (`assets/icons/*.svg`, `assets/images/process-*.svg`) are still green-only — recoloring some of them orange was considered and rejected for this pass; the icon set reads as one coherent family right now, and splitting it two ways risked looking arbitrary rather than intentional. Flag for a future pass if the user wants icons to carry the two-tone split too.
- Ran `anti_slop_scan.py style.css index.html about.html` (clean) and `audit_motion.py style.css` (29 pre-existing findings, none touched by or related to this color-only pass — out of scope, left as-is) after the edits.

## Career timeline (about.html, added 2026-09-05)

A "Werdegang" section (`.about-timeline`/`.timeline-rail`/`.timeline-item`) sits between the Story and Skills sections on about.html: a vertical dashed rail (reuses `--border-default`, same dashed-line device as `.ablauf-steps::before`) with one node per milestone (2019–2020 PC-Repair-Manager, 2024 Backend-Entwickler bei BUSCHMEIS, 2025 Stipendium & Abschlüsse, 2026 Gründung von Armsin).

Motion is zero-new-JS: each `<li>` carries the site's existing `[data-reveal]` attribute (fade + rise, toggled by the IntersectionObserver already in `assets/js/site.js`), and the `<ol>` carries `[data-reveal-group]` for the same nth-child stagger the services grid already uses. The only new CSS is `.timeline-item.is-visible .timeline-node`, keyed off the exact same `.is-visible` class the observer already sets — the rail node transitions from a dim ring to a glowing accent dot (`background-color`/`border-color`/`box-shadow`, not a new animation system). One blinking cursor (`.timeline-cursor`, reuses the existing `pc-cursor-blink` keyframe) sits only on the 2026/current entry — one blinking element reads as "you are here," four would read as flicker. Gated in the existing `prefers-reduced-motion` block alongside `.retro-pc-cursor`. See `.tastemaker/decisions.log` for the full build-sequence reasoning (built via the `animate` skill).

## Scope of this build

Only **Hero** and **Services** sections built (index.html + style.css). User is reviewing before Why-us / Contact / Footer are added.

## Anti-slop audit + fix pass (2026-09-05)

Full audit run against `references/anti-slop-checklist.md`; findings and fixes:

- **Removed** the hero blob background (`.hero-blobs`, 4 blurred drifting shapes) — flagged as the single most recognizable AI-hero decoration regardless of palette. Hero is now a plain `--ink` field behind the illustration + existing radial text-legibility wash (`.hero-copy::before`).
- **Removed** the Three.js WebGL hero scene (`assets/3d/hero-scene.js`, `hero-pc.js`, loaded `three@0.184.0` from a CDN) — directly violated CLAUDE.md's "no heavy libraries / minimal JS / non-technical-editable" constraint. The hero now shows only the static SVG illustration that was already the fallback — no visual regression, just removed a dependency that most visitors never actually saw render (WebGL init was async and many mobile visitors got the fallback anyway).
- **2026-09-05, later same day:** a concurrent session re-added `assets/3d/hero-scene.js`/`hero-pc.js` (Three.js again) after this audit ran, without updating this doc — caught when the user asked to redo the hero's "3 objects" as a cream-plastic retro PC. Re-removed for the same CLAUDE.md reason, this time rebuilt as **pure CSS/HTML** instead of falling back to a static image: `.pc-scene`/`.retro-pc`/`.code-float-*` in `style.css` (search those class names) + `initHeroParallax()` in `assets/js/site.js`. Same visual concept as the removed 3D version (cream/vanilla ABS-plastic CRT monitor + two floating code-window panels = the three objects), same color values (`#e8ddc4`/`#d6c9a8` case, `#14201a` bezel, `#06120b` screen — matches the retro-terminal palette above), but zero dependencies: idle CRT flicker/scanline/cursor-blink/LED-breathe run as CSS `@keyframes`, and the pointer-tilt is ~20 lines of vanilla JS setting `--tilt-x`/`--tilt-y` custom properties (desktop-hover only; touch devices keep the CSS float animation). All motion respects `prefers-reduced-motion`. `assets/images/hero-illustration.svg` (the old fallback, now unused since there's no async WebGL init to fall back from) was deleted.
- **Reduced** the repeated pill-eyebrow (`.hero-tag`) from 9 instances across every section/page down to 1 (homepage hero only) — gate 51, exact "same pill on every section" tell. Removed the now-dead `.page-hero .hero-tag`, `.booking-head .hero-tag`, `.hero-tag-dark` CSS.
- **Differentiated** the homepage Process section from Services — Process cards used to be boxed/tilted/bordered, i.e. the same "icon + heading + sentence card" rhythm as Services stacked directly beneath it. Process is now a flat numbered rail (circle badge + icon + heading + short line, no card chrome) connected by the existing dashed thread — Services stays the boxed tilted-card treatment.
- **Added visuals** to the about/projects/careers text-only story sections (previously a heading + one paragraph, no visual — gate 1 text-wall failure). Each now pairs an existing real icon (from `assets/icons/`, already fetched/curated) with a pull-quote excerpted verbatim from that section's own copy (`.story-grid`/`.story-visual`/`.story-pull` in style.css) — honest reuse of real assets, not a new illustration/photo (none was generated or fetched this pass; no image tool/network was used).
- **Fixed nav** on about/projects/careers — they only showed a "Studio" link; now match studio.html's set (Ablauf, Termin buchen, Studio).
- **Content fix:** careers.html referenced "Freiberg und Umgebung" as a hiring region, contradicting CLAUDE.md's Germany-wide/global framing — changed to "Deutschland."
- **Not fixed / flagged only:** about.html's founder photo is still a "Foto folgt" placeholder — a real content gap, not a design bug; needs the actual photo from the user.

See `.tastemaker/decisions.log` for the keep/reject record of this pass.
