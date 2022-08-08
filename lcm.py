#lcm
n=int(input("n:"))
lcm=1
for i in range (1,n/2):
    q=n//i
    lcm=lcm*q
print("lcm is :",lcm)