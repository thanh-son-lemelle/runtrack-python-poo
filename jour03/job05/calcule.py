def calcule(num1,operator,num2):
    
    if operator == "+":
        resultat = num1 + num2
        return resultat
    elif operator == "-":
        resultat = num1 - num2
        return resultat
    elif operator == "*":
        resultat = num1 * num2
        return resultat
    elif operator == "/":
        resultat = num1 / num2
        return resultat
    elif operator == "%":
        resultat = num1 % num2
        return resultat
    else:
        return"merci de renseigner le bon opératuer +, -, *, /, %"
    print("=============================================")

print(calcule(1,"+",10))
print(calcule(1,"-",10))
print(calcule(1,"*",10))   
print(calcule(1,"/",10))
print(calcule(1,"%",10))
print(calcule(1,"l",10))