###finditer()- Check Starting(Beginning) and Ending character---->

#Method1- Using comfile function
# import re #re module foor performing all the regular expression based operation
# count=0  #ro count the number of matching found
# pattern = re.compile("function") #string converts into bytecode
# #print(pattern)

# matcher = pattern.finditer("A function in python is defined by a def statment. python The general syntax looks like this:" \
# " def function-name (Parameter list): statments, i.e. the function body. The parameter python list consists of none or more parameters")

# for i in matcher: #i=0
#     count +=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurrence:",count)


#Method2-Using finditer function
# import re
# count=0
# matcher=re.finditer("Hi","HiHiHiHi")

# for i in matcher: #loop 4 times execute HiHiHiHi
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurrence:",count)

#=============================================================================================================
# import re
# obj = input("enter any character: ")
# objmatch=re.finditer(obj,"CSK crash and burn in Ahmedabad, exit IPL 2026 with 89-run loss to GT")
# #print(objmatch)
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())


#============================================================================================================

###Match()- character classes- Check starting(beginning) character---->

# import re
# a = input("enter string to perform match operation: ")
# mtch = re.match(a,"python is very important language")
# print(mtch)
# if mtch != None:
#     print("match found at beginning level")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("there is no matching at beginning level")

#============================================================================================================
###fullmatch()- In Python regex (Regular Expression) checks whether the entire string matches the pattern if not then it returns None
# import re
# a = input("enter string to perform match operation: ")
# mtch = re.fullmatch(a,"pythonisvery")
# print(mtch)
# if mtch != None:
#     print("match found at beginning level")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("there is no matching at beginning level")

#===============================================================================================================

# Write a Python Program to  check whether the given mail:
#valid gmail id or not?
# import re
# s=input("Enter mail id :")
# m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
# if m!=None:
#     print("Valid E-mail id")
# else:
#     print("Invalid E-mail iD")

#===============================================================================================================

#WAP to check the valid mobile number
# import re
# mo = input("Enter mobile number: ")
# obj = re.fullmatch("[6-9]\d{9}",mo)
# if obj!=None:
#     print("valid mobile number")
# else:
#     print("invalid mobile number")

#===============================================================================================================

### Search() function- 
# import re
# a = input("enter string to perform match operation :")
# mtch = re.search(a,"python sss dynamic lannn")
# print(mtch)
# if mtch != None:
#     print(mtch.start()," ",mtch.end()," ",mtch.group())
# else:
#     print("there is no matching anywhere")

#===============================================================================================================

### findall() function- return in list
# import re
# # mtch = re.findall('[0-9]',"abch3hdh45jknkjns") #checking 0 to 9
# # mtch = re.findall('[A-Z]',"abch3hdh45jknkjns") #checking A to Z
# mtch = re.findall('[0-9a-z]',"abch3hdh45jknkjns") #checking 0 to 9 and a to z
# #mtch = re.findall('[^0-9]',"abch3hdh45jknkjns") #excluding this characters
# print(mtch)

#==============================================================================================================

### sub() function- substitute function ex- Aadhar card number- 3245 XXXX XXXX XXXX
# import re
# obj = re.sub('[a-zA-Z]','X','2345 ABCD habc deff')
# print(obj)

#==============================================================================================================

### subn() function- substitute n-function returns in tuple and also returns no. of replacement
# import re
# obj = re.subn('[0-7]','@','ab3gd6nk17')
# print(obj)
# print("the string is=",obj[0])
# print("the number of replacement is=",obj[1])

#===============================================================================================================

