n=int(input("n:"))
sum=0
d=0
while n!=0:
    d=n%10
    n=n//10
    sum=sum+d

print("digit sum is:",sum)
    