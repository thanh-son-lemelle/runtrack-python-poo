#!/usr/bin/env python3

from personnage import Personnage
class Jeu:
    def __init__(self) -> None:
        self.__niveau = None

    def choisirNiveau(self):
        self.__niveau = int(input("Choisissez le niveau de diffuclté"))

    def lancerJeu(self):
        self.choisirNiveau()

        vieJoueur = self.__niveau * 5 +200
        vieAdversaire = self.__niveau * 10 +200

        joueur = Personnage ("Joueur", vieJoueur)
        adversaire = Personnage ("Adversaire", vieAdversaire)

        while joueur.get_vie() > 0 and adversaire.get_vie() > 0:
            print(f"Vie de l'adversaire: {adversaire.get_vie()}")
            joueur.attaquer(adversaire)
            print(f"Vous infligez {joueur.get_degatsinfligé()}\nVie de l'adversaire: {adversaire.get_vie()}\n")
            if adversaire.get_vie() <= 0:
                return f"{adversaire.get_nom()} a été vaincu. {joueur.get_nom()} a gagné!"
            print(f"Vie du joueur: {joueur.get_vie()}")
            adversaire.attaquer(joueur)
            print(f"Vous reçevez {adversaire.get_degatsinfligé()} dommages\nVie du joueur: {joueur.get_vie()}\n")
            if joueur.get_vie() <= 0:
                return f"{joueur.get_nom()} a été vaincu. {adversaire.get_nom()} a gagné!"

