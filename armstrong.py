n=int(input("n:"))
sum=0
x=n
d=0
while n!=0:
    d=n%10
    n=n//10
    sum=sum+d**3
    
if sum!=x:
    print("its not armstrong")
else:
    print("armstrong")
    