#!/usr/bin/env python3
from vehicule import Vehicule
class Moto(Vehicule):
    def __init__(self,marque,modele,annee,prix, roues = 2) -> None:
        self.__roues = roues
        super().__init__(marque,modele, annee, prix)


    def get_enMarche(self):
        return self.__en_marche
    
    def get_marque(self):
        return self.__marque
    
    
    def get_modele(self):
        return self.__modele
    
    
    def get_annee(self):
        return self.__annee
    
    
    def get_prix(self):
        return self.__prix


    def set_enMarche(self,value):
        self.__en_marche = value

    def set_marque(self,value):
        self.__marque = value


    def set_modele(self,value):
        self.__modele = value


    def set_annee (self,value):
        self.__annee = value
    

    def set_prix (self,value):
        self.__prix = value
    
    def get_informationVehicule(self):
        informationVehicule = f"{super().get_informationVehicule()}\nnombre de roues: {self.__roues}"
        return informationVehicule
    
    def demarrer(self):
        if not super().get_enMarche():
            super().set_enMarche(True)
            quote = "Vroum vroum, en y sur ma moto"
            return quote
        else:
            return "Déjà en marche ... Bip, bip, bip ... BOUM!"