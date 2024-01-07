#!/usr/bin/env python3

from joueur import Joueur
from equipe import Equipe

joueur1 = Joueur("Zidane", 10, "Attaquant")
joueur2 = Joueur("Payet", 7, "Milieu")
joueur3 = Joueur("Silva", 3, "Défenseur")

equipe1 = Equipe("OM")
equipe2 = Equipe("PSG")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)

joueur1.marquerUnBut()
joueur1.effectuerUnePasseDecisive()
joueur2.recevoirUnCartonJaune()
joueur3.recevoirUnCartonRouge()

print(equipe1)
print(equipe2)

print(equipe1.afficherStatistiquesJoueurs())
print(equipe2.afficherStatistiquesJoueurs())
equipe1.mettreAjourStatistiquesJoueur(10,"but")
print(joueur1.afficherStatistiques())
joueur2.recevoirUnCartonJaune()
print(joueur2.afficherStatistiques())