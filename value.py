from fobj import *
from collector import *
from transform import mutations

from helper import removeepsilon

import fmath

import random
import math

class value(fobj):
  def __init__(s,value):
    fobj.__init__(s)
    s.v=value
  def __str__(s)->str:
    return str(s.v)
  def asdict(s)->dict:
    return {"typ":"value","value":s.v}
  def fromdict(s,d)->"value":
    return value(value=d["value"])
  def diff(s,by)->"fobj":
    return value(0)
  def listvar(s)->"(str)":
    return set()
  def eval(s,**v)->float:
    return s.v
  def gettyp(s)->str:
    return "value"
  def copy(s)->"value":
    return value(s.v)
  def simplify(s)->'value':
    return s.copy()
  def removeepsilon(s)->'value':
    return value(removeepsilon(s.v))
  def _copywithparam(s,v)->"value":
    return value(v)
  def match(s,shape,dic=None)->"bool,dic":
    valid,dic=fobj.match(s,shape,dic=dic)
    if not valid:return False,dic
    if shape.gettyp()=="variable":return valid,dic
    if not s.v==shape.v:valid=False
    return valid,dic
  
  def deepmutate(s)->"[fobj]":
    ret= mutations(s)
    ret.append(s.copy())
    return ret

  def evaluable(s,**v)->bool:
    return True

  def order(s)->None:
    pass
  def applyfunc(s,nam,fun)->"fobj":
    return s.copy()
  def applyvar(s,nam,var)->"fobj":
    return s.copy()
  def listfunc(s)->"(str)":
    return set()
  def mutate(s,v=None)->"fobj":
    if v is None:v=list(s.listvar())
    if random.random()<0.5 and len(v)>0:
      return fmath.variable(random.choice(v))
    else:
      v=s.v
      v+=2*(random.random()-0.5)*math.exp(6*(random.random()-0.5))
      return value(v)
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
    return float(s.v)
  def maxpos(s)->"float(possibly inf)":
    return float(s.v)

register(value(0))

