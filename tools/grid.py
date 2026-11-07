import sys; sys.path.insert(0,'/home/user/mathlockin/tools')
from pages import page_path
from PIL import Image, ImageDraw
pages=[int(x) for x in sys.argv[2:]]
sc=0.5
tiles=[]
for p in pages:
    im=Image.open(page_path(p)).convert('RGB')
    d=ImageDraw.Draw(im)
    for x in range(0,im.width,100):
        d.line([(x,0),(x,im.height)],fill=(255,0,0) if x%500==0 else (255,160,160),width=1)
        d.text((x+2,2),str(x),fill='red')
    for y in range(0,im.height,100):
        d.line([(0,y),(im.width,y)],fill=(0,0,255) if y%500==0 else (160,160,255),width=1)
        d.text((2,y+2),str(y),fill='blue')
    d.text((500,20),f'p{p}',fill='red')
    im=im.resize((int(im.width*sc),int(im.height*sc)))
    tiles.append(im)
W=sum(t.width for t in tiles); H=max(t.height for t in tiles)
out=Image.new('RGB',(W,H),'white'); x=0
for t in tiles: out.paste(t,(x,0)); x+=t.width
out.save(sys.argv[1])
