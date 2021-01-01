from param2 import *
from collector import *

from mult import *
from subtr import *

from ferror import *

class divide(param2):
  def __init__(s,*q):
    param2.__init__(s)
    if len(q)>2:
      s.q1,s.q2=q[0],mult(*q[1:])
    elif len(q)<2:
      raise InvalidInitializerException(s,q)
    else:
      s.q1,s.q2=q
    
  def diff(s,by)->'divide':
    return divide(subtr(mult(s.q2.copy(),s.q1.diff(by)),mult(s.q1.copy(),s.q2.diff(by))),mult(s.q2.copy(),s.q2.copy()))
  def eval(s,**v)->float:
    return s.q1.eval(**v)/s.q2.eval(**v)
  def gettyp(s)->str:
    return "/"
  def _copywithparam(s,p1,p2)->"param2":
    return divide(p1,p2)
  def __str__(s)->str:
    return "("+str(s.q1)+s.gettyp()+str(s.q2)+")"
  
  def huntident(s)->"fobj":
    if s.q2.evaluable() and s.q2.eval()==1.0:return s.q1.huntident()
    return param2.huntident(s)

  def minpos(s)->"float(possibly inf)":
    return s.q1.minpos()/s.q2.maxpos()
  def maxpos(s)->"float(possibly inf)":
    return s.q1.maxpos()/s.q2.minpos()



register(divide(1.0,1.0))