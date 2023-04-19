from baseClass import Generic
from ItemEntry import Item
from PetEntry import Pets

class Customer(Generic):
    iOrderNumber=0
    def __init__(self,*obj):
        entry=self.setCateg(*obj)
        super().__init__("ORDER","customer.txt",entry)
        self.iOrderNumber+=1
    def setCateg(Self,*obj):
        numObj=len(obj)
        categSet=set()
        for objects in obj:
            print(objects.get_categ())
            categSet.update(objects.get_categ())
        print(categSet)
        return list(categSet)
    def checkQty(self,obj,dic,buyQty,toBuyKey):
        while True:
            origQty=dic["QTY"]
            if buyQty<origQty:
                leftObj=origQty-buyQty
                return True,leftObj
            
            else:
                raise Exception("insufficient quantity.")
    def get_QtyS(self,obj,buyKey):
        try:
            entry=dict(obj.get_entry(buyKey))
            origQty=entry["QTY"]
            buyQty=self._exceptObj.intInput("qty")
            return origQty,buyQty
        except KeyError as msg:
            raise
        except Exception as msg:
            raise
        
    def checkQty(self,obj,origQty,buyQty):
        while True:
            if buyQty<=origQty:
                return True
            
            else:
                print("insufficient quantity.")
                return False
    def inputQty(self,obj,buyKey):
        try:
            origQty,buyQty=self.get_QtyS(obj,buyKey)
            check=self.checkQty(obj,origQty,buyQty)
            while not check:
                print("Do you want to quit?")
                quit=self._exceptObj.boolInput("Y","N")
                if quit=="Y":
                    raise Exception("exiting")
                else:
                    origQty,buyQty=self.get_QtyS(obj,buyKey)
                    check=self.checkQty(obj,origQty,buyQty)
            return (origQty,buyQty)
        except KeyError as msg:
            raise
        except Exception as msg:
            raise
            
    def addItm(self,obj):
        if isinstance(obj,Item):
            print("Enter number of entries: ")
            numOfEntr=self._exceptObj.intInput("entries")
            try:
                for i in range(numOfEntr):
                    toBuyKey=obj.toSearchZ()
                    if not self.keyExistFR(toBuyKey): 
                        check=self.inputQty(obj,toBuyKey)
                        origQty,buyQty=check
                        leftQty=origQty-buyQty
                        entry=dict(obj.get_entry(toBuyKey))
                        entry=self.addQty(entry,buyQty)
                        self._items[toBuyKey]=entry
                        self.objReduceQty(obj,toBuyKey,leftQty)
                        self._fileHandl.writeFileComp(toBuyKey,self._items[toBuyKey]) 
                    else:
                        itemQty=self._items[toBuyKey]["QTY"]
                        print("Item exists in list.You have:",itemQty,"Do you want to update it ?")   
                        update=self._exceptObj.boolInput("Y","N")
                        if update=="Y":
                            check=self.inputQty(obj,toBuyKey) 
                            origQty,buyQty=check
                            leftQty=origQty-buyQty
                            self.UpdateValMan(toBuyKey,buyQty)
                            self.objReduceQty(obj,toBuyKey,leftQty)
                            
            except KeyError as error:
                print(error,"not found in entries")
            except Exception as error:
                print(error)
        else:
            print("object must be of class Item")
                    
                
    def addQty(self,dic,qty):
        item=dic
        item["QTY"]=0
        item["QTY"]=qty
        return item
    def objReduceQty(self,obj,key,qtyLeft):
        if isinstance(obj,Item):
            obj.UpdateValMan(key,"QTY",qtyLeft)
            obj.displayByKey(key)
            entry=obj.get_entry(key)
    
    def UpdateValMan(self,key,val):
        self._items[key]["QTY"]+=val
        entry=self.get_entry(key)
        self._fileHandl.updateLine(key,entry)
    def UpdateVal(self):
        try:
            raise Exception("Function not accesible for customer") 
        except Exception as msg:
            print(msg)  
    def addPet(self,obj):
        if isinstance(obj,Pets):
            try:
                toBuyKey=obj.toSearchZ()
                entry=obj.get_entry(toBuyKey)
                self._items[toBuyKey]=entry
                obj.removeItemMan(toBuyKey)
                self.displayByKey(toBuyKey)
                self._fileHandl.writeFileComp(toBuyKey,self._items[toBuyKey])
            except KeyError as error:
                print(error,"not found in entries")
            except Exception as error:
                print(error)
        else:
            print("object must be instance of class Pets")
    def clearShop(self):
        self._items.clear()
        self._fileHandl.removeAll()

