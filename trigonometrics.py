from fmath import *
from transform import *
from transform import addtrafo as addt

zero=value(0.0)
one=value(1.0)
mone=value(-1.0)
two=value(2.0)
three=value(3.0)
fourth=value(4.0)
pi=variable("pi",math.pi)
halfpi=pi/two
thirdpi=pi/three
fourthpi=pi/fourth




addt("sin",
     lambda v:True,
     lambda v:-v._copywithparam(-v.q))
addt("cos",
     lambda v:True,
     lambda v:v._copywithparam(-v.q))
addt("tan",
     lambda v:True,
     lambda v:-v._copywithparam(-v.q))

addt("cos",
     lambda v:True,
     lambda v:sin(halfpi-v.q))
addt("sin",
     lambda v:True,
     lambda v:cos(halfpi-v.q))
addt("tan",
     lambda v:True,
     lambda v:one/tan(halfpi-v.q))

addt("sin",
     lambda v:True,
     lambda v:-v._copywithparam(pi+v.q))
addt("cos",
     lambda v:True,
     lambda v:-v._copywithparam(pi+v.q))
addt("tan",
     lambda v:True,
     lambda v:-v._copywithparam(pi+v.q))

addt("cos",
     lambda v:True,
     lambda v:sin(v.q+halfpi))
addt("sin",
     lambda v:True,
     lambda v:cos(v.q-halfpi))
addt("cos",
     lambda v:True,
     lambda v:-sin(v.q-halfpi))
addt("sin",
     lambda v:True,
     lambda v:-cos(v.q+halfpi))
addt("tan",
     lambda v:True,
     lambda v:mone/tan(v.q+halfpi))

addt("sin",
     lambda v:v.q.gettyp()=="subtr",
     lambda v:(sin(v.q.q1)*cos(v.q.q2))-(cos(v.q.q1)*sin(v.q.q2))
    )
addt("cos",
     lambda v:v.q.gettyp()=="subtr",
     lambda v:(cos(v.q.q1)*cos(v.q.q2))+(sin(v.q.q1)*sin(v.q.q2))
    )
addt("sin",
     lambda v:v.q.gettyp()=="add",
     lambda v:(sin(v.q.q1())*cos(v.q.q2()))+(cos(v.q.q1())*sin(v.q.q2()))
    )
addt("cos",
     lambda v:v.q.gettyp()=="add",
     lambda v:(cos(v.q.q1())*cos(v.q.q2()))-(sin(v.q.q1())*sin(v.q.q2()))
    )

addt("tan",
     lambda v:v.q.gettyp()=="add",
     lambda v:(tan(v.q.q1())+tan(v.q.q2()))/(1-tan(v.q.q1())*tan(v.q.q2()))
    )
addt("tan",
     lambda v:v.q.gettyp()=="subtr",
     lambda v:(tan(v.q.q1())-tan(v.q.q2()))/(1+tan(v.q.q1())*tan(v.q.q2()))
    )

#2cos(a)cos(b)=cos(a-b)+cos(a+b)
#Product-to-sum and sum-to-product identities
