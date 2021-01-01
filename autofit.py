
from scipy.optimize import minimize

import random
import fmath

from const import *

#ignores signs!


def eval(guess,nam,x,y,ff,var,sigma):
  f=ff.copy()
  for g,n in zip(guess,nam):
    f=f.applyvar(n,fmath.value(g))
  try:
    fx=[f.eval(**{var:xx}) for xx in x]
  except:
    return 1e100
  ret=0.0
  for a,b in zip(fx,y):
    ret+=(abs(a)-abs(b))**2
  return ret/len(y)

def autofit(x,y,f,sigma=None):
  """returns fitting acc and fitting param"""
  if sigma is None:sigma=1
  if type(sigma) is int:sigma=float(sigma)
  if type(sigma) is float:
    sigma=[sigma for q in x]
  v=list(f.listvar())
  if INPUT_VAR in v:
    v.remove(INPUT_VAR)
    # del v[v.find(INPUT_VAR)]
  
  if len(v)>0:
    m=minimize(eval,[random.random() for vv in v],args=(v,x,y,f,INPUT_VAR,sigma))
  else:
    return eval([],[],x,y,f,INPUT_VAR,sigma),{}
  
  return m.fun,{a:b for a,b in zip(v,m.x)}



if __name__=="__main__":
  from importall import *

  from transform import *

  import trigonometrics
  import fmath
  
  f=fmath.exp(fmath.variable("a")*fmath.variable("x"))
  
  fs=f.copy()
  fs=fs.applyvar("a",fmath.value(3.0))
  
  x=[i/15.0 for i in range(15)]
  y=[fs.eval(x=xx) for xx in x]
  print("fitting",f,"to find",fs)
  
  ret,fit=autofit(x=x,y=y,f=f)
  
  print(fit)
  
  exit()
  
  


