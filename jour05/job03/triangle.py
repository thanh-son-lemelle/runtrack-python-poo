"""height = input 
w = 0
for h in range(height):
    w+=1
    print("/","","\")"""

def afficher_triangle(hauteur):
    y=0
    for i in range(hauteur):
        if i < (hauteur - 1):
            espaces = " " * (hauteur - i - 1)
            barre1 = "/" 
            barre2 = "\\"
            espaces2 = " " * (i + y)
            ligne = espaces + barre1 +espaces2 + barre2
            y+=1
            print(ligne)
        else:
            espaces = " " * (hauteur - i - 1)
            barre1 = "/" 
            barre2 = "\\"
            espaces2 = " " * (i + y)
            underscore = "_" * (i + y)
            ligne = espaces + barre1+ underscore + barre2
            print(ligne)

# Demander à l'utilisateur la hauteur du triangle
hauteur_triangle = int(input("Entrez la hauteur du triangle : "))

# Appeler la fonction pour afficher le triangle
afficher_triangle(hauteur_triangle)