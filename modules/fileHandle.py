from asyncio.windows_events import NULL
from pathlib import Path
import string
#fileName="testPyonz.txt"
#filepath = Path(__file__).parent / fileName
class FileHandling():
    def __init__(self,fname:string):
        self._fileName=fname
        self._fileObj=NULL
        self._filePath = Path(__file__).parent / self._fileName #so it opens in same working directory
    
    def openCloseFile(self,mode:string):
        try:
            with open(self._filePath,mode) as f:
                print(f.name)
        except ValueError as msg:
            print(msg)
        except IOError:
            print("file not found")
            self.IOerror()
    def openFile(self,mode:string):
        done=False
        try:
            self._fileObj=open(self._filePath,mode)
            print("opening.......")
            done=True
        except ValueError as msg:
            print(msg)
        except IOError:
            print("file not found")
        finally:
            return done
    def closeFile(self):
        print("closing file......")
        self._fileObj.close()
    def writeFile(self,*elements):
        for elem in elements:
            self._fileObj.write(str(elem))        
    def writeFileComp(self,key,diction):
        try:
            with open(self._filePath,"a") as self._fileObj:
                self.writeRecord(key,diction)
        except ValueError as msg:
            print(msg)
        except IOError:
            print("file not found")
    def writeRecord(self,key,diction:dict):
        self.writeFile(key," = ")
        for keySub,valSub in diction.items():
            self.writeFile(keySub,":",valSub,",")
        self.writeFile("\n")
    def readRecordtoList(self):
        try:
            with open(self._filePath,"r") as self._fileObj:
                recordList=[]
                line=self._fileObj.readline()
                while line!="":
                    print(line)
                    recordList.append(line)
                    line=self._fileObj.readline()
                print(recordList)
                return recordList
        except ValueError as msg:
            print(msg)
        except IOError:
            print("file not found")
            self.IOerror()
    def IOerror(self):
        done=False
        while not done:
            done=self.openFile("w")
    def readRecordtoDict(self):
        try:
            recordList=self.readRecordtoList()
            myDic=self.recordtoDict(recordList)
            return myDic
        except IndexError as msg:
            print(msg)
        except Exception as msg:
            print(msg)
    def Strip(self,listTwo):
        if len(listTwo)==2:
            listTwo[0]=listTwo[0].strip()
            listTwo[1]=listTwo[1].strip()
            return listTwo[0],listTwo[1]
        else:
            raise IndexError("list must be of pairs")    
    def recordtoDict(self,recordList:list):
        myDic={}
        try:
            for record in recordList:
                myRecord=record.split(" = ")
                Mainkey,val=self.Strip(myRecord)
                subVal=val.split(",")
                subVal.pop(-1)
                entries={}
                for val in subVal:
                    pair=val.split(":")
                    key,val=self.Strip(pair)
                    val=self.convertType(val)
                    entries[key]=val
                myDic[Mainkey]=entries
            return myDic
        except IndexError as msg:
            raise
        except Exception as msg:
            raise
        
    def convertType(self,val):
        try:
            if val.isdigit():
                val=int(val)
            elif "." in val:
                val=float(val)
            else:
                pass
        except ValueError as msg:
            print(msg)
        finally:
            return val
    def removeLine(self,key):
        try:
            with open(self._filePath, "r+") as self._fileObj:
                filecontent = self._fileObj.readlines()
                self._fileObj.seek(0)
                for record in filecontent:
                    entry=record.split("=")
                    if entry[0].strip() != key:
                        self._fileObj.write(record)
                self._fileObj.truncate()
        except ValueError as msg:
            print(msg)
        except IOError:
            print("file not found")
    def updateLine(self,key,diction):
        self.removeLine(key)
        self.writeFileComp(key,diction)
    def removeAll(self):
        open(self._filePath, 'w').close()