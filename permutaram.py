from fobj import *
from transform import mutations

from value import *

from helper import compsort

import itertools
import random

class permutaram(fobj):
  """simplifying class for functions that have exactly an arbitrary number of parameters, but which parameters are always similar to each other (like +). Assumes that if f(a,b,c) is a valid permutaram, also f(a,c) is one, aswell as f(c,b,a). We also assume f(x)=x.
requires
  def diff(s,by)->'fobj':
  def eval(s,**v)->float:
  def gettyp(s)->str:
  def _copywithparam(s,*p)->"permutaram":

  def minpos(s)->"float(possibly inf)":
  def maxpos(s)->"float(possibly inf)":
"""

  def __init__(s,*q):
    fobj.__init__(s)
    s.q=q
  def __str__(s)->str:
    return "("+(" "+str(s.gettyp())+" ").join([str(ac) for ac in s.q])+")"
  def asdict(s)->dict:
    return {"typ":s.gettyp(),"param":[ac.asdict() for ac in s.q]}
  
  @abstractmethod
  def _copywithparam(s,*p)->"permutaram":
    """create a copy of this object, but replace the parameters with p. Used in higher level functions, not to have to write the name of the class all the time"""
    pass
  
  def fromdict(s,d)->"permutaram":
    return s._copywithparam(*[fromdict(ac) for ac in d["param"]])
  def listvar(s)->"(str)":
    ret=set()
    for q in s.q:
      for zw in q.listvar():
        ret.add(zw)
    return ret
  def copy(s)->"permutaram":
    return s._copywithparam(*[ac.copy() for ac in s.q])
  def deeplevel(s)->"permutaram":
    """transforms f(a,f(b,c)) into f(a,b,c)"""
    
    mt=s.gettyp()
    
    q=[ac for ac in s.q if not ac.gettyp()==mt]
    aq=[ac for ac in s.q if not ac.gettyp()!=mt]
    
    for zw in aq:
      for zx in zw.q:
        q.append(zx)
    
    return s._copywithparam(*q)
  def simplify(s)->"permutaram":
  
    q=[ac.simplify() for ac in s.q]
    s=s._copywithparam(*q).deeplevel()
    q=s.q
    evy=[ac for ac in q if ac.evaluable()]
    evn=[ac for ac in q if not ac.evaluable()]
    
    if len(evy)>1:
      zx=s._copywithparam(*evy)
      evn.append(value(zx.eval()))
      
      if len(evn)==1:return evn[0]
      ret= s._copywithparam(*evn)
      if ret.evaluable():return value(ret.eval())
      return ret.deeplevel()
    else:
      ret= s._copywithparam(*q)
      if ret.evaluable():return value(ret.eval())
      return ret.deeplevel()
    
  def removeepsilon(s)->"permutaram":
    return s._copywithparam(*[ac.removeepsilon() for ac in s.q])
  
  def order(s)->None:
    for i in range(len(s.q)):s.q[i].order()
    s.q=compsort(s.q)

  def match(s,shape,dic=None)->"bool,dic":
    valid,dic=fobj.match(s,shape,dic=dic)
    if not valid:return False,dic
    if shape.gettyp()=="variable":return valid,dic
    if not len(s.q)==len(shape.q):return False,dic
    for a,b in zip(s.q,shape.q):
      valid,dic= a.match(b,dic=dic)
      if not valid:return False,dic
    return valid,dic

  def deepmutate(s)->"[fobj]":
    ret=mutations(s)
    dms=[qq.deepmutate() for qq in s.q]
    for zw in [s._copywithparam(*q) for q in itertools.product(*dms)]:
      ret.append(zw)
  
    ret.insert(0,s.copy())
    return ret

  def huntident(s)->"fobj":
    if len(s.q)==0:return value(0.0)
    if len(s.q)==1:return s.q[0].huntident()
    return s._copywithparam(*[ac.huntident() for ac in s.q])
  
  def q1(s)->"fobj":
    """return the first object"""
    return s.q[0]
  
  def q2(s)->"fobj":
    """return everything but the first object"""
    return s._copywithparam(*s.q[1:])

  def evaluable(s,**v)->bool:
    for qq in s.q:
      if not qq.evaluable(**v):return False
    return True

  def applyfunc(s,nam,fun)->"fobj":
    return s._copywithparam(*[ac.applyfunc(nam,fun) for ac in s.q])
  def applyvar(s,nam,var)->"fobj":
    return s._copywithparam(*[ac.applyvar(nam,var) for ac in s.q])

  def listfunc(s)->"(str)":
    ret=set()
    for q in s.q:
      for zw in q.listfunc():
        ret.add(zw)
    return ret

  def mutate(s,v=None)->"permutaram":
    if v is None:v=list(s.listvar())
    r=random.random()
    if r<0.3:
      try:
        return random.choice(fmath.mulparam)(*[ac.copy() for ac in s.q])
      except:
        return random.choice(fmath.mulparam)(s.q[0],s._copywithparam(*[ac.copy() for ac in s.q[1:]]))
    elif r<0.7:
      c=[ac.copy() for ac in s.q]
      i=random.randint(0,len(c)-1)
      c[i]=c[i].mutate(v)
      return s._copywithparam(*c)
    elif r<0.85:
      c=[ac.copy() for ac in s.q]
      c.append(fmath.rnd(variables=s.listvar()))
      return s._copywithparam(*c)
    else:
      c=[ac.copy() for ac in s.q]
      i=random.randint(0,len(c)-1)
      del c[i]
      if len(c)==0:return fmath.value(0.0)
      if len(c)==1:return c[0]
      return s._copywithparam(*c)

  def countme(s,p)->"int":
    ret=0
    if s==p:ret+=1
    for zw in s.q:ret+=zw.countme(p)
    return ret
  def findparamforfunc(s,f)->"[str]":
    for s in s.q:
      ac=s.findparamforfunc(f)
      if not ac is None:return ac
    return None
  def setparamforfunc(s,f,p)->"fobj":
    return s._copywithparam(*[ac.setparamforfunc(f,p) for ac in s.q])






