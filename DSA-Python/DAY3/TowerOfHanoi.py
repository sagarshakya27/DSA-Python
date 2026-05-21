import time
class Tower:
    def __init__(self):
        print("WELCOME TO TOWER OF HANOI GAME")
        print()
        print("Given Problem   A=[3,2,1]    B=[]    C[]  ")
        print()
        print("Expected Output A=[]         B=[]    C[3,2,1]")
        self.A=[]
        self.B=[]
        self.C=[]

    def tower(self,item):
        self.A.append(item)
        time.sleep(3)
        print("A=",self.A)
        print("Items in Tower a\n")
    
    def pass1(self):
        self.temp = self.A.pop(2) #A=[3,2]
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"   ",    "B=",self.B   ,"   ","C=",self.C)
        print("Pass One completed==============\n")

    def pass2(self):
        self.temp = self.A.pop(1) 
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"   ",    "B=",self.B   ,"   ","C=",self.C)
        print("Pass two completed==============\n")

    def pass3(self):
        self.temp = self.A.pop(0) #A=[3,2]
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"   ",    "B=",self.B   ,"   ","C=",self.C)
        print("Pass 3 completed==============\n")

    def pass4(self):
        self.temp = self.A.pop(0) #A=[3,2]
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"   ",    "B=",self.B   ,"   ","C=",self.C)
        print("Pass 4 completed==============\n")

    def pass5(self):
        self.temp = self.B.pop(1) #A=[3,2]
        self.A.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"   ",    "B=",self.B   ,"   ","C=",self.C)
        print("Pass 5 completed==============\n")

    def pass6(self):
        self.temp = self.A.pop(0) #A=[3,2]
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"   ",    "B=",self.B   ,"   ","C=",self.C)
        print("Pass 6 completed==============\n")  

    def pass7(self):
        self.temp = self.A.pop(0) #A=[3,2]
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"   ",    "B=",self.B   ,"   ","C=",self.C)
        print("Pass 7 completed==============\n")  

obj=Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()
