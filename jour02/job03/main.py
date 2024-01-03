#!#!/usr/bin/env python3
class Livre:
    def __init__(self, title, author, pageNumber) -> None:
        self.__title = title
        self.__author = author
        self.__pageNumber = pageNumber
        self.__available = True

    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author
    
    @property
    def pageNumber(self):
        return self.__pageNumber
    
    @property
    def available(self):
        return self.__available

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

    
    def verification(self):
            return self.__available
        
    def emprunter(self):
        if self.verification():
            print("vous empruntez le livre")
            self.__available = False
        else:
            print ("livre non disponible")

    def rendre(self):
        if not self.verification():
            print("vous rendez le livre")
            self.__available = True
        else:
            print("vous n'avez pas emprunter de livre")




communautéDeLAnneau = Livre("LOTR","Tolkien",768)

print(communautéDeLAnneau.verification())
communautéDeLAnneau.emprunter()
print(communautéDeLAnneau.verification())
communautéDeLAnneau.emprunter()
communautéDeLAnneau.rendre()
communautéDeLAnneau.rendre()