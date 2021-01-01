from param1 import *
from collector import *
from transform import addtrafo,addinv

import fmath

import math

class asinh(param1):
  def __init__(s,p):
    param1.__init__(s)
    s.q=p
  def diff(s,by)->'mult':
    return s.q.diff(by)/fmath.sqrt(fmath.value(1)+fmath.square(s.q))
  def eval(s,**v)->float:
    return math.asinh(s.q.eval(**v))
  def gettyp(s)->str:
    return "asinh"
  def _copywithparam(s,p)->"param1":
    return asinh(p)

  def minpos(s)->"float(possibly inf)":
    return math.asinh(s.q.minpos())

  def maxpos(s)->"float(possibly inf)":
    return math.asinh(s.q.maxpos())

register(asinh(1.0))
addinv("sinh","asinh")





