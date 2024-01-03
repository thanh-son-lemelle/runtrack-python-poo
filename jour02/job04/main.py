#!/usr/bin/env python3
class Student:
    def __init__(self, firstName, name, studentnumber) -> None:
        self.__firstName = firstName
        self.__name = name
        self.__studentnumber = studentnumber
        self.__credits = 0
        self.__level = self.__studentEval()
    
    def __str__(self) -> str:
        return f"Le nombre de credits de {self.__firstName} {self.__name} est de {self.__credits}"

    @property
    def firstName(self):
        return self.__firstName
    
    @property
    def name(self):
        return self.__name
    
    @property
    def studentnumber(self):
        return self.__studentnumber
    
    @property
    def credits(self):
        return self.__credits
    
    @property
    def Level(self):
        return self.__level
    
    @property
    def studentEval(self):
        return self.__studentEval()


    @name.setter
    def name(self, value):
        self.__name = value

    @firstName.setter
    def firstName(self,value):
        self.__firstName = value

    @studentnumber.setter
    def studentnumber(self,value):
        self.__studentnumber = value

    def add_credits(self,value):
        if value > 0 :
            self.__credits += value
            self.__level = self.__studentEval()
        else:
            print("Erreur, valeur non prise en charge. Entrer un chiffre supérieur à zero")

    def __studentEval(self):
        if self.credits >= 90:
            return "Excellent"
        elif 90 > self.credits >= 80:
            return "Très bien"
        elif 80 > self.credits >= 70:
            return "Bien"
        elif 70 > self.credits >= 60:
            return "Passable"
        elif self.credits < 60:
            return "Insuffisant"

    def studentinfo(self):
        return f"nom = {self.__name}\nPrénom = {self.__firstName}\nID = {self.__studentnumber}\nNiveau = {self.__studentEval()}\n------------------"

testStudent = Student("John","Doe",145)
print(testStudent)
testStudent.add_credits(10)
testStudent.add_credits(10)
testStudent.add_credits(10)
print(testStudent)
print(testStudent.studentinfo())
testStudent.add_credits(40)
print(testStudent)
print(testStudent.studentinfo())
testStudent.add_credits(10)
print(testStudent.studentinfo())
print(testStudent)
testStudent.add_credits(10)
print(testStudent.studentinfo())
print(testStudent)