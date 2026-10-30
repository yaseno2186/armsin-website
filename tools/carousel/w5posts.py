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

# ================= D: Vorher / Nachher Kontaktseite (design critique canvas) =================
SERIF_OLD = "font-family:'Times New Roman',Times,serif"
def old_page():
    lab = lambda t: f'<div style="font:400 22px/1 Arial;color:#333;margin-top:8px">{t}<span style="color:#c00">*</span></div><div style="height:30px;flex:none;border:1px solid #999;background:#fff"></div>'
    return f"""<div style="background:#e9e9e9;height:100%;display:flex;flex-direction:column">
<div style="background:#6d6d6d;padding:58px 16px 14px;display:flex;justify-content:space-between;align-items:center"><div style="{SERIF_OLD};font-size:28px;color:#fff;font-style:italic">Bäckerei Beispiel</div><div style="font:400 22px/1 Arial;color:#ddd">☰</div></div>
<div style="padding:16px 18px;display:flex;flex-direction:column;gap:4px">
<div style="{SERIF_OLD};font-size:34px;color:#222">Kontakt</div>
<div style="font:400 22px/1.3 Arial;color:#555">Für Anfragen nutzen Sie bitte das folgende Formular.</div>
<div style="margin:8px 0;width:230px;height:30px;background:#cfcfcf;display:flex;align-items:center;justify-content:center;font:italic 22px/1 Arial;color:#888">[bild: tel.jpg]</div>
{lab("Anrede")}{lab("Vorname")}{lab("Nachname")}{lab("E-Mail")}{lab("Betreff")}
<div style="margin-top:12px;align-self:flex-start;background:#ddd;border:1px solid #999;padding:6px 14px;font:400 22px/1 Arial;color:#333">Absenden</div>
<div style="margin-top:10px;font:400 22px/1.2 Arial;color:#777">Hauptstr. 12, 09599 Freiberg</div></div></div>"""
def new_page():
    fld = lambda t: f'<div style="height:52px;flex:none;border:2px solid #E2D6C4;border-radius:14px;background:#fff;font:400 24px/48px Inter;color:#9A8F80;padding-left:16px">{t}</div>'
    return f"""<div style="background:#FFFBF4;height:100%;display:flex;flex-direction:column">
<div style="height:280px;flex:none;background:radial-gradient(circle at 75% 40%,#F9D9A6,#E7A867 60%,#C9783E);position:relative;padding:22px 24px;display:flex;flex-direction:column;justify-content:flex-end">
<div style="position:absolute;right:26px;top:58px;font:400 100px/1 Outfit">🥐</div>
<div style="font:italic 400 46px/1 Serif;color:#2B1A0C">Bäckerei Beispiel</div>
<div style="margin-top:12px;align-self:flex-start;display:flex;align-items:center;gap:10px;background:#FFFBF4;border-radius:999px;padding:8px 16px;font:700 22px/1 Inter;color:#2E8F55"><span style="width:12px;height:12px;border-radius:50%;background:#2E8F55;display:inline-block"></span>Heute offen bis 18:00</div></div>
<div style="padding:20px 22px;display:flex;flex-direction:column;gap:14px">
<div style="background:#2B1A0C;color:#FFFBF4;border-radius:16px;padding:20px;text-align:center;font:700 30px/1 Outfit">📞 Jetzt anrufen</div>
<div style="border:2px solid #2B1A0C;color:#2B1A0C;border-radius:16px;padding:16px;text-align:center;font:700 26px/1 Outfit">📍 Route planen</div>
<div style="font:700 22px/1 Inter;color:#9A8F80;margin-top:6px;letter-spacing:1px">ODER SCHREIBEN SIE UNS</div>
{fld("Name")}{fld("Telefon oder E-Mail")}{fld("Ihre Nachricht")}</div></div>"""
def iphone(page, k=.8, w=390, h=800):
    return f"""<div style="width:{int(w*k)}px;height:{int(h*k)}px;flex:none;position:relative"><div style="transform:scale({k});transform-origin:top left;width:{w}px;height:{h}px;border-radius:58px;background:#111;padding:14px;box-shadow:0 30px 60px rgba(40,30,15,.28),0 0 0 2px #3a3a3a inset">
<div style="width:100%;height:100%;border-radius:46px;overflow:hidden;position:relative">{page}<div style="position:absolute;left:50%;top:10px;transform:translateX(-50%);width:120px;height:34px;border-radius:20px;background:#111"></div></div></div></div>"""
def split_phone(k=.8, w=390, h=800):
    half = lambda page, side: f'<div style="position:absolute;inset:0;clip-path:inset(0 {"50%" if side=="l" else "0"} 0 {"50%" if side=="r" else "0"})">{page}</div>'
    inner = half(old_page(), "l") + half(new_page(), "r") + f'<div style="position:absolute;left:50%;top:0;bottom:0;width:6px;margin-left:-3px;background:#fff;box-shadow:0 0 12px rgba(0,0,0,.4)"></div><div style="position:absolute;left:50%;top:50%;width:76px;height:76px;margin:-38px 0 0 -38px;border-radius:50%;background:#fff;box-shadow:0 6px 20px rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center;font:700 34px/1 Outfit;color:#1E1B16">‹ ›</div>'
    return iphone(inner, k, w, h)
def note(t, x, y, c, r=0, ax=None, w=260, flip=False):
    arr = ""
    if ax:
        d = "M4 20 C40 4 80 6 116 22" if not flip else "M116 20 C80 4 40 6 4 22"
        hd = "M100 10 L118 23 L100 34" if not flip else "M20 10 L2 23 L20 34"
        arr = f'<svg width="120" height="44" viewBox="0 0 120 44" style="position:absolute;{ax}"><path d="{d}" fill="none" stroke="{c}" stroke-width="4.5" stroke-linecap="round"/><path d="{hd}" fill="none" stroke="{c}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;transform:rotate({r}deg)"><div style="font:400 40px/1.08 Hand;color:{c};text-align:{"right" if not flip else "left"}">{t}</div>{arr}</div>'
RD, GN = "#D2452B", "#2E8F55"
n = 6
VN = [
 slide(1, n, 'Gleiche Bäckerei. <em>Neue</em> Seite.',
   '<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">' + split_phone(.8)
   + note("vorher", 70, 230, RD, -6, "left:150px;top:46px", 200)
   + note("nachher", 650, 230, GN, 5, "left:-30px;top:46px", 200, flip=True) + '</div>',
   kicker="VORHER / NACHHER · BEISPIEL", box="Ein ausgedachtes Beispiel. Aber solche Seiten gibt es überall.", boxcls="n", cover=True, variant="c"),
 slide(2, n, 'Vorher: <em>4 Stolpersteine</em>',
   '<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">' + iphone(old_page(), .8)
   + note("Nummer ist<br>ein Bild?!", 0, 120, RD, -4, "left:150px;top:100px")
   + note("6 Pflicht-<br>felder ...", 0, 330, RD, 3, "left:150px;top:100px")
   + note("Wann ist<br>offen??", 645, 40, RD, 4, "left:-40px;top:100px", flip=True)
   + note("Wo genau?<br>Kein Link.", 645, 450, RD, -3, "left:-40px;top:100px", flip=True) + '</div>',
   kicker="SO SIEHT ES OFT AUS", box="Am Computer okay. Am Handy mühsam.", boxcls="n", variant="c"),
 slide(3, n, 'Nachher: <em>alles auf einen Blick</em>',
   '<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">' + iphone(new_page(), .8)
   + note("Offen? Steht<br>ganz oben.", 0, 140, GN, -4, "left:150px;top:100px")
   + note("1 Tipp =<br>Anruf", 0, 330, GN, 3, "left:150px;top:100px")
   + note("Route per<br>Klick", 645, 300, GN, 4, "left:-40px;top:100px", flip=True)
   + note("nur 3<br>Felder", 645, 470, GN, -3, "left:-40px;top:100px", flip=True) + '</div>',
   kicker="DAS ERGEBNIS", box="Wer anrufen will, ruft an. Wer schreiben will, schreibt.", boxcls="n", variant="c"),
 slide(4, n, 'Der wichtigste <em>Button</em>',
   f"""<div style="display:flex;flex-direction:column;align-items:center;gap:40px;width:880px">
<div style="position:relative"><div style="background:#2B1A0C;color:#FFFBF4;border-radius:26px;padding:34px 70px;font:700 56px/1 Outfit;box-shadow:0 24px 50px rgba(40,30,15,.25)">📞 Jetzt anrufen</div>
<div style="position:absolute;right:-70px;bottom:-56px;width:100px;height:100px;border-radius:50%;border:5px solid {GN};background:rgba(46,143,85,.12)"></div></div>
<div style="background:#1E1B16;border-radius:20px;padding:26px 34px;font:400 28px/1.5 MonoR;color:#EAF6EE;text-align:left;width:860px;white-space:nowrap"><span style="color:#8FB19B">&lt;a href=</span><span style="color:#39D97A">"tel:+49 3731 ..."</span><span style="color:#8FB19B">&gt;</span>Jetzt anrufen<span style="color:#8FB19B">&lt;/a&gt;</span></div></div>""",
   kicker="KLEINES DETAIL · GROSSE WIRKUNG", box="Eine Zeile Code. Danach ruft man mit einem Tipp an statt abzutippen.", boxcls="n", variant="c"),
 slide(5, n, 'Ihr <em>Handy-Test</em> in 1 Minute',
   '<div style="display:flex;flex-direction:column;gap:18px;width:860px">' + ''.join(
     f'<div style="display:flex;align-items:center;gap:26px;background:#FFFDF8;border-radius:18px;padding:24px 30px;box-shadow:0 10px 24px rgba(40,30,15,.1)"><div style="flex:none;width:52px;height:52px;border-radius:12px;border:4px solid {INK}"></div><div style="font:700 40px/1.15 Outfit;color:{INK};text-align:left">{t}</div></div>'
     for t in ["Nummer mit einem Tipp anrufbar?", "Öffnungszeiten ohne Scrollen sichtbar?", "Adresse öffnet Google Maps?", "Formular mit 3 bis 4 Feldern?"]) + '</div>',
   kicker="ZUM SPEICHERN", box="Nehmen Sie Ihr Handy und haken Sie ab.", boxcls="n", variant="c"),
 slide(6, n, 'Wie sieht <em>Ihre</em> Seite aus?',
   '<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">' + iphone('<div style="height:100%;background:linear-gradient(180deg,#F6F4EF,#E4DED2);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px"><div style="font:400 120px/1 Outfit">📸</div><div style="font:700 34px/1.2 Outfit;color:#1E1B16;text-align:center;padding:0 30px">Ihr Screenshot</div></div>', .62)
   + note("per DM<br>an mich", 640, 120, GN, 4, "left:-40px;top:100px", flip=True)
   + note("ehrliche<br>Meinung", 30, 300, GN, -4, "left:150px;top:100px") + '</div>',
   kicker="KOSTENLOS · PER DM", box="Schicken Sie mir einen Screenshot Ihrer Kontaktseite. Ich sage Ihnen, was ich ändern würde.", boxcls="n", last=True, variant="c"),
]
POSTS["D-vorher-nachher"] = VN

# ================= F: Hacker + KI-Agenten (rich, dark brand) =================
def rlogo(w, light=True):
    sv = logo_svg("reuters")
    if light: sv = sv.replace('#212223', '#EAF6EE')
    return f'<div style="width:{w}px;height:{int(w*260.2/950)}px;flex:none">{sv.replace("width=\"950\" height=\"260.203\"", "width=\"100%\" height=\"100%\"")}</div>'
R2, G2 = "#E06A4E", "#39D97A"
def stamp(t, x, y, r=-10, size=40):
    return f'<div style="position:absolute;{x};{y};transform:rotate({r}deg);border:5px solid {R2};color:{R2};font:700 {size}px/1 Mono;letter-spacing:3px;padding:12px 20px;border-radius:8px;box-shadow:0 0 30px rgba(224,106,78,.35);background:rgba(26,10,8,.88)">{t}</div>'
def laptop(screen, w=760):
    h = int(w*0.62)
    return f"""<div style="display:flex;flex-direction:column;align-items:center"><div style="width:{w}px;height:{h}px;border-radius:22px 22px 6px 6px;background:#0b0f0c;border:10px solid #1d2420;box-shadow:0 0 60px rgba(57,217,122,.25);overflow:hidden;position:relative">{screen}</div>
<div style="width:{int(w*1.18)}px;height:22px;border-radius:0 0 20px 20px;background:linear-gradient(180deg,#2a322d,#151a17)"></div></div>"""
def agentlog():
    rows = [("agent-07", "shop-…ca", "✓", G2), ("agent-12", "store-…jp", "✗", "#5E7466"), ("agent-03", "admin-…au", "✓", G2), ("agent-19", "shop-…us", "…", "#8FB19B"), ("agent-21", "panel-…us", "✓", G2), ("agent-02", "store-…ca", "✗", "#5E7466")]
    r = ''.join(f'<div style="display:flex;justify-content:space-between;font:400 26px/1.65 MonoR;color:#C9DBCF"><span><span style="color:{G2}">{a}</span> → {b}</span><span style="color:{c}">{k}</span></div>' for a, b, k, c in rows)
    return f"""<div style="padding:22px 28px;height:100%;display:flex;flex-direction:column"><div style="display:flex;justify-content:space-between;font:400 22px/1 Pix;color:#8FB19B;margin-bottom:10px"><span>KI-AGENTEN · LIVE</span><span style="color:{R2}">● REC</span></div>{r}
<div style="margin-top:auto;display:flex;justify-content:space-between;align-items:center;border-top:2px solid rgba(234,246,238,.12);padding-top:12px"><span style="font:400 22px/1 Pix;color:#8FB19B">GEKNACKT</span><span style="font:700 40px/1 Outfit;color:{R2}">100+ / 1.200</span></div></div>"""
def dnote(t, x, y, c, r=0, ax=None, w=260, flip=False):
    return note(t, x, y, c, r, ax, w, flip)
def news_phone():
    page = f"""<div style="background:#0E1310;height:100%;padding:62px 26px 26px;display:flex;flex-direction:column;gap:20px">
<div style="display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid rgba(234,246,238,.12);padding-bottom:16px">{rlogo(210)}<div style="font:400 30px/1 Outfit;color:#8FB19B">☰</div></div>
<div style="font:700 22px/1 Inter;color:#FF8000;letter-spacing:1px">CYBERSECURITY</div>
<div style="font:700 40px/1.15 Outfit;color:#EAF6EE">How one hacker used AI agents to break into over 100 company websites</div>
<div style="font:400 22px/1.3 Inter;color:#8FB19B">By Raphael Satter · October 19, 2026</div>
<div style="height:170px;border-radius:14px;background:radial-gradient(circle at 30% 40%,rgba(57,217,122,.25),rgba(10,20,14,1) 70%);display:flex;align-items:center;justify-content:center;font:400 70px/1 Outfit">🤖</div>
<div class="ln" style="width:95%"></div><div class="ln" style="width:80%"></div><div class="ln" style="width:88%"></div></div>"""
    return iphone(page, .8)
def flow():
    agents = ''.join('<div style="width:76px;height:76px;border-radius:18px;border:2px solid rgba(57,217,122,.6);background:rgba(57,217,122,.1);display:flex;align-items:center;justify-content:center;font:400 42px/1 Outfit;box-shadow:0 0 18px rgba(57,217,122,.25)">🤖</div>' for _ in range(9))
    col = lambda big, lab, c, inner="": f'<div style="display:flex;flex-direction:column;align-items:center;gap:14px">{inner or ('<div style="font:700 84px/1 Outfit;color:'+c+'">'+big+'</div>')}<div class="lab" style="margin:0;color:{c};text-align:center">{lab}</div></div>'
    return ('<div style="display:flex;align-items:center;justify-content:center;gap:14px;width:920px">'
      + col("", "1 MENSCH", LIGHT, '<div class="tile" style="width:130px;height:130px;font:400 76px/1 Outfit">👤</div>')
      + arrow(G2, 70)
      + col("", "KI-AGENTEN", G2, f'<div style="display:grid;grid-template-columns:repeat(3,76px);gap:12px">{agents}</div>')
      + arrow(G2, 70)
      + '<div style="display:flex;flex-direction:column;gap:22px">' + col("1.200", "WEBSITES GETESTET", LIGHT) + col("100+", "GEKNACKT", R2) + '</div></div>')
def receipt():
    zig = "linear-gradient(135deg,transparent 12px,#F4F1EA 0) 0 0/24px 24px repeat-x, linear-gradient(225deg,transparent 12px,#F4F1EA 0) 0 0/24px 24px repeat-x"
    row = lambda a, b, bold=False, c="#1E1B16": f'<div style="display:flex;justify-content:space-between;font:{"700" if bold else "400"} 36px/1.6 MonoR;color:{c}"><span>{a}</span><span>{b}</span></div>'
    return f"""<div style="width:600px;margin-left:200px;transform:rotate(3deg);filter:drop-shadow(0 20px 40px rgba(0,0,0,.5))"><div style="height:16px;background:{zig};transform:scaleY(-1)"></div>
<div style="background:#F4F1EA;padding:20px 40px 30px;text-align:left"><div style="font:700 34px/1.2 Mono;color:#1E1B16;text-align:center;margin-bottom:10px">BELEG · KI-ANGRIFF</div><div style="font:400 22px/1.4 MonoR;color:#6E675B;text-align:center;margin-bottom:12px">Beleg · Okt 2026 · laut Forscher</div>
<div style="border-top:3px dashed #9A9488;margin:8px 0"></div>{row("KI-Rechenzeit", "5.000 $")}{row("Einbrüche", "100+")}
<div style="border-top:3px dashed #9A9488;margin:8px 0"></div>{row("PRO EINBRUCH", "≈ 50 $", True, "#B3261E")}
<div style="font:400 22px/1.4 MonoR;color:#6E675B;text-align:center;margin-top:14px">*** VIELEN DANK ***</div></div><div style="height:16px;background:{zig}"></div></div>"""
def shop_browser():
    return f"""<div style="position:relative"><div class="brow" style="width:780px"><div class="bar"><i></i><i></i><i></i><span>online-shop.example</span></div>
<div style="display:flex;gap:18px;padding:24px"><div style="flex:1;display:flex;flex-direction:column;gap:14px"><div style="display:flex;align-items:center;gap:12px;font:700 28px/1 Outfit;color:{G2}">🔒 Hauptseite</div><div style="height:150px;border-radius:12px;background:rgba(234,246,238,.08)"></div><div class="ln" style="width:80%"></div><div class="ln" style="width:60%"></div><div style="display:flex;gap:10px"><div style="flex:1;height:70px;border-radius:10px;background:rgba(234,246,238,.08)"></div><div style="flex:1;height:70px;border-radius:10px;background:rgba(234,246,238,.08)"></div></div></div>
<div style="flex:none;width:220px;border-radius:14px;border:3px solid {R2};background:rgba(224,106,78,.1);box-shadow:0 0 40px rgba(224,106,78,.45);padding:16px;display:flex;flex-direction:column;gap:10px"><div style="font:400 22px/1.2 MonoR;color:{R2}">/admin-alt</div><div style="font:700 24px/1.2 Outfit;color:{LIGHT}">Login-Panel</div><div style="height:34px;border-radius:8px;border:2px solid rgba(234,246,238,.25)"></div><div style="height:34px;border-radius:8px;border:2px solid rgba(234,246,238,.25)"></div><div style="font:400 22px/1.2 Inter;color:#8FB19B">zuletzt 2021 genutzt</div></div></div></div></div>"""
n = 7
HACK = [
 slide(1, n, '1 Hacker. Viele Agenten. <em style="color:#E06A4E;text-shadow:0 0 30px rgba(224,106,78,.55)">100 Websites.</em>',
   '<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">' + laptop(agentlog(), 620)
   + f'<div style="position:absolute;left:0;top:2%;display:flex;align-items:center;gap:12px;background:rgba(4,12,7,.9);border:2px solid rgba(234,246,238,.2);border-radius:14px;padding:12px 18px">{rlogo(170)}<span style="font:400 22px/1 Pix;color:#8FB19B">19.10.</span></div>'
   + stamp("ECHTER FALL", "right:30px", "bottom:6%", -10, 36) + '</div>',
   kicker="NEWS · KI-HACKING", box="Was passiert ist. Und was Ihre Website schützt.", cover=True),
 slide(2, n, 'Die <em>Quelle</em>',
   '<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">' + news_phone()
   + note("Original-<br>Schlagzeile", 0, 160, G2, -4, "left:150px;top:100px")
   + note("Reuters,<br>19.10.2026", 640, 380, G2, 4, "left:-40px;top:100px", flip=True) + '</div>',
   kicker="ECHTE NACHRICHT · NICHT AUSGEDACHT", box="Recherche: Sicherheitsforscher Snorre Fagerland (NorForge).", boxcls="o"),
 slide(3, n, 'So lief der <em>Angriff</em>', flow(),
   kicker="1 PERSON · DUTZENDE AGENTEN", box="Ein Mensch gibt Befehle. Die Maschinen machen die Arbeit.", boxcls="o"),
 slide(4, n, '<em>50 $</em> pro Einbruch',
   '<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">' + receipt()
   + note("lohnt sich<br>auch bei<br>kleinen Seiten", 0, 40, R2, -5, None, 240) + '</div>',
   kicker="DIE RECHNUNG", box="Wenn ein Einbruch so wenig kostet, ist keine Seite zu klein.", boxcls="o"),
 slide(5, n, 'Wen es <em>getroffen</em> hat',
   '<div style="display:flex;flex-direction:column;align-items:center;gap:26px">'
   + '<div style="display:flex;gap:20px">' + ''.join(f'<div class="tile" style="width:190px;height:200px;flex-direction:column;gap:14px"><div style="font:400 84px/1 Outfit">{f}</div><div class="lab" style="margin:0">{c}</div></div>' for f, c in [("🇺🇸","USA"),("🇨🇦","KANADA"),("🇦🇺","AUSTRALIEN"),("🇯🇵","JAPAN")]) + '</div>'
   + f'<div class="card" style="display:flex;align-items:center;gap:22px;width:840px"><div style="font:400 60px/1 Outfit">🛒</div><div><div class="big" style="font-size:42px">Meistens <em>Online-Shops</em></div><div class="txt" style="font-size:30px">Aber auch John Deere, SharkNinja, Cummins</div></div></div></div>',
   kicker="DIE OPFER", box="Nicht nur Konzerne. Vor allem ganz normale Shops.", boxcls="o"),
 slide(6, n, 'Wie sie <em>reinkamen</em>',
   '<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">' + shop_browser()
   + note("vorne: zu ✓", 40, 60, G2, -4, None, 260)
   + note("hinten:<br>vergessen!", 600, 30, R2, 4, None, 300) + '</div>',
   kicker="DER WEG REIN", box="Keine Lücke auf der Hauptseite. Aber ein altes Admin-Panel, öffentlich erreichbar.", boxcls="o"),
 slide(7, n, '5 Dinge, die Ihre Seite <em>schützen</em>',
   '<div style="display:flex;flex-direction:column;gap:12px;width:860px">' + ''.join(
     f'<div class="card" style="display:flex;align-items:center;gap:22px;padding:14px 26px"><div style="flex:none;width:54px;height:54px;border-radius:16px;background:rgba(57,217,122,.12);border:2px solid {G2};display:flex;align-items:center;justify-content:center;font:400 32px/1 Outfit">{i}</div><div class="big" style="font-size:34px">{t}</div></div>'
     for i, t in [("🔄","Updates für System, Plugins, PHP"),("🚪","Admin-Bereiche nicht offen im Netz"),("🧹","Alte Testseiten löschen"),("🔐","Zwei-Faktor-Login überall"),("💾","Backups, die funktionieren")]) + '</div>',
   kicker="WAS SIE TUN KÖNNEN", box="Speichern und Ihren Webdienstleister danach fragen.", boxcls="o", last=True),
]
POSTS["F-hacker-ki"] = HACK
