#!/usr/bin/env python3
import random

class Personnage:
    def __init__(self, nom, vie) -> None:
        self.__nom = nom
        self.__vie = vie
        self.__degatsInfligé = 0
    
    def get_nom(self):
        return self.__nom
    
    def get_vie(self):
        return self.__vie
    
    def get_degatsinfligé(self):
        return self.__degatsInfligé
    
    def attaquer(self, cible):
        degats = random.randint(50,100)
        cible.dommage(degats)
        self.__degatsInfligé = degats

    def dommage(self, degats):
        self.__vie -= degats


    
        
