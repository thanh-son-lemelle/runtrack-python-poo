#!/usr/bin/env python3

from joueur import Joueur

class Equipe:
    def __init__(self,nom) -> None:
        self.__nom = nom
        self.__listeDeJoueurs =[]
    
    def __str__(self) -> str:
        information1 = f"équipe: {self.__nom}\n"
        information2 ="\nListe des joueurs:"
        for joueur in self.__listeDeJoueurs:
            information2 += f"\n{joueur}"

        return information1 + information2

    def ajouterJoueur(self,joueur):
        self.__listeDeJoueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        information =""
        for joueur in self.__listeDeJoueurs:
            information += f"{joueur.afficherStatistiques()}"
        return information
    
    def mettreAjourStatistiquesJoueur(self, numeroJoueur, action):
        for joueur in self.__listeDeJoueurs:
            if joueur.get_numero() == numeroJoueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe_decisive":
                    joueur.effectuerUnePasseDecisive()
                elif action == "carton_jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "carton_rouge":
                    joueur.recevoirUnCartonRouge()