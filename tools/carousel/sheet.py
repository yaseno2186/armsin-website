import sys, glob
from PIL import Image
d=sys.argv[1]; out=sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 540
fs=sorted(glob.glob(f"out/{d}/*.png")); h=int(w*1.25); cols=4; rows=(len(fs)+cols-1)//cols
S=Image.new("RGB",(cols*w+(cols+1)*12,rows*h+(rows+1)*12),"#222")
for i,f in enumerate(fs):
    im=Image.open(f).convert("RGB").resize((w,h),Image.LANCZOS); S.paste(im,(12+(i%cols)*(w+12),12+(i//cols)*(h+12)))
S.save(out); print(S.size)
