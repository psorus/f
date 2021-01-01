from permutaram import *
from collector import *

from add import *

class mult(permutaram):

  def __init__(s,*q):
    permutaram.__init__(s,*q)

  def _copywithparam(s,*p):
    return mult(*p)
  
  def eval(s,**v)->float:
    ret=1.0
    for qq in s.q:
      ret*=qq.eval(**v)
    return ret
      
  def diff(s,by)->"add":
    rel=[]
    for i,ac in enumerate(s.q):
      zw=[ac.diff(by)]
      for j,ac2 in enumerate(s.q):
        if j==i:continue
        zw.append(ac2.copy())
      rel.append(mult(*zw))
    return add(*rel)

  def gettyp(s)->str:
    return "*"
  def simplify(s)->"mult":
    ret=permutaram.simplify(s)
    if ret.evaluable():return ret
    k=[zw for zw in ret.q if not (zw.evaluable() and zw.eval()==1.0)]
    i=[1 for zw in k if zw.evaluable() and zw.eval()==0.0]
    if len(i)>0:return value(0.0)
    return s._copywithparam(*k)
  def minpos(s)->"float(possibly inf)":
    ret=1.0
    for zw in s.q:
      ret*=zw.minpos()
    return ret
  def maxpos(s)->"float(possibly inf)":
    ret=1.0
    for zw in s.q:
      ret*=zw.maxpos()
    return ret
register(mult())


