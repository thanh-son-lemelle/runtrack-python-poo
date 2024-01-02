def test(language):
    
    if language == "JavaScript":
        return "tu es un développeur web"
    elif language == "python":
        return "tu es un développeur IA"
    elif language == "java":
        return "“tu es un développeur logiciel”"
    elif language == "reactjs":
        return "tu es un developpeur mobile"
    else:
        return"un jour, je serai le meilleur développeur... "
    print("=============================================")

print(test("JavaScript"))
print(test("python"))
print(test("java"))   
print(test("reactjs"))
print(test(""))
print(test("blalbalba"))