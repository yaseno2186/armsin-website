import os, re
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__)) + "/"
F = "/mnt/skills/examples/canvas-design/canvas-fonts/"
ASSETS = "/home/claude/yaseno2186/armsin-website/assets/"
INTER = HERE + "Inter.ttf"
G, LIGHT, MUT, OR = "#39D97A", "#EAF6EE", "#8FB19B", "#C1592B"

FONTS = f"""
@font-face {{ font-family:Outfit; src:url('file://{F}Outfit-Bold.ttf'); font-weight:700; }}
@font-face {{ font-family:Outfit; src:url('file://{F}Outfit-Regular.ttf'); font-weight:400; }}
@font-face {{ font-family:Pix; src:url('file://{F}Silkscreen-Regular.ttf'); }}
@font-face {{ font-family:Mono; src:url('file://{F}JetBrainsMono-Bold.ttf'); font-weight:700; }}
@font-face {{ font-family:MonoR; src:url('file://{F}JetBrainsMono-Regular.ttf'); }}
@font-face {{ font-family:Serif; src:url('file://{F}InstrumentSerif-Italic.ttf'); font-style:italic; }}
@font-face {{ font-family:Hand; src:url('file://{F}NothingYouCouldDo-Regular.ttf'); }}
@font-face {{ font-family:Inter; src:url('file://{INTER}'); font-weight:100 900; }}
*{{box-sizing:border-box;margin:0;padding:0}}
"""

CSS = FONTS + f"""
html,body{{width:1080px;height:1350px;overflow:hidden;background:#040A06;color:{LIGHT};font-family:Outfit}}
.bg{{position:absolute;inset:0;background:
 radial-gradient(ellipse 700px 520px at 50% 55%, rgba(57,217,122,.20), transparent 70%),
 radial-gradient(ellipse 900px 380px at 50% 100%, rgba(57,217,122,.30), transparent 70%),
 linear-gradient(180deg,#0B1A11,#040A06);}}
.bg:after{{content:"";position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(0,0,0,.16) 0 2px,transparent 2px 5px),radial-gradient(ellipse at center,transparent 55%,rgba(0,0,0,.55));}}
.grain{{position:absolute;inset:0;opacity:.10;mix-blend-mode:overlay;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}}
.wrap{{position:absolute;inset:0;padding:56px 80px 50px;display:flex;flex-direction:column;align-items:center;text-align:center}}
.top{{flex:none;width:920px;height:58px;display:flex;justify-content:space-between;align-items:center}}
.logo{{font:700 46px/58px Mono;color:{LIGHT};display:flex;align-items:center;gap:6px}}
.logo i{{display:block;width:19px;height:42px;background:{OR}}}
.cnt{{font:400 26px/30px Pix;color:{MUT};letter-spacing:2px}}
.kicker{{font:400 28px/34px Pix;color:{G};text-shadow:0 0 18px rgba(57,217,122,.7);letter-spacing:3px;text-transform:uppercase;margin-top:34px;flex:none;max-width:920px}}
.hand{{font:400 46px/1 Hand;color:{G};margin-top:30px;flex:none;transform:rotate(-3deg)}}
h1{{font:700 108px/1.06 Outfit;letter-spacing:-2px;margin-top:12px;padding-bottom:14px;flex:none;width:920px;color:{LIGHT}}}
h1 em{{font-style:normal;color:{G};text-shadow:0 0 30px rgba(57,217,122,.55);position:relative;white-space:nowrap}}
h1 .s{{font-family:Serif;font-style:italic;font-weight:400;letter-spacing:0;color:{LIGHT}}}
h1 em .s{{color:{G}}} h1 em:has(.circ){{display:inline-block;margin:0 34px;padding:0 10px}}
.circ{{position:absolute;left:-12%;top:-20%;width:124%;height:140%;overflow:visible;pointer-events:none}}
.und{{position:absolute;left:0;bottom:-12px;width:100%;height:26px;overflow:visible}}
.visual{{flex:1;min-height:0;width:920px;margin-top:20px;display:flex;align-items:center;justify-content:center;position:relative}}
.box{{flex:none;margin-top:22px;background:{G};color:#04150A;font:700 36px/1.22 Outfit;padding:20px 34px;border-radius:16px;box-shadow:0 0 40px rgba(57,217,122,.4);max-width:920px}}
.box.o{{background:rgba(57,217,122,.1);color:{LIGHT};border:3px solid {G};box-shadow:none}}
.box b{{color:{G}}} .box.n{{background:transparent;border:none;box-shadow:none;color:{MUT};font:400 26px/1.3 Inter;padding:4px 0}}
.hint{{flex:none;align-self:stretch;display:flex;justify-content:space-between;align-items:center;font:400 24px/30px Pix;color:{G};letter-spacing:3px;margin-top:14px;text-shadow:0 0 14px rgba(57,217,122,.6)}}
.hint .mk{{display:flex;align-items:center;gap:10px;color:{MUT};text-shadow:none}}
.hint svg{{width:24px;height:28px}}
.foot{{flex:none;margin-top:14px;width:920px;height:70px;border:2px solid rgba(234,246,238,.16);border-radius:22px;display:flex;align-items:center;justify-content:space-between;padding:0 32px;font:400 26px Inter;color:#B9C9BF;background:rgba(0,0,0,.25)}}
.foot .l{{display:flex;align-items:center;gap:14px}} .foot svg{{width:30px;height:30px}} .foot .in{{font:700 28px Inter}}
/* keyword slide */
.kw{{font:400 300px/1.18 Serif;font-style:italic;color:{G};text-shadow:0 0 60px rgba(57,217,122,.5);letter-spacing:-4px;white-space:nowrap}}
.kwsub{{font:400 40px/1.3 Outfit;color:{LIGHT};max-width:820px;margin-top:10px}}
/* cards etc */
.card{{border:2px solid rgba(57,217,122,.4);background:rgba(10,25,16,.85);border-radius:26px;padding:28px 34px;text-align:left}}
.lab{{font:400 24px/28px Pix;letter-spacing:2px;color:{MUT};margin-bottom:10px}} .lab.g{{color:{G}}}
.big{{font:700 46px/1.15 Outfit;color:{LIGHT}}} .big em{{font-style:normal;color:{G}}}
.txt{{font:400 32px/1.35 Outfit;color:#C9DBCF}}
.pill{{position:absolute;border:2px solid {G};background:rgba(4,12,7,.9);border-radius:999px;padding:12px 26px;font:700 30px Outfit;color:{LIGHT};box-shadow:0 0 22px rgba(57,217,122,.35);white-space:nowrap}}
.keybtn{{width:760px;height:250px;border-radius:34px;background:linear-gradient(180deg,#7DF0AC,#39D97A);box-shadow:0 14px 0 #1F8F4E,0 0 90px rgba(57,217,122,.55);display:flex;align-items:center;justify-content:center;font:700 150px/1 Outfit;color:#04150A;letter-spacing:-2px}}
.chip{{border:2px solid rgba(57,217,122,.55);border-radius:16px;padding:14px 26px;font:700 28px Outfit;color:{LIGHT};background:rgba(57,217,122,.08)}}
.chip span{{font:400 22px Pix;color:{G};margin-right:12px}}
.tile{{border-radius:28px;border:2px solid rgba(57,217,122,.45);background:radial-gradient(circle at 50% 40%,rgba(57,217,122,.16),rgba(8,20,13,.95) 70%);display:flex;align-items:center;justify-content:center;box-shadow:0 0 40px rgba(57,217,122,.18)}}
.logo-w svg{{fill:{LIGHT};width:100%;height:100%}} .logo-c svg{{width:100%;height:100%}} .logo-c svg, .logo-c svg path{{fill:var(--c) !important}} .logo-w svg path{{fill:{LIGHT}}}
.brow{{border-radius:22px;border:3px solid rgba(57,217,122,.6);background:#0A140E;box-shadow:0 0 50px rgba(57,217,122,.3);overflow:hidden;display:flex;flex-direction:column;text-align:left}}
.brow .bar{{height:46px;background:#122019;display:flex;align-items:center;gap:10px;padding:0 18px;flex:none}}
.brow .bar i{{width:14px;height:14px;border-radius:50%;background:rgba(234,246,238,.25)}}
.brow .bar span{{margin-left:14px;font:400 22px MonoR;color:{MUT}}}
.brow .in{{padding:24px 28px;display:flex;flex-direction:column;gap:14px;flex:1}}
.ln{{height:14px;border-radius:7px;background:rgba(234,246,238,.18)}}
.btn{{background:{G};color:#04150A;font:700 30px/1 Outfit;padding:20px 26px;border-radius:14px;text-align:center}}
.btn.o{{background:transparent;border:2px solid rgba(234,246,238,.35);color:{LIGHT}}}
.num{{font:400 34px/1 Pix;color:{G}}}
.phone{{width:290px;height:460px;border-radius:44px;border:3px solid rgba(234,246,238,.28);background:#0A140E;padding:26px 22px;display:flex;flex-direction:column;gap:14px;overflow:hidden;text-align:left}}
.phone.good{{border-color:{G};box-shadow:0 0 50px rgba(57,217,122,.45);background:#0B1D13}} .phone.bad{{opacity:.6}}
.cap{{font:400 24px/28px Pix;letter-spacing:2px;color:{MUT}}} .cap.g{{color:{G}}}
.x{{color:#E06A4E}}
/* paper variant */
.paper{{position:absolute;inset:0;background:radial-gradient(ellipse at 30% 20%,#F4EFE4,#E9E2D2 70%,#DDD4C1)}}
.paper:after{{content:"";position:absolute;inset:0;opacity:.35;mix-blend-mode:multiply;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .4 0 0 0 0 .35 0 0 0 0 .3 0 0 0 .5 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}}
.holes{{position:absolute;left:34px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:space-around;padding:240px 0}}
.holes i{{width:26px;height:26px;border-radius:50%;background:#2A2620;opacity:.85}}
body.p{{color:#1E1B16}}
body.p .logo{{color:#1E1B16}} body.p .cnt{{color:#6E675B}}
body.p .kicker{{color:#2E8F55;text-shadow:none}}
body.p h1{{color:#1E1B16;font:400 104px/1.04 Serif;font-style:italic;letter-spacing:-1px;text-align:left}}
body.p h1 em{{color:{OR};text-shadow:none}}
body.p .wrap{{align-items:flex-start;text-align:left}}
body.p .foot{{border-color:rgba(30,27,22,.2);background:rgba(255,255,255,.35);color:#4A453C}} body.p .foot svg{{stroke:#4A453C}}
body.p .hint{{color:#2E8F55;text-shadow:none}} body.p .hint .mk{{color:#6E675B}}
.step{{flex:1;border:2px solid rgba(30,27,22,.25);border-radius:22px;padding:26px 28px;background:rgba(255,255,255,.45);text-align:left;display:flex;flex-direction:column;gap:12px}}
.step .n{{font:400 30px Pix;color:#2E8F55}} .step h3{{font:700 52px/1.1 Outfit;color:#1E1B16}} .step p{{font:400 38px/1.3 Outfit;color:#4A453C}}
/* editorial */
body.e .bg{{background:radial-gradient(ellipse 800px 600px at 70% 30%,rgba(233,185,73,.10),transparent 70%),radial-gradient(ellipse 900px 380px at 50% 100%,rgba(57,217,122,.22),transparent 70%),linear-gradient(180deg,#0E1712,#050A07)}}
body.e h1 em{{color:#E9B949;text-shadow:none}} body.e .txt{{font-size:38px}} body.e h1 .s{{color:#F3EBDD}}
body.e .kicker{{color:#E9B949;text-shadow:0 0 18px rgba(233,185,73,.5)}} body.e .box.o{{border-color:#E9B949;background:rgba(233,185,73,.08)}} body.e .hint{{color:#E9B949;text-shadow:none}}
body.p .box.n{{color:#3A352D;font:600 32px/1.3 Inter}}
.manila{{position:absolute;inset:0;background:radial-gradient(ellipse at 30% 20%,#EBDDB6,#DCC78F 70%,#CFB77C)}}
.manila:after{{content:"";position:absolute;inset:0;opacity:.35;mix-blend-mode:multiply;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.7' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .45 0 0 0 0 .35 0 0 0 0 .2 0 0 0 .55 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}}
body.m h1 em{{color:#B3261E}} body.m .kicker{{color:#7A5A1E}} body.m .hint{{color:#7A5A1E}}
.canvas{{position:absolute;inset:0;background:radial-gradient(circle,rgba(30,27,22,.13) 1.6px,transparent 1.8px) 0 0/34px 34px,linear-gradient(180deg,#F6F4EF,#ECE8DF)}}
body.q h1{{font:700 96px/1.06 Outfit;font-style:normal;letter-spacing:-2px}}
"""

IG_SVG = '<svg viewBox="0 0 32 32" fill="none" stroke="#B9C9BF" stroke-width="2.4"><rect x="3" y="3" width="26" height="26" rx="8"/><circle cx="16" cy="16" r="6.2"/><circle cx="23.4" cy="8.6" r="1.4" fill="#B9C9BF" stroke="none"/></svg>'
MERK = '<svg viewBox="0 0 24 28" fill="none" stroke="currentColor" stroke-width="2.6"><path d="M4 3h16v22l-8-6-8 6z"/></svg>'

def circ(color=G):
    return f'<svg class="circ" viewBox="0 0 200 100" preserveAspectRatio="none"><path d="M18 55 C10 22 70 6 118 10 C170 14 196 34 190 58 C184 86 120 96 72 92 C30 88 6 74 14 50 C18 38 30 30 44 26" fill="none" stroke="{color}" stroke-width="3.2" stroke-linecap="round" vector-effect="non-scaling-stroke" style="stroke-width:6px"/></svg>'
def und(color=G):
    return f'<svg class="und" viewBox="0 0 300 20" preserveAspectRatio="none"><path d="M4 12 C60 4 120 16 180 9 C220 5 260 12 296 7" fill="none" stroke="{color}" stroke-linecap="round" vector-effect="non-scaling-stroke" style="stroke-width:6px"/></svg>'
def arrow(color=G, w=120):
    return f'<svg width="{w}" height="50" viewBox="0 0 120 50" style="flex:none"><path d="M6 30 C30 10 70 12 104 26" fill="none" stroke="{color}" stroke-width="5" stroke-linecap="round"/><path d="M90 14 L106 27 L88 36" fill="none" stroke="{color}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def sparkle(color=G, s=70):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 100 100" style="flex:none"><path d="M50 6 C53 38 62 47 94 50 C62 53 53 62 50 94 C47 62 38 53 6 50 C38 47 47 38 50 6Z" fill="none" stroke="{color}" stroke-width="4" stroke-linejoin="round"/></svg>'

def logo_svg(name):
    s = open(HERE + "icons/" + name + ".svg").read()
    s = re.sub(r'<title>.*?</title>', '', s)
    return s

def slide(i, n, h1, visual, kicker="", box="", boxcls="", hand="", cover=False, last=False, variant=""):
    top = f'<div class="top"><div class="logo">armsin<i></i></div><div class="cnt">{i:02d}/{n:02d}</div></div>'
    k = f'<div class="kicker">{kicker}</div>' if kicker else ""
    hd = f'<div class="hand">{hand}</div>' if hand else ""
    b = f'<div class="box {boxcls}">{box}</div>' if box else ""
    mk = f'<span class="mk">{MERK}MERKEN</span>' if (cover or last) else '<span></span>'
    hint = f'<div class="hint">{mk}<span>{"" if last else "WISCHEN &gt;"}</span></div>'
    bgl = '<div class="canvas"></div>' if variant == "c" else '<div class="manila"></div>' if variant == "m" else '<div class="paper"></div><div class="holes"><i></i><i></i><i></i></div>' if variant in ("p","q") else '<div class="bg"></div><div class="grain"></div>'
    return variant, f'''{bgl}<div class="wrap">{top}{k}{hd}<h1>{h1}</h1><div class="visual">{visual}</div>{b}{hint}
<div class="foot"><div class="l">{IG_SVG}<span class="in">in</span><span>@armsin_digital_media</span></div><span>armsin.de</span></div></div>'''

def kwslide(i, n, word, sub, kicker="GRATIS FÜR SIE"):
    vis = f'<div style="display:flex;flex-direction:column;align-items:center"><div class="kw">“{word}”</div><div class="kwsub">{sub}</div></div>'
    return slide(i, n, 'Kommentieren Sie <span class="s">das Wort</span>', vis, kicker=kicker)

JS_FIT = """
() => {
  const h1 = document.querySelector('h1');
  let fs = parseFloat(getComputedStyle(h1).fontSize);
  const lh = () => parseFloat(getComputedStyle(h1).lineHeight);
  while ((h1.scrollWidth > h1.clientWidth + 1 || (h1.getBoundingClientRect().height-14) / lh() > 2.05) && fs > 70) { fs -= 2; h1.style.fontSize = fs + 'px'; }
  const kw = document.querySelector('.kw'); if (kw) { let k = 300; while (kw.scrollWidth > 900 && k > 120) { k -= 10; kw.style.fontSize = k + 'px'; } }
  return fs;
}
"""
JS_CHECK = """
() => {
  const sel = ['.top','.kicker','.hand','h1','.visual','.box','.hint','.foot'];
  const els = sel.map(s => [s, document.querySelector(s)]).filter(x => x[1]);
  const R = els.map(([s,e]) => [s, e.getBoundingClientRect()]);
  const errs = [];
  for (let i=0;i<R.length;i++) for (let j=i+1;j<R.length;j++) {
    const a=R[i][1], b=R[j][1];
    if (a.left < b.right-1 && b.left < a.right-1 && a.top < b.bottom-1 && b.top < a.bottom-1) errs.push('overlap '+R[i][0]+' x '+R[j][0]);
  }
  for (const [s,r] of R) { if (r.left < 79 || r.right > 1001 || r.top < 0 || r.bottom > 1350) errs.push('margin '+s); }
  for (const [s,e] of els) { const tol = (s==='.visual'||s==='.box')?1:(s==='h1'?20:8); if (e.scrollHeight > e.clientHeight+tol || e.scrollWidth > e.clientWidth+tol) errs.push('clipped '+s+' '+e.scrollHeight+'/'+e.clientHeight+' '+e.scrollWidth+'/'+e.clientWidth); }
  const h1 = document.querySelector('h1'); const lines = (h1.getBoundingClientRect().height-14) / parseFloat(getComputedStyle(h1).lineHeight);
  if (lines > 2.05) errs.push('headline lines '+lines.toFixed(1));
  const v = document.querySelector('.visual').getBoundingClientRect();
  document.querySelectorAll('.visual *').forEach(c => { if (c.closest('svg') && c.tagName!=='svg') return; const r=c.getBoundingClientRect(); if (r.width && (r.left < v.left-2 || r.right > v.right+2 || r.top < v.top-2 || r.bottom > v.bottom+2)) errs.push('visual child outside: '+(c.className.baseVal!==undefined?c.className.baseVal:c.className||c.tagName)); });
  document.querySelectorAll('.visual *, .box').forEach(c => { if (c.closest('svg')) return; if ([...c.childNodes].some(n=>n.nodeType===3&&n.textContent.trim())) { const fs=parseFloat(getComputedStyle(c).fontSize); if (fs<21.5) errs.push('small text '+fs+' '+c.textContent.slice(0,14)); } });
  // pills must not overlap each other or text cards
  const pills=[...document.querySelectorAll('.visual .pill')].map(p=>p.getBoundingClientRect());
  for (let i=0;i<pills.length;i++) for (let j=i+1;j<pills.length;j++){const a=pills[i],b=pills[j]; if (a.left<b.right&&b.left<a.right&&a.top<b.bottom&&b.top<a.bottom) errs.push('pill overlap '+i+'x'+j);}
  // text leaves inside the visual must not overlap each other
  const leaves=[...document.querySelectorAll('.visual *')].filter(c=>!c.closest('svg')&&[...c.childNodes].some(n=>n.nodeType===3&&n.textContent.trim()));
  const LR=leaves.map(c=>{const r=document.createRange();r.selectNodeContents(c);return [c,r.getBoundingClientRect()]});
  for(let i=0;i<LR.length;i++)for(let j=i+1;j<LR.length;j++){const [ca,a]=LR[i],[cb,b]=LR[j]; if(ca.contains(cb)||cb.contains(ca))continue; if(a.left<b.right-2&&b.left<a.right-2&&a.top<b.bottom-2&&b.top<a.bottom-2) errs.push('text overlap: '+ca.textContent.slice(0,12)+' x '+cb.textContent.slice(0,12));}
  return {errs, fs: getComputedStyle(h1).fontSize, lines: +lines.toFixed(2)};
}
"""

async def render(post_dir, slides, out_root):
    d = out_root + post_dir + "/"
    os.makedirs(d, exist_ok=True)
    allok = True
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width":1080,"height":1350}, device_scale_factor=2)
        for i, (variant, body) in enumerate(slides, 1):
            path = d + f"{i:02d}.html"
            cls = {"p":"p","e":"e","q":"p q","c":"p q c","m":"p q m"}.get(variant, "")
            body = re.sub(r'<div class="cnt">\d+/\d+</div>', f'<div class="cnt">{i:02d}/{len(slides):02d}</div>', body)
            open(path, "w").write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{cls}">{body}</body></html>')
            await pg.goto("file://" + path)
            await pg.wait_for_timeout(400)
            await pg.evaluate(JS_FIT)
            await pg.wait_for_timeout(150)
            res = await pg.evaluate(JS_CHECK)
            await pg.screenshot(path=d + f"{i:02d}.png")
            ok = not res["errs"]; allok &= ok
            print(post_dir, i, "PASS" if ok else "FAIL " + "; ".join(res["errs"]), f"h1={res['fs']} lines={res['lines']}")
        await b.close()
    return allok
