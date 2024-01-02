def Add(nombre1,nombre2):
    resultat = nombre1 + nombre2
    print(nombre1,"+",nombre2,"=",resultat)
    print("--------------------------------")
Add(1,3)
Add(4,5)
Add(3,3)
"""autre façon de définir la fonction"""
print("====================================")

def Add2(a,b):
    c=a+b
    return c
print(Add2(5,5))