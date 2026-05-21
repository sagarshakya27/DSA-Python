#Stack implementation without size limit
#Stack implementation with size limit

# There are two ways
# 1. List/Array
# 2. Linkedlist(when have bulk amount of data)

#ex-1
# class Name:
#     age =30 # data member
#     def display(self):#method   #first default argument of class
#         print("Hello World")

# obj = Name() #object is also called as a reference variable
# print(obj.age)
# obj.display()


#ex-2
# class Student:
#     def __init__(self):
#         self.name = ""  # 4 byte
#         self.age=30     #2 byte
    
#     def display(self):
#         print("Name=",self.name)
#         print("Age",self.age)
# stuObj = Student()
# print(stuObj)



#ex-3(Defult constructor)
# class Message:
#     def __init__(self):
#         print("I am constructor")

#     def show(self):
#         print("Class program")

# obj = Message() # for one obj constructor call one time
# obj.show()
# obj2 = Message()

#ex-4(Parameterized constructor)
# class StudentInfo:
#     def __init__ (self,name,age,roll_no):
#         self.Name = name
#         self.Age = age
#         self.RollNo = roll_no
    
#     def displayStudentInfo(self):
#         print("Name", self.Name)
#         print("Age", self.Age)
#         print("RollNo",self.RollNo)
    
# studentObj = StudentInfo("Prakash",34,101)
# studentObj.displayStudentInfo()



#=====================================================================
#Stack implementation without size limit
#Stack implementation with size limit




# there are two ways
# 1.List/Array
# 2. Linkedlist(when have bulk amount of data)




#This is without size limit----->
# import sys
# class Stack:
#     def __init__(self):
#         self.myStack=[] #creating stack
    
#     def push(self,value):
#         self.myStack.append(value)
#         print("Element push")
    
#     def display(self):
#         print(self.myStack)

#     def isEmpty(self):
#         if self.myStack == []:
#             return True
#         else:
#              return False
    
#     def pop(self):#permanetly delete the top of the element
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print(self.myStack.pop())    
    
#     def peek(self):#only return top most element
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print(self.myStack[-1])

#     def deleteStack(self):
#         self.myStack = None

# obj = Stack()
# print("Stack  has created: ")
# while True:
#     print("1. Push Operation: ") 
#     print("2. Display stack: ")
#     print("3. Pop Operation: ")
#     print("4. Peek Operation: ")
#     print("5. Delete Operation: ")
#     print("6. Exit")
#     choice = int(input("Enter Your Choice: "))
#     if choice == 1:
#         value = int(input("Enter value to push in stack : "))
#         obj.push(value)
#     elif choice == 2:
#         obj.display()
#     elif choice == 3:
#         obj.pop()
#     elif choice == 4:
#         obj.peek()
#     elif choice ==5:
#         obj.deleteStack()
#     else:
#         sys.exit()






#This is with size limit----->
# import sys

# class Stack:
#     def __init__(self, size):
#         self.myStack = []    # creating stack
#         self.stackSize = size   #stack size defined

#     def isFull(self):
#         if len(self.myStack) == self.stackSize:
#             return True
#         else:
#             return False

#     def push(self, value):
#         if self.isFull():
#             print("Stack is full")
#         else:
#             self.myStack.append(value)
#             print("Element push")  

#     def display(self):
#         print(self.myStack)

#     def isEmpty(self):
#         return self.myStack == []

#     def pop(self):
#         if self.isEmpty():
#             print("Stack Underflow! Stack is empty.")
#         else:
#             print("Popped Element:", self.myStack.pop())

#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Top Element:", self.myStack[-1])

#     def deleteStack(self):
#         self.myStack = []
#         print("Stack Deleted")







# # Taking stack size from user
# size = int(input("Enter the size of stack: "))
# obj = Stack(size)
# print("Stack has created")
# while True:
#     print("1. Push Operation")
#     print("2. Display Stack")
#     print("3. Pop Operation")
#     print("4. Peek Operation")
#     print("5. Delete Stack")
#     print("6. Exit")

#     choice = int(input("Enter Your Choice: "))

#     if choice == 1:
#         value = int(input("Enter value to push in stack: "))
#         obj.push(value)

#     elif choice == 2:
#         obj.display()

#     elif choice == 3:
#         obj.pop()

#     elif choice == 4:
#         obj.peek()

#     elif choice == 5:
#         obj.deleteStack()

#     elif choice == 6:
#         sys.exit()

#     else:
#         print("Invalid Choice")


###Stack using list---->
# Easy to implemet
# speed problem when it grows

###Stack using Linked list---->
# fast performance
# Implementation is not easy

