import fmath

class trafo:
  def __init__(s,match,traf):
    s.match=match
    s.traf=traf
  
  def appliable(s,v)->bool:
    return s.match(v)
  def apply(s,v)->"fobj":
    return s.traf(v)
  def __getitem__(s,v)->"fobj":
    if s.appliable(v):
      return apply(v)
    else:
      return v.copy()
  
transformations={}

def addtrafo(what,match,traf):
  t=trafo(match,traf)
  global transformations
  if not what in transformations.keys():transformations[what]=[]
  transformations[what].append(t)

def addinv(a,b):
  addtrafo(a,lambda v:v.q.gettyp()==b,lambda v:v.q.q)
  addtrafo(b,lambda v:v.q.gettyp()==a,lambda v:v.q.q)

def mutations(*v):
  if len(v)>1:
    mm=[mutations(ac) for ac in v]
    ret=[]
    for x1 in mm:
      for x2 in x1:
        ret.append(x2)
    return ret
  else:
    v=v[0]
  ret=[]
  t=v.gettyp()
  if t in transformations.keys():
    for trafo in transformations[t]:
      if trafo.appliable(v):
        ret.append(trafo.apply(v))
  return ret
def _containedin(q,v):
  for qq in q:
    if qq==v:return True
  return False
def multideep(*v):
  ret=[]
  for vv in v:
    for k in vv.deepmutate():
      ret.append(k)
  return ret
def infinimut(v,maxn=-1):
  ret=[v.copy()]
  lastone=[v]
  
  i=0
  while len(lastone)>0:
    m=multideep(*lastone)
    nextone=[]
    for mm in m:
      mm=mm.S()
      if not _containedin(ret,mm):
        ret.append(mm.copy())
        nextone.append(mm.copy())
    lastone=nextone
    i+=1
    if i==maxn:
      break
  return ret


def permfind(v,k1,k2):
  posb=[]
  for i,a in enumerate(v.q):
    for j,b in enumerate(v.q):
      if i==j:continue
      if a.gettyp()==k1 and b.gettyp()==k2:
        posb.append([a.copy(),b.copy(),i,j])
  return posb
def permrest(v,*nt):
  ret=[]
  for k,zw in enumerate(v.q):
    if i in nt:continue
    ret.append(zw)
  return ret
