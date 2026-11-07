"""Crop slide snippets: figures (manual boxes) and coloured boxes (auto, by page + text)."""
import sys, json, os
sys.path.insert(0,'/home/user/mathlockin/tools')
from pages import page_path
from PIL import Image, ImageChops
ROOT='/home/user/mathlockin'
BOXES=json.load(open(f'{ROOT}/src/boxes.json'))
def auto(page, text):
    for b in BOXES:
        if b['book']==page and text.lower() in b['text'].lower(): return b['box']
    raise SystemExit(f'no box p{page} {text!r}')
# name -> (page, box or text)
SPEC = {
 '01': {
   'p5-domain': (5,[120, 496, 955, 783]),
   'p5-def': (5,'Definition 1.4'),
   'p6-natural': (6,'division by zero'),
   'p1-sets': (1,'N = {1'),
 },
 '02': {
   'p10-def': (10,[145,124,930,389]),
   'p10-contour': (10,[120, 399, 977, 746]),
   'p11-sin': (11,[140, 260, 860, 640],False),
   'p11-sphere': (11,[146, 765, 972, 1084]),
   'p12-key': (12,'Implicit equations of two variables'),
   'p13-spheres': (13,[120, 114, 950, 504]),
 },
 '03': {
   'p14-limit': (14,[120, 120, 961, 504]),
   'p14-twopath': (14,'Two-Path Test'),
   'p15-cont': (15,'Definition 1.34'),
   'p16-sub': (16,'Limits of continuous functions'),
   'p16-pinched': (16,[120, 695, 977, 1090]),
 },
 '04': {
   'p20-geom': (20,[227, 571, 896, 1063]),
   'p21-method': (21,'Method for Finding Partial'),
   'p21-plane': (21,[318, 469, 810, 896]),
   'p21-prop': (21,'Proposition 2.5'),
 },
 '05': {
   'p23-rule12': (23,'Rule “1-2”'),
   'p23-rule21': (23,'0r dx 0r'),
   'p23-rule32': (23,'Rule “3-2”'),
 },
 '06': {
   'p26-method': (26,'Method of Implicit Partial'),
   'p28-thm': (28,'Theorem 2.22'),
 },
 '07': {
   'p29-approx': (29,'For sufficiently small'),
   'p30-def': (30,'Definition 2.28'),
   'p30-power': (30,'Theorem 2.30'),
   'p31-lin': (31,'Definition 2.33'),
   'p31-idea': (31,'The basic idea'),
   'p31-fig': (31,[120, 1103, 977, 1504]),
 },
 '08': {
   'p33-grad': (33,'Definition 3.1'),
   'p34-fig': (34,[120, 351, 977, 783]),
   'p34-signs': (34,'Let P0'),
   'p35-thm': (35,'Theorem 3.4'),
   'p36-thm': (36,'Theorem 3.7'),
   'p37-fig': (37,[130, 501, 972, 1133]),
   'p38-fig': (38,[120, 727, 977, 1144]),
   'p41-fig': (41,[141, 146, 934, 746]),
   'p41-3d': (41,'zero change if we move'),
   'p41-props': (41,'a. Compute'),
 },
 '09': {
   'p39-fig': (39,[315, 940, 780, 1260],False),
   'p39-thm': (39,'Theorem 3.9'),
   'p40-cor': (40,'Corollary 3.11'),
   'p40-summary': (40,'Let z = f (x, y) be a differentiable'),
   'p42-fig': (42,[115, 1075, 960, 1395],False),
   'p43-thm': (43,'Theorem 3.16'),
   'p44-implicit': (44,'S : F (x, y, z) = 0'),
   'p44-explicit': (44,'S : z = f (x, y)'),
 },
 '10': {
   'p47-def': (47,'Definition 4.1'),
   'p48-hess': (48,'Definition 4.4'),
   'p49-clairaut': (49,'Theorem 4.5'),
   'p55-jac': (55,'Definition 5.1'),
   'p56-thm': (56,'Theorem 5.3'),
 },
 '11': {
   'p65-fig': (65,[335, 870, 750, 1245],False),
   'p68-fig': (68,[120, 114, 977, 482]),
   'p69-crit': (69,'Definition 6.13'),
   'p69-thm': (69,'Theorem 6.14'),
   'p70-saddle': (70,[185, 835, 840, 1228],False),
   'p70-def': (70,'Definition 6.17'),
   'p71-test': (71,'Theorem 6.18'),
   'p71-fig': (71,[120, 1017, 977, 1412]),
 },
 '12': {
   'p67-closed': (67,[351, 114, 789, 498]),
   'p67-disks': (67,[120, 657, 977, 1122]),
   'p68-evt': (68,'Theorem 6.10'),
   'p73-method': (73,'Method for finding the absolute'),
   'p74-fig': (74,[200, 114, 950, 466]),
   'p74-note': (74,'Note that the point'),
 },
 '13': {
   'p77-def': (77,'Definition 6.29'),
   'p77-thm': (77,'Theorem 6.30'),
   'p79-quick': (79,'Diagonal Entries'),
   'p80-zero': (80,'Zero Entries'),
   'p81-test': (81,'Theorem 6.41'),
   'p82-warn': (82,'Warning'),
 },
 '14': {
   'p88-thm': (88,'Theorem 7.2'),
   'p88-mlm': (88,'Method of Lagrange'),
   'p89-remarks': (89,'Important Remarks'),
   'p90-fig': (90,[120, 141, 977, 805]),
   'p93-ineq': (93,'Inequality constraints'),
   'p93-several': (93,'MLM with several'),
   'p95-fig': (95,[210, 718, 965, 1176],False),
   'p97-fig': (97,[120, 146, 977, 660]),
 },
 '15': {
   'p104-def': (104,'Definition 8.3'),
   'p106-direct': (106,'Solution Method: Integrating'),
   'p107-fig': (107,[255, 330, 780, 840],False),
   'p107-sep': (107,'Solution Method: we can separate'),
   'p110-lin': (110,'Integrating Factor'),
   'p111-lin2': (111,'The LHS is'),
 },
 '16': {
   'p113-ivp': (113,'It is important'),
   'p114-wronsk': (114,'Definition 8.28'),
   'p115-method': (115,'auxiliary (or characteristic)'),
   'p117-fig': (117,[255, 650, 850, 1025],False),
 },
 '17': {
   'p118-method': (118,'Method of Undetermined'),
   'p119-rules': (119,'Here C, K0'),
 },
 '18': {
   'p122-method': (122,'Method of Variation'),
 },
 '19': {
   'p125-mult': (125,'Definition 8.46'),
   'p125-prop': (125,'Proposition 8.47'),
   'p126-method': (126,'Solution Method'),
   'p130-check': (130,'Check your Answer'),
 },
}
import numpy as np
def runs(v):
    best=cur=0
    for x in v:
        cur=cur+1 if x else 0; best=max(best,cur)
    return best
def snap(page, box, grow=40):
    im=Image.open(page_path(page)).convert('L'); a=np.array(im)<200
    x0,y0,x1,y1=box; X0,Y0,X1,Y1=max(0,x0-grow),max(0,y0-grow),min(a.shape[1],x1+grow),min(a.shape[0],y1+grow)
    sub=a[Y0:Y1,X0:X1]; w=X1-X0; h=Y1-Y0
    rows=[y for y in range(h) if runs(sub[y])>0.3*(x1-x0)]
    cols=[x for x in range(w) if runs(sub[:,x])>0.5*(y1-y0)]
    if len(rows)>=2 and len(cols)>=2 and rows[-1]-rows[0]>0.5*(y1-y0):
        return [X0+cols[0]-2, Y0+rows[0]-2, X0+cols[-1]+3, Y0+rows[-1]+3]
    return box
def trim(im, pad=8):
    bg=Image.new(im.mode, im.size, (255,255,255))
    bbox=ImageChops.difference(im,bg).getbbox()
    if not bbox: return im
    x0,y0,x1,y1=bbox
    return im.crop((max(0,x0-pad),max(0,y0-pad),min(im.width,x1+pad),min(im.height,y1+pad)))
for topic, items in SPEC.items():
    os.makedirs(f'{ROOT}/img/{topic}', exist_ok=True)
    for name,v in items.items():
        page,box=v[0],v[1]; dosnap=(len(v)<3 or v[2])
        if isinstance(box,str): box=auto(page,box); box=[box[0]-6,box[1]-6,box[2]+6,box[3]+6]
        elif dosnap: box=snap(page,box)
        im=Image.open(page_path(page)).convert('RGB').crop(tuple(box))
        trim(im).save(f'{ROOT}/img/{topic}/{name}.png', optimize=True)
print('ok')
