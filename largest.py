def largest(a,b,c):
    if a>b and a>c:
        print("a is largest")
    if b>c and b>a:
        print('b is largest')
    if c>a and b<c:
        print("c is largest")

largest(1,c=2,b=4)