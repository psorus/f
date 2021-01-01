from param1 import *
from collector import *

# from sin import *
# from mult import *
# from value import *
import fmath

import math

class cos(param1):
  def __init__(s,p):
    param1.__init__(s)
    s.q=p
  def diff(s,by)->'mult':
    return -fmath.sin(s.q.copy())*s.q.diff(by)
  def eval(s,**v)->float:
    return math.cos(s.q.eval(**v))
  def gettyp(s)->str:
    return "cos"
  def _copywithparam(s,p)->"param1":
    return cos(p)
  def minpos(s)->"float(possibly inf)":
    minq=s.q.minpos()
    maxq=s.q.maxpos()
    if abs(maxq-minq)>math.pi:return float(-1)
    minqs=(minq+math.pi/2)%(2*math.pi)
    maxqs=(maxq+math.pi/2)%(2*math.pi)
    minq=min(minqs,maxqs)
    maxq=max(minqs,maxqs)
    if minq<3*math.pi/2 and maxq>3*math.pi/2:return -1.0
    return min(math.sin(minq),math.sin(maxq))
  def maxpos(s)->"float(possibly inf)":
    minq=s.q.minpos()
    maxq=s.q.maxpos()
    if abs(maxq-minq)>math.pi:return float(1)
    minqs=(minq+math.pi/2)%(2*math.pi)
    maxqs=(maxq+math.pi/2)%(2*math.pi)
    minq=min(minqs,maxqs)
    maxq=max(minqs,maxqs)
    if minq<math.pi/2 and maxq>math.pi/2:return 1.0
    return max(math.sin(minq),math.sin(maxq)) 

register(cos(1.0))