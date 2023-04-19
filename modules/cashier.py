from customer import Customer
class Cashier:
    def __init__(self):
        pass
    def billing(self,shopEntry):
        try:
            price=shopEntry["PRICE"]
            if "QTY" in shopEntry:
                qty=shopEntry["QTY"]
            else:
                qty=1
            bill=price*qty
            return bill
        except:
            raise
    
    def displayItm(self,srNum,entry):
        shopEntry=entry
        print("%-15s %-30s %-10s %-20s "%(srNum,shopEntry["ITEM"],shopEntry["QTY"],shopEntry["PRICE"]))
    def displayPet(self,srNum,entry):
        shopEntry=entry
        print("%-15s %-30s %-10s %-20s "%(srNum,shopEntry["BREED"],1,shopEntry["PRICE"]))
    def shopDisplaynBill(self,obj:Customer):
        try:
            print("%-15s %-30s %-5s %-25s "%("SrNum","ITEM","QTY","COST"))
            total=0
            shopList=obj.get_items()
            for srNum in shopList:
                total+=self.billing(shopList[srNum])
                if srNum.startswith("P"):
                    self.displayPet(srNum,shopList[srNum])
                else:
                    self.displayItm(srNum,shopList[srNum])
            return total
        except:
            raise
    def receiptPrint(self,shopObj):
        try:
            if(isinstance(shopObj,Customer)):
                print("%10s"%(" "),"*"*5,"THANK YOU FOR YOUR PATRONAGE","*"*5)
                print("%20s"%(" "),"-"*5,"Billing","-"*5)
                bill=self.shopDisplaynBill(shopObj)
                print("Your total is:  %52.2f"% (bill))
            else:
                raise Exception("Object must be of class Customer")
        except Exception as msg:
            print(msg)
test=Customer()
testBill=Cashier()
testBill.receiptPrint(test)