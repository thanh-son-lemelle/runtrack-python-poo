from rectangle import *

class Parallelepipede(Rectangle):
    def __init__(self,longueur,largeur, hauteur) -> None:
        super().__init__(longueur , largeur)
        self.__hauteur = hauteur

    
    def get_hauteur(self):
        return self.__hauteur
    def set_hauter(self, value):
        self.__hauteur = value

    def getVolume(self):
        volume = self.__hauteur * self.getSurface()
        return volume
