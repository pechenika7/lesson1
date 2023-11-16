def Eucl1(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return(a)

def Eucl2(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return(a+b)

a = int(input())
b = int(input())
print(Eucl1(a,b))
print(Eucl2(a,b))