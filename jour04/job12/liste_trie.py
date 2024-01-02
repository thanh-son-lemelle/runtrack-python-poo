L = [7, 11, 42, 39, 2]

def long(l):
    j=0
    for i in l:
        j+=1
    return j

def trie(l):
    for i in range(long(l)-1):
        for y in range(long(l)-i-1):
            if l[y] > l[y+1] :
                l[y], l[y+1] = l[y+1], l[y]
    return l

print(trie(L))
