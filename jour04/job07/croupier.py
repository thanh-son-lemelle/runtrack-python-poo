from joueur import Joueur

class Croupier(Joueur):
    def jouer(self, deck):
        while self.calculePoint() < 17:
            carte = deck.distribuerCarte()
            self.get_carte(carte)
            self.montrerCarte()