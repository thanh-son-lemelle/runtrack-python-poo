def tapis(n):
    plus = "+"
    score = "-"*(n+1)
    ligne = plus + score + plus
    y=0
    print (ligne)
    for i in range(n+1):
        
        barre = "|"
        dièse = "#"*(n+y)
        dièse2 = "#"*i
        espace = " "
        ligne_tapis = barre + dièse + espace + dièse2 + barre
        y-=1
        print (ligne_tapis) 
    print (ligne)


n=int(input("selectionnez n : "))
print (tapis(n))