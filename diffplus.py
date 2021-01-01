from fobj import *
from ferror import *


class diffplus(fobj):
  """like diff by by is a function"""
  def __init__(s,what,by):
    fobj.__init__(s)
    s.what=what
    s.by=by
  
  def __str__(s)->str:
    return "(d"+str(s.what)+"/d"+str(s.by)+")"
  def asdict(s)->dict:
    return {"typ":s.gettyp(),"by":s.by.asdict(),"what":s.what.asdict()}
  def fromdict(s,d)->'fobj':
    return diffplus(fromdict(d["what"]),fromdict(d["by"]))
  def diff(s,by)->'fobj':
    return fmath.diff(s,by)
  def listvar(s)->"(str)":
    ret=s.what.listvar()
    ret.add(s.by)
    for zw in s.by.listvar():ret.add(zw)
    return ret
  def eval(s,**v)->float:
    raise NotEvaluatableException(s)
  def gettyp(s)->str:
    return "diffplus"
  def _copywithparam(s,what,by)->"fobj":
    return diffplus(what,by)
  def copy(s)->'fobj':
    return s._copywithparam(s.what.copy(),s.by.copy())
  def simplify(s)->'fobj':
    p1=s.what.listall()#not sure if func and var are treated well like this
    #maybe diff by f(x,y,z)?
    p2=s.by.listall()
    params=[]
    for p in p1:
      if p in p2:params.append(p)
    rel=[]
    for p in params:
      print("diffing",p,"what",s.what,"whatd",s.what.diff(p),"by",s.by,"byd",s.by.diff(p),"res",s.what.diff(p)/s.by.diff(p),"S",(s.what.diff(p)/s.by.diff(p)).S())
      rel.append(s.what.diff(p)/s.by.diff(p))
    if len(rel)==0:return fmath.value(0.0)
    if len(rel)==1:return rel[0]
    return fmath.doadd(*rel)
  def removeepsilon(s)->'fobj':
    return s._copywithparam(s.what.removeepsilon(),s.by.removeepsilon())
  def evaluable(s,**v)->bool:
    """diff migth be technically evaluable, but this..."""
    return False

  def order(s)->None:
    s.what.order()
    s.by.order()
  def match(s,shape,dic=None)->"bool,dic":
    valid,dic=fobj.match(s,shape,dic=dic)
    if not valid:return False,dic
    if shape.gettyp()=="variable":return valid,dic
    valid,dic= s.what.match(shape.what,dic=dic)
    if not valid:return False,dic
    valid,dic= s.by.match(shape.by,dic=dic)
    if not valid:return False,dic
    
    return valid,dic
  def deepmutate(s)->"[fobj]":
    ret= mutations(s)
    ret.append(s.copy())
    return ret
  def applyfunc(s,nam,fun)->"fobj":
    return s._copywithparam(s.what.applyfunc(nam,fun),s.by.applyfunc(nam,fun))
  def applyvar(s,nam,var)->"fobj":
    return s._copywithparam(s.what.applyvar(nam,var),s.by.applyvar(nam,fun))
  def listfunc(s)->"(str)":
    ret=s.what.listfunc()
    for zw in s.by.listfunc():ret.add(zw)
    return ret
  def mutate(s,v=None)->"diff":
    return s.copy()
  def huntident(s)->"fobj":
    return s._copywithparam(s.what.huntident(),s.by.huntident())
  def countme(s,p)->"int":
    ret=0
    if s==p:ret=1
    return ret+s.what.countme(p)+s.by.countme(p)
  def findparamforfunc(s,f)->"[str]":
    ret=s.what.findparamforfunc(f)
    if not ret is None:return ret
    ret=s.by.findparamforfunc(f)
    if not ret is None:return ret
    return None    
  def setparamforfunc(s,f,p)->"fobj":
    return s._copywithparam(s.what.setparamforfunc(f,p),s.by.setparamforfunc(f,p))

  def minpos(s)->"float(possibly inf)":
    raise NonApproximatibleException(s)
  def maxpos(s)->"float(possibly inf)":
    raise NonApproximatibleException(s)

register(diffplus(0,1))



