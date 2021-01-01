from xevo import eobj

import fmath
from autofit import *

import random
import math

class evofit(eobj):
  """using xevo and f to fit any x,y values into a function"""
  def __init__(s,x=None,y=None,sigma=None,price=1.2,f=None):
    s.initial()
    s.x=x
    s.y=y
    s.sigma=sigma
    s.price=price
    s.f=f
    if s.f is None:
      s.f=fmath.rnd()
  def __str__(s):
    return str(s.f)
  def __add__(a,b):
    return evofit(x=a.x,y=a.y,sigma=a.sigma,price=a.price,f=(a.f+b.f)/fmath.value(2))
  def shallmaximize(s):return False

  
  def randomize(s):
    return evofit(x=s.x,y=s.y,sigma=s.sigma,price=s.price,f=fmath.rnd())
  def mutate(s):
    if random.random()<0.8:
      return evofit(x=s.x,y=s.y,sigma=s.sigma,price=s.price,f=s.f.mutate())
    else:
      return s.randomize()
  def calcstrength(s):
    # print("trying out",s.f)
    ret= autofit(x=s.x,y=s.y,sigma=s.sigma,f=s.f.copy())[0]*(s.price**len(s.f.listvar()))*len(str(s.f))
    # print("fitting",s.f,"into",ret)
    return ret
  def _copy(s):
    return evofit(x=s.x,y=s.y,sigma=s.sigma,price=s.price,f=s.f.copy())
  def getsave(s):
    return s.f.save