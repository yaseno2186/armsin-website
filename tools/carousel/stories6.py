import asyncio, os, sys
from playwright.async_api import async_playwright
from PIL import Image
# reuse styles + page() from stories.py without running its render loop
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "stories.py")).read()
exec(_src[:_src.index("S = {}")])
from w6posts import gword
OUT = HERE + "story/w6/"; os.makedirs(OUT, exist_ok=True)
S = {}

# ---- Mon 2: 10-second tip, Google profile opening hours ----
def maps_page():
    row = lambda d, t, hl=False: f'<div style="display:flex;justify-content:space-between;font:400 26px/1 Inter;color:{"#E8EDEA" if hl else "#9AA0A6"};font-weight:{700 if hl else 400}"><span>{d}</span><span>{t}</span></div>'
    return f'''<div style="background:#101412;height:100%;display:flex;flex-direction:column">
<div style="height:300px;flex:none;background:linear-gradient(135deg,#1C2A22,#14201A);position:relative;overflow:hidden">
<div style="position:absolute;inset:0;background:repeating-linear-gradient(35deg,transparent 0 46px,rgba(234,246,238,.06) 46px 52px),repeating-linear-gradient(-55deg,transparent 0 70px,rgba(234,246,238,.05) 70px 78px)"></div>
<div style="position:absolute;left:50%;top:52%;transform:translate(-50%,-100%);font:400 84px/1 Outfit">📍</div></div>
<div style="padding:24px 26px;display:flex;flex-direction:column;gap:16px">
<div style="font:700 36px/1.1 Outfit;color:#E8EDEA">Ihr Betrieb</div>
<div style="font:400 24px/1 Inter;color:#9AA0A6">★★★★★ · Friseur · Freiberg</div>
<div style="display:flex;gap:12px">{"".join(f'<div style="flex:1;border-radius:999px;border:2px solid #343B37;padding:12px 0;text-align:center;font:600 22px/1 Inter;color:#8AB4F8">{t}</div>' for t in ["Route","Anrufen","Website"])}</div>
<div id="hrs" style="position:relative;border-radius:18px;border:2px solid #343B37;padding:20px;display:flex;flex-direction:column;gap:14px">
<div style="font:700 26px/1 Inter;color:#81C995;white-space:nowrap">Geöffnet · bis 18:00</div>
{row("Montag","9:00–18:00",True)}{row("Dienstag","9:00–18:00")}{row("Mittwoch","9:00–18:00")}{row("Samstag","9:00–13:00")}</div></div></div>'''
tip = f'''<div style="position:relative">{iphone(maps_page(), .95)}
<div style="position:absolute;left:-26px;top:500px;width:430px;height:300px;border-radius:30px;border:6px solid {G};box-shadow:0 0 40px {G}"></div>
{note("prüfen!", 400, 600, G, 8, "left:-60px;top:56px", 220, flip=True)}</div>'''
S["2026-11-02-google-zeiten"] = page("", f'''<div class="kick">10-SEKUNDEN-TIPP</div><h2 style="font-size:100px">Stimmen Ihre Zeiten bei <em>Google</em>?</h2><div class="vis">{tip}</div>
<div class="sub" style="margin:0 0 30px">Betrieb bei Google suchen, Zeiten prüfen.<br>Feiertage nicht vergessen.</div><div class="when">MEHR DAZU · HEUTE 17:30 IM FEED</div>''')

# ---- Tue 3: this or that ----
mini_site = f'''<div class="brow" style="width:380px;height:520px"><div class="bar"><i></i><i></i><i></i><span>ihr-betrieb.de</span></div>
<div class="in"><div style="height:150px;border-radius:12px;background:radial-gradient(circle at 70% 40%,rgba(57,217,122,.35),rgba(10,20,14,1) 70%)"></div>
<div class="ln" style="width:85%"></div><div class="ln" style="width:65%"></div><div class="btn" style="font-size:24px;padding:16px">Termin buchen</div><div class="ln" style="width:75%"></div><div class="ln" style="width:55%"></div></div></div>'''
mini_ig = f'''<div style="width:300px;height:520px;border-radius:44px;border:3px solid rgba(234,246,238,.3);background:#0A140E;padding:46px 18px 18px;display:flex;flex-direction:column;gap:12px">
<div style="display:flex;align-items:center;gap:12px"><div style="width:56px;height:56px;border-radius:50%;background:linear-gradient(45deg,#F58529,#DD2A7B,#8134AF)"></div><div class="ln" style="width:50%"></div></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6px">{"".join('<div style="aspect-ratio:1;border-radius:6px;background:rgba(234,246,238,.12)"></div>' for _ in range(9))}</div>
<div class="ln" style="width:80%"></div><div class="ln" style="width:60%"></div></div>'''
def side(inner, emoji, label, c):
    return f'<div style="display:flex;flex-direction:column;align-items:center;gap:26px">{inner}<div style="display:flex;align-items:center;gap:14px;border:3px solid {c};border-radius:999px;padding:16px 30px;background:rgba(4,12,7,.85)"><span style="font:400 54px/1 Outfit">{emoji}</span><span style="font:700 40px/1 Outfit;color:{LIGHT}">{label}</span></div></div>'
tot = f'''<div style="position:relative;display:flex;gap:60px;align-items:flex-end">{side(mini_site, "🌐", "Website", G)}{side(mini_ig, "📱", "Nur Instagram", "#DD2A7B")}
<div style="position:absolute;left:50%;top:40%;transform:translate(-50%,-50%) rotate(-8deg);width:150px;height:150px;border-radius:50%;background:{G};box-shadow:0 0 60px rgba(57,217,122,.7);display:flex;align-items:center;justify-content:center;font:700 64px/1 Outfit;color:#04150A">VS</div></div>'''
S["2026-11-03-website-oder-insta"] = page("", f'''<div class="kick">DIES ODER DAS</div><h2 style="font-size:100px">Website oder <em>nur Instagram</em>?</h2><div class="vis">{tot}</div>
<div class="when">ANTWORTEN SIE MIT 🌐 ODER 📱</div>''')

# ---- Fri 6: Tech-News Friday teaser ----
def ncard(i, rot, x, y, op):
    return f'''<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({rot}deg);width:560px;height:200px;border-radius:26px;border:2px solid rgba(57,217,122,.5);background:rgba(10,25,16,.95);box-shadow:0 20px 50px rgba(0,0,0,.5);padding:26px 30px;display:flex;flex-direction:column;gap:16px;opacity:{op};text-align:left">
<div style="font:400 26px/1 Pix;color:{G};letter-spacing:3px">NEWS {i} VON 5</div><div style="height:26px;width:88%;border-radius:13px;background:rgba(234,246,238,.22);filter:blur(5px)"></div><div style="height:26px;width:62%;border-radius:13px;background:rgba(234,246,238,.16);filter:blur(5px)"></div></div>'''
stack = '<div style="position:relative;width:820px;height:900px">' + ''.join(
    ncard(i, r, x, y, o) for i, r, x, y, o in [(5, 6, 210, 40, .55), (4, -5, 40, 200, .7), (3, 4, 220, 360, .82), (2, -3, 50, 520, .92), (1, 2, 150, 680, 1)]) + \
    '</div>'
S["2026-11-06-tech-news-teaser"] = page("", f'''<div class="kick">TECH-NEWS FREITAG · KW 45</div><h2><em>5 News</em> in 2 Minuten</h2><div class="vis">{stack}</div>
<div class="when">HEUTE · NEU IM FEED</div>''')

async def main():
    sel = sys.argv[1:] or list(S)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width":1080,"height":1920}, device_scale_factor=2)
        for k in sel:
            f = OUT + k + ".html"; open(f, "w").write(S[k])
            await pg.goto("file://" + f); await pg.wait_for_timeout(500)
            await pg.screenshot(path=OUT + k + ".png")
            Image.open(OUT + k + ".png").convert("RGB").save(OUT + k + ".jpg", quality=92)
            print(k)
        await b.close()
asyncio.run(main())
