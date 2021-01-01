

class ferror(Exception):
  def __init__(s,m,d):
    super().__init__(m+"\nThis error did occour in\n"+str(d))

class NotEvaluatableException(ferror):
  
  def __init__(s,d):
    super().__init__("This object is not evaluable.",d)


class InvalidInitializerException(ferror): 
  def __init__(s,d,ini):
    super().__init__("The given initializers were not enough to generate an object of type "+str(d.gettyp())+"\nGiven initialisers were "+str(ini),d)

class NonApproximatibleException(ferror):
  def __init__(s,d):
    super().__init__("There is not enough Information to approximate this value",d)


