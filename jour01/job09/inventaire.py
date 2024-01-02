nom="pâte panzani"
prix_unit="1.26"
before_stock="100"
ask_quantity=0
infla=0
ask_quantity=input("renseigner la quantité demandé : ")
after_stock=(int(before_stock) - int(ask_quantity))
prix_tot=(float(prix_unit) * int(ask_quantity))
infla=input("rentrer l'inflation : ")
prix_infla=(float(prix_unit) + (float(prix_unit) * float(infla) / 100))

print("-------------------------------")
print(nom)
print("-------------------------------")
print("prix : ",prix_unit,"€")
print("-------------------------------")
print("stock : ",before_stock)
print("-------------------------------")
print("quantité prise : ",ask_quantity)
print("-------------------------------")
print("inventaire : ",after_stock)
print("-------------------------------")
print("prix total : ", prix_tot)
print("-------------------------------")
print("prix unitaire avec inflation",prix_infla)
print("-------------------------------")
print("prix total inflation : ", prix_infla * float(ask_quantity))