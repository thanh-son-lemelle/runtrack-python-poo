from forme import Forme
import math

class Cercle(Forme):

    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon (self,rayon):
        self.rayon = rayon
        return self.rayon
    
    def circonférence (self):
        return self.rayon * math.pi
    
    def aire (self):
        return (self.rayon^2)*math.pi
        
    def diametre (self):
        return self.rayon*2
        
    def afficherInfos (self):
        return f"rayon de {self.rayon} \ncirconference de {self.circonférence()} \naire de {self.aire()} \ndiamètre de {self.diametre()}"
    