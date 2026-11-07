from sympy import *
x,y,z,l,m=symbols('x y z lambda mu',real=True)
def lag(f,gs,v):
    lams=[l,m][:len(gs)]
    eqs=[diff(f,t)-sum(L*diff(g,t) for L,g in zip(lams,gs)) for t in v]+list(gs)
    sol=solve(eqs,list(v)+lams,dict=True)
    out=[]
    for s in sol:
        if all(s[t].is_real for t in v):
            out.append((tuple(nsimplify(s[t]) for t in v), simplify(f.subs(s))))
    return out
print('Q16',lag(x*y**6,[x**2+y**4-4],(x,y)))
print('Q17',lag(x**2*y*z,[x**2+y**2+z**2-2],(x,y,z)))
print('Q18',lag(x**2*y**2*z**2,[x+y+z,x**2+y**2+z**2-1],(x,y,z)))
print('Q19',lag(x**2+y**2+z**2,[x+y+z-1,x-y+2*z-1],(x,y,z)))
print('Q20',lag(x**2+y**2+z**2,[x+y+z-5,x*y*z-4],(x,y,z)))
print('Exam6a',lag(x**2*y*z+1,[z-1,x**2+y**2+z**2-10],(x,y,z)))
# Q15 wire: base 2a, rect height h, triangle sides s; a+h+s=1 ; area 2ah + a*sqrt(s^2-a^2)
a,h,s=symbols('a h s',positive=True)
A=2*a*h+a*sqrt(s**2-a**2)
Ah=A.subs(h,1-a-s)
sol=solve([diff(Ah,a),diff(Ah,s)],[a,s],dict=True)
for d in sol: print('Q15',d,simplify(Ah.subs(d)), N(Ah.subs(d)))
print(N((3+2*sqrt(3))), N(1/(2*(2+sqrt(3)))), N((2-sqrt(3))/2), N(1/(4+2*sqrt(3))) )
