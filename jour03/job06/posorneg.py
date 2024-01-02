def test(nombre):
    if nombre > 0 :
        return nombre,"est positif"
    elif nombre < 0 :
        return nombre,"est négatif"
    else:
        return "rentrez un autre nombre"
    
print(test(5))
print(test(-5))
print(test(0))
