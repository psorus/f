# from fobj import *

from importall import *

from transform import *

import trigonometrics


from dgl import *
# import random
# random.seed(3)

x=variable("x")
y=variable("y")
f=func("f","x")
fs=f.diff("x")
a=x
b=x*y
zero=value(0.0)
one=value(1.0)

dgl=f-fs


fa=func("a","x")
b=variable("b")

q=dgl.copy()

# q,fro,too=dglstep(q,replfunc=exp(fa))
# print("replacing",fro,"by",too,"results in",q)
# q,fro,too=dglstep(q,replfunc="funcvar")
# print("replacing",fro,"by",too,"results in",q)

# print("valid solution",validsolution(q))


# exit()

solutions=multisolve(dgl,show=False,count=250)


# print(solutions)

print("\n".join(set([str(q) for q in solutions])))


exit()


solvable,solution,steps=desperatedgl(dgl,show=False)


print("is solvable?",solvable)
print("solution",solution)
print("by steps",steps)


exit()




print(dgl)
dgl=dgl.S()
print(dgl)


print("doing one step")
dgl1,fro1,too1=dglstep(dgl)
print(fro1.S(),"->",too1.S())
print("did one step")

print(dgl1)
dgl1=dgl1.S()
print(dgl1)



print("doing one step")
dgl2,fro2,too2=dglstep(dgl1)
print(fro2,"->",too2.S())
print("did one step")

print(dgl2)
dgl2=dgl2.S()
print(dgl2)


exit()

print(q.findparamforfunc("f"))

exit()



q=integrateplus(x,x*y,zero,one)

print(q)

q=q.S()

print(q)



exit()



# q=one/(x+x)
# print(q)
# # q=q.S()
# q=q.copy()
# q.S()

# print(q)

# exit()




q=diffplus(a,b)

print(q)

q=q.S()

print(q)



exit()













f=func("f","x")
F=integrate(x*y,"y",a,b)

print(F)
F=F.copy()
print(F)
F=F.simplify()
print(F)
F=F.S()
print(F)

f=F.diff("x")
print(f)
f=f.simplify()
print(f)
f=f.S()
print(f)

exit()
q=f.q1.q[0]

print(q)
q=q.S()
print(q)

exit()

print(q.treestr())

# print(f.treestr())


#not not close, but also not rigth
#differentiate integral_x^x**2 f(y) dy

exit()


fs=diff(f,x)

h=func("h","x")
k=func("k","x")
ap=h*exp(k)

dgl=fs-f

m=dgl.applyfunc("f",ap)

print(dgl)

print(ap)
# print(ap.S())

# exit()


print(m)


m=m.S()

print(m)


exit()
y=variable("y")
v=value(3)

# q=divide(x,y+v)

# q=cos(x)

q=sin(x)#-x+v)
q=q.S()


print(q)

m=infinimut(q,2)

print(len(m))
for mm in m:
  print(mm)


exit()



# q=q.S()
# pat=pat.S()


print(q)
print(pat)

print(q.match(pat))

exit()


print(q)
q=q.S()
print(q)

exit()



qd=q.diff("x")
print(qd)
qd=qd.S()
print(qd)

