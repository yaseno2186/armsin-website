import asyncio, glob, os, sys
from playwright.async_api import async_playwright
from pypdf import PdfWriter
from lib3 import JS_FIT
async def main(d, name):
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1080,"height":1350})
        w=PdfWriter()
        for h in sorted(glob.glob(f"{d}/*.html")):
            await pg.goto("file://"+os.path.abspath(h)); await pg.wait_for_timeout(400); await pg.evaluate(JS_FIT)
            f=h.replace(".html",".pdf"); await pg.pdf(path=f,width="1080px",height="1350px",print_background=True,margin={"top":"0","right":"0","bottom":"0","left":"0"},page_ranges="1"); w.append(f)
        w.write(name); print(name, len(w.pages))
        await b.close()
asyncio.run(main(sys.argv[1], sys.argv[2]))
