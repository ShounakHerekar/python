from tempfile import tempdir


def exch(a,b):
    temp=a
    a=b
    b=temp
    print(f"{a} {b}")
    return 0

a=int(input("a:"))
b=int(input("b:"))
print(exch(a,b))
