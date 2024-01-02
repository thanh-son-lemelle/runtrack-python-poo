a=0
b=0
c=0
resultat1=False
resultat2=False
resultat3=False
a=float(input("rentrez a : "))
b=float(input("rentrez b : "))
c=float(input("rentrez c : "))

if a + b > c and  a + c > b and b + c > a :
    resultat1=True
else:
    print("nous n'avons pas de triangle")

if resultat1 == True:
    print("nous avons un triangle")
    if a == b and b == c:
        print("le triangle est équilatéral")
    elif a == b and b!= c or a == c and a != b or b==c and c!=a:
        print("le triangle est isocèle")
        if (a**2 + b**2) == c**2 or (b**2+c**2) == a**2 or (c**2+a**2)==b**2:
            print("le triangle est aussi rectangle")
    elif (a**2 + b**2) == int(c**2) or (b**2+c**2) == int(a**2) or (c**2+a**2)==int(b**2):
        print("le triangle est rectangle")

