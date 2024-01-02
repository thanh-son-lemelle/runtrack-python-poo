class Animal :
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def __str__(self):
        return f"L'âge de l'animal est de {self.age} ans"
    
    def vieillir (self):
        self.age += 1
        return f"l'age de lanimal {self.age} ans"
    
    def nommer (self, prenom):
        self.prenom = prenom
        print(f"L'animal se nomme {prenom}")
    
chevre = Animal ()
print (chevre)
chevre.vieillir()
print (chevre)
chevre.nommer("Biquette")

