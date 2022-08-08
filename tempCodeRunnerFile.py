if year%4==0:
        if year%100!=0:
            print("True")
        else:
            if year%400==0:
                print("True")
            else:
                print("False")
