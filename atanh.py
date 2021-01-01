from param1 import *
from collector import *
from transform import addtrafo,addinv

import fmath

import math

class atanh(param1):
  def __init__(s,p):
    param1.__init__(s)
    s.q=p
  def diff(s,by)->'mult':
    return s.q.diff(by)/(fmath.value(1)-fmath.square(s.q))
  def eval(s,**v)->float:
    return math.atanh(s.q.eval(**v))
  def gettyp(s)->str:
    return "atanh"
  def _copywithparam(s,p)->"param1":
    return atanh(p)

  def mininp(s)->"float(possibly inf)":
    return -1.0
  def maxinp(s)->"float(possibly inf)":
    return 1.0
  def minpos(s)->"float(possibly inf)":
    mp=s.q.minpos()
    mp=max(s.mininp(),mp)
    mp=min(s.maxinp(),mp)
    return math.atanh(mp)
  def maxpos(s)->"float(possibly inf)":
    mp=s.q.maxpos()
    mp=max(s.mininp(),mp)
    mp=min(s.maxinp(),mp)
    return math.atanh(mp)

register(atanh(0.5))

addinv("tanh","atanh")

