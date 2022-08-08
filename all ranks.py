a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if a>b and a>c:
    print("a is largest")
    if b>c:
        print("b is second largest")
        print("c is third largest")
    else:
        print("c is second largest")
        print("b is third largest")
    
elif b>a and b>c:
    print("b is largest")
    if a>c:
        print("a is second largest")
        print("c is third largest")

    else:
        print("c is second largest")
        print("a is third largest")

else:
    print("c is largest")
    if a>b:
        print("a is second largest")
        print("b is third largest")
    else:
        print("b is second largest")
        print("a is third largest")
   