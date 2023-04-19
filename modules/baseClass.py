from inputValid import inputValid
from fileHandle import FileHandling
class Generic:
    def __init__(self,code,fName,*category):
        self._category=[]
        for ele in category:
            self._category.append(ele) 
        self._fileHandl=FileHandling(fName)
        self._items=dict(self._fileHandl.readRecordtoDict())
        self._code=code
        self._num=len(self._items)
        self._exceptObj=inputValid()
    def srNum(self,add=1):
        self._num+=add
        srNum=self._code+str(self._num).zfill(4)
        return srNum
    def categList(self):
        raise NotImplementedError
    def addItm(self):
        print("Enter number of entries: ")
        numOfEntr=self._exceptObj.intInput("number")
        for entry in range(numOfEntr):
            entries=self.categList()
            if entries:
                key=self.srNum()
                print(key)
                self._items[key]=entries
                self._fileHandl.writeFileComp(key,self._items[key])
            else:
                continue
        self.display()
    def addEntry(self,val={}):
        key=self.srNum()
        self._items[key]=val
        self._fileHandl.writeFileComp(key,self._items[key])
    def getCateg(self):
        return self._category
    def removeItemMan(self,key):
        removeItm= self._items.pop(key)
        self._fileHandl.removeLine(key)
        print("You have successfully removed: ", removeItm)
    def removeItem(self):
        key=self.toSearchZ()
        if key:
            removeItm= self._items.pop(key)
            self._fileHandl.removeLine(key)
            print("You have successfully removed: ", removeItm)
    def UpdateValMan(self,key,subKey,val):
        self._items[key][subKey]=val
        self._fileHandl.updateLine(key,self._items[key])            
    def UpdateVal(self):
        print("-----------updating-------------")
        key=self.toSearchZ()
        for subKey,subVal in self._items[key].items():
            print(subKey,":",subVal," do you wish to change this category: ")
            usrChoice=self._exceptObj.boolInput("Y","N")
            if usrChoice.upper()=="Y":
                updateIt=input("Enter updated value: ")
                self._items[key][subKey]=updateIt
        self.displayByKey(key) 
        self._fileHandl.updateLine(key,self._items[key])
            
    def displayCat(self,category):
        if len(category)==0:
            print("Nothing to show")
        for count,elements in enumerate(category,1):
            print(count,")",elements)
    def get_categ(self):
        return self._category
    def FormatDisplay(self):
        if len(self._items)==0:
            print("Nothing to show")  
        for keys in self._items:
            print(keys,self._items[keys])
    def display(self):
        if len(self._items)==0:
            print("Nothing to show")  
        for keys in self._items:
            print(keys,self._items[keys])
    def displayByKey(self,key):
        print(key,self._items[key])
    def displayByKeyList(self,listEntry):
        for keys in listEntry:
            self.displayByKey(keys)
    def SearchCat(self,categ):
        valSet=set()
        for key in self._items:
            toAdd=self._items[key][categ]
            valSet.add(toAdd)
        if len(valSet)==0:
            raise Exception(categ,"is empty. Nothing to show yet.")
        else:
            return valSet
        
    def SearchSubCat(self,subCat,subVal):
        valList=[]
        for key in self._items:
            if self._items[key][subCat]==subVal:
                valList.append(key)
        return valList
    def keyExist(self,subVal):
        for key in self._items:
            if subVal in self._items[key].values():
                return True
        return False
    def keyExistFR(self,key):
        try:
            if key in self._items:
                return True
        except:
            return False
    def toSearchZ(self,categOnly=False):
        try:
            self.displayCat(self._category)
            categ= self._exceptObj.matchListInput(self._category)
            setCat=self.SearchCat(categ)
            self.displayCat(setCat)
            if not categOnly:
                valInp=self._exceptObj.matchListInput(setCat)
                buyList= self.SearchSubCat(categ,valInp)
                self.displayByKeyList(buyList)
                buy=self._exceptObj.matchListInput(buyList)
                return buy
        except KeyError as error:
            raise
        except Exception as msg:
             raise
        
    def get_items(self):
        return self._items
    def get_entry(self,key):
        return self._items[key]
    
