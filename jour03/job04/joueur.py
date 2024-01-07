#!/usr/bin/env python3

class Joueur:
    def __init__(self, nom, numero, position) -> None:
        self.__nom= nom
        self.__numero = numero
        self.__position = position
        self.__butMarquer = 0
        self.__passeDecisive = 0
        self.__cartonJaune = 0
        self.__cartonRouge = 0
    
    def __str__(self) -> str:
        return f"{self.__nom}, {self.__numero}"

    def get_numero(self):
        return self.__numero
    
    def marquerUnBut(self):
        self.__butMarquer += 1

    def effectuerUnePasseDecisive(self):
        self.__passeDecisive += 1

    def recevoirUnCartonJaune(self):
        self.__cartonJaune += 1
        if self.__cartonJaune == 2:
            self.recevoirUnCartonRouge()

    def recevoirUnCartonRouge(self):
        self.__cartonRouge += 1

    def afficherStatistiques(self):
        information1 = f"{"-"*30}\nStatistiques de {self.__nom} joueur n° {self.__numero}, {self.__position}\n"
        information2 = f"Buts marquées: {self.__butMarquer}\n"
        information3 = f"Passes décisives: {self.__passeDecisive}\n"
        information4 = f"Cartons jaunes: {self.__cartonJaune}\n"
        information5 = f"Cartons rouges: {self.__cartonRouge}\n{"-"*30}\n"
        return information1 + information2 + information3 + information4 + information5
    
