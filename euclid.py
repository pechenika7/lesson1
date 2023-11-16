def Eucl1(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return(a)

def Eucl2(a,b):
    while True:
        if a > b:
            try:
                a = a % b
            except:
                return a
        else:
            try:
                b = b % a
            except:
                return b

a = int(input())
b = int(input())
print(Eucl1(a,b))
print(Eucl2(a,b))