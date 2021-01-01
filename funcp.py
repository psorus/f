from fobj import *

from ferror import *

import fmath
#not yet fin
#put on ice for dgl I guess
class func(fobj):
  
  def __init__(s,nam,*par):
    fobj.__init__(s)
    s.q=nam
    s.p=par
  
  def __str__(s)->str:
    return str(s.q)+"("+",".join([str(p) for p in s.p])+")"
  def asdict(s)->dict:
    return {"typ":s.gettyp(),"nam":str(s.q),"par":[p.asdict() for p in s.p]}
  def fromdict(s,d)->'fobj':
    return func(d["nam"],*[q.fromdict() for q in d["par"]])
  def diff(s,by)->'fobj':
    if by in s.listvar():
      #require diff+
      return fmath.diff(s.copy(),by)
    else:
      return fmath.value(0.0)
  def listvar(s)->"(str)":
    ret=[]
    for p in s.p:
      for zw in p.listvar():
        ret.add(zw)
    return ret
  def eval(s,**v)->float:
    raise NotEvaluatableException(s)
  def gettyp(s)->str:
    return "func"
  def _copywithparam(s,nam,*par)->"fobj":
    return func(nam,*par)
  def copy(s)->'fobj':
    return s._copywithparam(s.q,*[p.copy() for p in s.p])
  def simplify(s)->'fobj':
    return s._copywithparam(s.q,*[p.simplify() for p in s.p])
  def removeepsilon(s)->'fobj':
    return s._copywithparam(s.q,*[p.removeepsilon() for p in s.p])
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
    if nam==s.q:return fun.copy()
    return s.copy()
  def listfunc(s)->"(str)":
    return set([s.q])
  def mutate(s,v=None)->"func":
    return s.copy()

register(func("f","x"))



