from const import *


def removeepsilon(q):
  return round(q,ROUNDING_ACC)

def compsort(q):
  """sorting function, by just comparing elements to elements, requires implementation of __gt__. Probably not the fastest version (n**2)"""
  ret=[]
  for j,qq in enumerate(q):
    for i,k in enumerate(ret):
      if k>qq:
        ret.insert(i,qq)
        break
    if len(ret)<=j:ret.append(qq)
  return ret

if __name__=="__main__":
  q=[5,2,7,4,2,7,4,9]

  p=compsort(q)
  
  print(q)
  print(p)
  



