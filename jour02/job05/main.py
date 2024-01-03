#!/usr/bin/env python3
class Voiture:
    def __init__(self,brand,model,year,kilometer) -> None:
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__kilometer = kilometer
        self.__running = False
        self.__fuelTank = 50

    @property
    def brand(self):
        return self.__brand
    
    @property
    def model(self):
        return self.__model
    
    @property
    def year(self):
        return self.__year
    
    @property
    def kilometer(self):
        return self.__kilometer
    
    @property
    def running(self):
        return self.__running
    
    @property
    def fuelTank(self):
        return self.__fuelTank

    @brand.setter
    def brand(self,value):
        self.__brand = value

    @model.setter
    def model(self,value):
        self.__model = value

    @year.setter
    def year (self,value):
        self.__year = value
    
    @kilometer.setter
    def kilometer (self,value):
        self.__kilometer = value

    @fuelTank.setter
    def fuelTank (self,value):
        self.__fuelTank = value

    def starter (self):   
        fuelTankCapacity = self.__checkFuelTank()
        if fuelTankCapacity > 5 :
            self.__running = True
        else:
            print ("fuelTank empty")
    
    def stop (self):
        self.__running = False

    def __checkFuelTank (self):
        return self.__fuelTank
    
car = Voiture("dacia", "sandero", 2015, 150000)

print(car.running)
car.starter()
print(car.running)
car.stop()
print(car.running)

car.fuelTank = 4
car.starter()