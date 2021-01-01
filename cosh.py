from param1 import *
from collector import *

# from sin import *
# from mult import *
# from value import *
import fmath

import math

class cosh(param1):
  def __init__(s,p):
    param1.__init__(s)
    s.q=p
  def diff(s,by)->'mult':
    return fmath.sinh(s.q.copy())*s.q.diff(by)
  def eval(s,**v)->float:
    return math.cosh(s.q.eval(**v))
  def gettyp(s)->str:
    return "cosh"
  def _copywithparam(s,p)->"param1":
    return cosh(p)
  def minpos(s)->"float(possibly inf)":
    minq=s.q.minpos()
    maxq=s.q.maxpos()
    if minq*maxq<=0.0:return float(1.0)
    mint=math.tan(minq)
    maxt=math.tan(maxq)
    return min(mint,maxt)
  def maxpos(s)->"float(possibly inf)":
    return max(math.tan(s.q.maxpos()),math.tan(s.q.maxpos()))
register(cosh(1.0))