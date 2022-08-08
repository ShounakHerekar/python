def per(n,r):
    fact=1
    fact1=1
    for i in range(1,n+1):
        fact=fact*i
    for j in range(1,(n-r)+1):
        fact1=fact1*j
    
    per=fact//fact1
    return per

n=int(input("n:"))
r=int(input("r:"))
print(per(n,r))