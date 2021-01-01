from fobj import *
from transform import mutations
import fmath

import random

class param1(fobj):
  """simplifying class for functions that have a single input
requires
  def diff(s,by)->'fobj':
  def eval(s,**v)->float:
  def gettyp(s)->str:
  def _copywithparam(s,p)->"param1":

  def minpos(s)->"float(possibly inf)":
  def maxpos(s)->"float(possibly inf)":
"""

  def __init__(s,q=None):
    fobj.__init__(s)
    s.q=q
  def __str__(s)->str:
    return str(s.gettyp())+"("+str(s.q)+")"
  def asdict(s)->dict:
    return {"typ":s.gettyp(),"param":[s.q.asdict()]}
  
  @abstractmethod
  def _copywithparam(s,p)->"param1":
    """create a copy of this object, but replace the parameter with p. Used in higher level functions, not to have to write the name of the class all the time"""
    pass
  
  def fromdict(s,d)->"param1":
    return s._copywithparam(fromdict(d["param"][0]))
  def listvar(s)->"(str)":
    return s.q.listvar()
  def copy(s)->"param1":
    return s._copywithparam(s.q.copy())
  def simplify(s)->'param1':
    ret= s._copywithparam(s.q.simplify())
    if ret.evaluable():return fmath.value(ret.eval())
    return ret
  def removeepsilon(s)->'param1':
    return s._copywithparam(s.q.removeepsilon())
  def order(s)->None:
    s.q.order()
  def match(s,shape,dic=None)->"bool,dic":
    valid,dic=fobj.match(s,shape,dic=dic)
    if not valid:return False,dic
    if shape.gettyp()=="variable":return valid,dic
    return s.q.match(shape.q,dic=dic)
    
  def deepmutate(s)->"[fobj]":
    ret=mutations(s)
    for zw in s.q.deepmutate():ret.append(s._copywithparam(zw))

    ret.insert(0,s.copy())
    return ret

  def huntident(s)->"fobj":
    return s._copywithparam(s.q.huntident())
  def evaluable(s,**v)->bool:
    return s.q.evaluable(**v)


  def applyfunc(s,nam,fun)->"fobj":
    return s._copywithparam(s.q.applyfunc(nam,fun))
  def applyvar(s,nam,var)->"fobj":
    return s._copywithparam(s.q.applyvar(nam,var))

  def listfunc(s)->"(str)":
    return s.q.listfunc()
  
  def mutate(s,v=None)->"param1":
    if v is None:v=list(s.listvar())
    r=random.random()
    if r<0.5:
      return random.choice(fmath.oneparam)(s.q.copy())
    else:
      return s._copywithparam(s.q.mutate(v))
    
  def countme(s,p)->"int":
    ret=0
    if s==p:ret=1
    return ret+s.q.countme(p)
  def findparamforfunc(s,f)->"[str]":
    return s.q.findparamforfunc(f)
  def setparamforfunc(s,f,p)->"fobj":
    return s._copywithparam(s.q.setparamforfunc(f,p))




