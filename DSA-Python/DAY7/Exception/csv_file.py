# import csv
# f = open("employee.csv", 'a', newline='')
# a = csv.writer(f)
# #a.writerow(["EmpID", "Emp Name", "Emp Age"]) #For creating column
# empid=int(input("Enter your empid :"))
# empName=input("Enter employee name :")
# age = int(input("Enter employee age :"))
# a.writerow([empid,empName,age])
# print("File has created")


# Col name= studID | studName |Phy | Chem | Math | Total | Percentage | Result
# input : studied, studname, phy, chem, math
# calulate : total, percentage
# check condition all paper marks >=40 pass else fail
import csv
f = open("student.csv", 'a', newline='')
a = csv.writer(f)
# a.writerow(["studID", "studName", "Phy","Chem","Math","Total","Percentage","Result"])
studID=int(input("Enter your stuid :"))
studName=input("Enter  studName :")
Phy = int(input("Enter Phy Marks :"))
Chem = int(input("Enter Chem Marks :"))
Math = int(input("Enter Math Marks :"))
if Phy>=40 and Chem>=40 and Math>=40:
    Result = "Pass"
    print("You are Pass")
else:
    Result="Fail"
Total = Phy + Chem + Math 
Percentage = Total/300*100
a.writerow([studID,studName,Phy,Chem,Math,Total,Percentage,Result])
print("File has created")
