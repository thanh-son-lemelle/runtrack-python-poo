from deck import Deck
from joueur import Joueur
from croupier import Croupier
from carte import Carte
class Jeu:
    def __init__(self) -> None:
        self.__deck = Deck()
        self.__joueurs = [Joueur("joueur"), Croupier("Croupier")]

    def tour1(self):
        for carte in range(2):
            for joueur in self.__joueurs:
                joueur.get_carte(self.__deck.distribuerCarte())
    
    def tour(self, joueur):
        joueur.montrerCarte()
        while True:
            
            choix = input(f"{joueur.get_nom()}, pour tirer une carte choisissez (t) ou (p) pour passer : ").lower()

            if choix == "t":
                joueur.get_carte(self.__deck.distribuerCarte())
                joueur.montrerCarte()
                points = joueur.calculePoint()

                if points > 21:
                    print(f"Perdu!! Vous avez dépassé 21.")
                    return
                elif points == 21:
                    print(f"{joueur.get_nom()}, vous avez un blackJack !")
                    return
            elif choix == "p":
                print("vous passez.")
                break
            else:
                print("choix invalide. Saisir (t) ou (p)")

    def jouer(self):
        self.tour1()

        for joueur in self.__joueurs[:-1]:
            self.tour(joueur)
        
        self.__joueurs[-1].jouer(self.__deck)

        for joueur in self.__joueurs[:-1]:
            pointsDuJoueur = joueur.calculePoint()
            pointsDuCroupier = self.__joueurs[-1].calculePoint()

            print(f"\nTotal {joueur.get_nom()} : {pointsDuJoueur}")
            print(f"Total Croupier : {pointsDuCroupier}")

            if pointsDuJoueur > 21 or (pointsDuCroupier <= 21 and pointsDuCroupier >= pointsDuJoueur):
                print(f"{joueur.get_nom()}, vous avez perdu !")
            else:    
                print(f"{joueur.get_nom()}, vous avez gagné !")