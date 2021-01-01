from param1 import *
from collector import *
from transform import addtrafo,addinv

import fmath

import math

class acos(param1):
  def __init__(s,p):
    param1.__init__(s)
    s.q=p
  def diff(s,by)->'divide':
    return -s.q.diff(by)/fmath.sqrt(fmath.value(1)-fmath.square(s.q))
  def eval(s,**v)->float:
    return math.acos(s.q.eval(**v))
  def gettyp(s)->str:
    return "acos"
  def _copywithparam(s,p)->"param1":
    return acos(p)

  def mininp(s)->"float(possibly inf)":
    return -1.0
  def maxinp(s)->"float(possibly inf)":
    return 1.0
  def minpos(s)->"float(possibly inf)":
    mp=s.q.maxpos()
    mp=max(s.mininp(),mp)
    mp=min(s.maxinp(),mp)
    return math.acos(mp)
  def maxpos(s)->"float(possibly inf)":
    mp=s.q.minpos()
    mp=max(s.mininp(),mp)
    mp=min(s.maxinp(),mp)
    return math.acos(mp)

register(acos(1.0))

addinv("cos","acos")




