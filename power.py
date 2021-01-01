from param2 import *
from collector import *

import fmath


class power(param2):
  def __init__(s,p1,p2):
    param2.__init__(s)
    s.q1,s.q2=p1,p2
    
  def diff(s,by)->'mult':
    f,g=s.q1,s.q2
    return ()*()
    return mult(power(f,subtr(g,value(1))),add(mult(g,f.diff(by)),mult(f,log(f),g.diff(by))))
  def eval(s,**v)->float:
    return s.q1.eval(**v)**s.q2.eval(**v)
  def gettyp(s)->str:
    return "power"
  def _copywithparam(s,p1,p2)->"param2":
    return power(p1,p2)
  def __str__(s)->str:
    return "("+str(s.q1)+"**"+str(s.q2)+")"
  def minpos(s)->"float(possibly inf)":
    return s.q1.minpos()**s.q2.minpos()
  def maxpos(s)->"float(possibly inf)":
    return s.q1.maxpos()**s.q2.maxpos()




register(power(1.0,1.0))