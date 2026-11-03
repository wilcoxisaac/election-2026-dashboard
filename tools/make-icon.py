import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
S=1024; SS=2; W=S*SS
RED=(191,10,48); WHITE=(255,255,255); NAVY=(0,40,104)
# flat flag on oversized canvas
flag=Image.new('RGB',(W,W),WHITE); d=ImageDraw.Draw(flag)
sh=W/13
for i in range(13):
    if i%2==0: d.rectangle([0,i*sh,W,(i+1)*sh],fill=RED)
cw,chh=int(W*0.5),int(sh*7)
d.rectangle([0,0,cw,chh],fill=NAVY)
def star(cx,cy,r,fill):
    pts=[]
    for k in range(10):
        rr=r if k%2==0 else r*0.382
        a=-math.pi/2+k*math.pi/5
        pts.append((cx+rr*math.cos(a),cy+rr*math.sin(a)))
    d.polygon(pts,fill=fill)
# 50 stars: 9 rows alternating 6/5
rows=9; gx=cw/12; gy=chh/10
for r in range(rows):
    n=6 if r%2==0 else 5
    for c in range(n):
        x=gx*(2*c+1) if r%2==0 else gx*(2*c+2)
        star(x,gy*(r+1),gy*0.42,WHITE)
# gentle wave: vertical displacement + shading
wave=Image.new('RGB',(W,W)); src=flag.load(); dst=wave.load()
amp=W*0.018
import array
for x in range(W):
    off=amp*math.sin(2*math.pi*(x/W)*1.15+0.6)
    shade=1+0.10*math.cos(2*math.pi*(x/W)*1.15+0.6)
    for y in range(W):
        yy=int(y-off*(0.4+0.6*y/W))
        if yy<0: yy=0
        if yy>=W: yy=W-1
        p=src[x,yy]; dst[x,y]=(min(255,int(p[0]*shade)),min(255,int(p[1]*shade)),min(255,int(p[2]*shade)))
img=wave.convert('RGBA')
# bottom vignette for legibility
grad=Image.new('L',(1,W))
for y in range(W): grad.putpixel((0,y),int(170*max(0,(y/W-0.38)/0.62)**1.4))
dark=Image.new('RGBA',(W,W),(0,20,60,0)); dark.putalpha(grad.resize((W,W)))
img=Image.alpha_composite(img,dark)
# 2026 text
font=ImageFont.truetype('/home/claude/fonts/node_modules/@fontsource/inter/files/inter-latin-900-normal.woff',int(W*0.30))
txt="2026"
tmp=ImageDraw.Draw(img); bb=tmp.textbbox((0,0),txt,font=font,stroke_width=0)
tw,th=bb[2]-bb[0],bb[3]-bb[1]
tx=(W-tw)/2-bb[0]; ty=W*0.60-bb[1]
shadow=Image.new('RGBA',(W,W),(0,0,0,0)); sd=ImageDraw.Draw(shadow)
sd.text((tx,ty+W*0.014),txt,font=font,fill=(0,10,40,200),stroke_width=int(W*0.018),stroke_fill=(0,10,40,200))
shadow=shadow.filter(ImageFilter.GaussianBlur(W*0.012))
img=Image.alpha_composite(img,shadow)
td=ImageDraw.Draw(img)
td.text((tx,ty),txt,font=font,fill=WHITE,stroke_width=int(W*0.014),stroke_fill=NAVY)
final=img.convert('RGB').resize((S,S),Image.LANCZOS)
final.save('/home/claude/icon-1024.png')
for n,name in [(180,'apple-touch-icon.png'),(192,'icon-192.png'),(512,'icon-512.png')]:
    final.resize((n,n),Image.LANCZOS).save('/home/claude/repo/'+name)
final.resize((64,64),Image.LANCZOS).save('/home/claude/icon-64.png')
