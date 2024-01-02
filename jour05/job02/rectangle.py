def draw_rectangle(width,height):
    print("|"+ width*"-"+ "|")
    for i in range (height-2):
        print ("|"+ width*" "+ "|")
    print("|"+ width*"-"+ "|")
width=int(input("rentrez la largeur : "))
height=int(input("rentrez la hauteur : "))
print(draw_rectangle(width,height))