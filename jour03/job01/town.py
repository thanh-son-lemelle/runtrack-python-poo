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
 

