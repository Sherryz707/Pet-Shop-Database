class inputValid(): 
    def floatInput(self,categ): 
        while True:
            try:
                print("Enter",categ,": ")
                price=float(input())
                if price<=0:
                    raise ValueError
            except ValueError as msg:
                print("Price entered must be greater than 0.")
            else:
                return price
    def intInput(self,categ): 
        while True:
            try:
                print("Enter",categ,": ")
                qty=int(input())
                if qty<=0:
                    raise ValueError
            except ValueError as msg:
                print("Price entered must greater than 0.")
            else:
                return qty
    def stringInput(self,categ): 
        while True:
            try:
                print("Enter",categ," in form of (e.g: BURGER_KING) : ")
                item=input()
                if " " in item or "-" in item or item.isdigit() or item.islower():
                    raise ValueError("Name must be in capital letters with no space.This is the required format: ABC_XYZ")
            except ValueError as msg:
                print(msg)
            except Exception as msg:
                print(msg)
            else:
                return item
    def boolInput(self,val1,val2): 
        while True:
            try:
                print("Enter",val1,"or",val2)
                boolInp=(input()).upper()
                if boolInp!=val1 and boolInp!=val2:
                    raise ValueError("Input must be",val1,"or",val2)
            except ValueError as msg:
                print(msg)
            except Exception as msg:
                print(msg)
            else:
                return boolInp
    def exceptionHandling(self,error):
            print("Error occured: ",type(error).__name__,"due to ",error)
    def matchInput(self,inp,categ): 
        while True:
            print("Enter",categ,"or Q to quit")
            match=input().upper()
            if match=="Q":
                raise Exception("exiting....")
            if match!=inp:
                raise Exception("Values dont match i.e", match,"is not equal to",inp)
            else:
                return match
    def matchListInput(self,categ): 
        categ=list(categ)
        while True:
            toConvert=type(categ[0])
            option=input("Enter to search by or Q to quit: ").upper()
            if option=="Q":
                raise Exception("exiting....")
            elif toConvert(option) in categ:
                return toConvert(option)
            else:
                print("Invalid category. Try again")        
            
