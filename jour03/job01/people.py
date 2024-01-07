#!/usr/bin/env python3

from town import Town

class People:
    def __init__(self, name, age, citie) -> None:
        self.__name = name
        self.__age = age
        self.__citie = citie

    def __str__(self) -> str:
        return f"{self.__name}, {self.__age}, habitant à {Town.get_nameTown(self.__citie)}"
    
    def addPop(self):
        self.__citie.updatePop()