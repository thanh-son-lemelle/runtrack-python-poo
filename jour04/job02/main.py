from Professeur import Professeur
from eleve import Eleve
from personne import Personne





person = Personne()   
JohnDoe = Eleve()
print(JohnDoe.afficherAge())
print(JohnDoe.allerEnCours())
JohnDoe.modifierAge(15)
print(JohnDoe.afficherAge())
DupondPierre = Professeur("Anglais")
DupondPierre.modifierAge(40)
print(DupondPierre.afficherAge())
print(DupondPierre.bonjour(),DupondPierre.enseigner())
