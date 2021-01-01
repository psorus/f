from param1 import *
from collector import *
from transform import addtrafo,addinv
from const import *


import fmath

import math

class log(param1):
  def __init__(s,p):
    param1.__init__(s)
    s.q=p
  def diff(s,by)->'divide':
    return s.copy()/s.q.diff(by)
  def eval(s,**v)->float:
    return math.log(s.q.eval(**v))
  def gettyp(s)->str:
    return "log"
  def huntident(s)->"fobj":#should not need to implement this everywhere when I use trigonometrics style stuff, but for now
    if s.q.gettyp()=="exp":return s.q.q.huntident()
    return param1.huntident(s)
  def _copywithparam(s,p)->"param1":
    return log(p)
  def mininp(s)->"float(possibly inf)":
    return EPSILON
  def minpos(s)->"float(possibly inf)":
    mp=max(EPSILON,s.q.minpos())
    return math.log(mp)

  def maxpos(s)->"float(possibly inf)":
    mp=max(EPSILON,s.q.maxpos())#could have weird consequences...but should not matter i guess
    return math.log(mp)


register(log(1.0))
addinv("log","exp")

