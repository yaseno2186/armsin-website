# Armsin carousel toolkit (week 3, Oct 2026)

Reusable renderer for Instagram/LinkedIn carousels in the Armsin green-tech + editorial + paper styles.

- `lib3.py` – shared CSS (fonts, green-tech, paper `variant="p"`, editorial `"e"`), `slide()`, hand-drawn SVG accents (`circ`, `und`, `arrow`, `sparkle`), automatic page counter, `JS_FIT` (headline shrink to 2 lines) and `JS_CHECK` (overlap / margin / clipping / text-leaf overlap / min text size).
- `posts.py` – week-3 posts as examples (NIS2, 5 Fehler, 7 Schritte, 3 Arten, Tech-News with floating brand logos, Instagram vs Website, editorial story with full-bleed photo). Copy it, replace the content.
- `run.py [post ...]` – render PNGs (2160x2700) into `out/<post>/` and print PASS/FAIL per slide.
- `sheet.py <post> <out.png> [w]` – contact sheet.
- `pdfs.py` – vector LinkedIn PDFs (edit the POSTS map).
- `extra.py` (+ `build3.py`) – free-item A4 PDFs and Google Business 2400x1800 JPGs.
- `icons/` – brand SVGs (simple-icons CC0 + Proofpoint/Varonis from their own sites).

Needs: python playwright (Chromium preinstalled), pypdf, PIL; fonts from /mnt/skills/examples/canvas-design/canvas-fonts/.
Put an Unsplash photo at `dl/story.jpg` for the editorial story post.
