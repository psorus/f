import fmath

import random

from loopnam import infinite
from const import *

pdgl=[#replace each variable by either
        #parameters of the function replaced
        #just a new parameter
        #variable in the dgl?ok maybe not
        #no that just does not work, simply add dynamically to this list each function parameter
    fmath.variable("a"),
    fmath.func("a","x")*fmath.func("b","x"),
    fmath.exp(fmath.func("a","x")),
    fmath.log(fmath.func("a","x")),
    fmath.variable("a")*fmath.variable("b"),
    None
    
    

]

#transform f(x)=g(h(x)), where g fixed
#f(x)-f'(x)=0
#g(h(x))-(dg/dh)*h'(x)=0
#let g(h)=exp(h)
#exp(h(x))-exp(h(x))*h'(x)=0
#h'(x)=1


##how to implemented this
#choose rnd func to replace
#choose replacement function
#chance all the function names
#set the parameters to match all parameters of the dgl (or partially I guess)
#apply function, hope for good simplify


def genname(inval):
  for q in infinite():
    if not q in inval:return q
  raise Exception("wait...what")

def dglstep(q,maxf=10000,replfunc=None):
  """returns: next dgl step, function that was replaced, with what"""


  #choose rnd func to replace
  allfunc=q.listfunc()
  f=random.choice(list(allfunc))
  par=q.findparamforfunc(f)

  #choose replacement function
  global pdgl
  r=None
  shallreplace=True
  while r is None:
    r=random.choice(list(pdgl))
    if not replfunc is None:
      r=replfunc#.copy()
      replfunc=None
    if r is None or (type(r) is str and r=="funcvar"):
      pv=list(q.listvar())
      if len(pv)==0:continue
      r=fmath.variable(random.choice(pv))
      shallreplace=False
    else:
      break
  
  #dont allow to many functions in the equation
  if len(allfunc)-1+len(r.listfunc())>maxf:
    return dglstep(q,maxf)#just retry
  
  
  #chance all the function names
  if shallreplace:
    inval1=q.listall()
    inval2=r.listall()
    inval=inval1|inval2
    
    for var in r.listvar():
      nn=genname(inval)
      r=r.applyvar(var,fmath.variable(nn))#does nothing to the parameters of protofunctions, this is needed to keep the variable names consistent in applyfunc, but leads to unused runs of this loop, since listvar still returns them
      inval.add(nn)
      #should be able to remove the old name now, but this could lead to weird bugs
      #inval.remove(var)
    for func in r.listfunc():
      nn=genname(inval)
      # print("before replace",r,func,nn)
      r=r.applyfunc(func,fmath.func(nn,*par))#enter the function parameters of the old function
      # print("after replace",r)

      inval.add(nn)
      #should be able to remove the old name now, but this could lead to weird bugs
      #inval.remove(var)
  
  
  
  
  #set the parameters to match all parameters of the dgl (or partially I guess)
  #already done live
  
  #apply function, hope for good simplify
  ret=q.applyfunc(f,r)
  ret=ret.S()
  #needs some dgl specific simplification
  return ret,fmath.func(f,*par),r.copy()


def validsolution(q,var=None):
  if var is None:var=INPUT_VAR
  solvable=var in q.listvar()
  # print("isin lv?",solvable)
  try:
  # for w in range(1):
    solvable=solvable and q.solvable()
    # print("generally solvable?",solvable)
    #NEED TO DIFFERENTIATE BETWEEN VARIABLES IN SOLVABLE (x-1 ist nicht solvable, aber c*x schon und x-c*x auch (input variables and functional constants

    #This is a very crude try
    for j in range(10):
      solvable=solvable and q.applyvar(var,fmath.value(random.random())).solvable()
      # print("random try?",solvable,q.applyvar(var,fmath.value(random.random())))

  except:
    solvable=False
  return solvable


def loopdgl(p,show=False,maxl=10000,maxf=10,var=None):
  if var is None:var=INPUT_VAR
  q=p.copy()
  alltrafos=[]
  
  
  while True:
    q0=q
    q,f0,f1=dglstep(q,maxf=maxf)
    q=q.S()
    if show:
      print("in",q0,"substituting",f0,"by",f1)
    alltrafos.append([f0,f1])
    if len(q.listfunc())==0:break
    if len(str(q))>maxl:return False,q,alltrafos
  
  solvable=validsolution(q,var)
  
  return solvable,q,alltrafos



def desperatedgl(p,show=False,maxl=10000,maxf=10,var=None,showcount=True):
  i=0
  while True:
    acs,acq,act=loopdgl(p,show=show,maxl=maxl,maxf=maxf,var=var)
    if acs:return acs,acq,act
    if showcount:print("failed",i)
    i+=1


def multisolve(p,show=False,maxl=10000,maxf=10,var=None,count=10,showcount=False):
  ret=[]
  for i in range(count):
    acs=False
    while not acs:
      acs,acq,act=desperatedgl(p,show=show,maxl=maxl,maxf=maxf,var=var,showcount=showcount)
      if acs:
        ret.append(act)
        print("having",len(ret),"solutions")
        break
  return ret










  


