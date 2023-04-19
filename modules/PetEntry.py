from baseClass import Generic

class Pets(Generic):
    def __init__(self):
        super().__init__("PET","PetInventory.txt","BREED","AGE","PRICE")
    def categList(self):
        entries={}
        BREED=self._exceptObj.stringInput("breed")
        AGE=self._exceptObj.intInput("age")
        PRICE=self._exceptObj.floatInput("price")
        entries.update({"BREED":BREED})
        entries.update({"AGE":AGE})
        entries.update({"PRICE":PRICE})
        return entries
    def categInp(self,categ):
        if categ=="BREED":
            inp=self._exceptObj.stringInput()
        elif categ=="AGE":
            inp=self._exceptObj.intInput()
        else:
            inp=self._exceptObj.floatInput()
        return inp
    def display(self):
        try:
            print("%-15s %-30s %-5s %-25s "%("SrNum","BREED","AGE","PRICE"))
            for srNum in self._items:
                entry=self._items[srNum]
                print("%-15s %-30s %-10s %-20s "%(srNum,entry["BREED"],entry["AGE"],entry["PRICE"]))
        except KeyError as msg:
            print("key not found",msg)
