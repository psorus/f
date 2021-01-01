from param1 import *
from collector import *

import fmath

import math

class exp(param1):
  def __init__(s,p):
    param1.__init__(s)
    s.q=p
  def diff(s,by)->'mult':
    return s*s.q.diff(by)
  def eval(s,**v)->float:
    return math.exp(s.q.eval(**v))
  def gettyp(s)->str:
    return "exp"
  def _copywithparam(s,p)->"param1":
    return exp(p)
  def huntident(s)->"fobj":#should not need to implement this everywhere when I use trigonometrics style stuff, but for now
    if s.q.gettyp()=="log":return s.q.q.huntident()
    return param1.huntident(s)
  def minpos(s)->"float(possibly inf)":
    return math.exp(s.q.minpos())

  def maxpos(s)->"float(possibly inf)":
    return math.exp(s.q.maxpos())
register(exp(0))