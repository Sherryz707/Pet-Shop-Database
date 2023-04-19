from baseClass import Generic

class Employee(Generic):
    def __init__(self):
        super().__init__("EMP","EmployeeInventory.txt","NAME","GENDER","AGE","SALARY")
    def categList(self):
        entries={}
        NAME=self._exceptObj.stringInput("name")
        GENDER=self._exceptObj.stringInput("gender")
        AGE=self._exceptObj.intInput("age")
        SALARY=self._exceptObj.floatInput("salary")
        entries.update({"NAME":NAME})
        entries.update({"GENDER":GENDER})
        entries.update({"AGE":AGE})
        entries.update({"SALARY":SALARY})
        return entries
    def display(self):
        try:
            print("%-15s %-30s %-10s %-10s %-30s"%("SrNum","NAME","GENDER","AGE","SALARY"))
            for srNum in self._items:
                entry=self._items[srNum]
                print("%-15s %-30s %-10s %-10s %-30s"%(srNum,entry["NAME"],entry["GENDER"],entry["AGE"],entry["SALARY"]))
        except KeyError as msg:
            print("key not found",msg)
