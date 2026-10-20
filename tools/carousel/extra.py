import asyncio, os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.dirname(os.path.abspath(__file__))+"/build3.py").read()
src = src[:src.index("PROFIL = pdf_page")] + src[src.index("# ---------------- Google Business"):src.index("GS = {")]
src = src.replace('HERE = os.path.dirname(os.path.abspath(__file__)) + "/"', 'HERE = os.path.dirname(os.path.abspath(__file__)) + "/"')
exec(src)
PDF_CSS = PDF_CSS + ".it .ln{display:none} .items{gap:8px;margin-top:14px} .it{padding:10px 18px} .it h2{font-size:23px} .it p{font-size:17px;line-height:1.3} h1{font-size:44px} .sub{font-size:19px;margin-top:8px} .kick{margin-top:16px}"
OUT = os.path.dirname(os.path.abspath(__file__)) + "/out/"
NIS2 = pdf_page("GRATIS-SCHNELLCHECK · STAND OKT 2026", "NIS2: Betrifft es <em>Ihren Betrieb?</em>", "Teil 1: drei Fragen zur Betroffenheit. Teil 2: fünf Basics, die jeder Betrieb haben sollte.", [
 ("1 · Größe", "Haben Sie 50 oder mehr Mitarbeitende, oder über 10 Mio. € Jahresumsatz und Bilanzsumme? Wenn nein: meist nicht direkt betroffen."),
 ("2 · Branche", "Sind Sie z. B. in Energie, Gesundheit, Transport, Wasser, Lebensmittel, Produktion oder IT-Diensten tätig? Die genaue Liste steht im BSI-Gesetz."),
 ("3 · Lieferkette", "Liefern Sie an größere Firmen in diesen Branchen? Dann fragen die oft nach Ihren Sicherheits-Basics."),
 ("Basics: Zugänge", "Starke Passwörter, Passwort-Manager, Zwei-Faktor-Anmeldung für E-Mail, Bank und Website."),
 ("Basics: Backups + Updates", "Regelmäßige Backups, eins davon getrennt aufbewahrt, Wiederherstellung einmal getestet. Updates zeitnah einspielen."),
 ("Basics: Notfall", "Wer wird bei einem Vorfall angerufen? Nummer aufschreiben. Mitarbeitende kurz zu Phishing-Mails schulen."),
], "Allgemeine Orientierung, keine Rechtsberatung. Ob Ihr Betrieb betroffen ist, klären Sie im Zweifel mit dem BSI-Betroffenheitscheck oder einer Fachanwältin / einem Fachanwalt. Quellen: SECJUR, KCERT.")
SYSTEM = pdf_page("CHECKLISTE FÜR FREELANCER", "7 Schritte für <em>jede Kunden-Website</em>", "Abhaken, bevor Sie zum nächsten Schritt gehen. Mit Platz für Notizen.", [
 ("1 · Ziel festhalten", "Eine messbare Sache: mehr Anrufe, Termine oder Anfragen. Schriftlich."),
 ("2 · Fester Umfang", "Im Angebot: Seiten, Funktionen, Korrekturrunden. Und was nicht dabei ist."),
 ("3 · Inhalte zuerst", "Texte, Fotos, Logo, Impressum und Datenschutz liegen vor dem Design vor."),
 ("4 · Ein Entwurf", "Eine klickbare Startseite. Feedback gesammelt in einer Runde."),
 ("5 · Checkliste vor Livegang", "Handy, Ladezeit, Formulare, Kontraste, Links, Impressum, Cookie-Hinweis falls nötig."),
 ("6 · Übergabe", "Domain und Zugänge auf den Kunden. Kurze Anleitung: Texte ändern, wen anrufen."),
 ("7 · Nach 30 Tagen", "Kurz nachfragen: Ist das Ziel aus Schritt 1 erreicht? Was fehlt?"),
], "Meine Arbeitsweise als Vorlage. Passen Sie sie an Ihre Projekte an. Keine Rechtsberatung.")
GS = {
 "1-handy": gslide("WEBSITE-CHECK", "Klingelt Ihr Telefon <em>seltener?</em>", chk(["Auf dem Handy gut lesbar","Nummer mit einem Tipp anrufen","Öffnungszeiten überall gleich"])),
 "2-arten": gslide("IHRE WEBSITE", "Welche Website <em>passt zu Ihnen?</em>", chk(["Visitenkarte: Anruf-Knopf","Buchungsseite: Termine auch nachts","Antwortseite: Fragen schon geklärt"])),
 "3-instagram": gslide("SICHTBARKEIT", "Instagram ist gut. <em>Eine Website gehört Ihnen.</em>", chk(["Bei Google und in KI-Antworten","Unabhängig von Plattform-Regeln","Anruf und Termin mit einem Tipp"])),
}
async def main():
    from playwright.async_api import async_playwright
    from PIL import Image
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, body in [("GRATIS-NIS2-Schnellcheck", NIS2), ("GRATIS-Projekt-Checkliste", SYSTEM)]:
            pg = await b.new_page(viewport={"width":794,"height":1123})
            f = OUT+name+".html"; open(f,"w").write(f'<!doctype html><html><head><meta charset="utf-8"><style>{PDF_CSS}</style></head><body>{body}</body></html>')
            await pg.goto("file://"+f); await pg.wait_for_timeout(400)
            ov = await pg.evaluate("()=>{const p=document.querySelector('.page');const it=document.querySelector('.items');return [p.scrollHeight,p.clientHeight,it.scrollHeight,it.clientHeight]}")
            print(name, "overflow", ov, "OK" if ov[0]<=ov[1] and ov[2]<=ov[3]+1 else "OVERFLOW")
            await pg.pdf(path=OUT+name+".pdf", width="794px", height="1123px", print_background=True, margin={"top":"0","right":"0","bottom":"0","left":"0"}, page_ranges="1")
            await pg.screenshot(path=OUT+name+"-preview.png"); await pg.close()
        for k, body in GS.items():
            pg = await b.new_page(viewport={"width":1200,"height":900}, device_scale_factor=2)
            f = OUT+f"google-{k}.html"; open(f,"w").write(f'<!doctype html><html><head><meta charset="utf-8"><style>{GCSS}</style></head><body>{body}</body></html>')
            await pg.goto("file://"+f); await pg.wait_for_timeout(400)
            res = await pg.evaluate("""()=>{const e=[];const m=document.querySelector('.mid');
              const r=[...document.querySelectorAll('.tag,h1,.mid,.f')].map(x=>[x.className||x.tagName,x.getBoundingClientRect()]);
              for(let i=0;i<r.length;i++)for(let j=i+1;j<r.length;j++){const a=r[i][1],b=r[j][1];if(a.left<b.right-1&&b.left<a.right-1&&a.top<b.bottom-1&&b.top<a.bottom-1)e.push(r[i][0]+' x '+r[j][0]);}
              for(const [n,x] of r){if(x.left<79||x.right>1121||x.bottom>900)e.push('margin '+n);}
              if(m.scrollHeight>m.clientHeight+1)e.push('mid clipped');
              const h=document.querySelector('h1');const l=h.getBoundingClientRect().height/parseFloat(getComputedStyle(h).lineHeight);if(l>2.05)e.push('h1 lines '+l.toFixed(1));
              return e}""")
            png = OUT+f"google-{k}.png"; await pg.screenshot(path=png)
            im = Image.open(png).convert("RGB"); im.save(OUT+f"Google-{k}.jpg", quality=90, optimize=True)
            print("google", k, "PASS" if not res else "FAIL "+"; ".join(res), im.size, os.path.getsize(OUT+f"Google-{k}.jpg")//1024, "KB")
            await pg.close()
        await b.close()
asyncio.run(main())
