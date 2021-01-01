
from importall import *

from transform import *

import trigonometrics
import fmath

import xevo
from evofit import *

import math
import numpy as np

sigma=0.03
x=[i/10 for i in range(100)]
y=[math.exp(3*xx)+np.random.normal(0,sigma,1)[0] for xx in x]





obj=evofit(x=x,y=y,sigma=sigma)

goalstrength=100.0
maxsteps=10000000
mins=1e100


while obj.strength()>goalstrength:
  # obj=obj.mutate()
  if (obj.strength())<mins:
    mins=obj.strength()
  print(mins,obj.strength())
  obj=obj.randomize()



print(obj)


