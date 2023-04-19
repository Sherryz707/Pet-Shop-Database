from EmployeeEntry import Employee
from ItemEntry import Item
from PetEntry import Pets
from baseClass import Generic
from customer import Customer
from inputValid import inputValid
from cashier import Cashier
class Menu:
    def __init__(self):
        self._emp= Employee()
        self._itm= Item()
        self._pet= Pets()
        self._customer= Customer(self._itm,self._pet)
        self._exceptObj=inputValid()
        self._cashier= Cashier()
    def get_emp(self):
        return self._emp
    def get_itm(self):
        return self._itm
    def get_pet(self):
        return self._pet
    def get_customer(self):
        return self._pet
    def ManageMenu(self,obj):
        if isinstance(obj,Generic):
            while True:
                manageChoice=["add","update","remove","display by category","display all","quit"]
                for count,elements in enumerate(manageChoice,1):
                    print(count,")",elements)
                admin=self._exceptObj.intInput("choice by number: ")
                if admin==1:
                    obj.addItm()
                elif admin==2:
                    obj.UpdateVal()
                elif admin==3:
                    try:
                        buyKey=obj.toSearchZ()
                        obj.removeItemMan(buyKey)
                    except Exception as msg:
                        print(msg)
                elif admin==4:
                    try:        
                        obj.toSearchZ(True)
                    except Exception as msg:
                        print(msg)
                elif admin==5:
                    obj.display()
                elif admin==6:
                    return
        else:
            print("wrong class used as parameter")
    def adminMenu(self):
        done=False
        while not done:
            admin=self._exceptObj.intInput("(1)Manage Pets (2) Manage Items (3)Manage Employee (4)Quit")
            if admin==1:#pets
                obj=self.get_pet()
                self.ManageMenu(obj)
            elif admin==2: #items
                obj=self.get_itm()
                self.ManageMenu(obj)
            elif admin==3: #employee
                obj=self.get_emp()
                self.ManageMenu(obj)
            elif admin==4:
                done=True
    def customerMenu(self):
        done=False
        while not done:
            customer= self._exceptObj.intInput("(1)Buy (2)Remove (3)Display Shopping List (4)Billling (5)Quit")
            if customer==1:
                while customer!=3:
                    customer=self._exceptObj.intInput("(1)Buy Pet (2)Buy Pet Items (3)Return to Menu ")
                    if customer==1:
                        obj=self.get_pet()
                        self._customer.addPet(obj)
                    elif customer==2:
                        obj=self.get_itm()
                        self._customer.addItm(obj)
            elif customer==2:
                self._customer.removeItem()
            elif customer==3:
                self._customer.display()
            elif customer==4:
                self._cashier.receiptPrint(self._customer)
                self._customer.clearShop()
            elif customer==5:
                done=True
    def MenuZ(self):
        print("Welcome to the Pet Shop: ")
        while True:
            choice=self._exceptObj.intInput("(1)Admin (2)Customer")
            if choice==1:
                self.adminMenu()
            else:
                self.customerMenu()

obj=Menu()
obj.MenuZ()
                        
                