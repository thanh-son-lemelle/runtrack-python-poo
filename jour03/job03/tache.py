#!/usr/bin/env python3

class Tache:
    def __init__(self,titre, description, ) -> None:
        self.__titre = titre
        self.__description = description
        self.__statut = 0
        self.__statutInformation = ["A faire", "Terminée"]

    def statutTerminé (self):
        self.__statut= 1
        return self.__statut
    
    def get_titre(self):
        return self.__titre
    
    def get_statut(self):
        return self.__statut

    def __str__(self):
        return f"\nTâche : {self.__titre}\nDescription : {self.__description}\nStatut : {self.__statutInformation[self.__statut]}"
