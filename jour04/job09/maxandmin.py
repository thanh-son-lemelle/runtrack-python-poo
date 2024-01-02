L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
max=L[0]
min=L[0]

for i in range (len(L)):
    if L[i]<=min: 
        min=L[i]
    elif L[i] >=max:
        max=L[i]
print("La valuer max est : ",max)
print("La valeur min est : ",min)

