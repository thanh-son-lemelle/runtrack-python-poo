"""=====définition variable et fonction======="""
def moyenne(note1,note2,note3):
    
    return ((float(note1)+float(note2)+float(note3))/3)
    
note1=input("rentrez la note1 :")
note2=input("rentrez la note2 :")
note3=input("rentrez la note3 :")

"""===code==="""

moyenne_etudiant = int(moyenne(note1,note2,note3))

print ("la moyenne etudiante est  : ",moyenne_etudiant)
if   20 >=  moyenne_etudiant <= 15:
    print("Très bon élève")
elif  14 >= moyenne_etudiant <= 11:
    print("Bon élève")
elif  10 >=moyenne_etudiant <= 8:
    print("Élève moyen")
elif  7 >= moyenne_etudiant <= 0:
    print("Élève devant faire des efforts")
else:
    print("moyenne invalide")
