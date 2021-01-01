from param1 import *
from collector import *
from transform import addtrafo

import fmath

import math

class sinh(param1):
  def __init__(s,p):
    param1.__init__(s)
    s.q=p
  def diff(s,by)->'mult':
    return fmath.cosh(s.q)*s.q.diff(by)
  def eval(s,**v)->float:
    return math.sinh(s.q.eval(**v))
  def gettyp(s)->str:
    return "sinh"
  def _copywithparam(s,p)->"param1":
    return sinh(p)
  def minpos(s)->"float(possibly inf)":
    return math.sinh(s.q.minpos())
  def maxpos(s)->"float(possibly inf)":
    return math.sinh(s.q.maxpos())


register(sinh(1.0))






