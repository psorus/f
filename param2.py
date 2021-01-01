from fobj import *
from transform import mutations
import fmath

import random

class param2(fobj):
  """simplifying class for functions that have exactly two inputs
requires
  def diff(s,by)->'fobj':
  def eval(s,**v)->float:
  def gettyp(s)->str:
  def _copywithparam(s,p1,p2)->"param2":

  def minpos(s)->"float(possibly inf)":
  def maxpos(s)->"float(possibly inf)":
"""

  def __init__(s,q1=None,q2=None):
    fobj.__init__(s)
    s.q1=q1
    s.q2=q2
  def __str__(s)->str:
    return str(s.gettyp())+"("+str(s.q1)+","+str(s.q2)+")"
  def asdict(s)->dict:
    return {"typ":s.gettyp(),"param":[s.q1.asdict(),s.q2.asdict()]}
  
  @abstractmethod
  def _copywithparam(s,p1,p2)->"param2s":
    """create a copy of this object, but replace the parameters with p1,p2. Used in higher level functions, not to have to write the name of the class all the time"""
    pass
  
  def fromdict(s,d)->"param2":
    return s._copywithparam(fromdict(d["param"][0]),fromdict(d["param"][1]))
  def listvar(s)->"(str)":
    ret=s.q1.listvar()
    for zw in s.q2.listvar():
      ret.add(zw)
    return ret
  def copy(s)->"param2":
    return s._copywithparam(s.q1.copy(),s.q2.copy())
  def simplify(s)->'param2':
    ret= s._copywithparam(s.q1.simplify(),s.q2.simplify())
    if ret.evaluable():return fmath.value(ret.eval())
    return ret
  def removeepsilon(s)->'param2':
    return s._copywithparam(s.q1.removeepsilon(),s.q2.removeepsilon())
  def order(s)->None:
    #in general not orderable
    pass 
    # s.q1.order()
    # s.q2.order()
    # if s.q1>s.q2:
      # zw=s.q1
      # s.q1=s.q2
      # s.q2=zw
  def match(s,shape,dic=None)->"bool,dic":
    valid,dic=fobj.match(s,shape,dic=dic)
    if not valid:return False,dic
    if shape.gettyp()=="variable":return valid,dic
    valid,dic= s.q1.match(shape.q1,dic=dic)
    if not valid:return False,dic
    valid,dic= s.q2.match(shape.q2,dic=dic)
    return valid,dic
    
  def deepmutate(s)->"[fobj]":
    ret=mutations(s)
    p1=s.q1.deepmutate()
    p2=s.q2.deepmutate()
    for z1 in p1:
      for z2 in p2:
        ret.append(s._copywithparam(z1,z2))

    ret.insert(0,s.copy())
    return ret

  def huntident(s)->"fobj":
    return s._copywithparam(s.q1.huntident(),s.q2.huntident())
  def evaluable(s,**v)->bool:
    return s.q1.evaluable(**v) and s.q2.evaluable(**v)
  def applyfunc(s,nam,fun)->"fobj":
    return s._copywithparam(s.q1.applyfunc(nam,fun),s.q2.applyfunc(nam,fun))
  def applyvar(s,nam,var)->"fobj":
    return s._copywithparam(s.q1.applyvar(nam,var),s.q2.applyvar(nam,var))
    
  def listfunc(s)->"(str)":
    ret=s.q1.listfunc()
    for zw in s.q2.listfunc():
      ret.add(zw)
    return ret
  def mutate(s,v=None)->"param2":
    if v is None:v=list(s.listvar())
    r=random.random()
    if r<0.4:
      return random.choice(fmath.mulparam)(s.q1.copy(),s.q2.copy())
    elif r<0.7:
      return s._copywithparam(s.q1.mutate(v),s.q2.copy())
    else:
      return s._copywithparam(s.q1.copy(),s.q2.mutate(v))

  def countme(s,p)->"int":
    ret=0
    if s==p:ret=1
    return ret+s.q1.countme(p)+s.q2.countme(p)
  def findparamforfunc(s,f)->"[str]":
    ret=s.q1.findparamforfunc(f)
    if not ret is None:return ret
    return s.q2.findparamforfunc(f)
  def setparamforfunc(s,f,p)->"fobj":
    return s._copywithparam(s.q1.setparamforfunc(f,p),s.q2.setparamforfunc(f,p))







