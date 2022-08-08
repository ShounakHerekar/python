n=1234
i=1
while i<4:
    guess=int(input("give passcode:"))
    if guess!=n:
        if i==3:
            print("try again later")
        else:
            print("try again")
    else:
        print("welcome")
        break
    i=i+1
