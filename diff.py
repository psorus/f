from fobj import *
from ferror import *

class diff(fobj):
  
  def __init__(s,what,by):
    fobj.__init__(s)
    s.what=what
    s.by=by
  
  def __str__(s)->str:
    return "(d"+str(s.what)+"/d"+str(s.by)+")"
  def asdict(s)->dict:
    return {"typ":s.gettyp(),"by":str(s.by),"what":s.what.asdict()}
  def fromdict(s,d)->'fobj':
    return diff(fromdict(d["what"]),d["by"])
  def diff(s,by)->'fobj':
    return diff(s.copy(),by)
  def listvar(s)->"(str)":
    ret=s.what.listvar()
    ret.add(s.by)
    return ret
  def eval(s,**v)->float:
    return s.what.diff(s.by).eval(**v)
  def gettyp(s)->str:
    return "diff"
  def _copywithparam(s,what,by)->"fobj":
    return diff(what,by)
  def copy(s)->'fobj':
    return s._copywithparam(s.what.copy(),s.by)
  def simplify(s)->'fobj':
    return s.what.diff(s.by)#.simplify()
    # return s._copywithparam(s.what.simplify(),s.by)
  def removeepsilon(s)->'fobj':
    return s._copywithparam(s.what.removeepsilon(),s.by)
  def evaluable(s,**v)->bool:
    """technically sometimes evaluable(since eval is implemented using diff), but we do not want diffs ever to be evaluable"""
    return False

  def order(s)->None:
    s.what.order()
  def match(s,shape,dic=None)->"bool,dic":
    valid,dic=fobj.match(s,shape,dic=dic)
    if not valid:return False,dic
    if shape.gettyp()=="variable":return valid,dic
    if not s.by==shape.by:valid=False
    valid,dic= s.what.match(shape.what,dic=dic)
    if not valid:return False,dic
    return valid,dic
  def deepmutate(s)->"[fobj]":
    ret= mutations(s)
    ret.append(s.copy())
    return ret
  def applyfunc(s,nam,fun)->"fobj":
    return s._copywithparam(s.what.applyfunc(nam,fun),s.by)
  def applyvar(s,nam,var)->"fobj":
    return s._copywithparam(s.what.applyvar(nam,var),s.by)
  def listfunc(s)->"(str)":
    return s.what.listfunc()
  def mutate(s,v=None)->"diff":
    return s.copy()
  def huntident(s)->"fobj":
    return s._copywithparam(s.what.huntident(),s.by)
  def countme(s,p)->"int":
    ret=0
    if s==p:ret=1
    if str(s.by)==str(p):ret+=1
    return ret+s.what.countme(p)
  def findparamforfunc(s,f)->"[str]":
    return s.what.findparamforfunc(f)
  def setparamforfunc(s,f,p)->"fobj":
    return s._copywithparam(s.what.setparamforfunc(f,p),s.by)

  def minpos(s)->"float(possibly inf)":
    raise NonApproximatibleException(s)
  def maxpos(s)->"float(possibly inf)":
    raise NonApproximatibleException(s)

register(diff(0,"x"))



