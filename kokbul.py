from math import sqrt

def get_digit(name):
    while True:
        x = input("{n} sayisini giriniz: ".format(n=name))
        if x.isdigit() or (x.startswith("-") and x[1:].isdigit()):
            return int(x)
        else:
            print("hatali giris, {} bir sayidir".format(name))

delta = lambda a,b,c : b**2-(4*a*c)

def karekok_bulma(a,b,c):
    disc = delta(a,b,c)
    if disc > 0:
        x1=(-b+sqrt(disc))/2*a
        x2=(-b-sqrt(disc))/2*a
        return x1, x2
    elif disc == 0:
        x=sqrt(-c/a)
        return x, -x
    else:
        raise ArithmeticError("reel kok yoktur")

def kok_varmi(a,b,c):
    try:
        karekok_bulma(a,b,c)
    except ArithmeticError:
        return False
    else:
        return True



print("polinomlar icin karekok bulma")
print("ax^2 + bx + c icin kok b^2-(4ac) ile hesaplanir")
a=get_digit("a")
b=get_digit("b")
c=get_digit("c")

if kok_varmi(a,b,c):
    print(*karekok_bulma(a,b,c))
else:
    print("kok yoktur")
