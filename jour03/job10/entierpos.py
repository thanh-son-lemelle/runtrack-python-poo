def test(chiffre):
    if chiffre%2==0 and chiffre >0 and chiffre == int(chiffre):
        return chiffre," est un entier positif paire "
    else:
        return "condition fausse rentrez un autre chiffre que", chiffre
    
print(test(2))
print(test(3))
print(test(2.5))
print(test(-2.5))