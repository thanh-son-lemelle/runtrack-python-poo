from personne import Personne

class Eleve(Personne):
    
    def allerEnCours(self):
        status = "je vais en cours"
        return status
    
    def afficherAge(self):
        quote = f"j'ai {self._Personne__age} ans"  
        return quote