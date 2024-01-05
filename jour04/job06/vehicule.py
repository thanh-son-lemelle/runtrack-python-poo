class Vehicule(object):
    def __init__(self, marque, modele, annee, prix, enMarche = False) -> None:
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__prix = prix
        self.__enMarche = enMarche

    def get_enMarche(self):
        return self.__enMarche
    
    def set_enMarche(self,value):
        self.__enMarche = value

    def get_informationVehicule(self):
        informationVehicule = f"marque: {self.__marque}\nmodele: {self.__modele}\nannee: {self.__annee}\nprix: {self.__prix}"
        return informationVehicule
    
    def demarrer(self):
        if  self.__enMarche == False:
            self.__enMarche = True
            quote = "Vehicule en marche"
            return quote
        else:
            return "Déja en marche ... Bip, bip, bip ... BOUM!."

