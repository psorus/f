from collector import collector as c
import math
from const import *

import random

def sin(x):
  return c["sin"]._copywithparam(x.copy())
def cos(x):
  return c["cos"]._copywithparam(x.copy())
def tan(x):
  return c["tan"]._copywithparam(x.copy()) 
def asin(x):
  return c["asin"]._copywithparam(x.copy())
def acos(x):
  return c["acos"]._copywithparam(x.copy())
def atan(x):
  return c["atan"]._copywithparam(x.copy()) 
def sinh(x):
  return c["sinh"]._copywithparam(x.copy())
def cosh(x):
  return c["cosh"]._copywithparam(x.copy())
def tanh(x):
  return c["tanh"]._copywithparam(x.copy()) 
def asinh(x):
  return c["asinh"]._copywithparam(x.copy())
def acosh(x):
  return c["acosh"]._copywithparam(x.copy())
def atanh(x):
  return c["atanh"]._copywithparam(x.copy()) 

def log(x):
  return c["log"]._copywithparam(x.copy())
def ln(x):
  return c["ln"]._copywithparam(x.copy())
def exp(x):
  return c["exp"]._copywithparam(x.copy()) 

def sqrt(x):
  return x.copy()**value(0.5)
def square(x):
  return x.copy()**value(2)


oneparam=[sin,cos,tan,asin,acos,atan,sinh,cosh,tanh,asinh,acosh,atanh,log,exp,sqrt,square]
oneparam=[sin,cos,tan,sinh,cosh,tanh,exp,square]#removing all divergences for now

def doadd(*q):
  ret=q[0]
  for i in range(1,len(q)):
    ret+=q[i]
  return ret
def domult(*q):
  ret=q[0]
  for i in range(1,len(q)):
    ret*=q[i]
  return ret
def dosubtr(q1,q2):
  return q1-q2
def dodivide(q1,q2):
  return q1/q2
def dopow(q1,q2):
  return q1**q2 

mulparam=[doadd,domult,dosubtr,dodivide,dopow]#always having two param

def randomvariables():
  return list(set([INPUT_VAR,"a","b","c"]))
def rnd(depth=3,variables=None):
  if variables is None:variables=list(randomvariables())
  variables=list(variables)
  if len(variables)==0:return rnd(depth=depth,variables=None)

  if depth==0:return variable(random.choice(variables))
  if random.random()<0.25:return rnd(depth=depth-1,variables=variables)
  l1=len(oneparam)
  lm=len(mulparam)
  l=l1+lm
  i=random.random()*l/1.000001
  i=int(math.floor(i))
  if i<l1:
    return oneparam[i](rnd(depth=depth-1,variables=variables))
  else:
    i-=l1
    return mulparam[i](rnd(depth=depth-1,variables=variables),rnd(depth=depth-1,variables=variables))




def diff(what,by):
  return c["diff"]._copywithparam(what.copy(),by)
def diffplus(what,by):
  return c["diffplus"]._copywithparam(what.copy(),by.copy())
def integrate(what,by,fro,too):
  return c["integrate"]._copywithparam(what.copy(),by,fro.copy(),too.copy())
def integrateplus(what,by,fro,too):
  return c["integrateplus"]._copywithparam(what.copy(),by.copy(),fro.copy(),too.copy())

def variable(x,v=None):
  return c["variable"]._copywithparam(x,v)
def value(x):
  return c["value"]._copywithparam(float(x))
def func(nam,*par):
  return c["func"]._copywithparam(nam,*par)

def var(x):
  try:
    return value(x)
  except:
    return variable(x)

def newvar(q,offs=""):
  for i in range(65+32,91+32):
    ac=offs+str(chr(i))
    if not ac in q:return ac
  return random.choice(q)#because why so many params
    


