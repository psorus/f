


  

def alphabet(modulo=1):
  while True:
    for i in range(65+32,91+32):
      for j in range(modulo):
        yield chr(i)

def infinite():
  lea=26
  border=lea
  gen=[alphabet()]
  
  i=0
  while True:
    yield "".join([zw.__next__() for zw in gen])
    i+=1
    if i==border:
      gen.insert(0,alphabet(modulo=border))
      border*=lea
      i=0
  

if __name__=="__main__":


  for i,q in enumerate(infinite()):
    print(q)
    
    # if i>20:break

