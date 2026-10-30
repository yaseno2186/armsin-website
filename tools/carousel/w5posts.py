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
