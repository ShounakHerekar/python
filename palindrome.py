n=int(input("n:"))
sum=0
temp=n
d=0
while n!=0:
    d=n%10
    n=n//10
    sum=sum*10+d

if sum==temp:
    print("palindrome")
else:
    print("not palindrome")    