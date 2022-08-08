def Leap(year):
    if year%4==0:
        if year%100!=0:
            leap=True
        else:
            if year%400==0:
                leap=True
            else :
                leap=False
    else:
        leap=False

    return leap
        
year=int(input("year:"))
print(Leap(year))
