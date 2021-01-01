class double(object):
  """forget it, kinda useless, float("inf")"""
  def __init__(s,v=0,typ=0):
    s.setvalue(v,typ)
    
  def setvalue(s,v=0,typ=0):
    """value v, and typ that is 0 for numeric, 1 for infinity and -1 for -infinity"""
    if typ==0:
      s.v=float(v)
    elif typ>0:
      s.v="infinity"
    else:
      s.v="-infinity"

  def __repr__(s):
    return str(s)
  def __str__(s):
    return str(s.v)
  
  def isfinite(s):
    return type(s.v) is float
  
  def __float__(s):
    
  
  def __add__
  
  