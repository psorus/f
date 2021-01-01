from param1 import *
from collector import *
from transform import addtrafo

import fmath

import math

class sin(param1):
  def __init__(s,p):
    param1.__init__(s)
    s.q=p
  def diff(s,by)->'mult':
    return fmath.cos(s.q)*s.q.diff(by)
  def eval(s,**v)->float:
    return math.sin(s.q.eval(**v))
  def gettyp(s)->str:
    return "sin"
  def _copywithparam(s,p)->"param1":
    return sin(p)

register(sin(1.0))


def test_sincos(v):
  for i,a in enumerate(v.q):
    for j,b in enumerate(v.q):
      if i==j:continue
      if a.gettyp()=="cos" and b.gettyp()=="sin":
        if a.q==b.q:return True
  return False
def apply_sincos(v):
  for i,a in enumerate(v.q):
    for j,b in enumerate(v.q):
      if i==j:continue
      if a.gettyp()=="cos" and b.gettyp()=="sin":
        if not a.q==b.q:continue
        ret=[]
        for k,zw in enumerate(v.q):
          if i==k or j==k:continue
          ret.append(zw)
        x=a.q.copy()
        ret.append(fmath.var(1/2))
        ret.append(fmath.sin(fmath.var(2)*x))
        return v._copywithparam(*ret)
  return v

  def minpos(s)->"float(possibly inf)":
    minq=s.q.minpos()
    maxq=s.q.maxpos()
    if abs(maxq-minq)>math.pi:return float(-1)
    minqs=minq%(2*math.pi)
    maxqs=maxq%(2*math.pi)
    minq=min(minqs,maxqs)
    maxq=max(minqs,maxqs)
    if minq<3*math.pi/2 and maxq>3*math.pi/2:return -1.0
    return min(math.sin(minq),math.sin(maxq))
  def maxpos(s)->"float(possibly inf)":
    minq=s.q.minpos()
    maxq=s.q.maxpos()
    if abs(maxq-minq)>math.pi:return float(1)
    minqs=minq%(2*math.pi)
    maxqs=maxq%(2*math.pi)
    minq=min(minqs,maxqs)
    maxq=max(minqs,maxqs)
    if minq<math.pi/2 and maxq>math.pi/2:return 1.0
    return max(math.sin(minq),math.sin(maxq)) 
  
  
addtrafo("*",test_sincos,apply_sincos)

addtrafo("sin",lambda v:v.q.evaluable() and v.q.eval()==0.0,lambda v:fmath.value(0.0))


