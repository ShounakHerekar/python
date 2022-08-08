#calculator
a=int(input("a:"))
b=int(input("b:"))
ask=input("give operator:")
if ask=="+":
    print(a+b)
elif ask=="-":
    print(a-b)
elif ask=="*":
    print(a*b)
elif ask=="/":
    print(a/b)
elif ask=="//":
    print(a//b)
elif ask=="**":
    print(a**b)
else:
    print("Enter again")
 