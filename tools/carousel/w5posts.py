from w4posts import *   # helpers: pills, cta, term, bubble, bignum, RED, GOLD ...
POSTS = {}
# ================= A: ChatGPT schlauer machen =================
def chatcmp(bad, good):
    b = lambda lab, t, me, c, bg, bd: f'<div style="width:840px;text-align:left"><div class="lab" style="color:{c};margin-left:8px">{lab}</div><div style="background:{bg};border:2px solid {bd};border-radius:28px 28px 28px 8px;padding:24px 30px;font:400 34px/1.32 Outfit;color:{LIGHT if me else "#9FB3A6"}">{t}</div></div>'
    return '<div style="display:flex;flex-direction:column;gap:26px;align-items:center">' + b("✗ STATT", bad, False, "#E06A4E", "rgba(234,246,238,.04)", "rgba(234,246,238,.15)") + b("✓ BESSER", good, True, G, "#123222", "rgba(57,217,122,.6)") + '</div>'
n = 7
GPT = [
 slide(1, n, 'So machen Sie ChatGPT <em>schlauer</em>',
   '<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">'
   + f'''<div class="brow" style="width:700px"><div class="bar"><i></i><i></i><i></i><span>chat</span></div><div class="in" style="gap:18px">
<div style="align-self:flex-end;background:#123222;border:2px solid rgba(57,217,122,.6);border-radius:24px 24px 6px 24px;padding:18px 24px;font:400 32px/1.3 Outfit">Schreib mir einen Text.</div>
<div style="align-self:flex-start;background:rgba(234,246,238,.06);border-radius:24px 24px 24px 6px;padding:18px 24px;font:400 32px/1.3 Outfit;color:#9FB3A6">Gern! Worüber? Für wen? Wie lang? 🤷</div>
<div style="display:flex;gap:10px;align-items:center;margin-top:6px"><div style="flex:1;height:58px;border-radius:16px;border:2px solid rgba(234,246,238,.2)"></div><div style="width:58px;height:58px;border-radius:16px;background:{G}"></div></div></div></div>'''
   + pills([("5 Tipps","left:20px;top:4%",-4),("ohne Technik-Wissen","right:10px;bottom:6%",3)]) + '</div>',
   kicker="KI IM ALLTAG · 5 TIPPS", box="Die KI ist nicht dumm. Sie weiß nur nichts über Sie.", cover=True),
 slide(2, n, '1. <em>Kontext</em> geben', chatcmp("Schreib einen Instagram-Post.", "Ich habe ein Café in Freiberg. Schreib einen Instagram-Post über unseren neuen Kürbiskuchen. Zielgruppe: Studierende."),
   kicker="TIPP 1 VON 5", box="Wer, was, für wen. Drei Angaben machen den Unterschied.", boxcls="o"),
 slide(3, n, '2. Ein <em>Beispiel</em> zeigen', chatcmp("Schreib das lockerer.", "Schreib es so locker wie dieser Post von uns: „Montag? Kaffee hilft. Kuchen auch.“"),
   kicker="TIPP 2 VON 5", box="Ein Beispiel sagt mehr als zehn Adjektive.", boxcls="o"),
 slide(4, n, '3. <em>Format</em> vorgeben', chatcmp("Gib mir Ideen für Werbung.", "Gib mir 5 Ideen als Tabelle: Idee, Kosten, Aufwand in Stunden. Maximal 1 Satz pro Idee."),
   kicker="TIPP 3 VON 5", box="Liste, Tabelle, Länge: sagen Sie, wie es aussehen soll.", boxcls="o"),
 slide(5, n, '4. Erst <em>fragen</em> lassen', chatcmp("Plan meine Rabattaktion.", "Plan meine Rabattaktion. Stell mir vorher 3 Fragen, bevor du loslegst."),
   kicker="TIPP 4 VON 5", box="So holt die KI sich selbst, was ihr fehlt.", boxcls="o"),
 slide(6, n, '5. <em>Einmal</em> erklären, immer nutzen',
   f'''<div style="display:flex;flex-direction:column;gap:22px;width:860px"><div class="card"><div class="lab g">EINSTELLUNGEN → PERSONALISIERUNG</div><div class="txt" style="font-size:34px;color:#DCE7DF">„Ich führe ein Café in Freiberg. Schreib kurz, freundlich, per Sie. Keine Emojis in E-Mails.“</div></div>
<div style="display:flex;gap:16px;justify-content:center"><div class="chip"><span>✓</span>gilt für jeden Chat</div><div class="chip"><span>✓</span>jederzeit änderbar</div></div></div>''',
   kicker="TIPP 5 VON 5", box="Dann müssen Sie sich nicht jedes Mal neu vorstellen.", boxcls="o"),
 slide(7, n, 'Die Vorlage zum <em>Speichern</em>',
   f'''<div class="brow" style="width:840px"><div class="bar"><i></i><i></i><i></i><span>vorlage.txt</span></div><div class="in" style="gap:10px">''' + ''.join(
     f'<div style="font:400 30px/1.4 MonoR;color:{LIGHT};text-align:left"><span style="color:{G}">{k}</span> {v}</div>' for k, v in [("Ich bin:", "[Ihr Betrieb, Ort]"), ("Ich brauche:", "[Text, Plan, Idee]"), ("Für:", "[Zielgruppe]"), ("So soll es klingen:", "[Beispiel]"), ("Format:", "[Liste, Länge]"), ("Vorher:", "Stell mir 3 Fragen.")]) + '</div></div>',
   kicker="ZUM KOPIEREN", box="Wichtig: Ergebnisse immer gegenlesen. Und keine Kundendaten eingeben.", last=True),
]
POSTS["A-chatgpt-schlauer"] = GPT

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
