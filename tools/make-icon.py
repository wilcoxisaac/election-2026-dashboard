import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
SS=2; W=1024*SS
RED=(191,10,48); WHITE=(255,255,255); NAVY=(0,40,104); BG=(10,31,68)
F='/home/claude/fonts/node_modules/@fontsource/inter/files/inter-latin-%s-normal.woff'
def star(d,cx,cy,r,fill):
    pts=[]
    for k in range(10):
        rr=r if k%2==0 else r*0.40
        a=-math.pi/2+k*math.pi/5; pts.append((cx+rr*math.cos(a),cy+rr*math.sin(a)))
    d.polygon(pts,fill=fill)
def flag(w,h):
    f=Image.new('RGB',(w,h),WHITE); d=ImageDraw.Draw(f); sh=h/13
    for i in range(0,13,2): d.rectangle([0,i*sh,w,(i+1)*sh],fill=RED)
    cw,ch=int(w*0.42),int(sh*7); d.rectangle([0,0,cw,ch],fill=NAVY)
    gx,gy=cw/12,ch/10
    for r in range(9):
        n=6 if r%2==0 else 5
        for c in range(n):
            star(d,gx*(2*c+1) if r%2==0 else gx*(2*c+2),gy*(r+1),gy*0.45,WHITE)
    # wave
    pad=int(h*0.12); out=Image.new('RGBA',(w,h+2*pad),(0,0,0,0)); src=f.load(); dst=out.load()
    for x in range(w):
        ph=2*math.pi*(x/w)*1.2+0.5; off=pad*0.9*math.sin(ph); shade=1+0.12*math.cos(ph)
        for y in range(h):
            p=src[x,y]; dst[x,int(y+pad+off)]=(min(255,int(p[0]*shade)),min(255,int(p[1]*shade)),min(255,int(p[2]*shade)),255)
    return out
img=Image.new('RGBA',(W,W),BG+(255,)); d=ImageDraw.Draw(img)
# subtle radial glow
glow=Image.new('L',(W,W),0); ImageDraw.Draw(glow).ellipse([W*.1,W*.05,W*.9,W*.75],fill=70)
glow=glow.filter(ImageFilter.GaussianBlur(W*.12)); lay=Image.new('RGBA',(W,W),(40,90,170,0)); lay.putalpha(glow); img=Image.alpha_composite(img,lay); d=ImageDraw.Draw(img)
def ctext(txt,size,weight,y,fill,track=0):
    font=ImageFont.truetype(F%weight,size)
    ws=[d.textbbox((0,0),ch,font=font) for ch in txt]; adv=[font.getlength(ch) for ch in txt]
    total=sum(adv)+track*(len(txt)-1); x=(W-total)/2
    bb=d.textbbox((0,0),txt,font=font)
    for ch,a in zip(txt,adv): d.text((x,y-bb[1]),ch,font=font,fill=fill); x+=a+track
    return bb[3]-bb[1]
# stars row
n=5; r=W*0.034; gap=W*0.105; y0=W*0.13
for i in range(n): star(d,W/2+(i-(n-1)/2)*gap,y0,r,WHITE)
# ELECTION
ctext("ELECTION",int(W*0.115),800,W*0.205,WHITE,track=int(W*0.018))
# flag
fw,fh=int(W*0.46),int(W*0.27); fl=flag(fw,fh)
sh=Image.new('RGBA',fl.size,(0,0,0,0)); sh.putalpha(fl.split()[3].point(lambda v:int(v*0.55))); sh=sh.filter(ImageFilter.GaussianBlur(W*0.012))
fx=(W-fw)//2; fy=int(W*0.345)
img.alpha_composite(sh,(fx,fy+int(W*0.015))); img.alpha_composite(fl,(fx,fy)); d=ImageDraw.Draw(img)
# 2026
ctext("2026",int(W*0.235),900,W*0.665,WHITE,track=int(W*0.004))
# solid line
lw=W*0.56; ly=W*0.885; lh=W*0.028
d.rounded_rectangle([(W-lw)/2,ly,(W+lw)/2,ly+lh],radius=lh/2,fill=RED)
final=img.convert('RGB').resize((1024,1024),Image.LANCZOS); final.save('icon2-1024.png')
for n_,name in [(180,'apple-touch-icon.png'),(192,'icon-192.png'),(512,'icon-512.png')]:
    final.resize((n_,n_),Image.LANCZOS).save('/home/claude/repo/'+name)
from PIL import ImageDraw as D
prev=Image.new('RGB',(600,400),(30,30,34))
for size,pos,rad in [(360,(20,20),80),(120,(420,30),27),(60,(450,200),13)]:
    s=final.resize((size,size),Image.LANCZOS); m=Image.new('L',(size,size),0); D.Draw(m).rounded_rectangle([0,0,size-1,size-1],radius=rad,fill=255); prev.paste(s,pos,m)
prev.save('preview2.png')
