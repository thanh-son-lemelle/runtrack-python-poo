class Personnage :
    def __init__(self):
        self.x = 0
        self.y = 0
        self.postion = ()
    def gauche (self):
        self.x -= 1
        return self.x
    
    def droite (self):
        self.x += 1
        return self.x
    
    def haut (self):
        self.y += 1
        return self.x
    
    def bas (self):
        self.y -= 1
        return self.x
    
    def position (self):
        self.nouvellePosition = (self.x,self.y)
        return self.nouvellePosition
    
player=Personnage ()
player.gauche()
print(player.position())
player.haut()
print(player.position())
player.droite()
print(player.position())
player.bas()
print(player.position())
