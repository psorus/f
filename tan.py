from param1 import *
from collector import *
from transform import addtrafo

import fmath

import math

class tan(param1):
  def __init__(s,p):
    param1.__init__(s)
    s.q=p
  def diff(s,by)->'mult':
    return s.q.diff(by)/(fmath.square(fmath.cos(s.q)))
  def eval(s,**v)->float:
    return math.tan(s.q.eval(**v))
  def gettyp(s)->str:
    return "tan"
  def _copywithparam(s,p)->"param1":
    return tan(p)
  def minpos(s)->"float(possibly inf)":
    minq=s.q.minpos()
    maxq=s.q.maxpos()
    if abs(maxq-minq)>math.pi:return float("-inf")
    ret=math.tan(minq)
    tob=math.tan(maxq)
    if tob<ret:ret=tob
    return ret
  def maxpos(s)->"float(possibly inf)":
    minq=s.q.minpos()
    maxq=s.q.maxpos()
    if abs(maxq-minq)>math.pi:return float("inf")
    ret=math.tan(minq)
    tob=math.tan(maxq)
    if tob>ret:ret=tob
    return retregister(tan(0.5))

addtrafo("tan",lambda v:True,lambda v:fmath.sin(v.q)/fmath.cos(v.q))

