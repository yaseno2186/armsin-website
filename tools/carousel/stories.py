import asyncio, os, sys
from playwright.async_api import async_playwright
from PIL import Image
from lib3 import CSS, HERE, G, LIGHT, OR
from w5posts import *
OUT = HERE + "story/w5/"; os.makedirs(OUT, exist_ok=True)
SCSS = CSS + """
html,body{width:1080px!important;height:1920px!important}
.st{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;text-align:center;padding:250px 80px 260px}
.st .lg{position:absolute;top:120px;left:80px}
.st .kick{font:400 30px/1 Pix;letter-spacing:6px;color:#39D97A;text-shadow:0 0 18px rgba(57,217,122,.7)}
.st h2{font:700 108px/1.04 Outfit;letter-spacing:-2px;color:#EAF6EE;margin-top:26px}
.st h2 em{font-style:normal;color:#39D97A;text-shadow:0 0 30px rgba(57,217,122,.55)}
.st .vis{flex:1;min-height:0;width:100%;display:flex;align-items:center;justify-content:center;position:relative}
.st .when{font:400 30px/1 Pix;letter-spacing:5px;color:#EAF6EE;border:3px solid #39D97A;border-radius:999px;padding:22px 40px;box-shadow:0 0 30px rgba(57,217,122,.4);background:rgba(4,12,7,.85)}
.st .sub{font:400 44px/1.3 Outfit;color:#C9DBCF;margin-top:30px;max-width:900px}
body.p .st .kick{color:#2E8F55;text-shadow:none} body.p .st h2{color:#1E1B16} body.p .st h2 em{color:#C1592B;text-shadow:none}
body.p .st .when{color:#1E1B16;border-color:#1E1B16;background:#FBF8F1;box-shadow:0 10px 24px rgba(60,45,20,.15)} body.p .st .sub{color:#4A453C}
body.e .st h2 em{color:#E9B949}
"""
LOGO = '<div class="lg"><div class="logo">armsin<i></i></div></div>'
def bg(v):
    return {'p':'<div class="paper"></div>','c':'<div class="canvas"></div>'}.get(v,'<div class="bg"></div><div class="grain"></div>')
def page(v, inner, cls=""):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{SCSS}</style></head><body class="{cls}">{bg(v)}<div class="st">{LOGO}{inner}</div></body></html>'

S = {}
# Tue 3: cinematic monitor teaser -> reuse s1.html, adjust labels
s1 = open(HERE+"story/s1.html").read().replace("DEMNÄCHST AUF ARMSIN","NEU AUF ARMSIN").replace("DI · 17:30 · IM FEED","HEUTE · 17:30 · IM FEED")
S["2026-11-03-chatgpt"] = s1
# Wed 4: quick tip
tap = f'''<div style="position:relative">{iphone(new_page(), .95)}<div style="position:absolute;left:62%;top:36%;width:130px;height:130px;margin-left:-65px;border-radius:50%;border:6px solid {G};background:rgba(57,217,122,.15);box-shadow:0 0 40px {G}"></div></div>'''
S["2026-11-04-tipp"] = page("", f'''<div class="kick">10-SEKUNDEN-TIPP</div><h2>Ist Ihre Nummer <em>antippbar</em>?</h2><div class="vis">{tap}</div>
<div class="sub" style="margin:0 0 30px">Seite am Handy öffnen, Nummer antippen.<br>Klingelt es nicht? Dann fehlt eine Zeile Code.</div>''')
# Thu 5: 41 %
S["2026-11-05-41prozent"] = page("p", f'''<div class="kick">DIHK-UMFRAGE · 5.000 FIRMEN</div><div class="vis" style="flex-direction:column;gap:40px">
<div style="font:700 360px/1 Outfit;letter-spacing:-12px;color:#2E8F55;margin:30px 0">41 %</div>
<div style="font:700 64px/1.15 Outfit;color:#1E1B16;max-width:860px">Was diese Zahl über KI im Betrieb sagt.</div></div><div class="when">HEUTE · 17:30 · IM FEED</div>''', "p q")
# Sat 7: split teaser canvas
S["2026-11-07-vorher-nachher"] = page("c", f'''<div class="kick" style="color:#2E8F55;text-shadow:none">VORHER / NACHHER</div><h2 style="color:#1E1B16;font-size:96px">Was hat sich <em style="color:#C1592B;text-shadow:none">geändert</em>?</h2>
<div class="vis">{split_phone(.95)}</div><div class="when" style="color:#1E1B16;border-color:#1E1B16;background:#FFFDF8;box-shadow:none">JETZT IM FEED</div>''', "p q c")
# Sun 8: postcard rule
card = f'''<div style="width:860px;height:560px;background:#F4EEDF;border-radius:10px;transform:rotate(-3deg);box-shadow:0 30px 60px rgba(0,0,0,.6);display:flex;padding:40px;gap:30px;text-align:left">
<div style="flex:1.3;font:italic 400 64px/1.15 Serif;color:#2B2116;display:flex;align-items:center">„Was nicht auf eine Postkarte passt, gehört nicht in den Chat.“</div>
<div style="width:2px;background:rgba(43,33,22,.25)"></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:space-between"><div style="align-self:flex-end;width:120px;height:140px;border:4px dashed #B3261E;display:flex;align-items:center;justify-content:center;font:700 26px/1.1 Mono;color:#B3261E;text-align:center">KI<br>CHAT</div>
<div><div style="height:2px;background:rgba(43,33,22,.35);margin:30px 0"></div><div style="height:2px;background:rgba(43,33,22,.35);margin:30px 0"></div><div style="height:2px;background:rgba(43,33,22,.35)"></div></div></div></div>'''
S["2026-11-08-postkarte"] = page("", f'''<div class="kick" style="color:#E9B949;text-shadow:none">FAUSTREGEL · KI &amp; DATEN</div><div class="vis">{card}</div>
<div class="sub" style="margin:0 0 30px">Mehr dazu heute um 18:00 im Feed.</div>''', "e")
# Mon 9: laptop log
S["2026-11-09-hacker"] = page("", f'''<div class="kick">ECHTER FALL · KI-HACKING</div><h2 style="font-size:96px">1 Hacker.<br><em style="color:#E06A4E;text-shadow:0 0 30px rgba(224,106,78,.55)">100 Websites.</em></h2>
<div class="vis" style="flex-direction:column;gap:34px">{laptop(agentlog(), 760)}<div style="display:flex;align-items:center;gap:14px;background:rgba(4,12,7,.9);border:2px solid rgba(234,246,238,.2);border-radius:14px;padding:14px 22px">{rlogo(220)}<span style="font:400 24px/1 Pix;color:#8FB19B">19.10.2026</span></div></div>
<div class="when">HEUTE · 17:30 · IM FEED</div>''')

async def main():
    sel = sys.argv[1:] or list(S)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width":1080,"height":1920}, device_scale_factor=2)
        for k in sel:
            f = OUT+k+".html"; open(f,"w").write(S[k])
            await pg.goto("file://"+f); await pg.wait_for_timeout(500)
            await pg.screenshot(path=OUT+k+".png")
            Image.open(OUT+k+".png").convert("RGB").save(OUT+k+".jpg", quality=92)
            print(k)
        await b.close()
asyncio.run(main())
