print("AB doit etre  le plus grand")


x1 = int(input("entrez coordone vecter 1 x "))
x2 = int(input("entrez coordone vecter 1 y "))
x3 = int(input("entrez coordone vecter 1 z "))
x4 = int(input("entrez coordone vecter 2 x "))
x5 = int(input("entrez coordone vecter 2 y "))
x6 = int(input("entrez coordone vecter 2 z "))



xab = x4 - x1 
yab = x5 - x2 
zab = x6 - x3



print("le vecteur AB et :", xab , yab , zab)


coordonevecteurAB = (xab , yab , zab)

x7 = int(input("entrez coordone vecter 3 x "))
x8 = int(input("entrez coordone vecter 3 y "))
x9 = int(input("entrez coordone vecter 3 z "))
x10 = int(input("entrez coordone vecter 4 x "))
x11 = int(input("entrez coordone vecter 4 y "))
x12= int(input("entrez coordone vecter 4 z "))



xbc = x10 - x7 
ybc = x11 - x8 
zbc = x12 - x9
print("le vecteur BC et :", xbc , ybc , zbc)
print("le vecteur AB et :", xab , yab , zab)
coordonevecteurBC = (xbc , ybc , zbc)

if xab/xbc == yab/ybc :
    print("le vecteur AB et AC collineaire")
elif xbc/xab ==ybc/yab:
    print("le vecteur AB et AC collineaire")
else:
    print("le vecteur AB pas colineraire")