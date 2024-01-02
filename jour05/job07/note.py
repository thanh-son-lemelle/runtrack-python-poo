import random 
l = []

for i in range(10):
    l.append(random.randint(0,100))

def arrondi(l):
    l2 = []
    for note in l: 
        if note > 40:
            prochain_multiple = (note//5+1)*5
            if (prochain_multiple-note) < 3:
                note=prochain_multiple
                l2 += [note,": test réussi et arrondie supérieur"]
            else:
                l2+=[note,": test réussi"]
        else:
            l2 +=[note,": echec du test"]
    return l2

print(l)
print(arrondi(l))
