#bill
n=int(input("Enter the no of items: "))
bill=0
for i in range(1,n+1):
    item=int(input("Enter the amount of items:$"))
    bill=bill+item
print("The bill is :$",bill)