#!/usr/bin/env python3
from datetime import datetime

class CompteBancaire:
    def __init__(self, accountNumber, name, firstname, balance, overdraft = False) -> None:
        self.__accountNumber = accountNumber
        self.__name = name
        self.__firstname = firstname
        self.__balance = balance
        self.__previousBalance = 0
        self.__overdraft = overdraft
        self.__movementDate = []
        self.__startingOverdraftDate = None
        self.__endOverdraftDate = None

    def get_accountNumber(self):
        return self.__accountNumber
    def get_name(self):
        return self.__name
    def get_firstname(self):
        return self.__firstname
    def get_balance(self):
        return self.__balance
    def get_movementDate(self):
        return self.__movementDate
    
    def set_balance(self, value):
        self.__balance = value
    
    def showAccount(self):
        return f"-------------------------\ncompte numéro: {self.__accountNumber}\nnom: {self.__name}\nprénom: {self.__firstname}\nsolde du compte: {self.showBalance()}\n-------------------------"
    def showBalance(self):
        return "{:.2f}".format(self.__balance)
    
    
    def payment(self,value, date):
        
        if value < 0:
            error = ValueError("Payment: Value must be a positive number")
            return error
        
        self.__previousBalance = self.__balance
        self.__balance += value
        self.__movementDate.append(date)
        self.add_agios()
        return self.showBalance()

    def withdrawal(self,value, date):
        if value < 0:
            error = ValueError("Withdrawal: Value must be a positive number")
            return error
        
        if value > self.__balance:
            if self.__overdraft == True:
                self.__previousBalance = self.__balance
                self.__balance -= value
                self.__movementDate.append(date)
                self.add_agios()
                return self.showBalance()
            
            else:
                error = ValueError("Insufficient funds: You don't have enough money in your account to cover the requested withdrawal amount.")
                return error
            
        self.__previousBalance = self.__balance
        self.__balance -= value
        self.__movementDate.append(date)
        self.add_agios()
        return self.showBalance()
    
    def dateToDay(self, datestart, dateend, date_format="%d/%m/%Y"):
        try:
            if datestart is not None and dateend is not None:
                date_objectstart = datetime.strptime(datestart, date_format)
                date_objectend = datetime.strptime(dateend, date_format)
                days_difference = (date_objectend - date_objectstart).days
                return days_difference
            
            if datestart is not None and dateend is None:
                days_difference = 0
                return days_difference
            
            if datestart is None and dateend is not None:
                days_difference = 0
                return days_difference
            
            else:
                days_difference = 0
                return days_difference
            
        except ValueError as e:
            print(f"Error converting date: {e}")
            return None
    
    def overdraftTimeLaps(self):
        if self.__previousBalance >= 0:
            if self.__balance <= 0:
                self.__startingOverdraftDate = self.__movementDate[-1]

        elif self.__previousBalance <= 0:
            if self.__balance >= 0:
                self.__endOverdraftDate = self.__movementDate[-1]

        daysDifference = self.dateToDay(self.__startingOverdraftDate, self.__endOverdraftDate)
        return daysDifference

    def agios(self):
        overdraft_time_laps = self.overdraftTimeLaps()
        if overdraft_time_laps is not None:
            agios = (self.__previousBalance * overdraft_time_laps * (17 / 100)) / 365
            return agios
        
    def add_agios(self):
        self.__balance += self.agios()

    def transfer(self, accountNumber, receivingAccount, value, date):
        if value < 0:
            error = ValueError("Transfer: Value must be a positive number")
            return error
        
        if self.__balance < value and self.__overdraft == False:
            error = ValueError("Insufficient funds: You don't have enough money in your account to cover the requested transfer amount.")
            return error
        
        self.withdrawal(value,date)
        receivingAccount.payment(value,date)
        return f"transfer from {value} to account {accountNumber} successfully completed."
        


accountA = CompteBancaire(2489635170, "Dupond", "Jean", 5_000, overdraft= False)
print(accountA.showAccount())
print(accountA.payment(1300, "04/01/2024"))
print("---------------------------------------------1")
print(accountA.withdrawal(5000, "04/01/2024"))
print("---------------------------------------------2")
print(accountA.withdrawal(1300, "04/01/2024"))
print("---------------------------------------------3")
print(accountA.withdrawal(1300, "04/01/2024"))
print("---------------------------------------------4")
accountA = CompteBancaire(2489635170, "Dupond", "Jean", 0, overdraft= True)
print(accountA.withdrawal(1300, "04/01/2024"))
print("---------------------------------------------5")
print(accountA.payment(1300, "04/02/2024"))
print(accountA.showAccount())
accountB = CompteBancaire(2489635171, "Smith", "Pierre", -5000, overdraft= True)
print(accountA.transfer(2489635171, accountB, 5_500, "05/02/2024"))
print(accountA.showAccount())
print(accountB.showAccount())