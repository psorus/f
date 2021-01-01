from param1 import *
from collector import *
from transform import addtrafo

import fmath

import math

class tanh(param1):
  def __init__(s,p):
    param1.__init__(s)
    s.q=p
  def diff(s,by)->'mult':
    return s.q.diff(by)/(fmath.square(fmath.cosh(s.q)))
  def eval(s,**v)->float:
    return math.tanh(s.q.eval(**v))
  def gettyp(s)->str:
    return "tanh"
  def _copywithparam(s,p)->"param1":
    return tanh(p)
  def minpos(s)->"float(possibly inf)":
    return math.tanh(s.q.minpos())
  def maxpos(s)->"float(possibly inf)":
    return math.tanh(s.q.maxpos())

register(tanh(0.5))

addtrafo("tanh",lambda v:True,lambda v:fmath.sinh(v.q)/fmath.cosh(v.q))

