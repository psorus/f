from permutaram import *
from collector import *

class add(permutaram):

  def __init__(s,*q):
    permutaram.__init__(s,*q)

  def _copywithparam(s,*p):
    return add(*p)
  
  def eval(s,**v)->float:
    ret=0.0
    for qq in s.q:
      ret+=qq.eval(**v)
    return ret
      
  def diff(s,by)->"add":
    return add(*[ac.diff(by) for ac in s.q])

  def gettyp(s)->str:
    return "+"
    
  def simplify(s)->"add":
    ret=permutaram.simplify(s)
    if ret.evaluable():return ret
    k=[zw for zw in ret.q if not (zw.evaluable() and zw.eval()==0.0)]
    return s._copywithparam(*k)
  def minpos(s)->"float(possibly inf)":
    ret=0.0
    for zw in s.q:
      ret+=zw.minpos()
    return ret
  def maxpos(s)->"float(possibly inf)":
    ret=0.0
    for zw in s.q:
      ret+=zw.maxpos()
    return ret
register(add())


