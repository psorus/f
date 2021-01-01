from param1 import *
from collector import *
from transform import addtrafo,addinv

# from sin import *
# from mult import *
# from value import *
import fmath

import math

class acosh(param1):
  def __init__(s,p):
    param1.__init__(s)
    s.q=p
  def diff(s,by)->'mult':
    return s.q.diff(by)/fmath.sqrt(fmath.square(s.q)-fmath.value(1))
  def eval(s,**v)->float:
    return math.acosh(s.q.eval(**v))
  def gettyp(s)->str:
    return "acosh"
  def _copywithparam(s,p)->"param1":
    return acosh(p)

  def mininp(s)->"float(possibly inf)":
    return 1.0

  def minpos(s)->"float(possibly inf)":
    mp=s.q.minpos()
    mp=max(s.mininp(),mp)
    return math.acosh(mp)
  def maxpos(s)->"float(possibly inf)":
    mp=s.q.maxpos()
    mp=max(s.mininp(),mp)
    return math.acosh(mp)

register(acosh(1.0))
addinv("cosh","acosh")