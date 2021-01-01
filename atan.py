from param1 import *
from collector import *
from transform import addtrafo,addinv

import fmath

import math

class atan(param1):
  def __init__(s,p):
    param1.__init__(s)
    s.q=p
  def diff(s,by)->'divide':
    return s.q.diff(by)/(fmath.value(1)+fmath.square(s.q))
  def eval(s,**v)->float:
    return math.atan(s.q.eval(**v))
  def gettyp(s)->str:
    return "atan"
  def _copywithparam(s,p)->"param1":
    return atan(p)
  def minpos(s)->"float(possibly inf)":
    return math.atan(s.q.minpos())

  def maxpos(s)->"float(possibly inf)":
    return math.atan(s.q.maxpos())
register(atan(1.0))

addinv("tan","atan")




