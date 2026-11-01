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
