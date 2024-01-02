def hauteur_parcourue(nbr_marche,hauteur):
    distance_parcourue_cm=5*7*2*(nbr_marche*hauteur)
    distance_parcourue= distance_parcourue_cm*10**-2
    return distance_parcourue


nbr_marche_saisie=int(input("saisissez le nombre de marche : "))
hauteur=int(input("saisissez la hauteur : "))

print(f"pour {nbr_marche_saisie} marches de {hauteur} cm, le gardien parcourt {hauteur_parcourue(nbr_marche_saisie,hauteur)} m par semaine.")