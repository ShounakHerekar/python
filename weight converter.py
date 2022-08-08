#weight converter
w=int(input("w:"))
ask=input("Is w in lbs(lorL) or kg(korK):")
if ask=="l" or ask=="L":
    k=w/2.205
    print("weight in kilo is:"+str(k))
elif ask=="k" or ask=="K":
    l=w*2.205
    print("weight in lbs is:"+str(l))
else:
    print("enter the damn thing again!")