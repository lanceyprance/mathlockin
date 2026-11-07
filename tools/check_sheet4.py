from sympy import *
x,y,z,x1,x2,x3=symbols('x y z x1 x2 x3',real=True)
def sec(f):
    return simplify(diff(f,x,2)),simplify(diff(f,y,2)),simplify(diff(f,x,y))
print('Q1')
for f in [x**2*y**3,(x+1)**3*log(y),exp(3*y)*sin(2*x),(x*y+1)/(y+2)]: print(' ',sec(f))
print('Q2',hessian(x**2*y**3,(x,y)), factor(hessian(x**2*y**3,(x,y)).det()))
print('Q3',hessian(exp(x)*sin(y),(x,y)), simplify(hessian(exp(x)*sin(y),(x,y)).det()))
J=Matrix([2*x1+3*x2+x3,3*x1+x2+2*x3,x1+2*x2+3*x3]).jacobian([x1,x2,x3]); print('Q4',J,J.det())
J=Matrix([x1**2+x2**2,2*x1*x2]).jacobian([x1,x2]); print('Q5',J,factor(J.det()))
J=Matrix([cos(x1)*cos(x2),sin(x1)*sin(x2)]).jacobian([x1,x2]); print('Q6',J,simplify(J.det()))
def crit(f,v=(x,y)):
    s=solve([diff(f,t) for t in v],v,dict=True)
    out=[]
    for d in s:
        if all(val.is_real for val in d.values()):
            H=hessian(f,v).subs(d)
            mins=[H[:k,:k].det() for k in range(1,len(v)+1)]
            out.append((tuple(d[t] for t in v),[simplify(m) for m in mins],simplify(f.subs(d))))
    return out
print('Q7a',crit(x**3+y**3-3*x*y))
print('Q7b',crit(x**3+3*x*y**2-12*x-6*y))
print('Q7c',crit(x**4+y**4-3*x**3-y**3))
for f in [x**2-y**2,x**2+2*y**2-4*x+4*y,y*(x-1)+8/x,x*y*exp(-(x**2+y**2)/2)]: print('Q8',f,crit(f))
print('Q9',crit(x**2+y**2+z**2+x*y+y*z+2*x-4*y+6*z,(x,y,z)))
print('Q10',crit(x*y*z+1/(2*x)+1/y+2/z,(x,y,z)))
print('Q11',crit(x**2+y**2+z**2-x*z-x+4*y-z,(x,y,z)))
print('Q12',crit(x**4+y**4-2*x**2+4*x*y-2*y**2))
print('Q13',crit(4*x*y-x**2-y**2-x**2*y**2))
