def supprdouble(l):
    l2=[]
    for i in l:
        if i not in l2:
            l2+=[i]
    return l2

L=[10,20,30,20,10,50,60,40,80,50,40]
print(supprdouble(L))