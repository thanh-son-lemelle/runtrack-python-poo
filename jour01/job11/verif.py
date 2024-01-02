verif=input("Ecrire une phrase : ")
if "e" in verif and "E" in verif:
    print("vous avez les caractère e majuscule et minuscule")
elif "e" in verif:
    print("vous avez une lettre 'e' dans votre phrase")
elif "E" in verif:
    print("vous avez une lettre 'E' dans votre phrase")
else:
    print("vous n'avez ni 'e' ni 'E' dans votre phrase")