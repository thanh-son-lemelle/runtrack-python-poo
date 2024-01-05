

class Personne:
    def __init__(self, age=14) -> None:
        self.__age = age

    def afficherAge(self):
        return self.__age
    
    def bonjour(self):
        quote = "Hello"
        return quote
    
    def modifierAge (self,value):
        self.__age = int(value)