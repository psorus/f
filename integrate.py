from fobj import *
from ferror import *

import fmath

class integrate(fobj):
  
  def __init__(s,what,by,fro,too):
    fobj.__init__(s)
    s.what=what
    s.by=by
    s.fro=fro
    s.too=too
  
  def __str__(s)->str:
    return "Int("+str(s.what)+" by "+str(s.by)+" from "+str(s.fro)+" to "+str(s.too)+")"
  def asdict(s)->dict:
    return {"typ":s.gettyp(),"by":str(s.by),"fro":s.fro.asdict(),"too":s.too.asdict(),"what":s.what.asdict()}
  def fromdict(s,d)->'fobj':
    return integrate(fromdict(d["what"]),d["by"],fromdict(d["fro"]),fromdict(d["too"]))
  def diff(s,by)->'fobj':
    term1=integrate(s.what.diff(by),s.by,s.fro,s.too)
    term2=s.fro.diff(by)*s.what.replace(s.by,s.fro)
    term3=s.too.diff(by)*s.what.replace(s.by,s.too)
    
    return term1+term3-term2
    

  def listvar(s)->"(str)":
    ret=s.what.listvar()
    if s.by in ret:ret.remove(s.by)
    for zw in s.fro.listvar():ret.add(zw)
    for zw in s.too.listvar():ret.add(zw)
    return ret
  def eval(s,**v)->float:
    raise NotEvaluatableException(s)
  def gettyp(s)->str:
    return "integrate"
  def _copywithparam(s,what,by,fro,too)->"fobj":
    return integrate(what,by,fro,too)
  def copy(s)->'fobj':
    return s._copywithparam(s.what.copy(),s.by,s.fro.copy(),s.too.copy())
  def simplify(s)->'fobj':
    if s.what.evaluable() and s.what==0.0:return fmath.value(0.0)
    if not s.by in s.what.listall():
      return s.what*(s.too-s.fro)
    return s._copywithparam(s.what.simplify(),s.by,s.fro.simplify(),s.too.simplify())
  def removeepsilon(s)->'fobj':
    return s._copywithparam(s.what.removeepsilon(),s.by,s.fro.removeepsilon(),s.too.removeepsilon())
  def evaluable(s,**v)->bool:
    """technically sometimes evaluable, but we do not want integrates (like diffs) ever to be evaluable"""
    return False

  def order(s)->None:
    s.what.order()
    s.fro.order()
    s.too.order()
  def match(s,shape,dic=None)->"bool,dic":
    valid,dic=fobj.match(s,shape,dic=dic)
    if not valid:return False,dic
    if shape.gettyp()=="variable":return valid,dic
    if not s.by==shape.by:return False,dic
    valid,dic= s.what.match(shape.what,dic=dic)
    if not valid:return False,dic
    valid,dic= s.fro.match(shape.fro,dic=dic)
    if not valid:return False,dic
    valid,dic= s.too.match(shape.too,dic=dic)
    if not valid:return False,dic
    
    return valid,dic
  def deepmutate(s)->"[fobj]":#who cares i guess
    ret= mutations(s)
    ret.append(s.copy())
    return ret
  def applyfunc(s,nam,fun)->"fobj":
    return s._copywithparam(s.what.applyfunc(nam,fun),s.by,s.fro.applyfunc(nam,fun),s.too.applyfunc(nam,fun))
  def applyvar(s,nam,var)->"fobj":
    return s._copywithparam(s.what.applyvar(nam,var),s.by,s.fro.applyvar(nam,var),s.too.applyvar(nam,var))
  def huntident(s)->"fobj":
    return s._copywithparam(s.what.huntident(),s.by,s.fro.huntident(),s.too.huntident())
  def listfunc(s)->"(str)":
    ret=s.what.listfunc()
    if s.by in ret:ret.remove(s.by)
    for zw in s.fro.listfunc():ret.add(zw)
    for zw in s.too.listfunc():ret.add(zw)
    return ret
  def mutate(s,v=None)->"integrate":
    return s.copy()
  def countme(s,p)->"int":
    ret=0
    if s==p:ret=1
    if str(s.by)==str(p):ret+=1
    return ret+s.what.countme(p)+s.fro.countme(p)+s.too.countme(p)
  def findparamforfunc(s,f)->"[str]":
    ret=s.what.findparamforfunc(f)
    if not ret is None:return ret
    ret=s.fro.findparamforfunc(f)
    if not ret is None:return ret
    ret=s.too.findparamforfunc(f)
    if not ret is None:return ret
    return None
  def setparamforfunc(s,f,p)->"fobj":
    return s._copywithparam(s.what.setparamforfunc(f,p),s.by,s.fro.setparamforfunc(f,p),s.too.setparamforfunc(f,p))


  def minpos(s)->"float(possibly inf)":
    raise NonApproximatibleException(s)
  def maxpos(s)->"float(possibly inf)":
    raise NonApproximatibleException(s)

register(integrate(0,"x",0,0))



