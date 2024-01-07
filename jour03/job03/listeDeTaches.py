#!/usr/bin/env python3

from tache import Tache

class ListeDeTaches:
    def __init__(self) -> None:
        self.__taches = []
    
    def ajouterTache(self,tache):
        self.__taches.append(tache)

    def supprimerTache(self,titre):
        for tache in self.__taches:
            if tache.get_titre() == titre:
                self.__taches.remove(tache)
                information = f"{'-'*30}\n Tâche '{titre}' supprimée\n{'-'*30}"
            else:
                information = f"{'-'*30}\n Tâche '{titre}' non trouvée\n{'-'*30}"
        return information
            
    
    def afficherTaches(self):
        getTache = ""
        for tache in self.__taches:
            getTache += f"{tache}\n{'-'*30}\n"
        return getTache
        
    def terminerTache(self,titreDeTache):
        for tache in self.__taches:
            if tache.get_titre() == titreDeTache:
                tache.statutTerminé()
                information = f"\n{'-'*30}\nTâche '{titreDeTache}' marquée comme terminée.\n{'-'*30}\n"
                return information
        else:
            information = f"La tâche {titreDeTache} n'est pas dans la liste"
            return information
        

    def filtreTaches(self, statut):
        tacheFiltrée = ""
        for tache in self.__taches:
            if tache.get_statut() == statut:
                if tache.get_statut() == 0:
                    tacheFiltrée += f"{tache}\n{'-'*30}\n"
                    information = f"Liste des tâches à faire\n{tacheFiltrée}"
                elif tache.get_statut() == 1:
                    tacheFiltrée += f"{tache}\n{'-'*30}\n"
                    information = f"Liste des tâches terminées\n{tacheFiltrée}"
                else:
                    information = f"Filtre non défini"
            else:
                if statut == 0:
                    information="Pas de tâche à faire"
                elif statut ==1:
                    information = "Pas de tâche terminée"
        return information