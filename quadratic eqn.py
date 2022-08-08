#quadratic eqn
import math
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
d=b**2-4*a*c
if d>0:
    x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    print("x1:"+str(x1))
    print("x2:"+str(x2))
else :
    print("Enter again.")

