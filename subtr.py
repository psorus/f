from param2 import *
from collector import *
from transform import addtrafo
from add import *

import fmath

from ferror import *

class subtr(param2):
  def __init__(s,*q):
    param2.__init__(s)
    if len(q)>2:
      s.q1,s.q2=q[0],add(*q[1:])
    elif len(q)<2:
      raise InvalidInitializerException(s,q)
    else:
      s.q1,s.q2=q
    
  def diff(s,by)->'subtr':
    return subtr(s.q1.diff(by),s.q2.diff(by))
  def eval(s,**v)->float:
    return s.q1.eval(**v)-s.q2.eval(**v)
  def gettyp(s)->str:
    return "-"
  def _copywithparam(s,p1,p2)->"param2":
    return subtr(p1,p2)
  def __str__(s)->str:
    return "("+str(s.q1)+s.gettyp()+str(s.q2)+")"
  def huntident(s)->"fobj":
    if s.q2.evaluable() and s.q2.eval()==0.0:return s.q1.huntident()
    return param2.huntident(s)
  def minpos(s)->"float(possibly inf)":
    return s.q1.minpos()-s.q2.maxpos()
  def maxpos(s)->"float(possibly inf)":
    return s.q1.maxpos()-s.q2.minpos()




register(subtr(0,0))
addtrafo("-",lambda v:v.q1==v.q2,lambda v:fmath.value(0.0))