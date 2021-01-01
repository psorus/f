from fobj import *

from ferror import *

import fmath

class func(fobj):
  
  def __init__(s,nam,*par):
    fobj.__init__(s)
    s.q=nam
    s.p=par
  
  def __str__(s)->str:
    return str(s.q)+"("+",".join([str(p) for p in s.p])+")"
  def asdict(s)->dict:
    return {"typ":s.gettyp(),"nam":str(s.q),"par":[str(p) for p in s.p]}
  def fromdict(s,d)->'fobj':
    return func(d["nam"],*d["par"])
  def diff(s,by)->'fobj':
    if by==s.q:return fmath.value(1.0)
    if by in s.p:
      return fmath.diff(s.copy(),by)
    else:
      return fmath.value(0.0)
  def listvar(s)->"(str)":
    ret=set([])
    for p in s.p:
      ret.add(p)
    return ret
  def eval(s,**v)->float:
    raise NotEvaluatableException(s)
  def gettyp(s)->str:
    return "func"
  def _copywithparam(s,nam,*par)->"fobj":
    return func(nam,*par)
  def copy(s)->'fobj':
    return s._copywithparam(s.q,*s.p)
  def simplify(s)->'fobj':
    return s._copywithparam(s.q,*s.p)
  def removeepsilon(s)->'fobj':
    return s._copywithparam(s.q,*s.p)
  def evaluable(s,**v)->bool:
    return False

  def order(s)->None:
    pass
  def match(s,shape,dic=None)->"bool,dic":
    valid,dic=fobj.match(s,shape,dic=dic)
    if not valid:return False,dic
    if shape.gettyp()=="variable":return valid,dic
    if not s.q==shape.q:valid=False
    if not s.p==shape.p:valid=False
    return valid,dic
  def deepmutate(s)->"[fobj]":
    ret= mutations(s)
    ret.append(s.copy())
    return ret
  def applyfunc(s,nam,fun)->"fobj":
    # print("trying to apply",nam,"too",s.q)
    if nam==s.q:return fun.copy()
    return s.copy()
  def applyvar(s,nam,var)->"fobj":
    return s.copy()
  def listfunc(s)->"(str)":
    return set([s.q])
  def mutate(s,v=None)->"func":
    return s.copy()
  def huntident(s)->"fobj":
    return s.copy()
  def countme(s,p)->"int":
    if s==p:return 1
    return 0
  def findparamforfunc(s,f)->"[str]":
    if f==s.q:return s.p
    return None
  def setparamforfunc(s,f,p)->"fobj":
    if f==s.q:return s._copywithparam(s.q,*p)
    return s.copy()

  def minpos(s)->"float(possibly inf)":
    return float("-inf")
  def maxpos(s)->"float(possibly inf)":
    return float("inf")
register(func("f","x"))



