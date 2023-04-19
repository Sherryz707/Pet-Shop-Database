from baseClass import Generic

class Item(Generic):
    def __init__(self):
        super().__init__("ITEM","ItemInventory.txt","ITEM","QTY","PRICE")
    def categList(self):
        entries={}
        done=False
        while not done:
            ITEM=self._exceptObj.stringInput("item")
            if ITEM.upper()=="Q":
                return False
            elif not self.keyExist(ITEM):
                done=True
            else:
                print("Item ",ITEM,"is already listed. Add another or Q to quit.")
        QTY=self._exceptObj.intInput("qty")
        PRICE=self._exceptObj.floatInput("price")
        entries.update({"ITEM":ITEM})
        entries.update({"QTY":QTY})
        entries.update({"PRICE":PRICE})
        return entries
def convertType(self,entry):
    entry={"ITEM0001":{"ITEM":"WRENCH","PRICE":"100.0","QTY":"7"}}
def display(self):
    try:
        print("%-15s %-30s %-5s %-25s "%("SrNum","ITEM","QTY","PRICE"))
        for srNum in self._items:
            entry=self._items[srNum]
            print("%-15s %-30s %-10s %-20s "%(srNum,entry["ITEM"],entry["QTY"],entry["PRICE"]))
    except KeyError as msg:
        print("key not found",msg)

