class Produit :
    def __init__(self, nom, prixHT):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = 0.2
        self.prixTTC = None
        self.ValeurTVA = 0

    def calculerPrixTTC (self):
        
        self.prixTTC = self.prixHT + self.getTVADuProduit()
        return self.prixTTC
        
        
    def getTVADuProduit (self):
        self.ValeurTVA = (self.prixHT * self.TVA)
        return self.ValeurTVA
        
    
        
    def modifierPrix (self, nouveauPrix):
        self.prixHT = nouveauPrix
        self.calculerPrixTTC()

    def modifierNom (self,nouveaunom):
        self.nom = nouveaunom


    def afficher (self):
        return f"nom du produit : {self.nom} \nprixHT est de : {self.prixHT} \ntaux TVA : {self.TVA} \nmontant TVA : {self.ValeurTVA} \nprixTTC : {self.prixTTC} \n ----------------------------------------"
    
penne = Produit("Penne Rigate", 1.08)
spaghetti = Produit ("Spaghetti", 1.35)
print (spaghetti.afficher())
spaghetti.calculerPrixTTC()
print (spaghetti.afficher())
spaghetti.modifierPrix(2.0)
print (spaghetti.afficher())
spaghetti.modifierNom("Pastabox")
print(spaghetti.afficher())
