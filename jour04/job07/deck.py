#!/usr/bin/env python3
from carte import Carte
import random

class Deck:
    def __init__(self) -> None:
        self.__deck52 = self.get_paquet()

    def get_deck52(self):
        return self.__deck52

    def get_paquet(self):
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        couleurs = ["Pique", "Coeur", "Trèfle", "Carreau"]
        paquet = [Carte(valeur,couleur)for valeur in valeurs for couleur in couleurs]
        random.shuffle(paquet)
        return paquet

    def distribuerCarte(self):
        return self.__deck52.pop()
    