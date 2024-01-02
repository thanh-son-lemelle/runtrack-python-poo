class Point :
    def __init__(self,x, y):
        self.x = x
        self.y = y
    
    def afficherLesPoints (self):
        return f"Coordonnée ({self.x},{self.y})"
    
    def afficherX (self):
        return f"Coordonnée X ({self.x})"
    
    def afficherY (self):
        return f"Coordonnée Y ({self.y})"
    
    def changerX (self):
        self.x = input("changer la valeur de X ")
        return self.x

    def changerY (self):
        self.y = input("changer la valeur de Y ")
    
point1=Point(12,41)

print(point1.afficherLesPoints())
print(point1.afficherX())
print(point1.afficherY())
print(point1.changerX())
print(point1.afficherX())