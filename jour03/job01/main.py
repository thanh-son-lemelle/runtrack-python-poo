#!/usr/bin/env python3

class Town:
    def __init__(self, nameTown , inhabitantsNumber,) -> None:
        self.__nameTown = nameTown
        self.__inhabitantsNumber = inhabitantsNumber

    def get_nameTown(self):
        return self.__nameTown
    
    def get_inhabitantNumber(self):
        return self.__inhabitantsNumber
    
    def updatePop(self):
        self.__inhabitantsNumber +=1
 


paris = Town("Paris", 1_000_000)
marseille = Town("Marseille", 861_635)

class People:
    def __init__(self, name, age, citie) -> None:
        self.__name = name
        self.__age = age
        self.__citie = citie

    def __str__(self) -> str:
        return f"{self.__name}, {self.__age}, habitant à {Town.get_nameTown(self.__citie)}"
    
    def addPop(self):
        self.__citie.updatePop()

    
john = People("John", 45, paris)
myrtille = People("Myrtille", 4, paris)
chloe = People("Chloé", 18, marseille)



print(f"Population de la Ville de {paris.get_nameTown()}: {paris.get_inhabitantNumber()} habitants")
print (john)
print(myrtille)
print(chloe)
john.addPop()
print(f"Population de la Ville de {paris.get_nameTown()}: {paris.get_inhabitantNumber()} habitants")
chloe.addPop()
myrtille.addPop()
print(f"Population de la Ville de {paris.get_nameTown()}: {paris.get_inhabitantNumber()} habitants")
print(f"Population de la Ville de {marseille.get_nameTown()}: {marseille.get_inhabitantNumber()} habitants")
