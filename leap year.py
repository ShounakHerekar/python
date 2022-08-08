n=int(input("n:"))
leap=True
if n%4==0:
    if n%100==0:
        if n%400==0:
            leap=True
        else:
            leap=False
    else:
        leap=True

print(leap)

    