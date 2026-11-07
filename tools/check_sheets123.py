from sympy import *
x,y,z=symbols('x y z',real=True)
t=symbols('t',positive=True)
# Sheet 1 Q6 limits (simplify then substitute) 
lims=[((3*x**2-y**2+5)/(x**2+y**2+2),{x:0,y:0}),(sqrt(x**2+y**2-1),{x:3,y:4}),(x*sin(y)/(x**2+1),{x:1,y:0}),
((x**2-2*x*y+y**2)/(x-y),{x:1,y:1}),((x*y-y-2*x+2)/(x-1),{x:1,y:1}),((y+4)/(x**2*y-x*y+4*x**2-4*x),{x:2,y:-4})]
print('S1Q6',[cancel(f).subs(p) for f,p in lims], limit(((t-t/4+2*sqrt(t)-2*sqrt(t)/2)/(sqrt(t)-sqrt(t)/2)),t,0))
f=(x**3-2*x**2-x*y**2+2*y**2)/(x**3-2*x**2+x*y**2-2*y**2+x-2); print('S1Q7a',cancel(f).subs({x:2,y:1}))
f=(x**3-x**2-x*y**2+y**2)/(x**3-x**2+x*y**2-y**2+2*x-2); print('S1Q7b',cancel(f).subs({x:1,y:1}))
print('S2Q11',N(sqrt(Rational(102,100)**2+Rational(201,100)**3)),'S2Q12',N((Rational(38,10)**2+2*Rational(21,10)**3)**Rational(1,5)))
g=lambda f,P: [simplify(diff(f,v).subs(P)) for v in (x,y,z)]
print('S3Q1d', g((x**2+y**2+z**2)**Rational(-1,2)+log(x*y*z),{x:-1,y:2,z:-2}))
print('S3Q3c', g(x/y-y*z,{x:4,y:1,z:1}))
# Notes ex 6.23 on unit square: f=x^2-y^2+xy
f=x**2-y**2+x*y; cands=[(1,Rational(1,2)),(0,1),(0,0),(1,0),(1,1)]; print('Ex6.23',[(c,f.subs({x:c[0],y:c[1]})) for c in cands])
# Topic 3 M2: x^2 y/(x^4+y^2) along y=x^2
print('T3M2',simplify((x**2*y/(x**4+y**2)).subs(y,x**2)))
# Topic 7 M3
print('T7M3',N(2.05**2*0.97))
# Topic 8 M3
f=x**2*y+y*z**3; G=Matrix(g(f,{x:1,y:2,z:1})); print('T8M3',G.dot(Matrix([2,1,2])/3))
# Topic 9 Q10c gradient
F=cos(pi*x)-x**2*y+exp(x*z)+y*z; print('S3Q10c',g(F,{x:0,y:1,z:2}), F.subs({x:0,y:1,z:2}))
# Topic 12 M3, Topic 11 M3, Topic 13 M3 value, Topic 14 M3
print('T11M3', (x**3-3*x+y**2-4*y).subs({x:1,y:2}))
