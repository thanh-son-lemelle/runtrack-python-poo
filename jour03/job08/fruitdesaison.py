def fruitdesaison(type,saison):
    if type == "fruits" and saison == "hiver":
        print("orange,mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print ("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print ("artichaut, aubergine, navet")
    else:
        print("changer de valeur")
"""============================================="""

fruitdesaison("fruits","hiver")
fruitdesaison("fruits","ete")
fruitdesaison("legume","hiver")
fruitdesaison("legume","ete")
fruitdesaison("oups","hiver")
fruitdesaison("fruits","oups")
fruitdesaison("oups","oups")