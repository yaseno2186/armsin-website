from w4posts import *   # helpers: pills, cta, term, bubble, bignum, RED, GOLD ...
POSTS = {}
# ================= A: 6 neue ChatGPT-Funktionen =================
IC = {
 "ui":'<svg viewBox="0 0 48 48" fill="none" stroke="#39D97A" stroke-width="3.2" stroke-linejoin="round"><rect x="6" y="8" width="36" height="32" rx="5"/><path d="M12 32v-8M19 32V18M26 32v-5M33 32V14"/></svg>',
 "mail":'<svg viewBox="0 0 48 48" fill="none" stroke="#39D97A" stroke-width="3.2" stroke-linejoin="round"><rect x="5" y="10" width="26" height="20" rx="4"/><path d="M5 13l13 9 13-9"/><rect x="24" y="24" width="19" height="18" rx="4" fill="#0A140E"/><path d="M24 30h19M29 21v6M38 21v6"/></svg>',
 "word":'<svg viewBox="0 0 48 48" fill="none" stroke="#39D97A" stroke-width="3.2" stroke-linejoin="round"><path d="M12 5h17l9 9v29H12z"/><path d="M29 5v9h9M18 24l3 12 3-8 3 8 3-12"/></svg>',
 "audio":'<svg viewBox="0 0 48 48" fill="none" stroke="#39D97A" stroke-width="3.2" stroke-linecap="round"><path d="M6 24v0M12 18v12M18 12v24M24 20v8M30 9v30M36 16v16M42 22v4"/></svg>',
 "scan":'<svg viewBox="0 0 48 48" fill="none" stroke="#39D97A" stroke-width="3.2" stroke-linejoin="round" stroke-linecap="round"><path d="M6 14V8h6M36 8h6v6M42 34v6h-6M12 40H6v-6"/><rect x="15" y="13" width="18" height="22" rx="2"/><path d="M19 20h10M19 25h10M19 30h6"/></svg>',
 "lock":'<svg viewBox="0 0 48 48" fill="none" stroke="#39D97A" stroke-width="3.2" stroke-linejoin="round"><rect x="9" y="21" width="30" height="21" rx="5"/><path d="M15 21v-6a9 9 0 0 1 18 0v6"/><circle cx="24" cy="31" r="3" fill="#39D97A"/></svg>'}
def feat(icon, name, date, plan, what, use):
    return f'''<div style="display:flex;flex-direction:column;gap:24px;width:880px">
<div style="display:flex;align-items:center;gap:30px"><div class="tile" style="flex:none;width:170px;height:170px"><div style="width:100px;height:100px">{IC[icon]}</div></div>
<div style="text-align:left;display:flex;flex-direction:column;gap:14px"><div class="big" style="font-size:52px">{name}</div><div style="display:flex;gap:12px"><div class="chip" style="padding:10px 18px;font-size:24px"><span>NEU</span>{date}</div><div class="chip" style="padding:10px 18px;font-size:24px">{plan}</div></div></div></div>
<div class="card"><div class="lab g">WAS ES KANN</div><div class="txt" style="font-size:34px;color:#DCE7DF">{what}</div></div>
<div class="card" style="border-color:{GOLD}"><div class="lab" style="color:{GOLD}">FÜR IHREN BETRIEB</div><div class="txt" style="font-size:34px;color:#DCE7DF">{use}</div></div></div>'''
n = 8
F = [("ui","Interaktive Antworten","07.10.","alle Tarife","Antworten mit Diagrammen, Rechnern und Buttons statt nur Text.","„Bau mir einen Preisrechner für meine Angebote.“"),
     ("mail","Mail + Kalender","27.10.","alle Tarife","Plugins für iCloud Mail und Kalender: Mails finden, Termine prüfen und ändern.","„Was steht diese Woche an? Welche Kunden warten auf Antwort?“"),
     ("word","ChatGPT in Word","23.09.","auch gratis","Eine Seitenleiste direkt in Microsoft Word, zum Schreiben und Überarbeiten.","Angebote und Briefe im gewohnten Word-Dokument verbessern."),
     ("audio","Audio hochladen","06.10.","Bezahl-Tarife","Aufnahmen abtippen, zusammenfassen und Fragen dazu stellen.","Sprachnotiz vom Kundentermin hochladen, To-dos bekommen."),
     ("scan","Mehrseitig scannen","01.10.","iPhone","Mehrere Seiten mit der Kamera zu einem PDF scannen.","Lieferschein oder Vertrag scannen und direkt erklären lassen."),
     ("lock","Gesperrte Chats","20.10.","schrittweise","Chats mit PIN oder Face ID verstecken.","Sensible Chats vor neugierigen Blicken schützen. Ersetzt aber keinen Datenschutz.")]
HL = ['Antworten zum <em>Anklicken</em>', 'ChatGPT liest Ihren <em>Kalender</em>', 'KI direkt in <em>Word</em>',
      'Sprachnotiz rein, <em>To-dos</em> raus', 'Papier zu <em>PDF</em> in Sekunden', 'Chats mit <em>PIN</em> sperren']
GPT = [
 slide(1, n, '6 neue <em>ChatGPT</em>-Funktionen, die kaum jemand kennt',
   '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;width:780px">' + ''.join(
     f'<div class="tile" style="height:200px;flex-direction:column;gap:14px"><div style="width:84px;height:84px">{IC[k]}</div><div style="font:400 22px/1 Pix;color:#8FB19B">NEU</div></div>' for k in IC) + '</div>',
   kicker="KI-UPDATE · HERBST 2026", box="Stand Oktober 2026. Mit einer Idee je Funktion für Ihren Betrieb.", cover=True)]
for i, f in enumerate(F, 2):
    GPT.append(slide(i, n, HL[i-2], feat(*f), kicker=f"FUNKTION {i-1} VON 6"))
GPT.append(slide(8, n, 'Welche probieren Sie <em>zuerst</em>?',
   '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:18px;width:820px">' + ''.join(
     f'<div class="tile" style="height:190px;flex-direction:column;gap:12px"><div style="font:400 40px/1 Pix;color:{G}">{j}</div><div class="big" style="font-size:30px">{f[1]}</div></div>' for j, f in enumerate(F, 1)) + '</div>',
   kicker="IHRE MEINUNG", box="Antworten Sie mit der Zahl. Verfügbarkeit kann je nach Land und Tarif abweichen.", last=True))
POSTS["A-chatgpt-neu"] = GPT

# ================= E: KI-Blase / Character.AI (Daten) =================
def leak():
    items = [("„Unser Umsatz war im Oktober …“", 0, 0), ("„Kundin Müller hat gesagt …“", 300, 17), ("„Mein Passwort-Hinweis ist …“", 30, 34), ("„Ich habe Angst, dass …“", 280, 51)]
    s = ''.join(f'<div style="position:absolute;left:{x}px;top:{y}%;background:rgba(234,246,238,.06);border:2px solid rgba(234,246,238,.2);border-radius:22px 22px 22px 6px;padding:16px 24px;font:400 32px/1.2 Outfit;color:#C9DBCF;white-space:nowrap">{t}</div>' for t, x, y in items)
    tag = f'<div style="position:absolute;right:30px;bottom:6%;transform:rotate(-8deg);border:5px solid {RED};color:{RED};font:400 46px/1 Pix;padding:18px 26px;border-radius:12px;box-shadow:0 0 40px rgba(224,106,78,.4);background:rgba(26,15,12,.85)">ZU VERKAUFEN</div>'
    return f'<div style="position:relative;width:900px;height:100%">{s}{tag}</div>'
def tl(items):
    return '<div style="display:flex;flex-direction:column;gap:0;width:840px;text-align:left">' + ''.join(
      f'<div style="display:flex;gap:28px"><div style="display:flex;flex-direction:column;align-items:center;flex:none"><div style="width:30px;height:30px;border-radius:50%;background:{c};box-shadow:0 0 18px {c}"></div>{"" if i==len(items)-1 else f"<div style=width:4px;flex:1;min-height:40px;background:rgba(234,246,238,.2)></div>"}</div><div style="margin-top:-6px;padding-bottom:40px"><div style="font:400 28px/1 Pix;color:{c}">{d}</div><div class="big" style="font-size:40px;margin-top:10px">{t}</div></div></div>'
      for i, (d, t, c) in enumerate(items)) + '</div>'
n = 6
BUB = [
 slide(1, n, 'Was Sie der KI erzählen, kann <em style="color:#E06A4E;text-shadow:0 0 30px rgba(224,106,78,.55)">verkauft</em> werden', leak(),
   kicker="KI · DATENSCHUTZ · BBC FUTURE", box="Ein echter Fall. Gerade jetzt in den USA.", cover=True),
 slide(2, n, 'Was ist <em>passiert</em>?',
   tl([("12.10.2026", "Character.AI meldet Insolvenz an.", RED), ("29.10.2026", "39 US-Bundesstaaten fordern Schutz der Nutzerdaten.", GOLD), ("23.11.2026", "Geplante Auktion der Firma.", LIGHT)]),
   kicker="DER FALL · CHARACTER.AI", box="Ein KI-Chat-Dienst mit Millionen Nutzern. Auch vielen Jugendlichen.", boxcls="o"),
 slide(3, n, 'Ihre Chats sind <em>Firmenvermögen</em>',
   '<div style="display:flex;flex-direction:column;gap:22px;width:860px">'
   + '<div class="card"><div class="lab" style="color:#E06A4E">DIE FIRMA SAGT</div><div class="big" style="font-size:42px">Die Datenschutzerklärung erlaubt die Weitergabe der Nutzerdaten.</div></div>'
   + '<div class="card"><div class="lab g">SCHON MAL PASSIERT</div><div class="big" style="font-size:42px">2025 bei 23andMe: Gen-Daten von Kunden wurden mitverkauft.</div></div></div>',
   kicker="DAS EIGENTLICHE PROBLEM", box="Geht eine Firma pleite, wird verkauft, was Wert hat. Auch Daten.", boxcls="o"),
 slide(4, n, 'Und die <em>KI-Blase</em>?',
   f'<div style="display:flex;flex-direction:column;align-items:center;gap:40px"><div style="font:400 120px/1 Pix;height:120px;color:{RED};text-shadow:0 0 50px rgba(224,106,78,.6);white-space:nowrap">8–9 Mio $</div><div class="txt" style="font-size:36px;max-width:820px">So viel hat Character.AI laut Berichten pro Monat verbraucht. Mehr, als hereinkam.</div></div>',
   kicker="WARUM DAS SIE BETRIFFT", box="Viele KI-Firmen verdienen noch kein Geld. Nicht alle werden überleben.", boxcls="o"),
 slide(5, n, '4 Regeln für Ihren <em>Betrieb</em>',
   '<div style="display:flex;flex-direction:column;gap:16px;width:860px">' + ''.join(
     f'<div class="card" style="display:flex;align-items:center;gap:26px;padding:22px 30px"><div style="flex:none;font:400 34px/1 Pix;color:{G}">{k}</div><div class="big" style="font-size:38px">{t}</div></div>'
     for k, t in [("01", "Keine Kundendaten in Gratis-Chatbots"), ("02", "Business-Tarif ohne Training auf Ihren Daten"), ("03", "Chatverläufe regelmäßig löschen"), ("04", "Vorher lesen: Wer steckt hinter dem Tool?")]) + '</div>',
   kicker="WAS SIE TUN KÖNNEN", box="Faustregel: Was nicht auf eine Postkarte passt, gehört nicht in den Chat.", boxcls="o"),
 slide(6, n, 'Was haben <em>Sie</em> der KI schon erzählt?',
   '<div style="display:flex;gap:30px">' + ''.join(f'<div class="tile" style="width:250px;height:260px;flex-direction:column;gap:16px"><div style="font:400 90px/1 Outfit">{e}</div><div class="big" style="font-size:34px">{t}</div></div>' for e, t in [("🙈", "zu viel"), ("🤔", "weiß nicht"), ("😌", "nichts")]) + '</div>',
   kicker="IHRE MEINUNG", box="Antworten Sie mit dem Emoji. Ehrlich.", last=True),
]
POSTS["E-ki-daten"] = BUB

# ================= B: KI-Studie DIHK (paper report) =================
def pbig(num, txt, c=PG):
    return f'<div style="display:flex;flex-direction:column;align-items:center;gap:60px"><div style="font:700 230px/1 Outfit;letter-spacing:-6px;color:{c}">{num}</div><div style="font:400 40px/1.3 Outfit;color:{INK2};max-width:800px;text-align:center">{txt}</div></div>'
def pbars(rows, w=860):
    r = ''.join(f'''<div style="display:flex;flex-direction:column;gap:10px"><div style="display:flex;justify-content:space-between;font:700 36px/1.1 Outfit;color:{INK}"><span>{t}</span><span style="color:{c}">{v} %</span></div>
<div style="height:34px;border-radius:17px;background:rgba(30,27,22,.1);overflow:hidden"><div style="width:{v}%;height:100%;border-radius:17px;background:{c}"></div></div></div>''' for t, v, c in rows)
    return f'<div style="display:flex;flex-direction:column;gap:30px;width:{w}px;background:#FBF8F1;border-radius:14px;padding:38px 44px;box-shadow:0 18px 40px rgba(60,45,20,.16);text-align:left">{r}</div>'
def pcard(items):
    return '<div style="display:flex;flex-direction:column;gap:20px;width:860px">' + ''.join(
      f'<div class="step" style="flex:none;padding:24px 30px"><div class="n">{k}</div><p style="font-size:36px;color:{INK}">{t}</p></div>' for k, t in items) + '</div>'
n = 7
KIS = [
 slide(1, n, 'Lohnt sich KI für Ihren <em>Betrieb</em>?',
   '<div style="position:relative;width:900px;height:100%;display:flex;align-items:center;justify-content:center">'
   + f'<div style="background:#FBF8F1;border-radius:14px;padding:40px 56px;box-shadow:0 18px 40px rgba(60,45,20,.18);transform:rotate(-1.5deg);text-align:center"><div style="font:400 24px/1 Pix;color:{PG};letter-spacing:2px">DIHK · UMFRAGE 2026</div><div style="font:700 190px/1 Outfit;letter-spacing:-6px;color:{PG};margin:44px 0 40px">41 %</div><div style="font:400 36px/1.25 Outfit;color:{INK2};max-width:560px">der Firmen mit KI sehen einen hohen Nutzen</div></div>'
   + pnote("echte Zahlen!", "right:10px", "bottom:6%", 4) + '</div>',
   kicker="STUDIE · 5.000 UNTERNEHMEN", box="Was die Zahlen sagen. Und was das für kleine Betriebe heißt.", boxcls="n", cover=True, variant="q"),
 slide(2, n, 'Die <em>Studie</em> in 20 Sekunden',
   pcard([("WER", "Deutsche Industrie- und Handelskammer (DIHK)"), ("WIE VIELE", "Rund 5.000 Unternehmen aus fast allen Branchen"), ("WANN", "Befragt Ende 2025, veröffentlicht 2026")]),
   kicker="DIGITALISIERUNGSUMFRAGE 2026", box="Keine Umfrage unter Tech-Firmen. Sondern quer durch die Wirtschaft.", boxcls="n", variant="q"),
 slide(3, n, 'Wer KI nutzt, <em>merkt</em> es',
   pbig("41 %", "der Betriebe, die KI schon im Alltag nutzen, bewerten den Effekt auf ihre Produktivität als hoch."),
   kicker="ZAHL 1", box="Nicht „etwas“. Sondern hoch.", boxcls="n", variant="q"),
 slide(4, n, 'Wofür KI <em>genutzt</em> wird',
   pbars([("Texte, Bilder, Code erstellen", 78, PG), ("Kundenkontakt und Service", 43, OR2), ("Qualität prüfen", 38, INK2)]),
   kicker="ZAHL 2 · EINSATZFELDER", box="Platz 1 ist das, was jeder sofort ausprobieren kann: Texte.", boxcls="n", variant="q"),
 slide(5, n, 'Gastro und Handel <em>vorne</em>',
   pbars([("Gastgewerbe", 62, PG), ("Handel", 53, OR2)]) + '',
   kicker="ZAHL 3 · KI IM KUNDENKONTAKT", box="Gerade lokale Betriebe nutzen KI, um schneller auf Kunden zu antworten.", boxcls="n", variant="q"),
 slide(6, n, 'Aber: <em>ein Drittel</em> wartet',
   pcard([("ZAHL 4", "Rund ein Drittel der Firmen nutzt keine KI und plant es auch nicht."), ("GRÖSSTE BREMSE", "Rechtliche Unsicherheit und Datenschutz.")]),
   kicker="DIE ANDERE SEITE", box="Verständlich. Ein kleiner, sicherer Start ist trotzdem möglich.", boxcls="n", variant="q"),
 slide(7, n, 'Und <em>Sie</em>?',
   '<div style="display:flex;gap:28px">' + ''.join(f'<div style="width:250px;height:270px;border-radius:22px;background:#FBF8F1;box-shadow:0 14px 30px rgba(60,45,20,.16);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px"><div style="font:400 90px/1 Outfit">{e}</div><div style="font:700 34px/1.1 Outfit;color:{INK};text-align:center">{t}</div></div>' for e, t in [("✅", "nutze ich"), ("🕐", "bald"), ("❌", "nein")]) + '</div>',
   kicker="IHRE MEINUNG", box="Antworten Sie mit dem Emoji. Quelle: DIHK-Digitalisierungsumfrage 2026.", boxcls="n", last=True, variant="q"),
]
POSTS["B-ki-studie"] = KIS

# ================= D: Vorher / Nachher Kontaktseite =================
def mark(k, x, y, c=RED):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:52px;height:52px;border-radius:50%;background:{c};color:#0A0503;font:700 30px/52px Outfit;text-align:center;box-shadow:0 0 20px {c}">{k}</div>'
def ph_before(marks=True):
    inner = f'''<div style="font:700 30px/1.1 Outfit;color:#DCE7DF">Kontakt</div>
<div style="font:400 22px/1.3 Outfit;color:#8FB19B">Sie haben Fragen zu Bestellungen, Torten oder Catering? Nutzen Sie bitte unser Formular.</div>
<div style="height:28px;border-radius:4px;background:repeating-linear-gradient(90deg,rgba(234,246,238,.35) 0 6px,transparent 6px 9px);width:70%;opacity:.6"></div>
''' + ''.join('<div style="height:24px;flex:none;border:1px solid rgba(234,246,238,.25);border-radius:4px"></div>' for _ in range(6)) + '''
<div style="align-self:flex-start;background:rgba(234,246,238,.15);color:#8FB19B;font:400 22px/1 Outfit;padding:8px 14px;border-radius:4px">Absenden</div>
<div style="font:400 22px/1.2 Outfit;color:#5E7466">Hauptstr. 12, Freiberg</div>'''
    m = (mark(1, 340, 150) + mark(2, -26, 230) + mark(3, 340, 20) + mark(4, -26, 470)) if marks else ''
    return f'<div style="position:relative;width:380px;height:540px"><div class="phone bad" style="width:380px;height:540px;opacity:.85;gap:10px;padding:28px 24px">{inner}</div>{m}</div>'
def ph_after():
    fld = lambda t: f'<div style="height:44px;flex:none;border:2px solid rgba(234,246,238,.25);border-radius:10px;font:400 22px/40px Outfit;color:#8FB19B;padding-left:12px">{t}</div>'
    return f'''<div class="phone good" style="width:380px;height:540px;gap:14px;padding:28px 24px">
<div style="font:700 32px/1.1 Outfit;color:{LIGHT}">Bäckerei Beispiel</div>
<div style="display:flex;align-items:center;gap:10px;font:700 22px/1 Outfit;color:{G}"><div style="width:14px;height:14px;border-radius:50%;background:{G};box-shadow:0 0 10px {G}"></div>Heute offen bis 18:00</div>
<div class="btn" style="font-size:26px;padding:16px">📞 Jetzt anrufen</div>
<div class="btn o" style="font-size:24px;padding:14px">📍 Route planen</div>
<div style="border-top:2px solid rgba(234,246,238,.12);padding-top:12px;display:flex;flex-direction:column;gap:10px">
<div style="font:400 22px/1 Pix;color:#8FB19B">ODER SCHREIBEN</div>{fld("Name")}{fld("Telefon oder E-Mail")}{fld("Nachricht")}</div></div>'''
def sc(html, k=.8, w=380, h=540):
    return f'<div style="width:{int(w*k)}px;height:{int(h*k)}px;flex:none"><div style="transform:scale({k});transform-origin:top left;width:{w}px">{html}</div></div>'
def fix(items):
    return '<div style="display:flex;flex-direction:column;gap:24px;width:880px">' + ''.join(
      f'''<div class="card" style="padding:36px 36px"><div style="display:flex;align-items:center;gap:20px"><div style="flex:none;width:62px;height:62px;border-radius:50%;background:{RED};color:#0A0503;font:700 36px/62px Outfit;text-align:center">{k}</div><div class="big" style="font-size:48px">{t}</div></div>
<div style="display:flex;gap:18px;margin-top:22px;align-items:flex-start"><div style="font:400 30px/1.35 Pix;color:{G};flex:none">FIX</div><div class="txt" style="font-size:38px;color:#DCE7DF">{f}</div></div></div>''' for k, t, f in items) + '</div>'
n = 7
VN = [
 slide(1, n, 'Vorher / <em>Nachher</em>: eine Kontaktseite',
   '<div style="display:flex;align-items:center;gap:30px">' + f'<div style="display:flex;flex-direction:column;align-items:center;gap:14px">{sc(ph_before(False))}<div class="cap" style="color:{RED}">VORHER</div></div>' + arrow(G, 100)
   + f'<div style="display:flex;flex-direction:column;align-items:center;gap:14px">{sc(ph_after())}<div class="cap g">NACHHER</div></div></div>',
   kicker="BEISPIEL · REDESIGN AM HANDY", box="Gleicher Betrieb, gleiche Infos. Nur fürs Handy gedacht.", cover=True),
 slide(2, n, 'Vorher: <em>4 Stolpersteine</em>', ph_before(),
   kicker="SO SIEHT ES OFT AUS", box="Ein Beispiel, kein echter Kunde. Aber Sie kennen solche Seiten.", boxcls="o"),
 slide(3, n, 'Stolperstein <em>1 + 2</em>',
   fix([("1", "Telefonnummer als Bild", "Echte Nummer als Button. Ein Tipp, und es klingelt."), ("2", "Formular mit 6 Pflichtfeldern", "Drei Felder reichen: Name, Kontakt, Nachricht.")]),
   kicker="ANRUFEN · SCHREIBEN", box="Am Handy zählt jeder Tipp weniger.", boxcls="o"),
 slide(4, n, 'Stolperstein <em>3 + 4</em>',
   fix([("3", "Keine Öffnungszeiten", "„Heute offen bis 18:00“ ganz oben. Die häufigste Frage."), ("4", "Adresse nur als Text", "Button „Route planen“, der Google Maps öffnet.")]),
   kicker="FINDEN · HINKOMMEN", box="Oft wollen Kunden nur wissen: Ist offen? Wie komme ich hin?", boxcls="o"),
 slide(5, n, 'Nachher: <em>alles auf einen Blick</em>', ph_after(),
   kicker="DAS ERGEBNIS", box="Wer anrufen will, ruft an. Wer schreiben will, schreibt. Ohne Suchen.", boxcls="o"),
 slide(6, n, 'Der <em>Unterschied</em>',
   '<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;width:860px;text-align:left">'
   + f'<div class="lab" style="color:{RED};margin:0 0 0 8px">VORHER</div><div class="lab g" style="margin:0 0 0 8px">NACHHER</div>' + ''.join(
     f'<div class="card" style="padding:20px 24px;border-color:rgba(224,106,78,.45)"><div class="txt" style="font-size:32px">{a}</div></div><div class="card" style="padding:20px 24px"><div class="txt" style="font-size:32px;color:{LIGHT}">{b}</div></div>'
     for a, b in [("Nummer abtippen", "1 Tipp: anrufen"), ("6 Pflichtfelder", "3 Felder"), ("Zeiten suchen", "Steht ganz oben"), ("Adresse kopieren", "Route per Klick")]) + '</div>',
   kicker="AUF EINEN BLICK", box="Kleine Änderungen. Für Kunden ein großer Unterschied.", boxcls="o"),
 slide(7, n, 'Wie sieht <em>Ihre</em> Kontaktseite aus?',
   '<div style="display:flex;flex-direction:column;align-items:center;gap:30px">' + f'<div class="tile" style="width:300px;height:300px;flex-direction:column;gap:18px"><div style="font:400 110px/1 Outfit">📱</div><div class="lab g" style="margin:0">SCREENSHOT</div></div>'
   + '<div class="txt" style="font-size:38px;max-width:780px;color:#DCE7DF">Schicken Sie mir einen Screenshot per DM. Ich sage Ihnen ehrlich, was ich ändern würde.</div></div>',
   kicker="KOSTENLOS · PER DM", box="Öffnen Sie Ihre Seite am Handy und testen Sie die 4 Punkte selbst.", last=True),
]
POSTS["D-vorher-nachher"] = VN
