
i=0
chaine="abcdefghijklmnopqrstuvwxyz"*10
print(len(chaine))



while i <= (len(chaine)+1):
    print(chaine[0:i])
    if i <=0:
        i+=1
    else:
        i+=2


""""
i=0
n=0
n=input("entrez un entier supérieur à zero (N) : ")
r=0
while int(i) <= int(n):
    print("table de multiplication de ", i, ": ")
    for i in range(0,10,1):
        r=n * i
        print(n,"x",i,"=",r)
"""
""""
print("-----------------------------")
print("-----------------------------")
# Chaîne de base
base_string = "abcdefghijklmnopqrstuvwxyz" * 10

# Longueur de la chaîne
length = len(base_string)

# Affichage sous forme de suite pyramidale
for i in range(1, length + 1):
    # Sélectionner les caractères à afficher pour cette rangée
    characters_to_display = base_string[:i]

    # Afficher la rangée avec des espaces entre les caractères
    print(length - i)


"""