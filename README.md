# f
do some complicated math using polymorphy


This is my implementation of symbolic math in python. This is not finished, so if you want general symbolic math, let my suggest sympy. Even though sympy is great, it did not give me the freedom I need to solve the problems I want.

It consists out of two parts, which both work, even though I have basically just tested the simplest example.


First, testloopfit2.py uses xevo (package written by me) to try to build function trees to fit to some data. Using this you could fit any f(x)=y without needing to have a function before. Its test was to fit the function exp(3x) from 0 to 10 (sigma=0.03), which it was able to do. Its resulting function was exp(exp(a)cosh(tan(cos(a)))x) where a is some fitting parameter. You migth think (as I did initially) that this is just way to complicated, as you could just define b(a)=exp(a)cosh(tan(cos(a))), and it is true, that my function tree mutator should more often just set a subtree to a variable, but there is more. If you look at b(a), b=3 at a≈0.61 and b(a) has a saddle point at b=3, which means, finding this value is fairly easy, especcially if you notice that I initialise each parameter randomly between 0 and 1, in which region, b(a) is basically 3 (see https://www.wolframalpha.com/input/?i=plot+exp%28a%29cosh%28tan%28cos%28a%29%29%29+from+0+to+1 ). So you could say, that my function generator is able to compensate for my terrible fitting algorithm (scipy.minimize, but random initial variables).


Secondly, testdgl.py is able to suggest possible solutions for differential equations. Its suggested dgl is f(x)-f'(x)=0 and it is able to suggest exp(x) (even though it also suggests a couple other functions)


Finally it you want to use it, each function is explained at the top level of the polymorphic tree (fobj which is inherited by param1,param2 and permutaram  (aswell as value, variable,func,diff,diffplus,integrate), which inturn are inherited by each function) and the inherited classes explain the function you have to define in your object, and (param1,param2 and permutaram) give some general behaviour (permutaram for example assumes that there is an arbitrary amount of parameters in this function, and that each is permutable (like a sum for example). This you would get by calling help(permutaram))

