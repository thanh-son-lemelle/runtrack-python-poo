#!/usr/bin/env python3
class Livre:
    def __init__(self, title, author, pageNumber) -> None:
        self.__title = title
        self.__author = author
        self.__pageNumber = pageNumber

    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author
    
    @property
    def pageNumber(self):
        return self.__pageNumber

    @author.setter
    def author(self, value):
        self.__author = value

    @title.setter
    def title(self,value):
        self.__title = value

    @pageNumber.setter
    def pageNumber(self,value):
        if value > 0 and isinstance(value,int):
            self.__pageNumber = value
        else:
            print("Erreur, valeur non prise en charge. Entrer un entier supérieur à zero")

communautéDeLAnneau = Livre("LOTR","Tolkien",768)
print(communautéDeLAnneau.title,communautéDeLAnneau.author)
communautéDeLAnneau.title = "LOTR Communauté de l'anneau"
communautéDeLAnneau.author = "J.R.R. Tolkien"
print(communautéDeLAnneau.title,communautéDeLAnneau.author)
communautéDeLAnneau.pageNumber = 4.5
print(communautéDeLAnneau.title,communautéDeLAnneau.author, communautéDeLAnneau.pageNumber)
communautéDeLAnneau.pageNumber = 900
print(communautéDeLAnneau.title,communautéDeLAnneau.author, communautéDeLAnneau.pageNumber)
