#!/usr/bin/env python3
class Rectangle:
    def __init__(self, longueur, largeur) -> None:
        self.__longueur = longueur
        self.__largeur = largeur

    @property
    def longueur(self):
        return self.__longueur
    
    @property
    def largeur(self):
        return self.__largeur
    

    @largeur.setter
    def largeur(self, value):
        self.__largeur = value

    @longueur.setter
    def longueur(self,value):
        self.__longueur = value


rectangleTest = Rectangle(10,5)
print(rectangleTest.longueur,rectangleTest.largeur)
rectangleTest.longueur = 20
rectangleTest.largeur = 15
print(rectangleTest.longueur,rectangleTest.largeur)