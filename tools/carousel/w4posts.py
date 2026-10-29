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

# ================= D: 3 Aufgaben / AUTOMAT (Sat 31), paper to-do =================
INK, INK2, PG, OR2 = "#1E1B16", "#4A453C", "#2E8F55", "#C1592B"
def todo(items, w=800):
    rows = ''.join(f'''<div style="display:flex;align-items:center;gap:26px;padding:22px 0;border-bottom:2px dashed rgba(30,27,22,.18)">
<div style="flex:none;width:58px;height:58px;border:4px solid {INK};border-radius:12px;position:relative;background:rgba(255,255,255,.5)">{'<svg viewBox="0 0 60 60" style="position:absolute;left:-6px;top:-14px;width:76px;height:76px;overflow:visible"><path d="M8 32 L24 48 L56 6" fill="none" stroke="'+PG+'" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>' if done else ''}</div>
<div style="position:relative;font:700 44px/1.15 Outfit;color:{INK if not done else INK2};text-align:left;white-space:nowrap">{t}{'<svg viewBox="0 0 300 20" preserveAspectRatio="none" style="position:absolute;left:-6px;top:46%;width:104%;height:18px;overflow:visible"><path d="M2 12 C80 4 160 16 298 6" fill="none" stroke="'+OR2+'" stroke-linecap="round" vector-effect="non-scaling-stroke" style="stroke-width:6px"/></svg>' if done else ''}</div></div>''' for t, done in items)
    return f'<div style="width:{w}px;background:#FBF8F1;border-radius:10px;padding:34px 48px 30px;box-shadow:0 18px 40px rgba(60,45,20,.18);transform:rotate(-1.5deg);text-align:left"><div style="font:400 24px/1 Pix;color:{PG};letter-spacing:2px;margin-bottom:6px">MEINE TO-DO-LISTE</div>{rows}</div>'
def pnote(text, x, y, r, bg="#F6D85C"):
    return f'<div style="position:absolute;{x};{y};transform:rotate({r}deg);background:{bg};padding:18px 26px;font:400 38px/1.1 Hand;color:{INK};box-shadow:0 10px 22px rgba(60,45,20,.22);white-space:nowrap">{text}</div>'
def pphone(msgs, w=470, label="Nachricht an Ihre Kundin"):
    b = ''.join(f'<div style="align-self:{"flex-end" if me else "flex-start"};max-width:88%;background:{"#2E8F55" if me else "#ECE6D9"};color:{"#F7F3EA" if me else INK};border-radius:24px {"24px 6px" if me else "24px 24px"} {"24px" if me else "6px"};padding:16px 22px;font:400 30px/1.3 Outfit;text-align:left">{t}</div>' for t, me in msgs)
    return f'''<div style="width:{w}px;border-radius:46px;border:4px solid {INK};background:#FBF8F1;padding:22px 20px 26px;box-shadow:0 18px 40px rgba(60,45,20,.22);display:flex;flex-direction:column;gap:14px">
<div style="align-self:center;width:110px;height:10px;border-radius:5px;background:{INK};opacity:.8"></div><div style="font:400 22px/1 Pix;color:{INK2};letter-spacing:1px;text-align:center">{label}</div>{b}</div>'''
def side(phone, items):
    lst = ''.join(f'<div style="display:flex;gap:14px;align-items:flex-start;font:400 34px/1.25 Outfit;color:{INK2};text-align:left"><span style="font:400 26px/1.4 Pix;color:{PG}">{k}</span><span>{t}</span></div>' for k, t in items)
    return f'<div style="display:flex;gap:44px;align-items:center;width:900px">{phone}<div style="display:flex;flex-direction:column;gap:26px;flex:1">{lst}</div></div>'
n = 6
AUT = [
 slide(1, n, 'Drei Aufgaben, die Sie <em>nicht mehr</em> selbst machen müssen',
   '<div style="position:relative;width:900px;height:100%;display:flex;align-items:center;justify-content:center">'
   + todo([("Termine erinnern", True), ("Um Bewertungen bitten", True), ("Gleiche Fragen beantworten", True)])
   + pnote("läuft automatisch!", "right:0px", "bottom:4%", 4) + '</div>',
   kicker="AUTOMATISIEREN · OHNE TECHNIK-STRESS", box="Das kann ein kleiner Betrieb heute abgeben.", boxcls="n", cover=True, variant="p"),
 slide(2, n, 'Aufgabe 1: <em>Termine erinnern</em>',
   side(pphone([("Hallo Frau Weber, kleine Erinnerung: morgen 10:00 Uhr Termin bei uns. Passt es nicht? Einfach hier absagen.", False), ("Danke, passt!", True)]),
        [("→", "Geht 24 h vorher raus, von allein"), ("→", "Absage per Klick statt Anruf"), ("→", "Freier Termin kann neu vergeben werden")]),
   kicker="AUFGABE 1 VON 3", box="Weniger leere Termine. Kein Hinterhertelefonieren.", boxcls="n", variant="p"),
 slide(3, n, 'Aufgabe 2: <em>um Bewertungen bitten</em>',
   side(pphone([("Danke für Ihren Besuch heute! Hat alles gepasst? Wir freuen uns über eine kurze Google-Bewertung: ★★★★★", False)]),
        [("→", "Kommt ein paar Stunden nach dem Termin"), ("→", "Nur einmal, freundlich, mit Link"), ("→", "Sie müssen nicht mehr daran denken")]),
   kicker="AUFGABE 2 VON 3", box="Mehr Bewertungen, ohne jedes Mal zu fragen.", boxcls="n", variant="p"),
 slide(4, n, 'Aufgabe 3: <em>immer gleiche Fragen</em>',
   '<div style="position:relative;width:900px;height:100%">'
   + pnote("Haben Sie heute offen?", "left:10px", "top:6%", -4)
   + pnote("Wo kann ich parken?", "right:20px", "top:19%", 3, "#BFE3C9")
   + pnote("Was kostet das?", "left:60px", "top:33%", 2, "#F2C4AE")
   + pnote("Nehmen Sie Karte?", "right:40px", "top:39%", -3)
   + f'<div style="position:absolute;left:50%;bottom:4%;transform:translateX(-50%);width:740px;background:#FBF8F1;border:4px solid {INK};border-radius:22px;padding:24px 32px;text-align:left;box-shadow:0 18px 40px rgba(60,45,20,.18)"><div style="font:400 24px/1 Pix;color:{PG};margin-bottom:10px">DIE LÖSUNG</div><div style="font:700 40px/1.2 Outfit;color:{INK}">Eine FAQ-Seite + eine automatische Antwort mit dem Link.</div></div></div>',
   kicker="AUFGABE 3 VON 3", box="Jede Frage nur noch einmal beantworten. Dann nie wieder.", boxcls="n", variant="p"),
 slide(5, n, 'Was Sie <em>dafür</em> brauchen',
   '<div style="display:flex;flex-direction:column;gap:22px;width:860px">' + ''.join(
     f'<div class="step" style="flex:none;flex-direction:row;align-items:center;gap:28px;padding:26px 32px"><div class="n" style="flex:none">{k}</div><div style="display:flex;flex-direction:column;gap:8px"><h3 style="font-size:46px">{h}</h3><p style="font-size:32px">{p}</p></div></div>'
     for k, h, p in [("01", "Online-Terminbuchung", "Viele haben Erinnerungen schon eingebaut."), ("02", "Ihr Google-Bewertungslink", "Gibt es kostenlos im Unternehmensprofil."), ("03", "Eine FAQ-Seite", "Zehn Fragen, ehrlich beantwortet.")]) + '</div>',
   kicker="KLEINER START", box="Oft reicht, was Sie schon haben. Es muss nur verbunden werden.", boxcls="n", variant="p"),
 cta(6, n, "AUTOMAT", "Ich schicke Ihnen meine Automation-Checkliste als PDF.", "Automation-Checkliste"),
]
POSTS["D-3-aufgaben"] = AUT

# ================= E: Baukasten (Sun 1), editorial =================
GOLD = "#E9B949"
def wire(w, h, gold=False, rot=0, op=1):
    c = GOLD if gold else "rgba(234,246,238,.28)"
    sh = f"box-shadow:0 0 60px rgba(233,185,73,.35);" if gold else ""
    inner = ('<div class="ln" style="width:70%;height:22px;background:rgba(233,185,73,.55)"></div><div style="display:flex;gap:12px"><div style="flex:2;height:110px;border-radius:12px;background:rgba(233,185,73,.18)"></div><div style="flex:1;height:110px;border-radius:12px;border:2px dashed rgba(233,185,73,.6)"></div></div><div class="ln" style="width:90%"></div><div class="ln" style="width:55%"></div>'
             if gold else '<div style="height:90px;border-radius:10px;background:rgba(234,246,238,.12)"></div><div class="ln" style="width:60%"></div><div style="display:flex;gap:10px"><div style="flex:1;height:60px;border-radius:8px;background:rgba(234,246,238,.1)"></div><div style="flex:1;height:60px;border-radius:8px;background:rgba(234,246,238,.1)"></div><div style="flex:1;height:60px;border-radius:8px;background:rgba(234,246,238,.1)"></div></div>')
    return f'<div class="brow" style="width:{w}px;height:{h}px;border-color:{c};{sh}transform:rotate({rot}deg);opacity:{op}"><div class="bar"><i></i><i></i><i></i></div><div class="in">{inner}</div></div>'
def quote(t, who=""):
    return f'<div style="width:860px;text-align:left"><svg width="140" height="110" viewBox="0 0 140 110"><text x="0" y="150" style="font:italic 400 220px Serif" fill="{GOLD}">“</text></svg><div style="font:400 64px/1.18 Serif;font-style:italic;color:#F3EBDD">{t}</div>{('<div style="margin-top:26px;font:400 26px/1 Pix;color:#8FB19B">'+who+'</div>') if who else ""}</div>'
def vs(a_t, a, b_t, b):
    col = lambda t, items, c, bd: f'<div class="card" style="flex:1;border-color:{bd};display:flex;flex-direction:column;gap:18px"><div class="lab" style="color:{c}">{t}</div>' + ''.join(f'<div class="txt" style="font-size:34px;color:#DCE7DF">{x}</div>' for x in items) + '</div>'
    return f'<div style="display:flex;gap:24px;width:900px">{col(a_t, a, "#8FB19B", "rgba(234,246,238,.2)")}{col(b_t, b, GOLD, GOLD)}</div>'
n = 6
BAU = [
 slide(1, n, f'Warum ich keine <em>Baukasten</em>-Websites verkaufe',
   '<div style="position:relative;width:900px;height:100%">'
   + f'<div style="position:absolute;left:0;top:8%">{wire(260,210,rot=-6,op=.55)}</div>'
   + f'<div style="position:absolute;left:140px;top:26%">{wire(260,210,rot=-2,op=.7)}</div>'
   + f'<div style="position:absolute;left:280px;top:46%">{wire(260,210,rot=2,op=.85)}</div>'
   + f'<div style="position:absolute;right:10px;top:8%">{wire(330,300,gold=True,rot=4)}</div>'
   + f'<div style="position:absolute;right:30px;bottom:2%;font:400 44px/1 Hand;color:{GOLD};transform:rotate(-4deg)">Ihre Seite</div></div>',
   kicker="EHRLICH GESAGT · MEINE SICHT", box="Kein Angriff. Nur der Grund, warum ich es anders mache.", boxcls="n", cover=True, variant="e"),
 slide(2, n, 'Erst mal: Baukästen sind <em>nicht schlecht</em>',
   quote("Wer gern selbst bastelt und Zeit hat, ist mit einem Baukasten oft gut bedient.", "DAS SAGE ICH AUCH KUNDEN"),
   kicker="FAIR BLEIBEN", box="Für einen schnellen Start sind sie eine gute Wahl.", boxcls="o", variant="e"),
 slide(3, n, 'Aber: Sie <em>mieten</em> nur',
   vs("BAUKASTEN", ["Seite läuft nur beim Anbieter", "Umzug ist oft schwer", "Monatlich zahlen, solange sie läuft"],
      "EIGENE SEITE", ["Code und Domain gehören Ihnen", "Umzug zu jedem Hoster möglich", "Sie entscheiden, wer daran arbeitet"]),
   kicker="GRUND 1 · BESITZ", box="Ihre Website ist ein Werkzeug. Es sollte Ihnen gehören.", boxcls="o", variant="e"),
 slide(4, n, 'Vorlage ist nicht gleich <em>passend</em>',
   '<div style="display:flex;align-items:center;gap:30px;width:900px;justify-content:center">'
   + f'<div style="display:flex;flex-direction:column;align-items:center;gap:16px">{wire(330,280,op=.7)}<div class="lab">VORLAGE „RESTAURANT“</div></div>'
   + arrow(GOLD, 110)
   + f'<div style="display:flex;flex-direction:column;align-items:center;gap:16px">{wire(330,280,gold=True)}<div class="lab" style="color:{GOLD}">IHR BETRIEB</div></div></div>',
   kicker="GRUND 2 · IHRE KUNDEN", box="Ihre Kunden haben eigene Fragen. Die Seite sollte genau die beantworten.", boxcls="o", variant="e"),
 slide(5, n, 'Was ich <em>stattdessen</em> mache',
   '<div style="display:flex;flex-direction:column;gap:22px;width:880px">' + ''.join(
     f'<div class="card" style="display:flex;align-items:center;gap:30px;border-color:rgba(233,185,73,.5)"><div style="flex:none;font:400 40px/1 Pix;color:{GOLD}">{k}</div><div><div class="big" style="font-size:44px">{h}</div><div class="txt" style="font-size:30px">{p}</div></div></div>'
     for k, h, p in [("01", "Zuhören", "Was fragen Ihre Kunden am Telefon?"), ("02", "Passend bauen", "Schlank, schnell, ohne Ballast."), ("03", "Ihnen übergeben", "Domain und Zugänge laufen auf Sie.")]) + '</div>',
   kicker="MEIN WEG", box="Etwas langsamer am Anfang. Dafür passt es länger.", boxcls="o", variant="e"),
 slide(6, n, 'Was ist Ihnen <em>wichtiger</em>?',
   '<div style="display:flex;gap:40px;align-items:center">'
   + f'<div class="tile" style="width:360px;height:320px;flex-direction:column;gap:20px"><div style="font:400 100px/1 Outfit">⚡</div><div class="big">schnell</div></div>'
   + f'<div style="font:400 60px/1 Serif;font-style:italic;color:#8FB19B">oder</div>'
   + f'<div class="tile" style="width:360px;height:320px;flex-direction:column;gap:20px;border-color:{GOLD};box-shadow:0 0 50px rgba(233,185,73,.3)"><div style="font:400 100px/1 Outfit">🎯</div><div class="big">passend</div></div></div>',
   kicker="IHRE MEINUNG", box="Schreiben Sie es in die Kommentare. Beides ist okay.", boxcls="o", last=True, variant="e"),
]
POSTS["E-baukasten"] = BAU

# ================= H: Armsin Hub (Mon 2), dev build-in-public =================
def dash(w=860):
    days = ["MO","DI","MI","DO","FR","SA","SO"]
    cells = ''
    marks = {0:("IG","17:30"),3:("IG","17:30"),4:("IG","17:30"),5:("IG","10:00"),6:("IG","18:00")}
    for i, d in enumerate(days):
        m = marks.get(i)
        chip = f'<div style="margin-top:10px;background:rgba(57,217,122,.18);border:2px solid {G};border-radius:10px;padding:6px 2px;font:400 22px/1.15 Pix;color:{G};text-align:center">{m[0]}<br>{m[1]}</div>' if m else ''
        cells += f'<div style="flex:1;border:2px solid rgba(234,246,238,.14);border-radius:12px;padding:10px 6px;min-height:150px;background:rgba(0,0,0,.25)"><div style="font:400 22px/1 Pix;color:#8FB19B;text-align:center">{d}</div>{chip}</div>'
    side_ = ''.join(f'<div style="font:400 22px/1 Outfit;color:{G if k==0 else "#8FB19B"};padding:10px 0">{t}</div>' for k, t in enumerate(["Kalender","Posts","Inbox","Statistik"]))
    return f'''<div class="brow" style="width:{w}px"><div class="bar"><i></i><i></i><i></i><span>hub · armsin</span></div>
<div style="display:flex;gap:20px;padding:22px"><div style="flex:none;width:118px;border-right:2px solid rgba(234,246,238,.1);text-align:left">{side_}</div>
<div style="flex:1;display:flex;flex-direction:column;gap:14px"><div style="font:700 32px/1 Outfit;text-align:left">Diese Woche</div><div style="display:flex;gap:8px">{cells}</div>
<div style="display:flex;gap:10px"><div class="btn" style="font-size:24px;padding:14px 20px">+ Neuer Post</div><div class="btn o" style="font-size:24px;padding:14px 20px">Karussell hochladen</div></div></div></div></div>'''
def stk(items):
    return '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;width:880px">' + ''.join(
        f'<div class="card" style="padding:26px 30px"><div class="lab g">{a}</div><div class="big" style="font-size:40px">{b}</div><div class="txt" style="font-size:28px">{c}</div></div>' for a, b, c in items) + '</div>'
n = 6
HUB = [
 slide(1, n, 'Mein eigener Social-Media-Planer für <em>0 €</em>',
   '<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">' + dash(900)
   + pills([("selbst gebaut","left:20px;top:6%",-4),("Gratis-Tarif","right:20px;bottom:7%",3)]) + '</div>',
   kicker="BUILD IN PUBLIC · ARMSIN HUB", box="Dieser Post wurde damit geplant.", cover=True),
 slide(2, n, 'Warum <em>selbst</em> bauen?',
   '<div style="display:flex;flex-direction:column;gap:24px;width:860px">'
   + term([("$ posts --diesen-monat", "#8FB19B"), ("⚠ Gratis-Limit erreicht", RED), ("→ nächster Post erst im November", LIGHT)], w=860, title="planer · gratis-version")
   + '<div class="card"><div class="lab g">MEINE LÖSUNG</div><div class="big" style="font-size:44px">Ein eigener Planer. Ohne Monatslimit, ohne Abo.</div></div></div>',
   kicker="DAS PROBLEM", box="Ich poste mehr, als ein Gratis-Tarif erlaubt.", boxcls="o"),
 slide(3, n, 'Der Stack: <em>alles gratis</em>',
   stk([("WORKERS", "Die App", "Seite, API, Webhooks"), ("CRON", "Jede Minute", "Postet, was fällig ist"),
        ("D1", "Datenbank", "Posts, Zeiten, Status"), ("R2", "Bilder", "Karussell-JPEGs")]),
   kicker="CLOUDFLARE · FREE PLAN", box="Kosten bisher: 0 €. Nur meine Zeit.", boxcls="o"),
 slide(4, n, 'Was er <em>schon</em> kann',
   '<div style="display:flex;flex-direction:column;gap:18px;width:860px">' + ''.join(
     f'<div class="card" style="display:flex;align-items:center;gap:24px;padding:24px 30px"><div style="flex:none;width:52px;height:52px;border-radius:14px;background:{G if ok else "transparent"};border:3px solid {G};display:flex;align-items:center;justify-content:center;font:700 34px/1 Outfit;color:#04150A">{"✓" if ok else ""}</div><div class="big" style="font-size:42px;color:{LIGHT if ok else "#8FB19B"}">{t}</div></div>'
     for t, ok in [("Instagram-Karussells planen", True), ("Auf die Minute posten", True), ("Kommentare + Keyword-Antworten", False), ("LinkedIn und Google", False)]) + '</div>',
   kicker="STAND HEUTE", box="Zwei Haken fehlen noch. Kommt Schritt für Schritt.", boxcls="o"),
 slide(5, n, 'Was ich <em>gelernt</em> habe',
   '<div style="display:flex;flex-direction:column;gap:22px;width:860px">' + ''.join(
     f'<div class="card"><div class="lab g">{k}</div><div class="big" style="font-size:40px">{t}</div></div>'
     for k, t in [("01 · APIS", "Offizielle Schnittstellen statt Tricks. Dann bleibt der Account sicher."), ("02 · KLEIN", "Erst eine Plattform fertig machen, dann die nächste."), ("03 · GEHEIM", "Schlüssel gehören nie in den Code.")]) + '</div>',
   kicker="3 LEHREN"),
 cta(6, n, "HUB", "Ich schicke Ihnen meine Cloudflare-Gratis-Stack Checkliste als PDF.", "Cloudflare-Free-Stack Checkliste"),
]
POSTS["H-hub"] = HUB
