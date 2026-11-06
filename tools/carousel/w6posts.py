from w5posts import iphone, note, arrow  # noqa
from w4posts import *   # helpers: pills, bignum, RED, GOLD ...
POSTS = {}
# ================= T: Tech-News Montag KW 45 · Google KI-Suche (Mon 2 Nov) =================
GB, GR, GY, GG = "#4285F4", "#EA4335", "#FBBC05", "#34A853"
def gword(size=64):
    c = [GB, GR, GY, GB, GG, GR]
    w = int(size * 3.45)
    sp = ''.join(f'<tspan fill="{k}">{ch}</tspan>' for ch, k in zip("Google", c))
    return f'<svg width="{w}" height="{int(size*1.15)}" viewBox="0 0 {w} {int(size*1.15)}" style="flex:none"><text x="0" y="{int(size*.88)}" font-family="Outfit" font-weight="700" font-size="{size}">{sp}</text></svg>'
def gbar(q):
    return f'<div style="height:58px;flex:none;border-radius:29px;background:#1F2421;border:2px solid #343B37;display:flex;align-items:center;gap:12px;padding:0 20px;font:400 24px/1 Inter;color:#E8EDEA;white-space:nowrap;overflow:hidden">🔍 {q}</div>'
def gtabs(active):
    t = ["KI-Modus", "Alle", "Bilder", "Maps"]
    return '<div style="display:flex;gap:18px;font:600 22px/1 Inter;flex:none">' + ''.join(
        f'<span style="padding-bottom:8px;{"color:#8AB4F8;border-bottom:3px solid #8AB4F8" if x == active else "color:#9AA0A6"}">{x}</span>' for x in t) + '</div>'
def link(w1=88, w2=70):
    return f'<div style="display:flex;flex-direction:column;gap:8px"><div style="display:flex;align-items:center;gap:10px"><div style="width:30px;height:30px;border-radius:50%;background:#3A403C"></div><div class="ln" style="width:45%;height:12px"></div></div><div style="height:18px;width:{w1}%;border-radius:9px;background:#8AB4F8;opacity:.85"></div><div class="ln" style="width:{w2}%;height:12px"></div></div>'
def ai_box(ad=False):
    adc = f'''<div style="border:3px solid {GOLD};border-radius:16px;padding:14px 16px;background:rgba(233,185,73,.10);box-shadow:0 0 30px rgba(233,185,73,.35);display:flex;flex-direction:column;gap:8px">
<div style="font:700 22px/1 Inter;color:{GOLD}">Gesponsert</div><div style="display:flex;gap:12px;align-items:center"><div style="width:70px;height:70px;border-radius:12px;background:#3A403C;flex:none"></div><div style="flex:1;display:flex;flex-direction:column;gap:8px"><div class="ln" style="width:90%;height:12px"></div><div class="ln" style="width:60%;height:12px"></div></div></div></div>''' if ad else ""
    return f'''<div style="border-radius:20px;background:linear-gradient(160deg,#1B2340,#151A17 60%);border:2px solid #2E3A5E;padding:18px;display:flex;flex-direction:column;gap:12px">
<div style="display:flex;align-items:center;gap:10px;font:700 22px/1 Inter;color:#C6D4FF"><span style="font-size:26px">✦</span>KI-Antwort</div>
<div class="ln" style="width:96%;height:12px;background:rgba(232,237,234,.35)"></div><div class="ln" style="width:88%;height:12px;background:rgba(232,237,234,.35)"></div><div class="ln" style="width:92%;height:12px;background:rgba(232,237,234,.35)"></div>{adc}
<div style="display:flex;gap:8px;flex-wrap:wrap">{"".join('<div style="border-radius:999px;background:#262D29;padding:7px 12px;font:400 22px/1 Inter;color:#9AA0A6">Quelle</div>' for _ in range(2))}</div></div>'''
def gpage(q, mode="ai", ad=False):
    body = (ai_box(ad) + '<div style="opacity:.45;display:flex;flex-direction:column;gap:20px">' + link() + '</div>') if mode == "ai" else ''.join(link(88 - i * 6, 70 - i * 5) for i in range(5))
    return f'''<div style="background:#101412;height:100%;padding:60px 20px 20px;display:flex;flex-direction:column;gap:18px">
<div style="display:flex;justify-content:center">{gword(44)}</div>{gbar(q)}{gtabs("KI-Modus" if mode == "ai" else "Alle")}{body}</div>'''
def chip(t, c=G):
    return f'<div class="chip" style="border-color:{c};white-space:nowrap">{t}</div>'
def tilechip(lab, val, c=G):
    return f'<div class="card" style="padding:20px 26px;border-color:{c}"><div class="lab" style="color:{c}">{lab}</div><div class="big" style="font-size:44px">{val}</div></div>'
def chart():
    return f'''<svg width="760" height="330" viewBox="0 0 760 330" style="flex:none">
<defs><linearGradient id="gf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E06A4E" stop-opacity=".35"/><stop offset="1" stop-color="#E06A4E" stop-opacity="0"/></linearGradient></defs>
<g stroke="rgba(234,246,238,.10)" stroke-width="2"><path d="M0 60H760M0 140H760M0 220H760M0 300H760"/></g>
<path d="M0 120 L80 104 L150 112 L220 92 L300 98 L380 80 L440 86 L470 84 L500 250 L560 238 L630 256 L700 246 L760 252 L760 330 L0 330Z" fill="url(#gf)"/>
<path d="M0 120 L80 104 L150 112 L220 92 L300 98 L380 80 L440 86 L470 84" fill="none" stroke="#39D97A" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M470 84 L500 250 L560 238 L630 256 L700 246 L760 252" fill="none" stroke="#E06A4E" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="470" cy="84" r="11" fill="#39D97A"/><circle cx="500" cy="250" r="11" fill="#E06A4E"/></svg>'''
n = 7
T45 = [
 slide(1, n, 'Google gibt zu: KI-Suche <em>verdient weniger</em>',
   '<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">'
   + iphone(gpage("Friseur in der Nähe mit Termin heute", "ai", ad=True), .74)
   + f'<div class="tile" style="position:absolute;left:16px;top:7%;width:290px;height:124px;transform:rotate(-5deg)">{gword(66)}</div>'
   + pills([("Quartalszahlen 28.10.", "right:10px;top:8%", 4), ("Aktie zeitweise -12 %", "left:10px;bottom:22%", -3), ("Werbung im KI-Modus", "right:10px;bottom:8%", 3)]) + '</div>',
   kicker="TECH-NEWS MONTAG · KW 45", box="Was das für Ihre Sichtbarkeit bei Google bedeutet.", cover=True),
 slide(2, n, 'Was am <em>28.10.</em> passiert ist',
   f'''<div style="display:flex;flex-direction:column;gap:26px;width:880px">
<div class="card" style="position:relative;padding:34px 40px"><div class="lab g">GOOGLE IN DER TELEFONKONFERENZ</div><div class="txt" style="font-size:40px;color:#EAF6EE;line-height:1.3">„Der KI-Modus wächst stark. Weil wir dort weniger verdienen, hat sich das ausgewirkt.“</div>
<div style="font:400 24px/1.3 Inter;color:#8FB19B;margin-top:16px">Philipp Schindler, Chief Business Officer · sinngemäß übersetzt</div></div>
<div style="display:flex;gap:22px">{tilechip("SUCHE · UMSATZ", "+12 %")}{tilechip("ERWARTET", "mehr", RED)}{tilechip("ANFRAGEN-WACHSTUM", "5-Jahres-Hoch", G)}</div>
<div style="font:400 24px/1.3 Inter;color:#8FB19B;text-align:left">Quellen: Alphabet-Quartalszahlen Q3 · The Next Web, 29.10.2026</div></div>''',
   kicker="NEWS · GOOGLE", box="Mehr Leute fragen die KI. Aber dort verdient Google noch weniger.", boxcls="o"),
 slide(3, n, 'Ein Tag, <em>511 Mrd. $</em> weg',
   f'''<div style="display:flex;flex-direction:column;align-items:center;gap:20px"><div style="position:relative">{chart()}
<div style="position:absolute;left:330px;top:-6px;font:400 26px/1 Pix;color:{G}">28.10.</div>
<div style="position:absolute;left:520px;top:280px;font:400 26px/1 Pix;color:{RED}">29.10.</div></div>
<div style="display:flex;gap:22px">{tilechip("ALPHABET-AKTIE", "zeitweise -12 %", RED)}{tilechip("BÖRSENWERT", "-511 Mrd. $", RED)}</div></div>''',
   kicker="BÖRSE · 29.10.2026", box="Zeitweise der größte Tagesverlust in Googles Geschichte.", boxcls="o"),
 slide(4, n, 'KI-Modus: <em>Antwort</em> statt Links',
   '<div style="display:flex;flex-direction:column;align-items:center;gap:12px"><div style="display:flex;align-items:flex-end;justify-content:center;gap:60px">'
   + '<div style="display:flex;flex-direction:column;align-items:center;gap:12px;opacity:.7">' + iphone(gpage("Friseur Freiberg", "classic"), .56) + '<div class="cap">KLASSISCH</div></div>'
   + arrow(G, 90)
   + '<div style="display:flex;flex-direction:column;align-items:center;gap:12px">' + iphone(gpage("Welcher Friseur in Freiberg hat heute frei?", "ai"), .56) + '<div class="cap g">KI-MODUS</div></div></div>'
   + '<div style="display:flex;gap:18px">' + chip("Fragen sind 3× länger") + chip("in Deutschland seit 2025") + '</div></div>',
   kicker="SO SIEHT ES AUS", box="Kunden lesen die Antwort direkt bei Google. Ihre Website ist eine der Quellen."),
 slide(5, n, 'Jetzt kommt <em>Werbung</em> in die KI-Antwort',
   '<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">'
   + iphone(gpage("Bester Friseur für Locken?", "ai", ad=True), .74)
   + note("Anzeige", 30, 300, GOLD, -6, "left:120px;top:48px", 200)
   + pills([("10 weitere Länder", "right:12px;top:6%", 3), ("USA: auch in Folgefragen", "right:12px;top:44%", -2), ("UK, Brasilien, Mexiko: bis Jahresende", "left:12px;bottom:4%", 2)]) + '</div>',
   kicker="WERBUNG · KI-MODUS", box="Google will dort mehr verdienen. Mit mehr Anzeigen.", boxcls="o"),
 slide(6, n, 'Was Sie <em>jetzt</em> tun können',
   '<div style="display:flex;flex-direction:column;gap:22px;width:880px">' + ''.join(
     f'<div class="card" style="display:flex;gap:26px;align-items:center;padding:26px 32px"><div class="num" style="font-size:46px;flex:none;width:60px">{k}</div><div style="text-align:left"><div class="big" style="font-size:44px">{h}</div><div class="txt" style="font-size:32px">{t}</div></div></div>'
     for k, h, t in [("1", "Google-Profil pflegen", "Öffnungszeiten, Fotos und Leistungen aktuell halten."),
                     ("2", "Klare Antworten auf der Website", "Preise, Ort und häufige Fragen gut lesbar."),
                     ("3", "Bewertungen sammeln", "Kunden vergleichen, bevor sie anrufen.")]) + '</div>',
   kicker="FÜR KLEINE BETRIEBE", box="Wer gut beschrieben ist, wird eher als Quelle gezeigt.", boxcls="o"),
 slide(7, n, 'Wie finden <em>Kunden</em> Sie heute?',
   '<div style="display:flex;gap:22px">' + ''.join(
     f'<div class="tile" style="width:200px;height:240px;flex-direction:column;gap:18px"><div style="font:400 84px/1 Outfit">{e}</div><div style="font:700 28px/1 Outfit;color:{LIGHT}">{t}</div></div>'
     for e, t in [("🔎", "Google"), ("🤖", "KI-Chat"), ("🗣️", "Empfehlung"), ("📱", "Instagram")]) + '</div>',
   kicker="IHRE MEINUNG", box="Antworten Sie mit dem Emoji in den Kommentaren.", last=True),
]
POSTS["T-tech-news-kw45-google"] = T45

# ================= F: Tech-News KW 45 (Fri 6 Nov) =================
def tile_logo(inner, w=520, h=340):
    return f'<div class="tile" style="width:{w}px;height:{h}px;gap:30px;flex-direction:column">{inner}</div>'
def pixbig(t, c=G, s=120, fam="Pix"):
    return f'<div style="font:{"700" if fam=="Mono" else "400"} {s}px/1 {fam};color:{c};text-shadow:0 0 40px {c}99;white-space:nowrap">{t}</div>'
def fnews(i, k, inner, h1, pills_, box):
    vis = f'<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">{tile_logo(inner)}' + pills(pills_) + '</div>'
    return slide(i, 7, h1, vis, kicker=k, box=box, boxcls="o")
oai = f'<div class="logo-c" style="width:300px;height:82px;--c:#FFFFFF">{logo_svg("openai")}</div>'
router = f'''<svg width="220" height="150" viewBox="0 0 220 150" fill="none" stroke="{G}" stroke-width="6" stroke-linecap="round"><rect x="10" y="70" width="200" height="60" rx="14"/><path d="M60 70 L40 10 M160 70 L180 10"/><circle cx="50" cy="100" r="6" fill="{G}"/><circle cx="75" cy="100" r="6" fill="{G}"/><circle cx="100" cy="100" r="6" fill="#E06A4E" stroke="#E06A4E"/></svg>'''
P = [(t, pos, r) for t, pos, r in []]
F45 = [
 slide(1, 7, f'Tech-News der <em><span class="s">Woche</span>{und()}</em>',
   '<div style="position:relative;width:920px;height:100%">'
   + flo(gword(110), 40, 8, -6, "#4285F4")
   + flo(oai, 520, 10, 5, "#FFFFFF")
   + flo(pixbig(".de", G, 150, "Mono"), 360, 36, -3, G)
   + flo(router, 640, 54, 6, G)
   + flo(f'<div style="font:400 120px/1 Outfit">⚖️</div>', 90, 56, -4, "#E9B949") + '</div>',
   kicker="KW 45 · 5 NEWS · 2 MINUTEN", box="Und was sie für kleine Betriebe bedeuten.", cover=True),
 fnews(2, "NEWS 1 VON 5 · EU-GERICHT", gword(120) + '<div style="font:400 80px/1 Outfit">⚖️</div>', 'KI-Chatbots können <em>Presserechte</em> verletzen',
   [("Gutachten EuGH · 3.11.2026", "left:8px;top:3%", -3), ("Fall: Google Gemini", "right:10px;bottom:22%", 3), ("noch kein Urteil", "left:8px;bottom:4%", 2)],
   "Für Sie: KI darf nicht einfach abschreiben. Auch nicht Ihre Website."),
 fnews(3, "NEWS 2 VON 5 · DEUTSCHLAND", pixbig("KI 2030", G, 84), 'Merz will <em>KI-Nation</em> bis 2030',
   [("Digital-Gipfel · 2.–3.11.", "left:8px;top:3%", -3), ("90 % der Bundesbehörden mit KI", "right:10px;bottom:22%", 3), ("neue Taskforce", "left:8px;bottom:4%", 2)],
   "Für Sie: Behörden werden digitaler. Ihr Betrieb sollte mithalten."),
 fnews(4, "NEWS 3 VON 5 · SICHERHEIT", router, '3 Fritzboxen ohne <em>Update-Garantie</em>',
   [("7582 · 5490 · 4020", "left:8px;top:3%", -3), ("Mindest-Support endet 10/2026", "right:10px;bottom:22%", 3), ("Modell: Etikett hinten", "left:8px;bottom:4%", 2)],
   "Für Sie: Router im Laden prüfen. Alte Technik ist ein Einfallstor."),
 fnews(5, "NEWS 4 VON 5 · OPENAI", oai, 'ChatGPT Bilder können jetzt <em>GIFs</em>',
   [("Images 2.6 · 5.11.2026", "left:8px;top:3%", -3), ("Referenzbilder speichern", "right:10px;bottom:22%", 3), ("genauer bearbeiten", "left:8px;bottom:4%", 2)],
   "Für Sie: Kleine Animationen für Instagram, ohne Designer."),
 fnews(6, "NEWS 5 VON 5 · INTERNET", pixbig(".de", G, 170, "Mono"), 'Die .de-Domain wird <em>40</em>',
   [("seit 5.11.1986", "left:8px;top:3%", -3), ("18 Mio. .de-Adressen", "right:10px;bottom:22%", 3), ("1988 waren es 6", "left:8px;bottom:4%", 2)],
   "Für Sie: Eine eigene .de-Adresse schafft Vertrauen bei Kunden."),
 slide(7, 7, 'Welche News betrifft <em>Sie</em> am meisten?',
   '<div style="display:flex;gap:18px">' + ''.join(f'<div class="tile" style="width:160px;height:210px;flex-direction:column;gap:16px"><div style="font:400 76px/1 Outfit">{e}</div><div style="font:700 26px/1 Outfit;color:{LIGHT}">{t}</div></div>' for e, t in [
     ("⚖️", "Recht"), ("🇩🇪", "KI-Land"), ("📶", "Router"), ("🎨", "Bilder"), ("🌐", ".de")]) + '</div>',
   kicker="IHRE MEINUNG", box="Antworten Sie mit dem Emoji in den Kommentaren.", last=True),
]
POSTS["F-tech-news-kw45"] = F45
