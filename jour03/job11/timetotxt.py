def time_to_text(nombre_entier):
    x=int(nombre_entier/60)
    y=nombre_entier-(x*60)
    print(x)
    print(y)
    print(x, "heures et",y ,"minutes")

time_to_text(190)
print("===================================")
time_to_text(385)