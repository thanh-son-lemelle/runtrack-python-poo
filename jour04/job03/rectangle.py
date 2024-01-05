class Rectangle(object):
    def __init__(self, longueur, largeur) -> None:
        self.__longueur = longueur
        self.__largeur = largeur
    
    def getPerimetre(self):
        perimetre = 2*(self.__longueur+self.__largeur)
        return perimetre
    
    def getSurface(self):
        surface = self.__largeur * self.__longueur
        return surface
    
    def get_longueur(self):
        return self.__longueur
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, value):
        self.__longueur = value
    def set_largeur(self,value):
        self.__largeur = value
    
