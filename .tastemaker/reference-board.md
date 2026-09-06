# Reference Board — Armsin Digital Media

User-supplied references (2026-09-05). These are inspiration for motion/imagery/layout feel — they do **not** override the locked palette/type in `style-lock.md` (client brief colors/fonts stay fixed), and any motion borrowed must still respect the CLAUDE.md constraint: plain HTML/CSS/JS only, minimal JS, no heavy libraries, code simple enough for a non-technical editor.

## 1. sharplink.com
Could not be fetched (page content truncated in the fetch tool both times — likely a heavy JS/SPA site). Revisit with a screenshot if the user wants specific elements copied.

## 2. pxpush.com
- **Structure:** vertical scroll, numbered sections (Nº001–004) with repeating section-label headers as rhythmic dividers. Sticky/persistent top nav (Index / About / Journal / Get Started).
- **Color:** minimal, high-contrast — black text on white/light background, accent colors kept subtle, restrained to imagery.
- **Type:** bold geometric sans headlines, clean sans body, numbered labels ("Nº001") as a distinctive technical/editorial detail.
- **Imagery:** looping portfolio-thumbnail carousel (work samples repeated to fake an infinite loop).
- **Motion (adoptable within our constraints):** scroll-triggered section reveals; auto-looping image strip; simple hover states on CTAs. All doable with vanilla CSS transitions + one small `IntersectionObserver`, no library needed.
- **Mood:** streamlined, confident, "on-demand professional crew" — matches our own "schnell, unkompliziert, fair kalkuliert" trust points well.
- **Takeaway for Armsin:** the **numbered-section-label** device (e.g. "01 — Websites", "02 — Apps") is a cheap, on-brief way to add editorial structure to the Services section without new libraries. The looping thumbnail strip is a good pattern for a future "recent work" section once real project photos exist.

## 3. areebali.com
- **Structure:** novelty retro-handheld-device UI shell (click wheel, tabbed WORK/AI Films/Playground). Highly bespoke, personal-portfolio-specific.
- **Type:** Libre Baskerville headlines + League Spartan body (serif/humanist-sans pairing, similar spirit to our own Fraunces/Inter pairing).
- **Motion:** 3D magnetic hover tilt, pixel-dissolve transitions, CRT power-on/off collapse — all heavy, JS/animation-library territory (GSAP-tier or custom canvas work).
- **Takeaway for Armsin:** the elaborate device-shell interaction model is **not a fit** — it directly conflicts with the CLAUDE.md requirement for a simple, non-technical-editable, lightweight site, and would need a real animation library we're deliberately not using. The one transferable idea, scaled way down: a subtle hover "lift/tilt" on service cards or portfolio thumbnails (a few degrees of `transform: rotate/translate` on `:hover`, pure CSS, no JS) — same spirit of "the interface responds to you," none of the CRT/audio/tilt-library overhead.

## 4. ghost-pitcher.com
- **Structure:** cinematic scroll narrative, sections framed as film "scenes" (SC 00–07) with timecode labels, vertical scene-anchor nav.
- **Color:** high-contrast minimalism — black backgrounds, white/light type, full-color client logos as punctuation.
- **Type:** bold condensed uppercase sans headlines with tracking, lighter clean sans body, italics for emphasis.
- **Imagery:** real production stills/video only, cinema aspect ratios (16:9, 2.39:1), no stock photography.
- **Motion:** scroll-driven scene reveals ("roll picture — scroll"), embedded video, hover-illuminate on clickable elements.
- **Mood:** confidential, elite, "invisible studio" mystique.
- **Takeaway for Armsin:** the **numbered "scene" labeling** reinforces the same numbered-section idea already logged from pxpush — worth using consistent numbering (e.g. "01 Websites", "02 Apps") across the whole site, not just Services. The dark, high-contrast full-bleed section idea doesn't fit our warm Paper/Ink palette, but a single dark full-bleed section (using our existing `--secondary` #2F4A3E or `--ink`) as a mood break between sections is a lightweight way to borrow the "cinematic pause" feeling without changing the palette.

## 5. scfo.de
- **Structure:** vertical scroll, 11 numbered full-viewport sections — hero, services, case studies, process, contact.
- **Color:** dark, high-contrast, minimal — depth via layering rather than color variety.
- **Type:** large dramatic headline scale with deliberate line breaks for emphasis ("Webdesign, das Marken größer wirken lässt"), clean sans body.
- **Imagery/Motion:** real-time WebGL 3D hero (out of scope — needs a 3D library, conflicts with our "no heavy libraries" rule); responsive complexity (full spatial layout on desktop, flat/calm on mobile).
- **Takeaway for Armsin:** skip the WebGL hero entirely — not compatible with the plain-HTML/CSS/JS constraint. But the **"simplify on mobile, don't just shrink"** principle is worth keeping: our mobile layouts should genuinely flatten/calm down, not just scale the desktop version down. The dramatic multi-line headline treatment (breaking a value-prop across 2-3 short lines instead of one long sentence) is a cheap, on-brief typographic upgrade for our Hero.

## 6. lutstudios.com
Fetch returned only the page title ("Every Frame Is a Painting — Creative Production Studio") — no real content came through. Revisit with a screenshot if the user wants specific elements copied.

## 7. User-pasted reference images (retro CRT mascot, added 2026-09-05)
- **Subject:** a set of 5 3D-rendered images of a cute retro CRT-monitor character — boxy beige/cream vintage-Mac-style monitor body, glowing simple face on the screen (two vertical rounded-rect "eyes" + a short mouth bar, in phosphor green or soft lavender/pink depending on the shot), paired with a matching mouse and sometimes a small potted plant. One image is a branded ad ("Technical support is now available in Telegram") using the mascot on a purple-to-pink gradient background with a "NG Network Graphics" logo.
- **Style:** soft-shaded 3D/claymorphism render — rounded plastic-toy geometry, gentle studio lighting, pastel/neutral body colors (cream, tan, lavender-grey) with the glowing face as the one saturated accent.
- **Relevance:** directly on-theme with the site's already-locked "retro terminal/CRT" repaint (see `style-lock.md`) and the prior "retro-PC 3D hero" concept that motivated picking that palette direction in the first place (the earlier Three.js hero scene was removed for being too heavy, not because the retro-PC idea was wrong).
- **Takeaway for Armsin:** the glowing-face CRT mascot is a strong candidate **motif** (not necessarily a literal 3D render, given the "no heavy libraries / plain HTML/CSS/JS" constraint) for a simplified flat SVG illustration or icon — e.g. redraw the hero illustration's terminal glyph as a small friendly face (two bars + a line) using the site's own `--accent` phosphor green on `--surface`, instead of a generic cursor-blink motif. Keep it as a **static SVG**, not a 3D/WebGL asset — same reasoning that killed the earlier `hero-pc.js`/`hero-scene.js` Three.js scene applies here. Do not adopt the pastel purple/lavender gradient background from the Telegram ad — it conflicts with the locked dark `--bg`/`--surface` palette; the green/amber glow-on-dark treatment is the right fit.
- **Do not adopt as-is:** literal photorealistic/claymorphism 3D rendering (needs a 3D pipeline/library, out of scope for a static site editable by a non-technical person); the mouse-and-plant desk-scene framing (nice-to-have prop detail, not core to the brand).

## 8. User-pasted reference image (grid/blueprint background, added 2026-09-05)
- **Subject:** dark perspective grid — fine hairline grid lines converging toward a horizon, small crosshair markers at major intersections, vertical gradient from near-black at top to a lighter blue glow at the bottom edge.
- **Style:** technical/blueprint/CAD aesthetic — reads as a "canvas" or "schematic" backdrop, not a literal photo.
- **Relevance:** fits the site's locked retro-terminal/CRT direction (grid = graph paper / schematic overlay, same technical register as the monospace type and terminal-cursor logo).
- **Takeaway for Armsin:** adopt as a **background preference** — a subtle full-bleed perspective/grid pattern (CSS `linear-gradient` + `repeating-linear-gradient` lines, no image asset needed) behind the hero or as a page-wide texture. Recolor to the site's own tokens when built: `--bg`/`--surface` for the dark base, `--accent` (phosphor green) at low opacity for the grid lines instead of the reference's blue — the blue in this image is just the reference's own palette, not something to import wholesale (conflicts with the locked green accent).
- **Not yet built** — this is a noted preference for a future pass, not implemented in index.html/style.css yet.

## Net decisions for this project
- Adopt: numbered section labels (pxpush, ghost-pitcher) applied consistently site-wide, not just Services; scroll-reveal-on-view (pxpush) — already partly in place via the existing `IntersectionObserver`; a light CSS-only hover tilt on cards (scaled-down areebali idea); a multi-line, deliberately-broken headline treatment in the Hero (scfo.de); mobile layouts that genuinely simplify rather than just shrink (scfo.de); optionally one dark full-bleed section using our existing `--secondary`/`--ink` tokens as a mood break (ghost-pitcher, toned down from pure black); a simplified flat-SVG "glowing face" motif (two bars + a line, `--accent` green on `--surface`) as a possible evolution of the hero's terminal-cursor glyph (user-pasted CRT-mascot images).
- Do not adopt: device-shell/tabbed-UI metaphor, CRT/pixel-dissolve transitions, magnetic 3D tilt, audio cues (areebali); WebGL/real-time 3D hero (scfo.de); photorealistic/claymorphism 3D rendering or a 3D pipeline of any kind (CRT-mascot images) — all need real animation/3D libraries the brief forbids. Also skip the mascot images' purple/lavender gradient background — conflicts with the locked dark palette.
- sharplink.com and lutstudios.com still need a real look (screenshot or retry) before they can inform anything.
