n=int(input())
list=input().split(" ")
for i in range(0,len(list)):
    list[i]=int(list[i])

list.sort()
lar=list[0]
sec=list[0]
for i in list:
    if i-1<i:
        largest=i
        index=list.index(i)

for j in range(index):
    if list[j]<largest:
        sec=list[j]




print(sec)