import sys, json, subprocess
sys.path.insert(0,'/home/user/mathlockin/tools')
from pages import page_path
from PIL import Image
import numpy as np
from scipy import ndimage
COLS={'peach':(255,229,204),'green':(204,255,204)}
def pdfinfo(book):
    if book<=93: return '/home/user/mathlockin/src/math20290_2026_2-1-99.pdf', book+6
    return '/home/user/mathlockin/src/math20290_2026_2-100-136.pdf', book-93
out=[]
for book in range(1,131):
    try: im=Image.open(page_path(book)).convert('RGB')
    except FileNotFoundError: continue
    a=np.array(im).astype(int)
    # find lavender colour too: detect any pastel fill where pixel != white and is light & frequent
    cands=dict(COLS)
    flat=a.reshape(-1,3)
    vals,counts=np.unique(flat[::3],axis=0,return_counts=True)
    for v,c in zip(vals,counts):
        v=tuple(int(x) for x in v)
        if c>3000 and min(v)>=190 and v!=(255,255,255) and max(v)-min(v)>=20 and v not in cands.values():
            cands['c%s'%(v,)]=v
    for name,col in cands.items():
        m=np.all(a==col,axis=2)
        m=ndimage.binary_closing(m,iterations=4)
        lab,n=ndimage.label(m)
        for sl in ndimage.find_objects(lab):
            y0,y1=sl[0].start,sl[0].stop; x0,x1=sl[1].start,sl[1].stop
            if (y1-y0)<30 or (x1-x0)<200: continue
            if (y1-y0)*(x1-x0)>0.8*a.shape[0]*a.shape[1]: continue
            pdf,pg=pdfinfo(book)
            s=130/72
            t=subprocess.run(['pdftotext','-f',str(pg),'-l',str(pg),'-x',str(int(x0/s)),'-y',str(int(y0/s)),'-W',str(int((x1-x0)/s)),'-H',str(int((y1-y0)/s)),pdf,'-'],capture_output=True,text=True).stdout
            first=' '.join(t.split())[:90]
            out.append(dict(book=book,col=name,box=[x0,y0,x1,y1],text=first))
json.dump(out,open('/home/user/mathlockin/src/boxes.json','w'),indent=0)
for o in out: print(o['book'],o['col'][:6],o['box'],o['text'])
