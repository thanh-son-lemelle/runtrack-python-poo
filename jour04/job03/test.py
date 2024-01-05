class Personne(object):     
       
    # Constructeur         
    def __init__(self, nom, cin):    
        self.nom = nom 
        self.cin = cin 
 
    def afficher(self): 
        print("Nom : ",self.nom) 
        print("CIN : ",self.cin) 

class Employe( Personne ): 

    def __init__(self, nom, cin, salaire): 
        self.salaire = salaire 

        # appeler __init__ de la classe mère (Personne) 
        super().__init__(nom, cin) 
    
# création d'une variable d'instance
p=Employe("Ismail", "EE4567", 7000)
p.afficher()