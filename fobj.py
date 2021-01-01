from abc import ABCMeta,abstractmethod

import json

from collector import *


# def max(*q):
  # """i really dont want to import np"""
  # assert len(q)>0,"cannot calculate maxima of nothing"
  # ret=q[0]
  # for zw in q[1:]:
    # if zw>ret:ret=zw
  # return ret
# def min(*q):
  # """i really dont want to import np"""
  # assert len(q)>0,"cannot calculate minima of nothing"
  # ret=q[0]
  # for zw in q[1:]:
    # if zw<ret:ret=zw
  # return ret

def fromdict(d):
  """central reading function"""
  global collector
  return collector[d["typ"]].fromdict(d)

def load(fil):
  with open(fil,"r") as f:
    return fromdict(json.loads(f.write()))


class fobj(object):
  """central formulaic object, each other part of the formula should inherit this class

Minimum required functions:
  def __str__(s)->str:
  def asdict(s)->dict:
  def fromdict(s,d)->'fobj':
  def diff(s,by)->'fobj':
  def listvar(s)->"(str)":
  def eval(s,**v)->float:
  def gettyp(s)->str:
  def copy(s)->'fobj':
  def simplify(s)->'fobj':
  def removeepsilon(s)->'fobj':
  def order(s)->None:
  def match(s,shape,dic=None)->"bool,dic":
  def deepmutate(s)->"[fobj]":
  def applyfunc(s,nam,fun)->"fobj":
  def listfunc(s)->"(str)":
  def mutate(s,v=None)->"fobj":
  def applyvar(s,nam,var)->"fobj":
  def huntident(s)->"fobj":
  def countme(s,p)->"int":
  def findparamforfunc(s,f)->"[str]":
  def minpos(s)->"float(possibly inf)":
  def maxpos(s)->"float(possibly inf)":


"""
  __metaclass__=ABCMeta

  def __init__(s):
    pass
  
  @abstractmethod
  def __str__(s)->str:
    """This functions converts the current object into a string. Needs to be implemented to keep each object neat."""
    pass
  
  def __repr__(s):
    return str(s)

  @abstractmethod
  def asdict(s)->dict:
    """This function converts the object into a dictionary. Should then only contain basic (json serializable) types). Is used to save the formula"""
    pass
    
  @abstractmethod
  def fromdict(s,d)->"fobj":
    """This function returns a new fobj by reading in a dictionary. Is used to read in formulä that were saved by asdict before"""
    pass

  def readdict(s,v)->"fobj":
    """just a helper function, using fromdict and json to read in a string"""
    return s.fromdict(json.loads(v))

  @abstractmethod
  def diff(s,by)->"fobj":
    '''differentiates the current object by "by". Forces each set of objects you implement to be selfconsistent (you cannot implement sin(x) but not cos(x)'''
    pass
  
  @abstractmethod
  def listvar(s)->"(str)":
    """helper func that just lists all variables that are used in the current tree"""
    pass
    
  def evaluable(s,**v)->bool:
    """simple function that returns if the function is evaluable assuming the variables in v. Should be overwritten for special functions (consider x*y, which is evaluable when v={x:0})"""
    vv=s.listvar()
    for av in vv:
      if not av in v.keys():return False
    return True

  @abstractmethod
  def eval(s,**v)->float:
    """Evaluate the current tree by the variables given in **v"""
    pass
  
  @abstractmethod
  def gettyp(s)->str:
    """should return a simple identifier. Used for the reading system"""
    pass

  @abstractmethod
  def copy(s)->"fobj":
    """a simple deep copy function"""
    pass
    
  @abstractmethod
  def simplify(s)->'fobj':
    """trivial simplification function. Things that are obvious should enter here (x*0=0, etc...)"""
    pass
    
  @abstractmethod
  def removeepsilon(s)->'fobj':
    """a method that is used to remove numerical errors, aka round each object to the neirest value. Accuracy defined by ROUNDING_ACC"""
    pass
  
  def S(s)->'fobj':
    """a simple combination of simplification functions"""
    s0=str(s)
    s.order()
    ret= s.removeepsilon().simplify().removeepsilon()
    ret.order()
    ret=ret.huntident()
    s1=str(ret)
    if not s1==s0:return ret.S()
    return ret
  
  def __eq__(a,b)->bool:
    """using __str__ to compare two objects"""
    return str(a)==str(b)
    return a.asdict()==b.asdict()

  def __add__(a,b)->"add":
    return collector["+"]._copywithparam(a.copy(),b.copy())
  
  def __mul__(a,b)->"mul":
    return collector["*"]._copywithparam(a.copy(),b.copy())

  def __neg__(a)->"mul":
    return collector["*"]._copywithparam(collector["value"]._copywithparam(-1),a.copy())

  def __truediv__(a,b)->"divide":
    return collector["/"]._copywithparam(a.copy(),b.copy())

  def __sub__(a,b)->"subtr":
    return collector["-"]._copywithparam(a.copy(),b.copy())
  
  def __pow__(a,b)->"power":
    return collector["power"]._copywithparam(a.copy(),b.copy())
  
  @abstractmethod
  def order(s)->None:
    """does not return anything, but sorts everything. Minimal object at the beginning"""
    pass
  
  def __lt__(a,b)->bool:
    return str(a)<str(b)
  
  def __gt__(a,b)->bool:
    return str(a)>str(b)#yes I know, kind of redundant, but faster like this
  
  def __ne__(a,b)->bool:
    return not a==b
  
  def __le__(a,b)->bool:
    return str(a)<=str(b)
  
  def __ge__(a,b)->bool:
    return str(a)>=str(b)
  
  def match(s,shape,dic=None)->"bool,dic":
    """does this object match the given shape. Also returns the variables that are used. Works, but not very strong cos(x+y)+x+y does not match cos(a)+a. Also order can mess it up, since the variable name defines the position. Not the most useful function"""
    if dic is None:dic={}
    mt=s.gettyp()
    st=shape.gettyp()
    if st=="variable":
      nam=shape.q
      if nam in dic:
        return dic[nam]==s,dic
      else:
        dic[nam]=s.copy()
        return True,dic
    if not s.gettyp()==shape.gettyp():
      return False,dic
    return True,dic
    
  @abstractmethod
  def deepmutate(s)->"[fobj]":
    """using transform.mutate on each object in the tree and return each possible return"""
    pass
  
  def treestr(s)->"str":
    """using asdict and json.dumps to visualise the current tree"""
    return json.dumps(s.asdict(),indent=2)
  
  @abstractmethod
  def huntident(s)->"fobj":
    """removes semitrivial identities (mostly in permutaram, consider x+y after y is shown to be 0)"""
    return s.copy()

  @abstractmethod
  def applyfunc(s,nam,fun)->"fobj":
    """replaces all func of nam with fun"""
    pass
  
  @abstractmethod
  def applyvar(s,nam,var)->"fobj":
    """replaces all var of nam with var"""
    pass
  
  

  
  @abstractmethod
  def listfunc(s)->"(str)":
    """lists all functions that are used in the tree"""
    pass
  
  def listall(s)->"(str)":
    """helper function: listvar+listfunc"""
    ret=s.listvar()
    for zw in s.listfunc():
      ret.add(zw)
    return ret
  
  @abstractmethod
  def mutate(s,v=None)->"fobj":
    """randomly alters an object, v contains all variables (if None->listvar())"""
    pass

  def save(s,fil):
    with open(fil,"w") as f:
      f.write(json.dumps(s.asdict(),indent=2))

  def replace(s,nam,var)->"fobj":
    """just applyvar and applyfunc together"""
    return s.applyfunc(nam,var).applyvar(nam,var)

  @abstractmethod
  def countme(s,p)->"int":
    """function to count how often p appears in the tree"""
    pass

  @abstractmethod
  def findparamforfunc(s,f)->"[str]":
    """find the parameters for the first mention of the function with name f"""
    pass
  
  @abstractmethod
  def setparamforfunc(s,f,p)->"fobj":
    """set the parameters of each function f to be p"""
    pass
  
  @abstractmethod
  def minpos(s)->"float(possibly inf)":
    """return an approximation of the minimum value this expression can have. Fails if there are any int/diff (or special functions). Only approximation for standart function (z.B. -), since correlation between subobjects possible (z.B. -.q1=-.q2). Should be true, that the real minimum value is above this value"""
    pass
  @abstractmethod
  def maxpos(s)->"float(possibly inf)":
    """return an approximation of the maximum value this expression can have. Fails if there are any int/diff (or special functions). Only approximation for standart function (z.B. -), since correlation between subobjects possible (z.B. -.q1=-.q2). Should be true, that the real maximum value is below this value"""
    pass
  
  def mininp(s)->"float(possibly inf)":
    """helper function that gives the maximum possible input for the current formula. Does not use the tree, but the current object. Does not understand different input ranges or noncontinouos ranges)"""
    return float("-inf")
  def maxinp(s)->"float(possibly inf)":
    """helper function that gives the maximum possible input for the current formula. Does not use the tree, but the current object. Does not understand different input ranges or noncontinouos ranges)"""
    return float("+inf")
  
  def solvable(s)->"bool":
    """approximates if this tree is solvable (find variables so that f(x)=0). To do this it used minpos and maxpos"""
    return s.minpos()*s.maxpos()<=0
  
  
  
  