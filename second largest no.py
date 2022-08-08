#second largest no
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if a>b and a>c:
    if b>c:
        print("b is second largest")
    else:
        print("c is second largest")
elif b>a and b>c:
    if a>c:
        print("a is second largest")
    else:
        print("c is second largest")

else:
    if a>b:
        print("a is second largest")
    else:
        print("b is second largest")
   