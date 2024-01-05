from personne import Personne

class Professeur(Personne):
    def __init__(self,matiere) -> None:
        self.__matiereEnseignée = matiere

    def enseigner(self):
        quote = f"Le cours de {self.__matiereEnseignée} va commencer"
        return quote
