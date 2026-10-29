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
 slide(1, n, f'Läuft Ihre Website mit <em>PHP<span class="s">?</span>{circ(RED)}</em>',
   '<div style="position:relative;width:920px;height:100%;display:flex;align-items:center;justify-content:center">'
   + term([("$ status --sicherheit", "#8FB19B"), ("⚠ CVE-2026-109618", RED), ("⚠ CVE-2026-109619", RED), ("Name: PHP2Shell", LIGHT)], w=620)
   + pills([("seit 21.10.2026","left:10px;top:4%",-4),("WordPress & Shops","right:10px;top:16%",3),("Mainz: Seite offline","left:10px;bottom:4%",2)]) + '</div>',
   kicker="SICHERHEITSLÜCKE · OKTOBER 2026", box="2 Fragen an Ihren Hoster. Am besten heute.", cover=True),
 slide(2, n, 'Was ist <em>PHP2Shell</em>?',
   f'''<div style="display:flex;flex-direction:column;gap:28px;width:880px"><svg width="160" height="173" viewBox="0 0 120 130" style="filter:drop-shadow(0 0 30px rgba(224,106,78,.55));align-self:center"><path d="M30 58 V38 C30 20 44 8 60 8 C74 8 86 18 89 32" fill="none" stroke="#E06A4E" stroke-width="9" stroke-linecap="round"/><rect x="16" y="56" width="88" height="66" rx="14" fill="#1A0F0C" stroke="#E06A4E" stroke-width="6"/><path d="M60 74 L54 90 L64 94 L58 110" fill="none" stroke="#E06A4E" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>
<div class="card"><div class="lab g">KURZ ERKLÄRT</div><div class="big" style="font-size:46px">Zwei kritische Lücken in PHP. Angreifer können damit <em>Code auf Ihrem Server</em> ausführen.</div></div>
<div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap"><div class="chip"><span>1</span>Website übernehmen</div><div class="chip"><span>2</span>Kundendaten lesen</div><div class="chip"><span>3</span>weiter angreifen</div></div></div>''',
   kicker="ERST MAL KURZ ERKLÄRT", box="Die Updates gibt es schon. Sie müssen nur installiert sein.", boxcls="o"),
 slide(3, n, 'Bin ich <em>betroffen</em>?',
   '<div style="display:flex;flex-direction:column;gap:26px;width:880px">' + ''.join(
     f'<div class="card" style="display:flex;justify-content:space-between;align-items:center;gap:20px;padding:40px 38px"><div class="big" style="font-size:50px">{a}</div><div class="chip" style="flex:none;border-color:{c};color:{c}">{b}</div></div>'
     for a,b,c in [("WordPress-Seite","prüfen",RED),("Online-Shop mit PHP","prüfen",RED),("Website-Baukasten","kurz nachfragen",G)]) + '</div>',
   kicker="BETROFFEN? · 3 FÄLLE", box="Bei Baukästen kümmert sich meist der Anbieter. Fragen schadet nicht."),
 slide(4, n, '„Ist das <em>Update</em> installiert?“',
   bignum("01", bubble("Hallo, ist auf meinem Server das Notfall-Update gegen PHP2Shell schon installiert?")),
   kicker="FRAGE 1 VON 2 · AN IHREN HOSTER", box="Kopieren, einfügen, abschicken."),
 slide(5, n, '„Läuft es auch <em>wirklich</em>?“',
   bignum("02", bubble("Welche PHP-Version läuft jetzt aktiv auf meiner Seite, und ist sie gepatcht?") + '<div class="txt" style="font-size:28px;color:#8FB19B">Rat von Thomas Boele (Check Point), laut web.de</div>'),
   kicker="FRAGE 2 VON 2 · NACHPRÜFEN", box="„Vertrauen ist gut, Kontrolle ist besser.“"),
 cta(6, n, "CHECK", "Ich schicke Ihnen meinen 5-Punkte Website-Check als PDF.", "5-Punkte Website-Check"),
]
POSTS = {"A-php2shell": PHP}
