from fobj import *
from ferror import *

import fmath

class integrateplus(fobj):
  """like diffplus for diff, this is intregrate, but by is another function"""
  def __init__(s,what,by,fro,too):
    raise Exception("""integrateplus should not be used atm. Simplify splits the integrals, but has no way of dealing with the changing borders. This can only be solved if you can invert functions ;(""")
    fobj.__init__(s)
    s.what=what
    s.by=by
    s.fro=fro
    s.too=too
  
  def __str__(s)->str:
    return "Int("+str(s.what)+" by "+str(s.by)+" from "+str(s.fro)+" to "+str(s.too)+")"
  def asdict(s)->dict:
    return {"typ":s.gettyp(),"by":s.by.asdict(),"fro":s.fro.asdict(),"too":s.too.asdict(),"what":s.what.asdict()}
  def fromdict(s,d)->'fobj':
    return integrateplus(fromdict(d["what"]),fromdict(d["by"]),fromdict(d["fro"]),fromdict(d["too"]))
  def diff(s,by)->'fobj':
    return fmath.diff(s.simplify(),by)#yes this is a bit easy...but why not?
    # term1=integrate(s.what.diff(by),s.by,s.fro,s.too)
    # term2=s.fro.diff(by)*s.what.replace(s.by,s.fro)
    # term3=s.too.diff(by)*s.what.replace(s.by,s.too)
    
    # return term1+term3-term2
    

  def listvar(s)->"(str)":
    ret=s.what.listvar()
    for zw in s.by.listvar():
      if zw in ret:ret.remove(zw)
    for zw in s.fro.listvar():ret.add(zw)
    for zw in s.too.listvar():ret.add(zw)
    return ret
  def eval(s,**v)->float:
    raise NotEvaluatableException(s)
  def gettyp(s)->str:
    return "integrateplus"
  def _copywithparam(s,what,by,fro,too)->"fobj":
    return integrateplus(what,by,fro,too)
  def copy(s)->'fobj':
    return s._copywithparam(s.what.copy(),s.by.copy(),s.fro.copy(),s.too.copy())
  def simplify(s)->'fobj':
    if s.what.evaluable() and s.what==0.0:return fmath.value(0.0)
    
    params=s.by.listall()
    rel=[]
    
    whats=s.what.simplify()
    fros=s.fro.simplify()
    toos=s.too.simplify()
    bys=s.by.simplify()
    
    for param in params:
      rel.append(fmath.integrate(whats*bys.diff(param),param,fros,toos))
      
    if len(rel)==0:
      print("THIS SHOULD NOT HAPPEN (integrateplus.py). The integrationsvariable should not be constant. Ignoring the integral")
      return whats
    if len(rel)==1:
      return rel[0]
    return fmath.doadd(*rel)
    
    
    return s._copywithparam(s.what.simplify(),s.by,s.fro.simplify(),s.too.simplify())
  def removeepsilon(s)->'fobj':
    return s._copywithparam(s.what.removeepsilon(),s.by,s.fro.removeepsilon(),s.too.removeepsilon())
  def evaluable(s,**v)->bool:
    return False

  def order(s)->None:
    s.what.order()
    s.by.order()
    s.fro.order()
    s.too.order()
  def match(s,shape,dic=None)->"bool,dic":
    valid,dic=fobj.match(s,shape,dic=dic)
    if not valid:return False,dic
    if shape.gettyp()=="variable":return valid,dic
    valid,dic= s.what.match(shape.what,dic=dic)
    if not valid:return False,dic
    valid,dic= s.by.match(shape.by,dic=dic)
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
    return s._copywithparam(s.what.applyfunc(nam,fun),s.by.applyfunc(nam,fun),s.fro.applyfunc(nam,fun),s.too.applyfunc(nam,fun))
  def applyvar(s,nam,var)->"fobj":
    return s._copywithparam(s.what.applyvar(nam,var),s.by.applyvar(nam,var),s.fro.applyvar(nam,var),s.too.applyvar(nam,var))
  def huntident(s)->"fobj":
    return s._copywithparam(s.what.huntident(),s.by.huntident(),s.fro.huntident(),s.too.huntident())
  def listfunc(s)->"(str)":
    ret=s.what.listfunc()
    for zw in s.by.listvar():
      if zw in ret:ret.remove(zw)
    for zw in s.fro.listfunc():ret.add(zw)
    for zw in s.too.listfunc():ret.add(zw)
    return ret
  def mutate(s,v=None)->"integrateplus":
    return s.copy()
  def countme(s,p)->"int":
    ret=0
    if s==p:ret=1
    return ret+s.what.countme(p)+s.fro.countme(p)+s.too.countme(p)+s.by.countme(p)
  def findparamforfunc(s,f)->"[str]":
    ret=s.what.findparamforfunc(f)
    if not ret is None:return ret
    ret=s.fro.findparamforfunc(f)
    if not ret is None:return ret
    ret=s.too.findparamforfunc(f)
    if not ret is None:return ret
    ret=s.by.findparamforfunc(f)
    if not ret is None:return ret
    
    return None
  def setparamforfunc(s,f,p)->"fobj":
    return s._copywithparam(s.what.setparamforfunc(f,p),s.by.setparamforfunc(f,p),s.fro.setparamforfunc(f,p),s.too.setparamforfunc(f,p))

  def minpos(s)->"float(possibly inf)":
    raise NonApproximatibleException(s)
  def maxpos(s)->"float(possibly inf)":
    raise NonApproximatibleException(s)
  
  
register(integrateplus(0,1,0,0))



