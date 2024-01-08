from carte import Carte
class Joueur:
    def __init__(self, nom) -> None:
        self.__nom = nom
        self.__main = []
    
    def get_nom(self):
        return self.__nom

    def get_carte(self, carte):
        self.__main.append(carte)

    def montrerCarte(self):
        print(f"Main de {self.__nom}\n")
        for carte in self.__main:
            print(f"{carte.get_valeur()} de {carte.get_couleur()}")
            
    def calculePoint(self):
        total = 0
        nombreAs = 0
        for carte in self.__main:
            if carte.get_valeur().isdigit():
                total += int(carte.get_valeur())
            elif carte.get_valeur() in ["Valet", "Dame","Roi"]:
                total += 10
            elif carte.get_valeur() == "As":
                nombreAs += 1

        for _ in range(nombreAs):
            if (total + 11) <= 21:
                total += 11
            else:
                total += 1
    
        return total