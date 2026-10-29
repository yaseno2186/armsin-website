from lib3 import *
RED = "#E06A4E"
def pills(items, cls="pill"):
    return ''.join(f'<div class="{cls}" style="{pos};transform:rotate({rot}deg)">{t}</div>' for t, pos, rot in items)
def cta(i, n, word, what, chip):
    vis = f'<div style="display:flex;flex-direction:column;align-items:center;gap:34px"><div class="keybtn">{word}</div><div class="chip"><span>PDF</span>{chip}</div></div>'
    return slide(i, n, f'Kommentieren Sie <em>{word}</em>', vis, kicker="GRATIS · PER DM", box=what, last=True)
def term(lines, w=700, title="server@ihre-seite.de"):
    body = ''.join(f'<div style="font:400 30px/1.5 MonoR;color:{c};white-space:nowrap">{t}</div>' for t,c in lines)
    return f'''<div class="brow" style="width:{w}px;border-color:rgba(224,106,78,.7);box-shadow:0 0 60px rgba(224,106,78,.28)"><div class="bar"><i style="background:{RED}"></i><i></i><i></i><span>{title}</span></div><div class="in" style="gap:4px;padding:26px 30px">{body}<div style="width:18px;height:34px;background:{G};margin-top:6px;box-shadow:0 0 14px {G}"></div></div></div>'''
def bubble(text, who="Sie → Ihr Hoster", w=820):
    return f'''<div style="width:{w}px;text-align:left"><div class="lab g" style="margin-left:8px">{who}</div>
<div style="background:#123222;border:2px solid rgba(57,217,122,.55);border-radius:30px 30px 30px 8px;padding:28px 34px;font:400 40px/1.32 Outfit;color:{LIGHT};box-shadow:0 0 40px rgba(57,217,122,.2)">{text}</div></div>'''
def bignum(n_, txt):
    return f'<div style="display:flex;flex-direction:column;align-items:center;gap:48px"><div style="font:400 170px/1 Pix;height:150px;overflow:visible;color:{G};text-shadow:0 0 50px rgba(57,217,122,.6)">{n_}</div>{txt}</div>'

# ---------------- A: PHP2Shell (Thu 29) ----------------
n = 6
PHP = [
 slide(1, n, f'Läuft Ihre Website mit <em style="padding:0 34px"><span class="logo-c" style="display:inline-block;width:1.95em;height:1.04em;vertical-align:-0.16em;margin-right:0.06em;--c:#8B8FD0;filter:drop-shadow(0 0 22px rgba(119,123,180,.9))">{logo_svg("php").replace('viewBox="0 0 24 24"','viewBox="0 5.6 24 12.8" preserveAspectRatio="xMidYMid meet"')}</span><span class="s">?</span>{circ(RED)}</em>',
   '<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">'
   + term([("$ status --sicherheit", "#8FB19B"), ("⚠ CVE-2026-109618", RED), ("⚠ CVE-2026-109619", RED), ("Name: PHP2Shell", LIGHT)], w=620)
   + pills([("seit 21.10.2026","left:10px;top:4%",-4),("BSI: Update noch heute","right:10px;top:16%",3),("WordPress & Shops","left:30px;bottom:4%",2)]) + '</div>',
   kicker="SICHERHEITSLÜCKE · PHP2SHELL", box="2 Fragen an Ihren Hoster. Am besten heute.", cover=True),
 slide(2, n, 'Was ist <em>PHP2Shell</em>?',
   f'''<div style="display:flex;flex-direction:column;gap:20px;width:880px"><svg width="120" height="130" viewBox="0 0 120 130" style="filter:drop-shadow(0 0 30px rgba(224,106,78,.55));align-self:center"><path d="M30 58 V38 C30 20 44 8 60 8 C74 8 86 18 89 32" fill="none" stroke="#E06A4E" stroke-width="9" stroke-linecap="round"/><rect x="16" y="56" width="88" height="66" rx="14" fill="#1A0F0C" stroke="#E06A4E" stroke-width="6"/><path d="M60 74 L54 90 L64 94 L58 110" fill="none" stroke="#E06A4E" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>
<div class="card"><div class="lab g">KURZ ERKLÄRT</div><div class="big" style="font-size:46px">Zwei kritische Lücken in PHP. Angreifer können damit <em>Code auf Ihrem Server</em> ausführen.</div></div>
<div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap"><div class="chip"><span>1</span>Website übernehmen</div><div class="chip"><span>2</span>Kundendaten lesen</div><div class="chip"><span>3</span>weiter angreifen</div></div><div class="txt" style="text-align:center;font-size:30px">Laut BSI betroffen: alle bekannten Versionen bis mindestens PHP 5.</div></div>''',
   kicker="ERST MAL KURZ ERKLÄRT", box="Die Updates gibt es schon. Sie müssen nur installiert sein.", boxcls="o"),
 slide(3, n, 'Bin ich <em>betroffen</em>?',
   '<div style="display:flex;flex-direction:column;gap:26px;width:880px">' + ''.join(
     f'<div class="card" style="display:flex;justify-content:space-between;align-items:center;gap:20px;padding:40px 38px"><div class="big" style="font-size:50px">{a}</div><div class="chip" style="flex:none;border-color:{c};color:{c}">{b}</div></div>'
     for a,b,c in [("WordPress-Seite","prüfen",RED),("Online-Shop mit PHP","prüfen",RED),("Website-Baukasten","kurz nachfragen",G)]) + '</div>',
   kicker="BETROFFEN? · 3 FÄLLE", box="Bei Baukästen kümmert sich meist der Anbieter. Fragen schadet nicht."),
 slide(4, n, '„Ist das <em>Update</em> installiert?“',
   bignum("01", bubble("Hallo, ist auf meinem Server das Notfall-Update gegen PHP2Shell installiert? Also z. B. PHP 8.4.27 oder 8.3.36?")),
   kicker="FRAGE 1 VON 2 · AN IHREN HOSTER", box="Kopieren, einfügen, abschicken."),
 slide(5, n, '„Läuft es auch <em>wirklich</em>?“',
   bignum("02", bubble("Welche PHP-Version läuft jetzt aktiv auf meiner Seite, und ist sie gepatcht?") + '<div class="txt" style="font-size:30px;color:#8FB19B">Wichtig: Nach dem Update muss der Dienst neu starten.</div>'),
   kicker="FRAGE 2 VON 2 · NACHPRÜFEN", box="„Es besteht unverzüglicher Handlungsbedarf!“ · BSI"),
 cta(6, n, "CHECK", "Ich schicke Ihnen meinen 5-Punkte Website-Check als PDF.", "5-Punkte Website-Check"),
]
POSTS = {"A-php2shell": PHP}

# ---------------- L: Tech-News KW 44 (Fri 30) ----------------
n = 7
def lg(name, w, h, pad=0, cls="logo-w"):
    return f'<div class="{cls}" style="width:{w}px;height:{h}px;padding:{pad}px">{logo_svg(name)}</div>'
def ms(w):
    return f'<div style="width:{w}px;height:{w}px">{logo_svg("microsoft")}</div>'
def ddi(s=150):
    return f'<div style="width:{s*1.6}px;height:{s}px;border-radius:24px;border:3px solid {G};display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 0 40px rgba(57,217,122,.35)"><div style="font:400 {int(s*.40)}px/1 Pix;color:{G};height:{int(s*.44)}px">0,73</div><div style="font:400 {max(23,int(s*.16))}px/1 Pix;color:{LIGHT};margin-top:{int(s*.06)}px">DE · DDI</div></div>'
def news(i, k, logos, h1, pills_, box):
    vis = f'<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center"><div class="tile" style="width:440px;height:300px;gap:30px">{logos}</div>' + pills(pills_) + '</div>'
    return slide(i, n, h1, vis, kicker=k, box=box, boxcls="o")
def flo(inner, x, y, r, c):
    return f'<div style="position:absolute;left:{x}px;top:{y}%;transform:rotate({r}deg);filter:drop-shadow(0 0 28px {c}88)">{inner}</div>'
CEO = HERE + "dl/ceo/"
def pnews(i, k, who, badge, credit, h1, pills_, box):
    photo = f'''<div style="display:flex;flex-direction:column;align-items:center;gap:12px"><div style="position:relative;width:330px;height:410px;border-radius:28px;border:3px solid {G};box-shadow:0 0 60px rgba(57,217,122,.4);background:url(file://{CEO}{who}.jpg) center 20%/cover;overflow:hidden"><div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 60%,rgba(4,12,7,.55))"></div><div style="position:absolute;right:14px;bottom:14px;width:92px;height:92px;border-radius:22px;background:rgba(4,12,7,.88);border:2px solid rgba(57,217,122,.6);display:flex;align-items:center;justify-content:center">{badge}</div></div><div style="font:400 22px/1.2 Inter;color:#8FB19B;max-width:880px;white-space:nowrap">{credit}</div></div>'''
    vis = f'<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">{photo}' + pills(pills_) + '</div>'
    return slide(i, n, h1, vis, kicker=k, box=box, boxcls="o")
L44 = [
 slide(1, n, f'Tech-News der <em><span class="s">Woche</span>{und()}</em>',
   '<div style="position:relative;width:920px;height:100%">'
   + flo(ms(150), 60, 6, -8, "#00A4EF")
   + flo(f'<div class="logo-c" style="width:290px;height:78px;--c:#FFFFFF">{logo_svg("openai")}</div>', 560, 8, 6, "#FFFFFF")
   + flo(f'<div class="logo-c" style="width:130px;height:160px;--c:#F5F5F7">{logo_svg("apple")}</div>', 390, 34, -4, "#F5F5F7")
   + flo(f'<div class="logo-c" style="width:150px;height:150px;--c:#D97757">{logo_svg("anthropic")}</div>', 700, 50, 6, "#D97757")
   + flo(ddi(150), 40, 58, 0, "#39D97A") + '</div>',
   kicker="KW 44 · 5 NEWS · 2 MINUTEN", box="Und was sie für kleine Betriebe bedeuten.", cover=True),
 pnews(2, "NEWS 1 VON 5 · MICROSOFT", "nadella", ms(56), "Satya Nadella, CEO · Foto: Brian Smale / Microsoft · CC BY-SA 4.0", 'Microsoft: <em>60.000</em> Abfindungs-Angebote',
   [("seit 26.10.2026","left:8px;top:3%",-3),("rund ein Viertel der Belegschaft","right:10px;top:52%",3),("Grund: hohe KI-Kosten","left:8px;bottom:30%",2)],
   "Für Sie: KI kostet auch Konzerne viel. Klein anfangen lohnt sich."),
 pnews(3, "NEWS 2 VON 5 · OPENAI", "altman", f'<div class="logo-c" style="width:120px;height:32px;--c:#FFFFFF">{logo_svg("openai")}</div>', "Sam Altman, CEO · Foto: Office of the PM of Japan · CC BY 4.0", 'GPT-6.1 Terra: <em>halber Preis</em>',
   [("seit 26.10.2026","left:8px;top:3%",-3),("1 $ / 5 $ pro Mio. Tokens","right:10px;top:52%",3),("kann den Computer bedienen","left:8px;bottom:30%",2)],
   "Für Sie: Gute KI wird billiger. Auch für kleine Projekte."),
 pnews(4, "NEWS 3 VON 5 · APPLE", "ternus", lg("apple",46,56), "John Ternus, CEO · Foto: Tessa Bury · CC BY 4.0", 'MacBook Pro jetzt mit <em>Touchscreen</em>',
   [("vorgestellt 28.10.2026","left:8px;top:3%",-3),("OLED, M5 Pro / Max","right:10px;top:52%",3),("ab 2.899 $ · ab 6.11.","left:8px;bottom:30%",2)],
   "Für Sie: Websites müssen jetzt auch am Laptop per Finger gut gehen."),
 pnews(5, "NEWS 4 VON 5 · ANTHROPIC", "amodei", lg("anthropic",56,56), "Dario Amodei, CEO · Foto: TechCrunch · CC BY 2.0", 'Anthropic will an die <em>Börse</em>',
   [("Börsenprospekt seit 26.10.","left:8px;top:3%",-3),("Kürzel: ANT (geplant)","right:10px;top:52%",3),("Start evtl. ab 9.11. (Bloomberg)","left:8px;bottom:30%",2)],
   "Für Sie: KI wird Großkonzern-Sache. Prüfen Sie, wem Sie Daten geben."),
 news(6, "NEWS 5 VON 5 · DEUTSCHLAND", ddi(170), 'Deutschland wird digital <em>abhängiger</em>',
   [("Studie Uni Bonn · 28.10.","left:14px;top:6%",-3),("Index 0,73 · 1 = ganz abhängig","right:10px;top:24%",3),("Platz 25 von 51 Ländern","left:10px;bottom:6%",2)],
   "Für Sie: Wo liegen Ihre Daten? Ein Blick lohnt sich."),
 slide(7, n, 'Welche News betrifft <em>Sie</em> am meisten?',
   '<div style="display:flex;gap:18px">' + ''.join(f'<div class="tile" style="width:160px;height:210px;flex-direction:column;gap:16px"><div style="font:400 76px/1 Outfit">{k}</div>{v}</div>' for k,v in [
     ("💼", ms(50)), ("🤖", f'<div class="logo-c" style="width:110px;height:30px;--c:#FFFFFF">{logo_svg("openai")}</div>'), ("💻", lg("apple",50,60)), ("📈", lg("anthropic",50,50)), ("🌍", f'<div style="font:400 30px Pix;color:{G}">DE</div>')]) + '</div>',
   kicker="IHRE MEINUNG", box="Antworten Sie mit dem Emoji in den Kommentaren.", last=True),
]
POSTS["L-tech-news-kw44"] = L44
