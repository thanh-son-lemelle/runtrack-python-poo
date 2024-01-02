def long(l):
    j=0
    for i in l:
        j+=1
    return j

def trie(l):
    for i in range(long(l)-1):
        for y in range(long(l)-i-1):
            if l[y] > l[y+1]:
                l[y], l[y+1] = l[y+1], l[y]
    return l

def arrondi(l):
    for i in range(long(l)):
        entier = l[i] // 1
        fraction = l[i] - entier
        if fraction >=0.5:
            résultat = entier + 1
            l[i] = résultat
        else:
            résultat = entier
            l[i] = résultat
    return l



        
L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]


print(arrondi(trie(L)))
