#!#!/usr/bin/env python3
class Livre:
    def __init__(self, title, autor, pageNumber) -> None:
        self.__longueur = title
        self.__largeur = autor
        self.__pageNumber = pageNumber

    @property
    def title(self):
        return self.__longueur
    
    @property
    def autor(self):
        return self.__largeur
    
    @property
    def pageNumber(self):
        return self.__pageNumber

    @autor.setter
    def autor(self, value):
        self.__largeur = value

    @title.setter
    def title(self,value):
        self.__longueur = value

    @pageNumber.setter
    def pageNumber(self,value):
        if value > 0 and isinstance(value,int):
            self.__pageNumber = value
        else:
            print("Erreur, valeur non prise en charge. Entrer un entier supérieur à zero")

communautéDeLAnneau = Livre("LOTR","Tolkien",768)
print(communautéDeLAnneau.title,communautéDeLAnneau.autor)
communautéDeLAnneau.title = "LOTR Communauté de l'anneau"
communautéDeLAnneau.autor = "J.R.R. Tolkien"
print(communautéDeLAnneau.title,communautéDeLAnneau.autor)
communautéDeLAnneau.pageNumber = 4.5
print(communautéDeLAnneau.title,communautéDeLAnneau.autor, communautéDeLAnneau.pageNumber)
communautéDeLAnneau.pageNumber = 900
print(communautéDeLAnneau.title,communautéDeLAnneau.autor, communautéDeLAnneau.pageNumber)
