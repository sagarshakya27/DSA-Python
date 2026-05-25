# class student:
#     #by using class name we can access static method
#     @staticmethod #decorator
#     def get_personal_detail(firstname,lastname):
#         print("your personal detail=",firstname,lastname)

#     @staticmethod
#     def contact_detail(mobile_no,rollno):
#         print("your contact detail=", mobile_no,rollno)

# student.get_personal_detail("prashant","jha")
# student.contact_detail(545454545,1001)

# ========================================================
#Garbage collector in python
#desructor -> resource reallocate

#=========================================================
'''Inheritance'''
'''Single level inheritance'''

# class College: #parent class
#     def college_name(self): #member function of college
#         print("Modern College")
    
# class Student(College): #child class
#     def student_info(self): #member function
#         print("Name: Prashant Jha")
#         print("Branch: Computer Science")

# obj = Student() #object create child class
# obj.college_name()
# obj.student_info()

#=========================================================
'''Multilevel inheritance'''
# class College: #first class first--level
#     def college_name(self): #member function of college
#         print("Modern College")
    
# class Student(College): #second class second-level
#     def student_info(self): #member function
#         print("Name: Prashant Jha")
#         print("Branch: Computer Science")
# class Exam(Student): #child class
#     def subject(self):
#         print("Subject1: Design Engineering")
#         print("Subject2: Matg")
#         print("Subject3: C-Language")
# obj = Exam()
# obj.college_name()
# obj.student_info()
# obj.subject() 

#=========================================================
'''Multiple inheritance'''
# class SubjMarks:  #class-1
#     math = int(input("Enter paper marks of math :"))
#     DE = int(input("Enter paper marks of DE :"))
#     C = int(input("Enter paper marks of C :"))
#     english = int(input("Enter paper marks of english :"))

# class PracticalMarks:
#     cpract=int(input("Enter practicals marks of c language:"))

# class Result(SubjMarks,PracticalMarks):
#     def total(self):
#         if self.math>=40 and self.DE>=40 and self.C>=40 and self.english>=40 and self.cpract>=20:
#             print("pass")
#         else:
#             print("fail")
# obj = Result()
# obj.total()  

#=========================================================
'''Multiple Inheritance example-(To check Ambiguity)'''

# class A:
#     def college_name(self):
#         print("ABC College")

# class B:
#     def student_info(self):
#         print("Name: Rahul")
#         print("Roll No: 101")

# class C(A, B):
#     def all_info(self):
#         self.college_name()
#         self.student_info()

# obj = C()
# obj.all_info()

#============================================================
#Python does not support constructor overloading 

#============================================================
# class Rbi:
#     def home_loan(self):
#         print("Home Loan ROI = 8%")
#     def education_loan(self):
#         print("Education Loan ROI = 9%")

# class Sbi(Rbi):# Inheriting Rbi
#     def education_loan(self):
#         print("Education loan = 10%")
#         #When you want to acces parent class method then?? -> super()
#         super().education_loan()


# obj = Sbi()
# obj.education_loan() #child class method overrides the parent class method
    
#=================================================================================

# class Rbi:
#     def __init__(self):
#        print("Parent class constructor")

# class Sbi(Rbi):# Inheriting Rbi
#     def __init__(self):
#        print("Child class constructor")
#        #super().__init__() #for accessing parent class constructor
# obj = Sbi()
