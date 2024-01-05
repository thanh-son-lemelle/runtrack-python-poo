from forme import Forme
class Rectangle(Forme):
    def __init__(self, longueur, largeur) -> None:
        self.__longueur = longueur
        self.__largeur = largeur
    
    def getPerimetre(self):
        perimetre = 2*(self.__longueur+self.__largeur)
        return perimetre
    
    
    def get_longueur(self):
        return self.__longueur
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, value):
        self.__longueur = value
    def set_largeur(self,value):
        self.__largeur = value
    
    def aire(self):
        #super().aire() optionnel récupère la valeur 0 retourné par la methode de aire de forme
        surface = self.__largeur * self.__longueur
        return surface
        