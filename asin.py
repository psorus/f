from param1 import *
from collector import *
from transform import addtrafo,addinv

import fmath

import math

class asin(param1):
  def __init__(s,p):
    param1.__init__(s)
    s.q=p
  def diff(s,by)->'divide':
    return s.q.diff(by)/fmath.sqrt(fmath.value(1)-fmath.square(s.q))
  def eval(s,**v)->float:
    return math.asin(s.q.eval(**v))
  def gettyp(s)->str:
    return "asin"
  def _copywithparam(s,p)->"param1":
    return asin(p)

  def mininp(s)->"float(possibly inf)":
    return -1.0
  def maxinp(s)->"float(possibly inf)":
    return 1.0
  def minpos(s)->"float(possibly inf)":
    mp=s.q.minpos()
    mp=max(s.mininp(),mp)
    mp=min(s.maxinp(),mp)
    return math.asin(mp)
  def maxpos(s)->"float(possibly inf)":
    mp=s.q.maxpos()
    mp=max(s.mininp(),mp)
    mp=min(s.maxinp(),mp)
    return math.asin(mp)


register(asin(1.0))

addinv("sin","asin")




