#why python is called as dynamic typed language
#(interpreter check code line by line)
# age=33
# pi=3.14
# name="Rushi"
# result=True


#print(type(age))  #type gives you in which class the values belong
#print(type(pi))
#print(type(name))
#print(type(result))


# print(id(age))  #id function returns the address of that function
# print(id(pi))
# print(id(name))
# print(id(result))


#why all fundamental datatypes are immutable(Not changable)
# math=50
# chem=50
# phy=50
# print(id(math))  #temporary allocation of memory
# print(id(chem))
# print(id(phy))


#print(2+2)
#print("2"+"2")
#a = int(input("Enter the first number :")) #input function takes everything as a string
# = int(input("Enter  the second number: "))
#print(a+b)


#int() used to convert
# print(int(3.14))
# #print(int(10+5j)) 
# print(int(True))#=1
# print(int(False))#=0
# #print(int("4.22"))
# print(int("4"))
#print(int("rushi"))
#we can not convert complex value to int
#we can not convert floating point value string to int
#can't convert string name to int'''


#float() used to convert
# print(float(3))
# #print(float(50+2j)) 
# print(float(True))#=1
# print(float(False))#=0
# print(float("4.22"))
# print(float("4"))
#print(float("rushi"))
#print(float("name"))
#we can not convert complex value to float
# can't convert string name to float


# complex() used to convert
# print(complex(3))
# print(complex(12.5)) 
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))
# #print(complex("name"))
# print(complex(5,-3))
# print(complex(True,False))


#bool() is used to convert
# print(bool(0))
# print(bool(15)) 
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2j))
# print(bool(0+0j))
# print(bool(-1))
# print(bool(True))
# print(bool(False))

#simple if
# a = int(input("Enter any single digit :"))
# if a>0:
#     print("positive number")
# if a<0:
#     print("negative number")
# if a==0:
#     print("zero")


# day = input("Enter you day name :")
# if day == "SATURDAY" or day =="saturday" or day =="SUNDAY" or day =="sunday":
#     print("weekend")
# else:
#     print("working day")


# per = 50
# if per >= 65:
#     print("Grade A")
# elif per <= 65 and per >= 50:
#     print("Grade B")
# else:
#     print("Fail")


# ASCII CODE VALUES 
# A=65
# a=97
# 0=48
 

# ch = ord(input("Enter any one character : ")) #ord function convert the value to ascii code
# if ch >= 65 and ch <= 90:
#     print("Upper Case")
# elif ch >= 97 and ch <= 122:
#     print("Lower Case")
# elif ch >= 48 and ch <= 57:
#     print("Digit")
# else:
#     print("Special Symbol")  


# #membership operator (in)
# name = "help4code"
# print ('z' not in name)


# #identity operator (used for address comparision)
# math = 50
# chem = 50
# print(math is chem)


#for loop (When range is given)
#for(initialization; condition; inc/dec) -> c language
# for i in range(5): #by default value for i=0 to 5
#     print(i)

# for i in range(2,11): #intiatilize i=2 and i<11 is condition
#     print(i)

# for i in range(2,11,2): #i=2 and i<11 is condition and incremented by 2
#      print(i) 

# for i in range(5,0,-1): #i=5
#      print(i)

# for i in range(1,11): #i=1
#     print(i*2) #2, 4, 6, 8, ....20

# #Make a table of multiplication 2 to 20
# for i in range(1,11): 
#      print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)
# print()
# print("=======================================================================================")
# for i in range(1,11): 
#      print(i*11," ",i*12," ",i*13," ",i*14," ",i*15," ",i*16," ",i*17," ",i*18," ",i*19," ",i*20)
# print("=======================================================================================")


# #WAP to accept three paper marks and calculate total, percentage and check if he/she is passed in all the subject so print
# #pass else print fail  if percentage is greater than 65 and gender ="male" so he is eligible cor placement else not eligible
# phy = int(input("Enter the marks of phy :"))
# che = int(input("Enter the marks of che :"))
# math = int(input("Enter the marks of math :"))
# total = math + phy + che
# percentage = total/3.0
# print("Total =",total)
# print("percentage =",percentage,"%")
# if phy >=40 and che >=40 and math >=40:
#     print("Pass")
# else:
#     print("False")
# gender =input("Enter your gender M/F :")
# if percentage >=65 and gender == "M":
#     print("Eligible for placement")
# else:
#     print("Not Eligible")


# for i in range(1,5):#i=1
#         if i == 3:
#             break
#         print(i)

# for i in range(1,5):#i=1
#         if i == 3:
#             continue #continue means next iteration without printing anything
#         print(i)

#Que- WAP for Output-
# 1    5
# 2    4 
# 4    2
# 5    1
#zip() function- we can take multiple range function inside zip()
# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i," ",j)




# Removing spaces from the string:
# 1. rstrip()==> To remove spaces at right hand side
# 2. lstrip()==> To remove spaces at left hand side
# 3. strip()==> To remove spaces both side

# city = input("Enter your city Name:")
# scity=city.strip()
# if scity =='Hydrabad':
#     print("Hello Hydrabadi..Adab")
# elif scity =='Channai':
#     print("Hello Madrasi..Vabakkam")
# elif scity =='Bangalore':
#     print("Hello Kannadiga..Shubhodaya")
# else: print("Your enterd city is invalid")



#Row wise max value
# mylist=[[100,198,333,323],
#   [122,232,221,111],
#   [223,565,245,764]]


# newlist=[]
# for i in range(3):
#     j=0
#     max = mylist[i][j]
#     for j in range(4):
#         c_max = mylist[i][j] 
#         if max < c_max:
#             max = c_max
#     newlist.append(max)
# print(newlist)


#i/p- prashant*is*a*good*progrmmer
#o/p-****prashantisagoodprogrammer
# name="prashant*is*a*good*progrmmer"
# newname='' # prashant
# val=''# ****
# for i in name:#i=8:*
#     if i !='*':
#         newname += i
#     else:
#         val += i
# print(newname)
# print(str(val+newname))


#i/p- aaabbbbccceeeee
#o/p- a3b4c3e5
# name = "aabbbbeeeeffggg"
# newname={}
# for i in range(len(name)):
#     key= name[i]
#     count=0
#     for j in range(len(name)):
#         if key == name[j]:
#             count +=1
#     newname[key] = count
# #print(newname)
# for i,j in newname.items():
#     print(i,j,sep='',end='')


# salary = int(input('Enter your salary :'))
# rating = int(input('Enter your performance appraisal rating :'))
# increment =0
# if rating >= 1 and rating <=3:
#     increment = salary*10/100
# if rating >= 3.1 and rating <=4:
#     increment = salary*30/100
# if rating >= 4.1 and rating <=5:
#     increment = salary*40/100
# else:
#     print('Invalid rating')
# print('Incremented Salary: ',increment+salary)


#basic salary=20000
# so we have to calulate the 
# HRA of basicSalary =20%
# TA of -------------=30%
# DA of--------------= 45%
# calculate GrossSalary= ?
# salary = int(input('Enter your salary :'))
# HRA=salary*20/100
# TA=salary*30/100
# DA=salary*45/100
# GROSSSALARY=salary+(HRA+TA+DA)
# print(GROSSSALARY)







