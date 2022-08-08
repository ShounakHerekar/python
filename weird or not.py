n=int(input())
r=n%2
if r!=0:
    print("Weird")
elif r==0 and n>=2 and n<=5 :
    print("Not Weird")
elif r==0 and (n>=6 and n<=20) :
    print("Weird")
else :
    if r==0 and n>20:
        print("Not Weird")

    