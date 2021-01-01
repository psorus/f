from fobj import *
from collector import *
from transform import mutations

from ferror import *
from const import *

from value import *

from helper import removeepsilon

import random

#not sure if I still like variables to have values...soft disabling them
class variable(fobj):
  def __init__(s,name,value=None):
    fobj.__init__(s)
    s.q=str(name)
    if not value is None:
      s.v=value
  def __str__(s)->str:
    return str(s.q)
  def asdict(s)->dict:
    if s.hasvalue():
      return {"type":"variable","name":s.q,"value":s.v}
    else:
      return {"type":"variable","name":s.q}

  def fromdict(s,d)->"variable":
    if "variable" in d.keys():
      return variable(name=d["name"],variable=d["variable"])
    else:
      return variable(name=d["name"],variable=None)
  def diff(s,by)->"fobj":
    if by==s.q:
      return value(1.0)
    else:
      return value(0.0)
  def listvar(s)->"(str)":
    return set((s.q,))
  def hasvalue(s):
    return hasattr(s,"v")
  def eval(s,**v)->float:
    if s.q in v.keys():return v[s.q]
    if s.hasvalue():return s.v
    raise NotEvaluatableException(s)
      
  def gettyp(s)->str:
    return "variable"
  def copy(s)->"variable":
    if s.hasvalue():
      return variable(s.q,s.v)
    else:
      return variable(s.q)

  def simplify(s)->'variable':
    return s.copy()
  def removeepsilon(s)->'variable':
    if not s.hasvalue():
      return s.copy()
    else:
      return variable(s.q,removeepsilon(s.v))
  
  def _copywithparam(s,name,value=None)->"variable":
    return variable(name,value)
  
  def deepmutate(s)->"[fobj]":
    ret= mutations(s)
    ret.append(s.copy())
    return ret

  def evaluable(s,**v)->bool:
    return s.hasvalue() or s.q in v.keys()

  def order(s)->None:
    pass
  def applyfunc(s,nam,fun)->"fobj":
    return s.copy()
  def applyvar(s,nam,var)->"fobj":
    if nam==s.q:return var.copy()
    return s.copy()
  def listfunc(s)->"(str)":
    return set()
  def mutate(s,v=None)->"variable":
    if v is None:v=list(s.listvar())
    if random.random()<0.2:
      return fmath.rnd(variables=v)
    if random.random()<0.6666 or len(v)>=MAX_MUT_VAR:
      return variable(random.choice(v))
    elif random.random()<0.5:
      return variable(INPUT_VAR)
    else:
      return variable(fmath.newvar(v))
  def huntident(s)->"fobj":
    return s.copy()
  def countme(s,p)->"int":
    if s==p:return 1
    return 0
  def findparamforfunc(s,f)->"[str]":
    return None
  def setparamforfunc(s,f,p)->"fobj":
    return s.copy()

  def minpos(s)->"float(possibly inf)":
    if s.hasvalue():return float(s.v)
    return float("-inf")
  def maxpos(s)->"float(possibly inf)":
    if s.hasvalue():return float(s.v)
    return float("inf")



register(variable("",0))


