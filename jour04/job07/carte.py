class Carte:
    def __init__(self,valeur,couleur) -> None:
        self.__valeur = valeur
        self.__couleur = couleur
        
    def get_valeur(self):
        return self.__valeur
    
    def get_couleur(self):
        return self.__couleur
    
    def __str__(self):
        return f"{self.get_valeurvaleur()} de {self.get_couleur}"
