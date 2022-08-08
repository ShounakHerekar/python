#calculate paycheck
hours=input("hours: ")
paycheck=int(hours)*100
taxcut=paycheck-(paycheck/5)
print("paycheck: "+str(paycheck))
print("taxcut: "+str(taxcut))
