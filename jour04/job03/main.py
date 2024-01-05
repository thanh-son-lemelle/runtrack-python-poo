from parallelepipede import Parallelepipede
from rectangle import Rectangle

rectangleA = Rectangle(10,20)
print(rectangleA.getPerimetre())
print(rectangleA.getSurface())
print(rectangleA.get_largeur())
print(rectangleA.get_longueur())
parallelepipedeA = Parallelepipede(15,25,10)
print(parallelepipedeA.getPerimetre())
print(parallelepipedeA.getSurface())
print(parallelepipedeA.get_largeur())
print(parallelepipedeA.get_longueur())
print(parallelepipedeA.getVolume())
