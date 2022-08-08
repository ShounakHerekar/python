n=int(input("n:"))
sum=0
for i in range(1,n+1):
    r=n%i
    if r==0:
        sum=sum+i
    if sum==n:
        print("perfect")
        break

if sum!=n:
    print("not perfect")


        






         