from lib3 import *

def shield(label="NIS2"):
    return f'''<div style="position:relative;width:340px;height:400px">
<svg viewBox="0 0 200 236" width="340" height="400" style="filter:drop-shadow(0 0 40px rgba(57,217,122,.5))"><path d="M100 6 L188 38 V112 C188 170 148 210 100 230 C52 210 12 170 12 112 V38 Z" fill="#0B1D13" stroke="{G}" stroke-width="5"/></svg>
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font:400 78px Pix;color:{G};text-shadow:0 0 24px rgba(57,217,122,.7);padding-bottom:30px">{label}</div></div>'''

def pills(items):
    return ''.join(f'<div class="pill" style="{pos};transform:rotate({rot}deg)">{t}</div>' for t, pos, rot in items)

def cta(i, n, word, what, chip):
    vis = f'<div style="display:flex;flex-direction:column;align-items:center;gap:34px"><div class="keybtn">{word}</div><div class="chip"><span>PDF</span>{chip}</div></div>'
    return slide(i, n, f'Kommentieren Sie <em>{word}</em>', vis, kicker="GRATIS · PER DM", box=what, last=True)

# ---------------- K: NIS2 (Mon 19) ----------------
n = 7
K = [
 slide(1, n, f'Betrifft NIS2 <em><span class="s">Ihren</span>{circ()}</em> Betrieb?',
   f'<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">{shield()}'
   + pills([("bis 10 Mio. € Bußgeld","left:14px;top:12%",-4),("Chefs haften persönlich","right:10px;top:3%",3),("≈ 29.500 Firmen in DE","left:20px;bottom:14%",2)]) + '</div>',
   kicker="NEWS · CYBERSICHERHEIT · 2026", box="Die kurze Antwort in 5 Folien.", cover=True),
 slide(2, n, 'Was ist <em>NIS2</em> überhaupt?',
   f'''<div style="display:flex;flex-direction:column;gap:22px;width:880px">
<div class="card"><div class="lab g">KURZ ERKLÄRT</div><div class="big" style="font-size:42px">Eine EU-Richtlinie für mehr <em>Cybersicherheit</em>. Deutschland setzt sie mit dem NIS2-Umsetzungsgesetz um.</div></div>
<div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap"><div class="chip"><span>1</span>Risiken managen</div><div class="chip"><span>2</span>Vorfälle schnell melden</div><div class="chip"><span>3</span>Beim BSI registrieren</div></div></div>''',
   kicker="ERST MAL KURZ ERKLÄRT", box="Ziel: Wichtige Firmen sollen Angriffe besser abwehren."),
 slide(3, n, 'Seit Dezember 2025 gilt NIS2 in <em>Deutschland</em>',
   f'''<div style="display:flex;flex-direction:column;gap:22px;width:860px">
<div class="card" style="display:flex;gap:28px;align-items:center"><div class="num" style="flex:none;width:230px;font-size:30px">6.12.2025</div><div class="big">Gesetz in Kraft, <em>ohne Übergangsfrist</em></div></div>
<div style="display:flex;justify-content:center">{arrow(G,140).replace('width="140"','width="140" style="transform:rotate(90deg)"')}</div>
<div class="card" style="display:flex;gap:28px;align-items:center"><div class="num" style="flex:none;width:230px;font-size:30px">6.3.2026</div><div class="big">Registrierung beim <em>BSI</em> war fällig</div></div></div>''',
   kicker="FAKT 1 VON 4 · DAS GESETZ", box="Es kommt kein Brief vom Amt. Jede Firma muss selbst prüfen.", boxcls="o"),
 slide(4, n, 'Vor allem Firmen ab <em>50 Mitarbeitern</em>',
   f'''<div style="display:flex;flex-direction:column;gap:20px;width:880px">
<div class="card"><div class="lab g">WICHTIGE EINRICHTUNG</div><div class="big">ab 50 Mitarbeitende <span style="color:{MUT}">oder</span> über 10 Mio. € Umsatz und Bilanz</div></div>
<div class="card"><div class="lab g">BESONDERS WICHTIGE EINRICHTUNG</div><div class="big">ab 250 Mitarbeitende <span style="color:{MUT}">oder</span> über 50 Mio. € Umsatz</div></div>
<div class="txt" style="text-align:center">… in bestimmten Branchen, z. B. Energie, Gesundheit, Transport, Lebensmittel, IT-Dienste.</div></div>''',
   kicker="FAKT 2 VON 4 · WER IST BETROFFEN?"),
 slide(5, n, 'Bis zu <em>10 Mio. €</em> Bußgeld',
   f'''<div style="display:flex;gap:26px;width:900px">
<div class="card" style="flex:1;text-align:center"><div class="lab g">BESONDERS WICHTIGE</div><div style="font:700 78px/1 Outfit;color:{G};margin:14px 0;white-space:nowrap">10 Mio. €</div><div class="txt">oder 2 % vom Umsatz*</div></div>
<div class="card" style="flex:1;text-align:center"><div class="lab g">WICHTIGE</div><div style="font:700 78px/1 Outfit;color:{LIGHT};margin:14px 0;white-space:nowrap">7 Mio. €</div><div class="txt">oder 1,4 % vom Umsatz*</div></div></div>''',
   kicker="FAKT 3 VON 4 · STRAFEN", box="Und: Die Geschäftsleitung kann persönlich haften.<br><span style=\"font:400 24px Inter;opacity:.8\">* Prozente gelten bei Konzernen mit über 500 Mio. € Umsatz.</span>"),
 slide(6, n, 'Kleiner Betrieb? Dann fragen <em>Ihre Kunden</em>',
   f'''<div style="display:flex;flex-direction:column;align-items:center;gap:22px">
<div style="display:flex;align-items:center;gap:22px"><div class="card" style="text-align:center;width:330px"><div class="lab g">GROSSKUNDE</div><div class="big">muss NIS2 erfüllen</div></div>{arrow(G,130)}<div class="card" style="text-align:center;width:330px;border-color:{G}"><div class="lab g">LIEFERANT</div><div class="big">Sie</div></div></div>
<div style="display:flex;gap:16px;flex-wrap:wrap;justify-content:center;max-width:880px">
<div class="chip">Passwörter + 2FA</div><div class="chip">Backups getestet</div><div class="chip">Updates aktuell</div><div class="chip">Notfall-Kontakt</div></div></div>''',
   kicker="FAKT 4 VON 4 · UND KLEINE BETRIEBE?", box="Meist nicht direkt betroffen. Aber die Basics sollten Sie zeigen können."),
 cta(7, n, "NIS2", "Ich schicke Ihnen den Schnellcheck: betroffen ja/nein + 5 Basics.", "NIS2-Schnellcheck · 1 Seite"),
]

# ---------------- A: 5 weitere Fehler (Tue 20) ----------------
n = 8
def phone(good, lines):
    return f'<div class="phone {"good" if good else "bad"}"><div style="width:70px;height:7px;border-radius:4px;background:rgba(234,246,238,.2);align-self:center"></div>{lines}</div>'
def pair(bad, good, lb="VORHER", lg="NACHHER"):
    return f'''<div style="display:flex;gap:60px;align-items:center;height:100%"><div style="display:flex;flex-direction:column;align-items:center;gap:12px"><div class="cap">{lb}</div>{bad}</div>
<div style="display:flex;flex-direction:column;align-items:center;gap:12px"><div class="cap g">{lg}</div>{good}</div></div>'''
A = [
 slide(1, n, f'5 <em><span class="s">weitere</span>{und()}</em> Fehler, die Anrufe kosten',
   f'''<div style="position:relative;height:100%;display:flex;align-items:center;justify-content:center;gap:24px">
{''.join(f'<div class="tile" style="width:150px;height:{170+40*(k%2)}px;flex-direction:column;gap:10px"><div class="num" style="font-size:64px">{k}</div></div>' for k in range(1,6))}</div>''',
   kicker="TEIL 2 · WEBSITE-FEHLER", box="Teil 1 lief am Montag. Hier kommt der Rest.", cover=True),
 slide(3, n, 'Auf dem Handy <em>kaum lesbar</em>',
   pair(phone(False, '<div style="font:400 22px/1.25 Outfit;color:#8FB19B">Willkommen bei Ihr Salon. Wir freuen uns auf Ihren Besuch und bieten seit vielen Jahren Schnitt, Farbe und Pflege für die ganze Familie an, Termine nach Vereinbarung, Anfahrt siehe unten …</div>' + '<div class="ln"></div>'*3),
        phone(True, '<div style="font:700 38px/1.1 Outfit">Ihr Salon</div><div class="txt" style="font-size:26px">Schnitt, Farbe, Pflege in Freiberg</div><div class="btn">Termin buchen</div><div class="btn o">Anrufen</div>')),
   kicker="FEHLER 1 VON 5 · HANDY", box="Test: Seite am Handy öffnen. Lesbar, ohne zu zoomen?", boxcls="o"),
 slide(4, n, 'Die Nummer ist <em>nicht antippbar</em>',
   pair(phone(False, '<div class="txt" style="font-size:26px">Telefon:</div><div style="font:400 26px MonoR;color:#C9DBCF">0 37 31 / XX XX XX</div><div class="txt" style="font-size:24px;color:#8FB19B">abschreiben, wechseln, tippen …</div>' + '<div class="ln"></div>'*4),
        phone(True, '<div class="txt" style="font-size:26px">Fragen? Rufen Sie an.</div><div class="btn" style="font-size:34px;padding:28px">📞 Jetzt anrufen</div><div class="txt" style="font-size:24px;color:#8FB19B">ein Tipp genügt</div>')),
   kicker="FEHLER 2 VON 5 · ANRUFEN", box="Ein Tipp zum Anruf. Nicht abschreiben lassen.", boxcls="o"),
 slide(5, n, 'Öffnungszeiten von <em>letztem Jahr</em>',
   f'''<div style="display:flex;gap:30px;align-items:center">
<div class="card" style="width:370px;opacity:.65"><div class="lab">WEBSITE</div><div class="big" style="text-decoration:line-through;text-decoration-color:#E06A4E">Mo–Fr 9–18</div><div class="txt">Sa 9–13</div><div class="txt">Stand: 2024</div></div>
{arrow(G,110)}
<div class="card" style="width:370px;border-color:{G}"><div class="lab g">GOOGLE + WEBSITE</div><div class="big">Mo–Fr 9–17</div><div class="txt">Sa geschlossen</div><div class="txt" style="color:{G}">Feiertage eingetragen</div></div></div>''',
   kicker="FEHLER 3 VON 5 · ZEITEN", box="Google und Website: immer dieselben Zeiten.", boxcls="o"),
 slide(6, n, 'Kein Weg zu <em>Google Maps</em>',
   f'''<div class="brow" style="width:640px;height:440px"><div class="bar"><i></i><i></i><i></i><span>ihr-salon.de/kontakt</span></div>
<div class="in"><div class="lab g">SO FINDEN SIE UNS</div><div class="big">Musterstraße 1<br>09599 Freiberg</div><div class="btn">📍 Route starten</div><div class="txt" style="font-size:26px;color:#8FB19B">öffnet die Karten-App direkt</div></div></div>''',
   kicker="FEHLER 4 VON 5 · ANFAHRT", box="Adresse als Link: ein Tipp, und die Route startet.", boxcls="o"),
 slide(7, n, 'Bilder, die <em>ewig laden</em>',
   f'''<div style="display:flex;flex-direction:column;gap:26px;width:820px">
<div class="card"><div class="lab">FOTO DIREKT VOM HANDY</div><div style="height:30px;border-radius:15px;background:rgba(234,246,238,.12);overflow:hidden;margin:10px 0"><div style="width:28%;height:100%;background:#E06A4E"></div></div><div class="txt">ca. 8 MB · lädt und lädt …</div></div>
<div class="card" style="border-color:{G}"><div class="lab g">VERKLEINERT FÜRS WEB</div><div style="height:30px;border-radius:15px;background:rgba(234,246,238,.12);overflow:hidden;margin:10px 0"><div style="width:100%;height:100%;background:{G}"></div></div><div class="txt">ca. 300 KB · sofort da</div></div></div>''',
   kicker="FEHLER 5 VON 5 · TEMPO", box="Fotos vor dem Hochladen verkleinern. Beispielwerte.", boxcls="o"),
 cta(8, n, "CHECK", "Ich schicke Ihnen den 5-Punkte Website-Check als PDF.", "5-Punkte Website-Check"),
]

# ---------------- E: 7-Schritte-Plan (Wed 21), paper steps ----------------
n = 7
def steps(a, b=None):
    s = lambda k, h, p: f'<div class="step"><div class="n">SCHRITT {k}</div><h3>{h}</h3><p>{p}</p></div>'
    inner = s(*a) + (f'<div style="display:flex;align-items:center">{arrow(OR,80).replace("width=\"80\"","width=\"80\"")}</div>' + s(*b) if b else "")
    return f'<div style="display:flex;gap:10px;align-items:stretch;width:920px">{inner}</div>'
E = [
 slide(1, n, f'Mein <em><span class="s">7-Schritte</span>{circ()}</em> Plan für Kunden-Websites',
   '<div style="display:flex;gap:14px;flex-wrap:wrap;justify-content:center;width:820px">' + ''.join(f'<div class="tile" style="width:150px;height:150px"><div class="num" style="font-size:64px">{k}</div></div>' for k in range(1,8)) + '</div>',
   kicker="FÜR FREELANCER + ENTWICKLER", box="Ohne Chaos und ohne endlose Korrekturschleifen.", cover=True),
 slide(3, n, 'Schritt 1 + 2: <em>vorher klären</em>', steps(("1","Ziel festhalten","Eine messbare Sache: mehr Anrufe, mehr Termine, weniger Mails."),("2","Fester Umfang","Im Angebot steht, was drin ist. Und was nicht.")), kicker="BEVOR ICH BAUE", variant="p"),
 slide(4, n, 'Schritt 3 + 4: <em>Inhalt zuerst</em>', steps(("3","Texte und Fotos","Kommen vor dem Design. Impressum und Datenschutz gleich mit."),("4","Ein Entwurf","Eine klickbare Startseite. Feedback in einer Runde, gesammelt.")), kicker="DANN ERST DESIGN", variant="p"),
 slide(5, n, 'Schritt 5 + 6: <em>prüfen, übergeben</em>', steps(("5","Checkliste","Handy, Tempo, Formulare, Kontraste, Links. Vor dem Livegang."),("6","Übergabe","Domain und Zugänge auf den Kunden. Kurze Anleitung dazu.")), kicker="LIVE GEHEN", variant="p"),
 slide(6, n, 'Schritt 7: <em>nachfragen</em>', steps(("7","Nach 30 Tagen","Kommen Anfragen? Was fehlt? Ein kurzer Anruf, keine Rechnung.")), kicker="DER SCHRITT, DEN VIELE VERGESSEN", box="Das Ziel aus Schritt 1 wird hier geprüft.", boxcls="n", variant="p"),
 cta(7, n, "SYSTEM", "Ich schicke Ihnen die Projekt-Checkliste mit allen 7 Schritten.", "Projekt-Checkliste · 1 Seite"),
]

# ---------------- C: 3 Arten (Thu 22) ----------------
n = 7
def site(url, inner, w=620, h=470):
    return f'<div class="brow" style="width:{w}px;height:{h}px"><div class="bar"><i></i><i></i><i></i><span>{url}</span></div><div class="in">{inner}</div></div>'
def typ(k, name, desc, fuer, mock):
    return f'''<div style="display:flex;flex-direction:column;gap:24px;align-items:center;width:920px">{mock}
<div style="text-align:center;display:flex;flex-direction:column;gap:12px;max-width:880px"><div style="font:400 48px/1.25 Outfit;color:{LIGHT}">{desc}</div><div style="font:700 40px/1.25 Outfit;color:{G}">Passt für: <span style="color:{LIGHT};font-weight:400">{fuer}</span></div></div></div>'''
C = [
 slide(1, n, f'3 Arten von Websites, die <em><span class="s">Anrufe</span>{und()}</em> bringen',
   f'''<div style="position:relative;width:760px;height:100%">
<div style="position:absolute;left:0;top:8%;transform:rotate(-5deg)">{site("visitenkarte.de",'<div class="ln"></div><div class="btn">Anrufen</div>',360,260)}</div>
<div style="position:absolute;right:0;top:4%;transform:rotate(4deg)">{site("termin.de",'<div class="ln"></div><div class="btn">Termin buchen</div>',360,260)}</div>
<div style="position:absolute;left:200px;bottom:2%">{site("antworten.de",'<div class="ln"></div><div class="btn o">Häufige Fragen</div>',360,260)}</div></div>''',
   kicker="WELCHE PASST ZU IHNEN?", cover=True),
 slide(3, n, 'Die <em>Visitenkarte</em>', typ(1, "", "Eine Seite: wer Sie sind, was Sie machen, wo Sie sind. Und ein großer Anruf-Knopf.", "Handwerk, kleine Läden, Dienstleister",
   site("ihr-betrieb.de",'<div class="big" style="font-size:36px">Ihr Betrieb</div><div class="btn">📞 Anrufen</div>',620,250)), hand="Typ 01", kicker=""),
 slide(4, n, 'Die <em>Buchungsseite</em>', typ(2, "", "Kunden buchen selbst, auch abends und am Sonntag. Weniger Telefon, volle Kalender.", "Salon, Physio, Werkstatt, Beratung",
   site("ihr-salon.de/termin",'<div class="lab g">FREIE TERMINE</div><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px">'+''.join(f'<div class="chip" style="text-align:center;padding:12px 6px">{t}</div>' for t in ["Di 10:00","Di 14:30","Mi 9:00","Do 16:00"])+'</div><div class="btn">Buchen</div>',620,270)), hand="Typ 02"),
 slide(5, n, 'Die <em>Antwortseite</em>', typ(3, "", "Die häufigsten Fragen sind schon beantwortet. Es rufen die an, die wirklich wollen.", "Restaurant, Handwerk, Vermietung",
   site("ihr-betrieb.de/faq",'<div class="lab g">HÄUFIGE FRAGEN</div>'+''.join(f'<div class="txt" style="font-size:26px;border-bottom:1px solid rgba(234,246,238,.15);padding-bottom:8px">+ {q}</div>' for q in ["Was kostet …?","Wo kann ich parken?"]),620,270)), hand="Typ 03"),
 slide(6, n, 'Welche passt <em>zu Ihnen?</em>',
   '<div style="display:flex;flex-direction:column;gap:18px;width:900px">' + ''.join(f'<div class="card" style="display:flex;align-items:center;gap:24px;padding:22px 30px"><div class="txt" style="flex:1;color:{LIGHT}">{a}</div>{arrow(G,90)}<div class="big" style="flex:none;width:300px;font-size:40px"><em>{b}</em></div></div>' for a,b in [("Kunden wollen Sie anrufen","Visitenkarte"),("Kunden wollen Termine","Buchungsseite"),("Kunden fragen immer das Gleiche","Antwortseite")]) + '</div>',
   kicker="KURZ-ENTSCHEIDUNG", box="Oft reicht eine davon. Mehr muss es am Anfang nicht sein.", boxcls="o"),
 cta(7, n, "CHECK", "Ich schicke Ihnen den 5-Punkte Website-Check als PDF.", "5-Punkte Website-Check"),
]

# ---------------- J: Instagram allein (Sat 24) ----------------
n = 7
def igphone():
    cells = ''.join(f'<div style="aspect-ratio:1;border-radius:6px;background:linear-gradient(135deg,#1E3A2A,#2F5B40);opacity:{.5+.08*(k%5)}"></div>' for k in range(9))
    return f'<div class="phone" style="width:300px;height:520px"><div style="display:flex;gap:12px;align-items:center"><div style="width:60px;height:60px;border-radius:50%;border:3px solid {G}"></div><div class="ln" style="flex:1"></div></div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6px">{cells}</div></div>'
J = [
 slide(1, n, f'Instagram allein ist <em><span class="s">keine</span>{circ()}</em> Website.',
   f'<div style="display:flex;align-items:center;gap:40px">{igphone()}<div style="font:700 80px Outfit;color:{MUT}">≠</div>{site("ihr-betrieb.de",'<div class="big" style="font-size:34px">Ihr Betrieb</div><div class="ln"></div><div class="btn">Anrufen</div><div class="btn o">Termin</div>',360,420)}</div>',
   kicker="UNBEQUEME WAHRHEIT", box="Warum Sie beides brauchen.", cover=True),
 slide(3, n, 'KI-Antworten verlinken <em>Websites</em>',
   f'''<div class="card" style="width:860px"><div class="lab g">FRAGE: FRISEUR IN FREIBERG HEUTE OFFEN?</div><div class="txt" style="color:{LIGHT}">„Ihr Salon hat heute bis 18 Uhr geöffnet. Termine buchen Sie online.“</div>
<div style="display:flex;gap:14px;margin-top:20px"><div class="chip"><span>QUELLE</span>ihr-salon.de</div><div class="chip"><span>QUELLE</span>Google-Profil</div></div></div>''',
   kicker="GRUND 1 VON 3 · GOOGLE", box="Seit 15.10. zeigt Google in KI-Antworten mehr Quellen-Links.", boxcls="o"),
 slide(4, n, 'Die Plattform gehört <em>nicht Ihnen</em>',
   '<div style="display:flex;flex-direction:column;gap:18px;width:820px">' + ''.join(f'<div class="card" style="display:flex;gap:22px;align-items:center;padding:22px 30px"><div class="num" style="color:#E06A4E">✕</div><div class="txt" style="color:{LIGHT}">{t}</div></div>' for t in ["Konto gesperrt oder gehackt","Regeln und Reichweite ändern sich","Ihre Inhalte liegen auf fremden Servern"]) + '</div>',
   kicker="GRUND 2 VON 3 · KONTROLLE", box="Ihre Website bleibt. Egal, was Instagram ändert.", boxcls="o"),
 slide(5, n, 'Nicht jeder Kunde ist <em>auf Instagram</em>',
   f'''<div style="display:flex;gap:26px">{''.join(f'<div class="card" style="width:270px;text-align:center"><div style="font:700 64px Outfit;color:{G}">{i}</div><div class="txt" style="color:{LIGHT}">{t}</div></div>' for i,t in [("🔎","sucht bei Google"),("🗺️","fragt die Karten-App"),("💬","fragt eine KI")])}</div>''',
   kicker="GRUND 3 VON 3 · REICHWEITE", box="Wer nicht scrollt, sucht. Dann braucht er eine Seite.", boxcls="o"),
 slide(6, n, 'Die Lösung: <em>beides</em>',
   f'<div style="display:flex;align-items:center;gap:24px">{igphone().replace("width:300px;height:520px","width:250px;height:440px")}<div style="display:flex;flex-direction:column;align-items:center;gap:6px"><div class="cap g">LINK IN BIO</div>{arrow(G,130)}</div>{site("ihr-betrieb.de",'<div class="btn">Anrufen</div><div class="btn o">Termin buchen</div>',340,360)}</div>',
   kicker="SO GEHT ES ZUSAMMEN", box="Instagram zeigt. Die Website bringt den Anruf."),
 cta(7, n, "CHECK", "Ich schicke Ihnen den 5-Punkte Website-Check als PDF.", "5-Punkte Website-Check"),
]

# ---------------- L: Tech-News (Fri 23) ----------------
n = 7
def lg(name, w, h, pad=0):
    return f'<div class="logo-w" style="width:{w}px;height:{h}px;padding:{pad}px">{logo_svg(name)}</div>'
def news(i, k, logos, h1, pills_, box):
    vis = f'<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center"><div class="tile" style="width:440px;height:300px;gap:30px">{logos}</div>' + pills(pills_) + '</div>'
    return slide(i, n, h1, vis, kicker=k, box=box, boxcls="o")
L = [
 slide(1, n, f'Tech-News der <em><span class="s">Woche</span>{und()}</em>',
   '<div style="position:relative;width:920px;height:100%">' + ''.join(f'<div class="logo-c" style="position:absolute;left:{x}px;top:{y}%;width:{w}px;height:{h}px;transform:rotate({r}deg);--c:{c};filter:drop-shadow(0 0 28px {c}88)">{logo_svg(name)}</div>' for name,x,y,w,h,r,c in [
     ("nvidia",40,6,230,150,-8,"#76B900"),("google",680,2,150,150,7,"#4285F4"),("apple",400,30,130,160,-4,"#F5F5F7"),
     ("anthropic",700,52,150,150,6,"#D97757"),("proofpoint",30,58,280,54,4,"#FFFFFF"),("varonis",320,82,250,42,-3,"#FFFFFF")]) + '</div>',
   kicker="KW 43 · 5 NEWS · 2 MINUTEN", box="Und was sie für kleine Betriebe bedeuten.", cover=True),
 news(2, "NEWS 1 VON 5 · NVIDIA", lg("nvidia",260,170), 'Nvidia: <em>96,2 Mrd. $</em> in einem Quartal',
   [("Rekord · Q2 (Aug. 2026)","left:14px;top:6%",-3),("+106 % zum Vorjahr","right:14px;top:24%",3),("KI-Deal mit dem Bund geplant","left:10px;bottom:6%",2)],
   "Für Sie: KI-Rechenleistung wird Grundversorgung, wie Strom."),
 news(3, "NEWS 2 VON 5 · DATENSICHERHEIT", lg("proofpoint",170,40) + f'<div style="font:700 50px Outfit;color:{G}">×</div>' + lg("varonis",160,30), 'Proofpoint kauft Varonis für <em>6,3 Mrd. $</em>',
   [("angekündigt 15.10.2026","left:14px;top:8%",-3),("komplett in bar","right:14px;top:28%",3),("Abschluss 1. Hälfte 2027","right:30px;bottom:8%",-2)],
   "Für Sie: Datenschutz wird Chefsache, auch bei Ihren Kunden."),
 news(4, "NEWS 3 VON 5 · APPLE", lg("apple",150,180), '12-Zoll-MacBook ist jetzt <em>obsolet</em>',
   [("seit 14.10.2026","left:14px;top:8%",-3),("keine Reparatur mehr bei Apple","right:14px;top:28%",3),("auch iPad 6 + BeatsX","left:20px;bottom:8%",2)],
   "Für Sie: Alte Firmengeräte prüfen. Gibt es noch Updates?"),
 news(5, "NEWS 4 VON 5 · ANTHROPIC", lg("anthropic",170,170), 'Anthropic: <em>16,8 Mrd. $</em> Quartalsumsatz',
   [("laut Financial Times","left:14px;top:8%",-3),("nicht offiziell bestätigt","right:14px;top:28%",3),("Börsengang evtl. im November","left:10px;bottom:8%",2)],
   "Für Sie: KI-Tools sind kein Experiment mehr, sondern Alltag."),
 news(6, "NEWS 5 VON 5 · GOOGLE", lg("google",170,170), 'Google zeigt in KI-Antworten <em>mehr Links</em>',
   [("seit 15.10.2026","left:14px;top:8%",-3),("Quellen-Box ganz oben","right:14px;top:28%",3),("AI Mode + AI Overviews","left:20px;bottom:8%",2)],
   "Für Sie: Klare Fakten auf Ihrer Website = Chance auf einen Link."),
 slide(7, n, 'Welche News betrifft <em>Sie</em> am meisten?',
   '<div style="display:flex;gap:18px">' + ''.join(f'<div class="tile" style="width:160px;height:210px;flex-direction:column;gap:16px"><div style="font:400 76px/1 Outfit">{k}</div>{lg(x,90,50)}</div>' for k,x in [("🚀","nvidia"),("🔐","proofpoint"),("💻","apple"),("🤖","anthropic"),("🔎","google")]) + '</div>',
   kicker="IHRE MEINUNG", box="Antworten Sie mit dem Emoji in den Kommentaren.", last=True),
]

# ---------------- H: Story (Sun 25), editorial ----------------
n = 5
YASS = ASSETS + "about/yass.png"
STORY = HERE + "dl/story.jpg"
def ed(i, h1, vis, kicker="", box="", boxcls="o", cover=False, last=False, photo=False, op=1):
    v, body = slide(i, n, h1, vis, kicker=kicker, box=box, boxcls=boxcls, cover=cover, last=last)
    if photo:
        body = body.replace('<div class="bg"></div>', f'<div style="position:absolute;inset:0;background:url(file://{STORY}) center 60%/cover;opacity:{op}"></div><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,10,7,.92) 0%,rgba(5,10,7,.55) 34%,rgba(5,10,7,.15) 55%,rgba(5,10,7,.75) 85%,rgba(5,10,7,.95) 100%)"></div>', 1)
    return "e", body
H = [
 ed(1, f'<span class="s">Ehrlich gesagt:</span> ich stehe <em>am Anfang.</em>',
   '<div></div>', kicker="EINE KURZE GESCHICHTE", cover=True, box="Schüler. Gewerbe. Freiberg.", photo=True),
 ed(2, f'Schüler. Und seit August ein <em>Gewerbe.</em>',
   f'<div style="display:flex;gap:24px">' + ''.join(f'<div class="card" style="width:280px;text-align:center;border-color:rgba(233,185,73,.5)"><div class="lab" style="color:#E9B949">{a}</div><div class="big">{b}</div></div>' for a,b in [("VORMITTAGS","Schule"),("NACHMITTAGS","Websites"),("ABENDS","Lernen")]) + '</div>',
   kicker="WER ICH BIN"),
 ed(3, f'Viele würden das <em><span class="s">verstecken.</span></em>',
   f'<div style="display:flex;flex-direction:column;gap:18px;width:760px">' + ''.join(f'<div class="card" style="display:flex;gap:22px;align-items:center;opacity:.75"><div class="num" style="color:#E06A4E">✕</div><div class="txt" style="color:{LIGHT}">{t}</div></div>' for t in ["„Über 20 Jahre Erfahrung“","Stockfotos vom „Team“","Große Worte, kleine Schrift"]) + '</div>',
   kicker="WAS ICH NICHT MACHE", box="Ich sage lieber gleich, wo ich stehe."),
 ed(4, f'Was Sie bei mir <em>bekommen</em>',
   f'<div style="display:flex;flex-direction:column;gap:18px;width:820px">' + ''.join(f'<div class="card" style="display:flex;gap:22px;align-items:center;border-color:rgba(233,185,73,.5)"><div class="num" style="color:#E9B949">✓</div><div class="txt" style="color:{LIGHT}">{t}</div></div>' for t in ["Ehrliche Antworten. Auch: „Das brauchen Sie nicht.“","Kurze Wege. Ich antworte selbst.","Den Preis kennen Sie, bevor ich anfange."]) + '</div>',
   kicker="WAS ICH STATTDESSEN MACHE"),
 ed(5, f'Wie war <em><span class="s">Ihr</span></em> Anfang?',
   f'<div style="font:400 58px/1.3 Serif;font-style:italic;color:#F3EBDD;max-width:780px">„Jeder fängt irgendwo an. Ich fange eben hier an, in Freiberg.“</div>',
   kicker="IHRE GESCHICHTE", box="Schreiben Sie es in die Kommentare. Ich lese jede Antwort.", last=True, photo=True, op=.45),
]

POSTS = {"K-nis2": K, "A-5-weitere-fehler": A, "E-7-schritte": E, "C-3-arten": C, "L-tech-news": L, "J-instagram-allein": J, "H-story-anfang": H}
