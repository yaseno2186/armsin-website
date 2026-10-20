import asyncio, sys
from posts import POSTS
from lib3 import render, HERE
sel = sys.argv[1:] or list(POSTS)
async def main():
    ok = True
    for k in sel: ok &= await render(k, POSTS[k], HERE + "out/")
    print("ALL PASS" if ok else "SOME FAIL")
asyncio.run(main())
