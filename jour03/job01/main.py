#!/usr/bin/env python3

from town import Town
from people import People

paris = Town("Paris", 1_000_000)
marseille = Town("Marseille", 861_635)

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
