import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np
from matplotlib.patches import Circle, Wedge, Polygon
OUT='/home/user/mathlockin/img/'
SH='#f6c99a'; ED='#c0392b'
def ax_(lim=5):
    f,a=plt.subplots(figsize=(3,3),dpi=110)
    a.set_xlim(-lim,lim); a.set_ylim(-lim,lim); a.set_aspect('equal')
    for s in a.spines.values(): s.set_visible(False)
    a.set_xticks([]); a.set_yticks([])
    return f,a
def axes(a,lim=5):
    a.annotate('',xy=(lim,0),xytext=(-lim,0),arrowprops=dict(arrowstyle='->',lw=1,color='k'),zorder=5)
    a.annotate('',xy=(0,lim),xytext=(0,-lim),arrowprops=dict(arrowstyle='->',lw=1,color='k'),zorder=5)
    a.text(lim-0.3,-0.6,'x'); a.text(0.25,lim-0.5,'y')
def save(f,name): f.tight_layout(pad=0.2); f.savefig(OUT+name); plt.close(f)
def bg(a,lim=5): a.add_patch(Polygon([(-lim,-lim),(lim,-lim),(lim,lim),(-lim,lim)],color=SH,alpha=.6,lw=0))
# 01: domains
f,a=ax_(); bg(a); axes(a); a.plot(0,0,'o',mfc='white',mec=ED,ms=8,zorder=6); a.set_title('R² \\ {(0,0)}  punctured plane',fontsize=9); save(f,'01/dom-a.png')
f,a=ax_(); bg(a); axes(a); a.axvline(-1.5,color=ED,ls='--',lw=2); a.axhline(-1.5,color=ED,ls='--',lw=2); a.text(-1.4,4.2,'x=−1',color=ED,fontsize=8); a.text(2.5,-1.3,'y=−1',color=ED,fontsize=8); a.set_title('plane minus lines x=−1, y=−1',fontsize=9); save(f,'01/dom-b.png')
f,a=ax_(); bg(a); axes(a); a.axhline(0,color=ED,ls='--',lw=2,zorder=7); a.set_title('R² minus the x-axis',fontsize=9); save(f,'01/dom-c.png')
f,a=ax_(); a.add_patch(Polygon([(-5,-5),(5,5),(-5,5)],color=SH,alpha=.6,lw=0)); axes(a); a.plot([-5,5],[-5,5],color=ED,lw=2); a.text(2.2,3.6,'y = x',color=ED,fontsize=9); a.text(-4,2.5,'y ≥ x',fontsize=10); a.set_title('closed half-plane y ≥ x',fontsize=9); save(f,'01/dom-e.png')
f,a=ax_(); bg(a); axes(a); a.axvline(0,color=ED,ls='--',lw=2,zorder=7); a.set_title('R² minus the y-axis',fontsize=9); save(f,'01/dom-i.png')
f,a=ax_(); a.add_patch(Circle((0,0),4,color=SH,alpha=.6,lw=0)); a.add_patch(Circle((0,0),4,fill=False,ec=ED,ls='--',lw=2)); axes(a); a.text(4.05,0.25,'4',fontsize=9); a.set_title('open disk x²+y² < 16',fontsize=9); save(f,'01/dom-j.png')
f,a=ax_(); a.add_patch(Circle((0,0),3,color=SH,alpha=.6,lw=0)); a.add_patch(Circle((0,0),3,fill=False,ec=ED,lw=2)); axes(a); a.text(3.05,0.25,'3',fontsize=9); a.set_title('closed disk x²+y² ≤ 9',fontsize=9); save(f,'01/dom-k.png')
f,a=ax_(3); a.add_patch(Wedge((0,0),2,-90,90,color=SH,alpha=.6,lw=0)); a.add_patch(Wedge((0,0),2,-90,90,fill=False,ec=ED,ls='--',lw=2)); axes(a,3); a.text(2.05,0.15,'2',fontsize=9); a.set_title('x > 0 and x²+y² < 4',fontsize=9); save(f,'01/dom-exam.png')
print('ok')
# 02: level curves
f,a=ax_(5); axes(a)
for c,col in [(1,'#bbb'),(2,'#999'),(3,'#777'),(4,'#555')]:
    a.add_patch(Circle((0,0),c,fill=False,ec=col,lw=1))
    a.text(c*0.71+0.05,c*0.71+0.05,f'{16-c*c}',fontsize=7,color=col)
a.set_title('level curves of 16 − x² − y²\n(label = height z₀)',fontsize=9); save(f,'02/lc-circles.png')
f,a=ax_(4); axes(a,4); a.add_patch(Circle((0,0),np.sqrt(10)*0.9,fill=False,ec=ED,lw=2)); a.plot(2*np.sqrt(2)*0.9,np.sqrt(2)*0.9,'ko',ms=4); a.text(2.6,1.3,'P',fontsize=9)
a.set_title('x² + y² = 10 (radius √10)',fontsize=9); save(f,'02/lc-a.png')
f,a=ax_(3); axes(a,3); a.axvline(1,color=ED,lw=2); a.axvline(-1,color=ED,lw=2); a.plot(1,0,'ko',ms=4); a.text(1.1,0.2,'P',fontsize=9)
a.set_title('x² − 1 = 0: lines x = ±1',fontsize=9); save(f,'02/lc-b.png')
f,a=ax_(3); axes(a,3); xs=np.linspace(-1.4,1.4,50); a.plot(xs,2*xs,color=ED,lw=2); a.plot(0,0,'o',mfc='white',mec=ED,ms=7,zorder=8); a.plot(1,2,'ko',ms=4); a.text(1.1,1.9,'P',fontsize=9)
a.set_title('y = 2x (origin not included)',fontsize=9); save(f,'02/lc-d.png')
print('ok2')
