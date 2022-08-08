n=[45,98,63,7412,65]
x=len(n)
largest=n[0]
for i in range (0,x):
    if n[i-1]<n[i]:
        largest=n[i]

print(largest,"is the largest")