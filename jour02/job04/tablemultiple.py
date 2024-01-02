i=0
occurence=1
n=0
n=input("entrez un entier supérieur à zero (N) : ")
r=0
while occurence <= int(n):
    print("table de multiplication de ", occurence, ": ")
    for i in range(0,10,):
        r= occurence * i
        print(occurence,"x",i,"=",r)
    occurence+=1
