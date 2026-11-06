from w4posts import *   # slide, pills, G, LIGHT, RED, GOLD, ...
POSTS = {}
PH = HERE + "photos7/armsin-foto-"
SRC = "/home/claude/brag-src/assets/projects/youroma-fotos/"
CREDIT = {"tue_a": "Julie Mallet", "tue_b": "Gabrielle Henderson", "wed_a": "Noman Khan", "wed_b": "Ulysse Pointcheval",
          "thu_a": "TourBox", "thu_b": "Darya Ezerskaya", "fri_a": "Andras Vas", "fri_b": "delfina pan",
          "sat_a": "Georgia de Lotz", "sat_b": "Jojo Yuen", "sun_a": "Chloe Frost-Smith", "sun_b": "Behnam Norouzi",
          "mon_a": "Kyle Loftus", "mon_b": "Muhammad Ateeb"}
N = 5

def photo(k, pills_=(), w=820, h=470, pos="center"):
    card = f'''<div style="display:flex;flex-direction:column;align-items:center;gap:10px"><div style="position:relative;width:{w}px;height:{h}px;border-radius:30px;overflow:hidden;border:3px solid {G};box-shadow:0 0 60px rgba(57,217,122,.35)">
<div style="position:absolute;inset:0;background:url(file://{PH}{k}.jpg) {pos}/cover"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(4,12,7,0) 55%,rgba(4,12,7,.55))"></div></div>
<div style="font:400 22px/1 Inter;color:#8FB19B">Foto: {CREDIT[k]} / Unsplash</div></div>'''
    return f'<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">{card}' + pills(list(pills_)) + '</div>'

def cover(k, h1, kicker, box, pl, pos="center"):
    return slide(1, N, h1, photo(k, pl, pos=pos), kicker=kicker, box=box, cover=True)

def cards(items, size=44):
    pad = '18px 30px' if len(items) > 3 else '24px 32px'
    tsz = 28 if len(items) > 3 else 31
    return '<div style="display:flex;flex-direction:column;gap:20px;width:880px">' + ''.join(
        f'<div class="card" style="display:flex;gap:26px;align-items:center;padding:{pad}"><div class="num" style="font-size:44px;flex:none;width:64px">{n}</div><div style="text-align:left"><div class="big" style="font-size:{size}px">{h}</div><div class="txt" style="font-size:{tsz}px">{t}</div></div></div>'
        for n, h, t in items) + '</div>'

def vs(lt, litems, rt, ritems, lc=RED, rc=G):
    col = lambda t, items, c, mark: f'''<div class="card" style="flex:1;border-color:{c};padding:28px 26px;display:flex;flex-direction:column;gap:16px"><div class="lab" style="color:{c};font-size:26px">{t}</div>''' + ''.join(
        f'<div style="display:flex;gap:12px;align-items:flex-start"><span style="font:700 34px/1.2 Outfit;color:{c};flex:none">{mark}</span><span class="txt" style="font-size:31px;color:#DCE7DF">{x}</span></div>' for x in items) + '</div>'
    return f'<div style="display:flex;gap:22px;width:900px;align-items:stretch">{col(lt, litems, lc, "✕")}{col(rt, ritems, rc, "✓")}</div>'

def myth(m, f):
    return f'''<div style="display:flex;flex-direction:column;gap:26px;width:880px">
<div class="card" style="border-color:{RED};position:relative"><div class="lab" style="color:{RED}">MYTHOS</div><div class="big" style="font-size:50px;text-decoration:line-through;text-decoration-color:{RED};text-decoration-thickness:5px">„{m}“</div></div>
<div class="card" style="border-color:{G}"><div class="lab g">FAKT</div><div class="txt" style="font-size:36px;color:#EAF6EE">{f}</div></div></div>'''

def checks(items):
    return '<div style="display:flex;flex-direction:column;gap:18px;width:860px">' + ''.join(
        f'<div class="card" style="display:flex;gap:24px;align-items:center;padding:22px 30px"><div style="flex:none;width:52px;height:52px;border-radius:12px;border:4px solid {G}"></div><div class="txt" style="font-size:34px;color:#EAF6EE">{x}</div></div>'
        for x in items) + '</div>'

def big(n_, txt, src=""):
    s = f'<div style="font:400 24px/1.2 Inter;color:#8FB19B">{src}</div>' if src else ""
    return f'<div style="display:flex;flex-direction:column;align-items:center;gap:36px"><div style="font:700 220px/1 Outfit;letter-spacing:-6px;color:{G};text-shadow:0 0 60px rgba(57,217,122,.55)">{n_}</div><div class="txt" style="font-size:42px;color:#EAF6EE;max-width:820px;text-align:center">{txt}</div>{s}</div>'

def quote(t, sub=""):
    s = f'<div class="txt" style="font-size:30px;margin-top:22px">{sub}</div>' if sub else ""
    return f'<div class="card" style="width:860px;padding:50px 54px;border-width:3px;text-align:left"><svg width="90" height="70" viewBox="0 0 90 70"><path d="M8 66 C8 30 20 10 40 4 L42 14 C30 20 26 32 26 40 L40 40 L40 66Z M50 66 C50 30 62 10 82 4 L84 14 C72 20 68 32 68 40 L82 40 L82 66Z" fill="#39D97A"/></svg><div style="font:700 56px/1.2 Outfit;color:#EAF6EE">{t}</div>{s}</div>'

def tiles(items):
    return '<div style="display:flex;gap:18px;flex-wrap:wrap;justify-content:center;width:900px">' + ''.join(
        f'<div class="tile" style="width:200px;height:230px;flex-direction:column;gap:18px"><div style="font:400 80px/1 Outfit">{e}</div><div style="font:700 26px/1.15 Outfit;color:{LIGHT};text-align:center;padding:0 8px">{t}</div></div>' for e, t in items) + '</div>'

def last(h1, items, box, kicker="IHRE MEINUNG"):
    return slide(N, N, h1, tiles(items), kicker=kicker, box=box, last=True)

def s(i, h1, vis, kicker, box="", boxcls="o"):
    return slide(i, N, h1, vis, kicker=kicker, box=box, boxcls=boxcls)

def ba(name, lab_note):
    im = lambda f, t, c: f'<div style="display:flex;flex-direction:column;align-items:center;gap:14px"><div style="width:370px;height:460px;border-radius:26px;overflow:hidden;border:3px solid {c};background:url(file://{SRC}{f}) center/cover"></div><div class="chip" style="border-color:{c}">{t}</div></div>'
    return f'<div style="display:flex;gap:30px;align-items:center">{im("vorher-"+name+".jpg","VORHER · Handyfoto","#8FB19B")}{arrow(G,70)}{im("nachher-"+name+".jpg","NACHHER · "+lab_note,G)}</div>'

# ---------------- TUE A: Restaurant-Websites ----------------
POSTS["tue_a-restaurant"] = [
 cover("tue_a", 'Der Tisch ist frei. Die <em>Website</em> sagt es nicht.', "GASTRO · 5 FEHLER", "5 Fehler auf Restaurant-Websites. Und die Lösung.",
       [("Speisekarte als PDF", "left:14px;top:4%", -4), ("Zeiten versteckt", "right:14px;top:40%", 3), ("Kein Reservieren", "left:14px;bottom:12%", -2)]),
 s(2, 'Fehler 1 bis 3', cards([("1", "Speisekarte nur als PDF", "Am Handy winzig. Besser: als Text direkt auf der Seite."),
                               ("2", "Öffnungszeiten versteckt", "Gehören ganz nach oben. Mit Ruhetag."),
                               ("3", "Kein Reservieren", "Ein Button: anrufen oder online buchen.")]), "GASTRO · FEHLER", "Gäste entscheiden in Sekunden. Am Handy."),
 s(3, 'Fehler 4 und 5', cards([("4", "Fotos von 2015", "Aktuelle Bilder von Gerichten, Raum und Team."),
                              ("5", "Adresse ohne Link", "Ein Tipp, und Google Maps zeigt den Weg.")]), "GASTRO · FEHLER", "Kleine Änderungen. Große Wirkung."),
 s(4, 'Ihr 30-Sekunden-<em>Test</em>', checks(["Speisekarte mit 1 Tipp gefunden?", "Öffnungszeiten ohne Scrollen?", "Reservieren mit 1 Tipp?", "Adresse öffnet die Karte?"]),
   "AM HANDY TESTEN", "Viermal Ja? Glückwunsch. Sonst: melden Sie sich."),
 last('Was nervt Sie als <em>Gast</em> am meisten?', [("📄", "PDF-Karte"), ("🕐", "Keine Zeiten"), ("📞", "Kein Reservieren"), ("📍", "Keine Anfahrt")],
      "Antworten Sie mit dem Emoji in den Kommentaren."),
]
# ---------------- TUE B: Google-Bewertungen ----------------
POSTS["tue_b-bewertungen"] = [
 cover("tue_b", 'Mehr <em>Google-Bewertungen</em>, ohne zu betteln', "BEWERTUNGEN · 4 WEGE", "4 Wege, die wirklich funktionieren.",
       [("★★★★★", "right:14px;top:6%", 4), ("Direkt fragen", "left:14px;bottom:20%", -3)]),
 s(2, 'Weg 1 und 2', cards([("1", "Direkt fragen", "Nach einem guten Termin: „Würden Sie uns bewerten?“"),
                           ("2", "QR-Code an der Kasse", "Führt direkt zum Bewertungsformular.")]), "BEWERTUNGEN", "Der beste Moment: wenn der Kunde zufrieden ist."),
 s(3, 'Weg 3 und 4', cards([("3", "Link in Rechnung und Mail", "Ein Klick, und das Formular ist offen."),
                           ("4", "Jede Bewertung beantworten", "Auch die schlechten. Ruhig und sachlich.")]), "BEWERTUNGEN", "Antworten zeigen: Hier kümmert sich jemand."),
 s(4, 'Was Sie <em>nicht</em> tun sollten', vs("NICHT", ["Rabatt gegen Bewertung", "Bewertungen von Freunden schreiben lassen", "Nur zufriedene Kunden fragen"],
                                                 "STATTDESSEN", ["Alle Kunden fragen", "Ehrliches Feedback annehmen", "Kritik als Chance nutzen"]),
   "VORSICHT", "Google verbietet Anreize für Bewertungen."),
 last('Wie viele Bewertungen hat Ihr <em>Betrieb</em>?', [("🌱", "0 bis 10"), ("🌿", "10 bis 50"), ("🌳", "über 50"), ("🤷", "Keine Ahnung")],
      "Antworten Sie mit dem Emoji in den Kommentaren."),
]
# ---------------- WED A: Website-Mythen ----------------
POSTS["wed_a-mythen"] = [
 cover("wed_a", '3 Website-<em>Mythen</em>, die Sie Geld kosten', "MYTHOS VS. FAKT", "Ehrlich aufgeräumt.",
       [("„Instagram reicht“", "left:14px;top:6%", -4), ("„Zu teuer“", "right:14px;top:42%", 3), ("„Einmal und fertig“", "left:14px;bottom:12%", -2)], pos="center 30%"),
 s(2, 'Mythos 1', myth("Instagram reicht doch", "Instagram gehört Meta. Ihre Website gehört Ihnen. Und Google findet sie."), "MYTHOS VS. FAKT", "Social Media ist das Schaufenster, nicht der Laden."),
 s(3, 'Mythos 2', myth("Eine Website ist zu teuer", "Eine schlanke Seite zum Festpreis kostet oft weniger als gedacht. Und hält jahrelang."), "MYTHOS VS. FAKT", "Rechnen Sie: Was bringt ein neuer Kunde pro Jahr?"),
 s(4, 'Mythos 3', myth("Einmal gebaut, fertig", "Zeiten, Preise und Fotos ändern sich. Kleine Updates halten die Seite lebendig."), "MYTHOS VS. FAKT", "Eine alte Seite wirkt wie ein geschlossener Laden."),
 last('Welchen Mythos haben Sie schon <em>gehört</em>?', [("📱", "Insta reicht"), ("💸", "Zu teuer"), ("✅", "Einmal fertig")],
      "Antworten Sie mit dem Emoji in den Kommentaren."),
]
# ---------------- WED B: Produktfotos (echtes Projekt) ----------------
POSTS["wed_b-produktfotos"] = [
 cover("wed_b", 'Vom Handyfoto zum <em>Produktbild</em>', "ECHTES PROJEKT · YOUROMA DRESDEN", "So sehen Ihre Produkte aus wie im Katalog.",
       [("Echtes Projekt", "right:14px;top:6%", 4), ("Mit KI bearbeitet", "left:14px;bottom:16%", -3)]),
 s(2, 'Vorher und <em>nachher</em>', ba("ameerat", "Produktbild"), "BEISPIEL 1", "Gleiches Produkt. Ganz anderer Eindruck."),
 s(3, 'Noch ein <em>Beispiel</em>', ba("sultan", "Produktbild"), "BEISPIEL 2", "Aus dem Laden direkt auf die Website."),
 s(4, 'Was den <em>Unterschied</em> macht', cards([("1", "Ruhiger Hintergrund", "Nichts lenkt vom Produkt ab."),
                                                   ("2", "Weiches Licht", "Keine harten Schatten, echte Farben."),
                                                   ("3", "Einheitlicher Look", "Alle Bilder passen zusammen.")]), "DAHINTER", "Mit KI bearbeitet, von mir geprüft."),
 last('Welches Produkt soll <em>glänzen</em>?', [("📸", "Schick mir ein Foto"), ("💬", "Per DM"), ("✨", "Ich zeige wie")],
      "Schicken Sie mir ein Handyfoto per DM. Ich sage Ihnen, was möglich ist.", kicker="IHR PRODUKT"),
]
# ---------------- THU A: Ablauf ----------------
POSTS["thu_a-ablauf"] = [
 cover("thu_a", 'So entsteht Ihre <em>Website</em>', "HINTER DEN KULISSEN · 4 SCHRITTE", "Vom ersten Gespräch bis zum Livegang.",
       [("Festpreis", "right:14px;top:6%", 4), ("1 Ansprechpartner", "left:14px;bottom:14%", -3)]),
 s(2, 'Schritt 1 und 2', cards([("01", "Kurzes Gespräch", "Sie erzählen von Ihrem Betrieb. Ich höre zu und frage nach."),
                               ("02", "Klares Angebot", "Festpreis und realistische Timeline. Schriftlich.")]), "SO ARBEITE ICH", "Keine versteckten Kosten."),
 s(3, 'Schritt 3 und 4', cards([("03", "Umsetzung mit Abstimmung", "Sie sehen Zwischenstände, nicht erst am Ende."),
                               ("04", "Übergabe und Betreuung", "Auf Wunsch kümmere ich mich danach um Updates.")]), "SO ARBEITE ICH", "Sie wissen immer, was gerade passiert."),
 s(4, 'Was Sie <em>mitbringen</em>', checks(["Ihr Logo (falls vorhanden)", "Ein paar Fotos", "Öffnungszeiten und Angebot", "30 Minuten für ein Gespräch"]),
   "IHR TEIL", "Bei Texten und Fotos helfe ich mit."),
 last('Was ist Ihnen am <em>wichtigsten</em>?', [("💶", "Preis"), ("⏱️", "Tempo"), ("🤝", "Ein Kontakt"), ("🎨", "Design")],
      "Antworten Sie mit dem Emoji in den Kommentaren."),
]
# ---------------- THU B: Ladezeit ----------------
POSTS["thu_b-ladezeit"] = [
 cover("thu_b", '3 Sekunden. Dann sind Ihre <em>Kunden</em> weg.', "LADEZEIT", "Warum langsame Seiten Kunden kosten.",
       [("Lädt …", "right:14px;top:8%", 4), ("⏱ 3 s", "left:14px;bottom:16%", -3)]),
 s(2, 'Die <em>Zahl</em> dazu', big("53 %", "der Handy-Besucher verlassen eine Seite, die länger als 3 Sekunden lädt.", "Quelle: Google, 2016"), "STUDIE", "Jede Sekunde zählt."),
 s(3, 'Die häufigsten <em>Bremsen</em>', cards([("1", "Riesige Fotos", "Vor dem Hochladen verkleinern."),
                                                 ("2", "Zu viele Plugins", "Jedes Extra kostet Zeit."),
                                                 ("3", "Billiges Hosting", "Ein langsamer Server bremst alles.")]), "URSACHEN", "Meist sind es Kleinigkeiten."),
 s(4, 'So testen Sie <em>selbst</em>', cards([("1", "PageSpeed Insights öffnen", "Kostenloses Tool von Google."),
                                              ("2", "Ihre Adresse eingeben", "Ergebnis für Handy anschauen."),
                                              ("3", "Unter 50 Punkte?", "Dann lohnt sich ein Blick hinter die Kulissen.")]), "GRATIS-TEST", "Dauert 1 Minute."),
 last('Wie schnell ist Ihre <em>Seite</em>?', [("⚡", "Blitzschnell"), ("🐢", "Eher langsam"), ("🤷", "Keine Ahnung")],
      "Testen Sie und schreiben Sie Ihre Punktzahl in die Kommentare."),
]
# ---------------- FRI A: Freitag der 13. ----------------
POSTS["fri_a-horror"] = [
 cover("fri_a", 'Freitag, der 13.: 5 Website-<em>Horror</em>-Momente', "GRUSEL-SPECIAL 👻", "Erkennen Sie Ihre Seite wieder?",
       [("Nicht sicher!", "right:14px;top:6%", 4), ("© 2019", "left:14px;bottom:16%", -3)]),
 s(2, 'Horror 1 bis 3', cards([("1", "„Nicht sicher“ im Browser", "Das Schloss fehlt. Kunden springen ab."),
                              ("2", "© 2019 im Footer", "Wirkt, als wäre der Laden zu."),
                              ("3", "Handy-Ansicht kaputt", "Winzige Schrift, Buttons zu eng.")]), "GRUSELIG", "Für Besucher sofort sichtbar."),
 s(3, 'Horror 4 und 5', cards([("4", "Formular ins Nichts", "Anfragen kommen nie an. Niemand merkt es."),
                              ("5", "Domain abgelaufen", "Über Nacht ist die Seite weg.")]), "NOCH GRUSELIGER", "Die schlimmsten merkt man erst zu spät."),
 s(4, 'Ihr Anti-<em>Horror</em>-Check', checks(["Schloss-Symbol in der Adresszeile?", "Jahreszahl im Footer aktuell?", "Test-Anfrage übers Formular geschickt?", "Domain-Ablaufdatum notiert?"]),
   "5 MINUTEN", "Einmal im Monat reicht."),
 last('Welcher Horror ist Ihnen <em>passiert</em>?', [("🔓", "Nicht sicher"), ("📅", "Alt"), ("📱", "Handy kaputt"), ("📭", "Formular"), ("💀", "Domain weg")],
      "Beichten Sie in den Kommentaren. 👻"),
]
# ---------------- FRI B: Online-Buchung ----------------
POSTS["fri_b-buchung"] = [
 cover("fri_b", 'Termine buchen, während Sie <em>schlafen</em>', "ONLINE-BUCHUNG", "Rund um die Uhr, ohne Telefon-Hin-und-Her.",
       [("24/7", "right:14px;top:6%", 4), ("Keine verpassten Anrufe", "left:14px;bottom:14%", -3)]),
 s(2, 'Vorher und <em>nachher</em>', vs("OHNE", ["Telefon klingelt mitten im Termin", "Rückruf vergessen", "Nur zu Öffnungszeiten"],
                                        "MIT ONLINE-BUCHUNG", ["Kunden buchen selbst", "Bestätigung automatisch", "Auch nachts und am Wochenende"]),
   "DER UNTERSCHIED", "Sie arbeiten. Der Kalender füllt sich."),
 s(3, 'So einfach geht <em>Buchen</em>', cards([("1", "Leistung wählen", "Zum Beispiel: Haarschnitt, 30 Minuten."),
                                                 ("2", "Freie Zeit tippen", "Nur echte freie Slots."),
                                                 ("3", "Fertig", "Bestätigung und Erinnerung per Mail.")]), "FÜR IHRE KUNDEN", "3 Tipps statt 3 Anrufe."),
 s(4, 'Für wen lohnt es <em>sich</em>?', checks(["Friseur und Kosmetik", "Physio und Praxen", "Werkstätten", "Nachhilfe und Kurse"]), "PASST ZU", "Überall, wo Termine vergeben werden."),
 last('Wie buchen Ihre Kunden <em>heute</em>?', [("📞", "Telefon"), ("💬", "WhatsApp"), ("🌐", "Online"), ("🚶", "Vorbeikommen")],
      "Antworten Sie mit dem Emoji in den Kommentaren."),
]
# ---------------- SAT A: Instagram oder Website ----------------
POSTS["sat_a-insta-website"] = [
 cover("sat_a", 'Instagram oder <em>Website</em>? Was Ihnen gehört.', "WOCHENEND-GEDANKE", "Beides hat seinen Platz. Aber nicht denselben.",
       [("Gehört Meta", "right:14px;top:6%", 4), ("Gehört Ihnen", "left:14px;bottom:14%", -3)]),
 s(2, 'Der <em>Vergleich</em>', vs("INSTAGRAM", ["Regeln macht Meta", "Konto kann gesperrt werden", "Infos gehen im Feed unter"],
                                   "WEBSITE", ["Gehört Ihnen", "Google findet sie", "Alle Infos an einem Ort"], lc=GOLD),
   "EHRLICH VERGLICHEN", "Instagram bringt Reichweite. Die Website bringt Vertrauen."),
 s(3, 'Merksatz', quote("Instagram ist das Schaufenster. Die Website ist der Laden.", "Wer reinschaut, braucht eine Tür."), "KURZ GESAGT"),
 s(4, 'So spielen beide <em>zusammen</em>', cards([("1", "Link in der Bio", "Führt direkt auf Ihre Website."),
                                                    ("2", "Posts mit Ziel", "Jeder Beitrag zeigt auf ein Angebot."),
                                                    ("3", "Website zeigt Social", "Neue Besucher finden Ihr Profil.")]), "DAS DUO", "Zusammen sind sie stark."),
 last('Was nutzen <em>Sie</em>?', [("📱", "Nur Instagram"), ("🌐", "Nur Website"), ("🤝", "Beides"), ("❌", "Nichts davon")],
      "Antworten Sie mit dem Emoji in den Kommentaren."),
]
# ---------------- SAT B: Google-Profil-Check ----------------
POSTS["sat_b-google-profil"] = [
 cover("sat_b", '5 Minuten für Ihr <em>Google-Profil</em>', "WOCHENEND-CHECK", "Der günstigste Kunden-Magnet, den es gibt.",
       [("Kostenlos", "right:14px;top:6%", 4), ("5 Minuten", "left:14px;bottom:14%", -3)]),
 s(2, 'Check 1 bis 3', checks(["Öffnungszeiten aktuell?", "Telefonnummer richtig?", "Link zur Website drin?"]), "BASICS", "Falsche Zeiten kosten Vertrauen."),
 s(3, 'Check 4 bis 6', checks(["Aktuelle Fotos, innen und außen?", "Richtige Kategorie gewählt?", "Beschreibung mit Ihrem Ort?"]), "FÜR MEHR SICHTBARKEIT", "Google zeigt gern vollständige Profile."),
 s(4, '<em>Feiertage</em> nicht vergessen', quote("Weihnachten kommt schneller als gedacht.", "Tragen Sie Sonderöffnungszeiten jetzt schon ein. Kunden sehen sie sofort."), "SAISON-TIPP"),
 last('Wann haben Sie zuletzt <em>geprüft</em>?', [("✅", "Diese Woche"), ("🗓️", "Dieses Jahr"), ("😬", "Noch nie")],
      "Antworten Sie mit dem Emoji in den Kommentaren."),
]
# ---------------- SUN A: Startseiten-Satz ----------------
POSTS["sun_a-startseite"] = [
 cover("sun_a", 'Der wichtigste Satz auf Ihrer <em>Startseite</em>', "SONNTAGS-TIPP", "Ein Satz entscheidet, ob Besucher bleiben.",
       [("Willkommen auf …", "right:14px;top:6%", 4), ("Was. Wo. Warum.", "left:14px;bottom:14%", -3)]),
 s(2, 'Vorher und <em>nachher</em>', vs("VORHER", ["„Herzlich willkommen auf unserer Homepage“"], "NACHHER", ["„Frisches Brot aus Freiberg. Heute ab 6 Uhr.“"]),
   "AUSGEDACHTES BEISPIEL", "Der zweite Satz sagt in 2 Sekunden alles."),
 s(3, 'Die <em>Formel</em>', big("Was + Wo", "plus ein Grund, jetzt zu kommen.", ""), "SO GEHT ES", "Kurz, konkret, ohne Fachwörter."),
 s(4, 'Noch 3 <em>Beispiele</em>', cards([("✂", "Friseur", "„Haarschnitt in Freiberg. Termin online in 1 Minute.“"),
                                          ("🔧", "Werkstatt", "„Ihr Auto in guten Händen. Heute noch Termin.“"),
                                          ("☕", "Café", "„Frühstück am Obermarkt. Ab 8 Uhr geöffnet.“")], size=40), "AUSGEDACHTE BEISPIELE", "Probieren Sie es für Ihren Betrieb."),
 last('Was steht oben auf <em>Ihrer</em> Seite?', [("👋", "Willkommen"), ("🎯", "Klarer Satz"), ("🤔", "Weiß nicht")],
      "Schicken Sie mir Ihren Satz per DM. Ich gebe ehrliches Feedback."),
]
# ---------------- SUN B: Kosten ----------------
POSTS["sun_b-kosten"] = [
 cover("sun_b", 'Was kostet eine <em>Website</em> wirklich?', "EHRLICHE ANTWORT", "Die Faktoren, die den Preis bestimmen.",
       [("Festpreis?", "right:14px;top:6%", 4), ("Laufende Kosten?", "left:14px;bottom:14%", -3)]),
 s(2, 'Das bestimmt den <em>Preis</em>', cards([("1", "Anzahl der Seiten", "Eine Seite oder zehn?"),
                                                 ("2", "Funktionen", "Buchung, Shop, Formulare."),
                                                 ("3", "Texte und Fotos", "Vorhanden oder neu?"),
                                                 ("4", "Laufende Kosten", "Domain, Hosting, Pflege.")], size=40), "FAKTOREN", "Jeder Betrieb braucht etwas anderes."),
 s(3, 'Worauf Sie <em>achten</em> sollten', vs("VORSICHT", ["Versteckte Zusatzkosten", "Nur eine Vorlage", "Keiner antwortet später"],
                                              "GUT", ["Alles vorher schriftlich", "Passend zu Ihrem Betrieb", "Ein fester Ansprechpartner"]),
   "VERGLEICHEN", "Der billigste Preis ist nicht immer der günstigste."),
 s(4, 'So mache ich <em>es</em>', quote("Erst ein kostenloser Check. Dann ein Festpreis.", "Schriftlich, ohne Überraschungen später."), "BEI ARMSIN"),
 last('Was ist Ihnen beim Preis <em>wichtig</em>?', [("💶", "Günstig"), ("📝", "Festpreis"), ("🔁", "Monatlich"), ("❓", "Erst beraten")],
      "Antworten Sie mit dem Emoji in den Kommentaren."),
]
# ---------------- MON A: KI-Helfer ----------------
POSTS["mon_a-ki-helfer"] = [
 cover("mon_a", '4 KI-Helfer für den <em>Alltag</em> im Betrieb', "KI-MONTAG", "Spart Zeit. Ohne Technik-Studium.",
       [("Texte", "right:14px;top:6%", 4), ("Bilder", "left:14px;top:36%", -3), ("Ideen", "right:14px;bottom:12%", 2)], pos="center 35%"),
 s(2, 'Helfer 1 und 2', cards([("1", "Texte schreiben", "Angebote, Mails, Antworten auf Bewertungen."),
                              ("2", "Bilder aufhübschen", "Produktfotos mit ruhigem Hintergrund.")]), "KI IM ALLTAG", "Sie prüfen, die KI tippt."),
 s(3, 'Helfer 3 und 4', cards([("3", "Zusammenfassen", "Lange Mails oder Dokumente in 3 Sätzen."),
                              ("4", "Social-Media-Ideen", "10 Post-Ideen für Ihren Betrieb in 1 Minute.")]), "KI IM ALLTAG", "Ideal für den Montagmorgen."),
 s(4, 'Eine <em>Regel</em> zuerst', quote("Keine Kundendaten in Gratis-Chatbots.", "Namen, Adressen und Rechnungen bleiben draußen."), "DATENSCHUTZ"),
 last('Nutzen Sie schon <em>KI</em>?', [("🤖", "Täglich"), ("🙂", "Manchmal"), ("🤔", "Noch nie")],
      "Antworten Sie mit dem Emoji in den Kommentaren."),
]
# ---------------- MON B: Handwerk-Fotos ----------------
POSTS["mon_b-handwerk"] = [
 cover("mon_b", 'Handwerk verkauft sich mit <em>Fotos</em>', "FÜR HANDWERKSBETRIEBE", "Zeigen, was Sie können.",
       [("Vorher / Nachher", "right:14px;top:6%", 4), ("Echte Arbeit", "left:14px;bottom:14%", -3)]),
 s(2, 'Was Kunden <em>sehen</em> wollen', cards([("1", "Vorher und nachher", "Der stärkste Beweis für gute Arbeit."),
                                                  ("2", "Das Team", "Gesichter schaffen Vertrauen."),
                                                  ("3", "Details", "Material, Fugen, saubere Kanten.")]), "WAS WIRKT", "Echte Fotos schlagen jedes Stockfoto."),
 s(3, 'So gelingen <em>Handyfotos</em>', checks(["Tageslicht nutzen", "Vorher und nachher aus gleichem Winkel", "Kurz aufräumen", "Querformat für die Website"]),
   "4 TIPPS", "Kein Profi nötig."),
 s(4, 'Erst <em>fragen</em>', quote("Darf ich das Ergebnis zeigen?", "Fragen Sie Ihre Kunden, bevor Fotos online gehen. Ohne Hausnummer, ohne Gesichter."), "FAIR BLEIBEN"),
 last('Zeigen Sie Ihre Arbeit <em>online</em>?', [("📸", "Ja, oft"), ("🙈", "Selten"), ("🤷", "Noch nie")],
      "Antworten Sie mit dem Emoji in den Kommentaren."),
]
