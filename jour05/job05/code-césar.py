def code_cesar(message,décalage):
    resultats=""
    for i in message:
        if i.isalpha():
            code_ascii = ord(i)
            if 65<= code_ascii <=90:
                code_décalé =(code_ascii - ord("A") + décalage) % 26 + ord("A")
            else:
                code_décalé =(code_ascii - ord("a") + décalage) % 26 + ord("a")
            
            resultats+=chr(code_décalé)
        else:
            resultats+=i
    
    return resultats

message = input("rentrez message : ")
décalage = int(input("rentrez le décalage : "))

print(message)
print(code_cesar(message,décalage))