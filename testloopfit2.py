
from importall import *

from transform import *

import trigonometrics
import fmath

import xevo
from evofit import *
from trivmute import *

import math
import numpy as np

sigma=0.03
x=[i/10 for i in range(100)]
y=[math.exp(3*xx)+np.random.normal(0,sigma,1)[0] for xx in x]
# y=[3*xx+np.random.normal(0,sigma,1)[0] for xx in x]

# obj=evofit(x=x,y=y,sigma=sigma,f=fmath.exp(fmath.variable("a")*fmath.variable("x")))
# obj=evofit(x=x,y=y,sigma=sigma,f=fmath.sin(fmath.tanh(fmath.variable("x"))))


# print(obj)

# print(obj.strength())


# exit()





genetics=trivmute()
obj=evofit(x=x,y=y,sigma=sigma)

goalstrength=100.0
maxsteps=10000000

def runone(show=True):
  global c
  c=xevo.erun(genetics.copy(),obj,show=show,population=100,delay=0.001)
  c.run(goalstrength=goalstrength,maxsteps=maxsteps)

runone()

print(c.getwinner())

c.show_history(log=True)

