#!/usr/bin/env python3

class command:
    
    def __init__(self,commandOrder,orderListOfPlats, priceList) -> None:
        self.listStatus = ["ongoing", "finished", "canceled"]
        self.__commandOrder = commandOrder
        self.__orderListOfPlats = orderListOfPlats
        self.__pricelist = priceList
        self.__status = self.listStatus[0]
        self.__total = 0
        self.__dict_from_list = ()
    



    def get_commandOrder (self):
        return self.__commandOrder
    
    def get_orderListOfPlats (self):
        return self.__orderListOfPlats
    
    def get_status (self):
        return self.__status
    
    def get_pricelist (self):
        return self.__pricelist
    
    def get_total (self):
        self.__calculTotal()
        return self.__total
    
    def get_TVA (self):
        self.TVA = self.__total * 0.20
        return self.TVA

    def get_dict (self):
        self.__dict_from_list = dict(zip(self.__orderListOfPlats, self.__pricelist))
        self.__dict_from_list['status'] = self.__status
        return self.__dict_from_list

    def setter_commandOrder (self,value):
        self.__commandOrder = value

    def setter_orderListOfPlats (self,value):
        self.__orderListOfPlats = value

    def setter_status (self,value):
        self.__status = self.listStatus[value]

    def addPlatToList (self,plat,price):
        self.__orderListOfPlats.append(plat)
        self.__pricelist.append(price)

    def cancelCommand (self):
        self.__status=self.listStatus[2]

    def __calculTotal (self):
        for i in range(len(self.__pricelist)):
            self.__total += self.__pricelist[i]
    
            


courses = command(10,["pâtes","melon","haricots"], [1.64,1.20,0.88])

print(courses.get_commandOrder())
print(courses.get_orderListOfPlats())
courses.addPlatToList("tomates", 0.5)
print(courses.get_orderListOfPlats())
print(courses.get_pricelist())
print(courses.get_status())
courses.cancelCommand()
print(courses.get_status())
print(courses.get_total())
print(courses.get_TVA())
print(courses.get_dict())