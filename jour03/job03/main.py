#!/usr/bin/env python3

from listeDeTaches import ListeDeTaches
from tache import Tache

tache1 = Tache ("Faire son CV","Mettre à jour son CV")
tache2 = Tache ("Finir le kickoff","Faire les jobs03 à 05")

listeDeTaches = ListeDeTaches()
listeDeTaches.ajouterTache(tache1)
listeDeTaches.ajouterTache(tache2)

print(listeDeTaches.afficherTaches())
print(listeDeTaches.terminerTache("Faire son CV"))
print(listeDeTaches.afficherTaches())
print(listeDeTaches.filtreTaches(0))
print(listeDeTaches.filtreTaches(1))
print(listeDeTaches.supprimerTache("Faire son CV"))
print(listeDeTaches.afficherTaches())
print(listeDeTaches.filtreTaches(1))
