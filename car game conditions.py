#car
cmd=""
while True:
    prev =cmd
    cmd=input("give input :").lower()
    
    if cmd==prev:
        print("already done")
        continue
    if cmd=="start":
        print("Ready set go!!!")
    elif cmd=="help" :
        print('''
start - start the car
stop - stop the car
quit - end game '''
        )
    elif cmd=="stop" :
        print("Stop the car")
    elif cmd=="quit":
        break
    else:
        print("Invalid input")
    
    
    
    
    



         

      
 