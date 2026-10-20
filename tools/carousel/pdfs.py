import asyncio, glob
from playwright.async_api import async_playwright
from pypdf import PdfWriter
from lib3 import JS_FIT
OUT="out/"
POSTS={"K-nis2":"LinkedIn-NIS2.pdf","E-7-schritte":"LinkedIn-7-Schritte.pdf","C-3-arten":"LinkedIn-3-Arten-Websites.pdf","L-tech-news":"LinkedIn-Tech-News-KW43.pdf"}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1080,"height":1350})
        for d,name in POSTS.items():
            w=PdfWriter(); parts=[]
            for h in sorted(glob.glob(OUT+d+"/*.html")):
                await pg.goto("file://"+__import__('os').path.abspath(h)); await pg.wait_for_timeout(400); await pg.evaluate(JS_FIT)
                f=h.replace(".html",".pdf"); await pg.pdf(path=f,width="1080px",height="1350px",print_background=True,margin={"top":"0","right":"0","bottom":"0","left":"0"},page_ranges="1"); w.append(f)
            w.write(OUT+name); print(name, len(w.pages))
        await b.close()
asyncio.run(main())
