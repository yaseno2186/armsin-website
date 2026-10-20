import asyncio, os
from playwright.async_api import async_playwright
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)) + "/"
F = "/mnt/skills/examples/canvas-design/canvas-fonts/"
ASSETS = "/home/claude/yaseno2186/armsin-website/assets/"
G = "#39D97A"
FONTS = f"""
@font-face {{ font-family:Outfit; src:url('file://{F}Outfit-Bold.ttf'); font-weight:700; }}
@font-face {{ font-family:Outfit; src:url('file://{F}Outfit-Regular.ttf'); font-weight:400; }}
@font-face {{ font-family:Pix; src:url('file://{F}Silkscreen-Regular.ttf'); }}
@font-face {{ font-family:Mono; src:url('file://{F}JetBrainsMono-Bold.ttf'); font-weight:700; }}
@font-face {{ font-family:MonoR; src:url('file://{F}JetBrainsMono-Regular.ttf'); }}
@font-face {{ font-family:Inter; src:url('file://{HERE}Inter.ttf'); font-weight:100 900; }}
*{{box-sizing:border-box;margin:0;padding:0}}
"""

# ---------------- free items (A4 PDF) ----------------
PDF_CSS = FONTS + f"""
@page {{ size:210mm 297mm; margin:0 }}
html,body{{width:794px;height:1123px;background:#040A06;color:#EAF6EE;font-family:Outfit;-webkit-print-color-adjust:exact}}
.bg{{position:absolute;inset:0;background:radial-gradient(ellipse 600px 420px at 80% 8%,rgba(57,217,122,.22),transparent 70%),radial-gradient(ellipse 800px 300px at 50% 100%,rgba(57,217,122,.28),transparent 70%),linear-gradient(180deg,#0B1A11,#040A06)}}
.page{{position:absolute;inset:0;padding:44px 60px 34px;display:flex;flex-direction:column}}
.logo{{font:700 34px/40px Mono;display:flex;align-items:center;gap:6px}} .logo i{{display:block;width:14px;height:30px;background:#C1592B}}
.kick{{font:400 18px Pix;color:{G};letter-spacing:2px;margin-top:22px;text-shadow:0 0 12px rgba(57,217,122,.6)}}
h1{{font:700 50px/1.05 Outfit;letter-spacing:-1px;margin-top:8px}} h1 em{{font-style:normal;color:{G}}}
.sub{{font:400 21px/1.35 Outfit;color:#B9C9BF;margin-top:12px}}
.items{{margin-top:20px;display:flex;flex-direction:column;gap:10px;flex:1}}
.it{{border:2px solid rgba(57,217,122,.4);background:rgba(10,25,16,.8);border-radius:18px;padding:12px 20px;display:flex;gap:18px;align-items:flex-start}}
.it .bx{{flex:none;width:30px;height:30px;border:3px solid {G};border-radius:8px;margin-top:4px}}
.it h2{{font:700 25px/1.15 Outfit}} .it p{{font:400 18px/1.35 Outfit;color:#B9C9BF;margin-top:4px}}
.it .ln{{border-bottom:2px dashed rgba(234,246,238,.25);height:22px;margin-top:6px}}
.foot{{margin-top:16px;border-top:2px solid rgba(234,246,238,.16);padding-top:14px;display:flex;justify-content:space-between;align-items:flex-end;font:400 15px/1.4 Inter;color:#9DB3A5}}
.foot b{{font:700 19px Outfit;color:#EAF6EE}}
"""
def pdf_page(kick, h1, sub, items, note):
    its = ''.join(f'<div class="it"><div class="bx"></div><div style="flex:1"><h2>{t}</h2><p>{p}</p><div class="ln"></div></div></div>' for t,p in items)
    return f'''<div class="bg"></div><div class="page"><div class="logo">armsin<i></i></div><div class="kick">{kick}</div><h1>{h1}</h1><div class="sub">{sub}</div>
<div class="items">{its}</div>
<div class="foot"><div style="max-width:470px">{note}</div><div style="text-align:right"><b>armsin.de</b><br>Yass · Freiberg und Umgebung<br>@armsin_digital_media</div></div></div>'''

PROFIL = pdf_page("GRATIS-CHECK · STAND OKT 2026", "Google-Profil-<em>Check</em>", "5 Punkte, 3 Minuten. Öffnen Sie Ihr Profil bei Google und haken Sie ab.", [
 ("Name, Adresse, Telefon", "Stimmen sie mit Ihrer Website und Ihrem Impressum überein? Eine Schreibweise überall."),
 ("Öffnungszeiten", "Aktuell, auch für Feiertage, Urlaub und Sonderöffnungen?"),
 ("Vorschläge von Nutzern", "Im Profil nachsehen, ob jemand Änderungen vorgeschlagen hat. Falsche ablehnen. Laut Branchenbericht (Okt. 2026) bleiben dafür vier Tage."),
 ("Fotos", "Mindestens drei aktuelle: Eingang, Innenraum, Ihre Arbeit oder Produkte."),
 ("Beiträge und Bewertungen", "Stehen in Beiträgen nur Ihre echten Kontaktdaten? Neue Bewertungen freundlich beantwortet?"),
], "Allgemeine Hinweise. Google ändert Funktionen laufend, Details können abweichen. Keine Rechtsberatung.")

AUTOMAT = pdf_page("CHECKLISTE FÜR ENTWICKLER", "Erst fragen, <em>dann bauen.</em>", "5 Fragen vor jeder Automatisierung für einen Kunden. Mit Platz für Notizen.", [
 ("Wer macht es heute?", "Wer, wie oft, wie lange, welche Schritte? Den echten Ablauf aufschreiben, nicht den vermuteten."),
 ("Lohnt es sich?", "Zeit pro Jahr von Hand gegen Bauzeit und Wartung rechnen. Selten und kurz: oft besser lassen."),
 ("Was, wenn es schiefgeht?", "Wer wird benachrichtigt? Wo liegt das Log? Gibt es einen manuellen Notweg?"),
 ("Wohin gehen die Daten?", "Welcher Dienst, Auftragsverarbeitungsvertrag (AVV), Serverstandort, Löschfristen? Bei Unsicherheit Datenschutz-Fachleute fragen."),
 ("Wer wartet es später?", "Kurze Doku (was es tut, wo Zugänge liegen, wen man fragt) und eine Ersatzperson."),
], "Allgemeine Orientierung für die Praxis. Keine Rechtsberatung.")

# ---------------- Google Business JPGs (4:3) ----------------
GCSS = FONTS + f"""
html,body{{width:1200px;height:900px;background:#0A0E0C;color:#D6E8DD;font-family:Inter}}
.bg{{position:absolute;inset:0;background:radial-gradient(circle,rgba(57,217,122,.14) 1.4px,transparent 1.6px) 0 0/34px 34px,radial-gradient(ellipse 700px 500px at 75% 45%,rgba(57,217,122,.22),transparent 70%),#0A0E0C}}
.w{{position:absolute;inset:0;padding:64px 80px 52px;display:flex;flex-direction:column}}
.tag{{align-self:flex-start;font:700 24px Mono;color:#0A0E0C;background:{G};border-radius:999px;padding:10px 24px;letter-spacing:1px}}
h1{{font:700 64px/1.1 Mono;color:#EAF6EE;margin-top:30px;letter-spacing:-1px}} h1 em{{font-style:normal;color:{G};text-shadow:0 0 24px rgba(57,217,122,.5)}}
.mid{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:18px}}
.c{{background:#131E17;border:2px solid rgba(57,217,122,.35);border-radius:20px;padding:22px 30px;font:600 34px/1.2 Inter;display:flex;gap:22px;align-items:center}}
.c i{{flex:none;width:36px;height:36px;border-radius:10px;background:{G};position:relative}} .c i:after{{content:"";position:absolute;left:12px;top:5px;width:10px;height:19px;border:solid #04150A;border-width:0 5px 5px 0;transform:rotate(45deg)}}
.f{{display:flex;justify-content:space-between;align-items:center;border-top:2px solid rgba(214,232,221,.15);padding-top:20px;font:400 26px Inter;color:#9DB3A5}}
.f .lg{{font:700 40px Mono;color:#EAF6EE;display:flex;align-items:center;gap:6px}} .f .lg b{{display:block;width:16px;height:34px;background:#C1592B}}
"""
def gslide(tag, h1, mid):
    return f'<div class="bg"></div><div class="w"><div class="tag">{tag}</div><h1>{h1}</h1><div class="mid">{mid}</div><div class="f"><div class="lg">armsin<b></b></div><div style="text-align:right">armsin.de · Freiberg und Umgebung</div></div></div>'
def chk(items): return ''.join(f'<div class="c"><i></i><span>{t}</span></div>' for t in items)
GS = {
 "d": gslide("GOOGLE-PROFIL", "Ist Ihr Google-Profil <em>auf Stand?</em>", chk(["Nummer und Öffnungszeiten stimmen","Fremde Änderungen geprüft","Aktuelle Fotos eingestellt"])),
 "e": gslide("ERREICHBARKEIT", "Verpasster Anruf, <em>verlorener Kunde?</em>", chk(["Rückruf per Knopfdruck anfordern","Termin online buchen","Antworten schon auf der Seite"])),
 "f": f'<div class="bg"></div><div class="w"><div class="tag">ÜBER MICH</div><h1>Hallo, ich bin Yass aus <em>Freiberg.</em></h1><div class="mid" style="flex-direction:row;align-items:center;gap:44px"><div style="flex:none;width:300px;height:360px;border-radius:24px;background:url(file://{HERE}yass-story.jpg) center 30%/cover;border:3px solid {G};box-shadow:0 0 50px rgba(57,217,122,.45)"></div><div style="font:500 36px/1.35 Inter;color:#D6E8DD">Websites, Abläufe und Fotos für kleine Betriebe.<br><span style="color:{G}">Ehrlich beraten, auch am Anfang.</span></div></div><div class="f"><div class="lg">armsin<b></b></div><div>armsin.de · Freiberg und Umgebung</div></div></div>',
 "g": gslide("ABLÄUFE", "Weniger Routine <em>im Betrieb.</em>", chk(["Lohnt sich die Automatisierung?","Wo liegen Ihre Daten?","Wer pflegt es später?"])),
}
NAMES = {"d":"post-d-google-profil","e":"post-e-verpasster-anruf","f":"post-f-story","g":"post-g-automation"}

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, body in [("free-google-profil-check", PROFIL), ("free-automation-checkliste", AUTOMAT)]:
            pg = await b.new_page(viewport={"width":794,"height":1123})
            open(HERE+name+".html","w").write(f'<!doctype html><html><head><meta charset="utf-8"><style>{PDF_CSS}</style></head><body>{body}</body></html>')
            await pg.goto("file://"+HERE+name+".html"); await pg.wait_for_timeout(400)
            ov = await pg.evaluate("()=>{const p=document.querySelector('.page');const it=document.querySelector('.items');return [p.scrollHeight,p.clientHeight,it.scrollHeight,it.clientHeight]}")
            print(name, "overflow check", ov)
            await pg.pdf(path=HERE+name+".pdf", width="794px", height="1123px", print_background=True, margin={"top":"0","right":"0","bottom":"0","left":"0"}, page_ranges="1")
            await pg.close()
        for k, body in GS.items():
            pg = await b.new_page(viewport={"width":1200,"height":900}, device_scale_factor=2)
            path = HERE+f"google-{k}.html"
            open(path,"w").write(f'<!doctype html><html><head><meta charset="utf-8"><style>{GCSS}</style></head><body>{body}</body></html>')
            await pg.goto("file://"+path); await pg.wait_for_timeout(400)
            res = await pg.evaluate("""()=>{const w=document.querySelector('.w');const e=[];const m=document.querySelector('.mid');
              const r=[...document.querySelectorAll('.tag,h1,.mid,.f')].map(x=>[x.className||x.tagName,x.getBoundingClientRect()]);
              for(let i=0;i<r.length;i++)for(let j=i+1;j<r.length;j++){const a=r[i][1],b=r[j][1];if(a.left<b.right-1&&b.left<a.right-1&&a.top<b.bottom-1&&b.top<a.bottom-1)e.push(r[i][0]+' x '+r[j][0]);}
              for(const [n,x] of r){if(x.left<79||x.right>1121||x.bottom>900)e.push('margin '+n);}
              if(m.scrollHeight>m.clientHeight+1)e.push('mid clipped');
              const h=document.querySelector('h1');const l=(h.getBoundingClientRect().height)/parseFloat(getComputedStyle(h).lineHeight);if(l>2.05)e.push('h1 lines '+l.toFixed(1));
              return e}""")
            png = HERE+f"google-{k}.png"
            await pg.screenshot(path=png)
            im = Image.open(png).convert("RGB"); im.save(HERE+f"google-{k}.jpg", quality=90, optimize=True)
            print("google", k, "PASS" if not res else "FAIL "+"; ".join(res), im.size, os.path.getsize(HERE+f"google-{k}.jpg")//1024, "KB")
            await pg.close()
        await b.close()
asyncio.run(main())
