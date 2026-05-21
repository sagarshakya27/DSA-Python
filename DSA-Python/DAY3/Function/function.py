#function

# def hello(): #called function
#     print("hello world")

# hello() #calling function
# hello()


# def arithmatic():
#     a = int(input("Enter value fo a: "))
#     b = int(input("Enter value of b: "))
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum,sub,div,mul

# #print(arithmatic())     #returns the values in tuple format 
#                         #it is possible to return multiple values
# #or
# result = arithmatic()
# print("Arithmatic :",result)



#How many types of arguments we pass in function?
# 1. Positional argument
# 2. Keyboard argument
# 3. default argument
# 4. variable length argument/variable number of arguements

# 1. Positional argument
# def arithmatic(a,b):
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum,sub,div,mul
# #Positional argument
# result = arithmatic(5,5)
# print("Arithmatic :",result)


# 2. Keyboard argument
#parameter name and keyword name must be same
# def crdential (username,password):
#     if username == password:
#         print("login successfully")
#     else:
#         print("invalid crdentials")
    
# crdential(username="admin",password="admin") #calling function


# 3. default argument
# def cityName(city="Pune"): #default argument
#     print(city)

# cityName("Nagpur")
# cityName("Mumbai")
# cityName()#calling default argument


# 4. variable length argument/variable number of arguements
# def cityName(*name): #the no. of argument accept in tuple format using *
#     print(name)

# cityName("Nagpur","Delhi","Mumbai","Pune")



#modularity approach in function
import sys

def add():
    a = int(input("Enter value of A:"))
    b = int(input("Enter value of B:"))
    print(a+b)

def sub():
    a = int(input("Enter value of A:"))
    b = int(input("Enter value of B:"))
    print(a-b)

def mul():
    a = int(input("Enter value of A:"))
    b = int(input("Enter value of B:"))
    print(a*b)

def div():
    a = int(input("Enter value of A:"))
    b = int(input("Enter value of B:"))
    print(a/b)

while True: # True means it will run infinite times
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice =int(input("Enter your choice: "))
    if choice == 1:
        add() #calling function
    elif choice == 2:
        sub() #calling function
    elif choice == 3:
        mul() #calling function
    elif choice == 4:
        div() #calling function 
    elif choice == 5: 
        sys.exit() 
