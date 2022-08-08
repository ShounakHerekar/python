#guess
n=9
i=1 #count
while i<4: #limit
  guess=int(input("guess:"))
  i=i+1
  if guess==n:
        print("good guess")
        break
else:
    print("guess again")




