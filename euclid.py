def Eucl1(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return(a)

a = int(input())
b = int(input())
print(Eucl1(a,b))