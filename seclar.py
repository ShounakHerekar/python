list=[]
n=int(input("n:"))
for i in range(n):
    data=int(input(">"))
    list.append(data)
list.sort()
largest=list[0]
sec=list[0]
sec=list
for i in list:
    if i-1<i:
        largest=i
        index=list.index(i)

for j in range(index):
    if list[j]<largest:
        sec=list[j]




print(sec)