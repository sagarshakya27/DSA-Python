#{key,value}

# mydict = {
#     101:"prashant",
#     102:"ashish",
#     "103":"monini",
#     "104":"trivini",#string data type
#     101:"ashish",#value updated
#     104:"ashish" #int data type
# }
# print(mydict)

#Note- Tuple is considered as a key

#wiht the help of key we have to print values
# a=mydict[102]
# print(a)

#we will replace old value by new value
# mydict[102]="peter"
# print(mydict)

#only print key x=0,1
# for x in mydict:
#     print(x)

#only print values
# for x in mydict.keys():
#     print(x)

#printing key and values both
# for x,y in mydict.items():
#     print(x,y)

#adding a new key:value pair
# mydict["mobile_no"]=4646463738
# print(mydict)

# mydict["Departmnet"]="management"
# print(mydict)

#pop() method remove pair by specific key name
# mydict.pop(101)
# print(mydict)

# a={(1,2):1,(2,3):2,(4,5):3} #(1,2) is considerd as a key and 1 as a value
# print(a[(4,5)])

# a={'a':1,'b':2,'c':3}
# print(a['a','b']) #syntactical error

# arr = {} 
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# #print(arr) #{1:2,'1':2}
# sum = 0 #2,2=4
# for k in arr: #k=1, k='1'
#     sum += arr[k]
# print(sum)

# my_dict = {} 
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4 #this is updated in privious key value
# #print(my_dict) #{1:4,'1':2}
# sum = 0 
# for k in my_dict: #k=1, k='1'
#     sum += my_dict[k]
# print(sum)

# my_dict ={}
# my_dict[(1,2,4)]=8
# my_dict[(4,2,1)]=10
# my_dict[(1,2)]=12
# sum=0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)


# box ={}
# jars={}
# crates={}
# box['biscuit']=1
# box['cake']=3
# jars['jam']=4
# crates['box']=box
# crates['jars']=jars
# print(len(crates[box]))


# dict = {'c':97,'a':96,'b':98}
# for _ in sorted(dict): #use _ instead of variable
#     print(dict[_])


# rec = {"Name":"Python","Age":"20"}
# r = rec.copy()
# # print(id(rec))  #id() function returns address
# # print(id(r))
# print(id(r) == id(rec))

# rec = {"Name":"Python","Age":"20","Addr":"NJ","Country":"USA"}
# id1=id(rec)
# #print(id1)
# del rec
# rec = {"Name":"Python","Age":"20","Addr":"NJ","Country":"USA"}
# id2=id(rec)
# #print(id2)
# print(id1 == id2)

#i/p- {"A":50,"B":30,"C":70}
#o/p- "C"
# mydict={"A":50,"B":30,"C":70}
# max_key = max(mydict, key=mydict.get)
# print(max_key) 

#i/p- {"X":20,"Y":10,"Z":30}
#o/p- "Y"
# mydict = {"X":20, "Y":10, "Z":30}
# min_key = min(mydict, key=mydict.get)
# print(min_key)


# #i/p- {1,2,2,3,4,3,5}
# #o/p- {"1":1,"2":2,"3":2,"4":1,"5":1}
# mydict={1,2,2,3,4,3,5}
# for i in mydict:
#     print()




#Write a program to accept student name and marks from the keyboard and creates
# a dictionary. Also display student marks by taking student name

# n=int(input("Enter the number of student: "))
# d={}
# for i in range(n):
#     name=input("Enter the name: ")
#     marks=input("Enter the marks: ")
#     d[name]=marks #add key:value
# while True:
#     name=input("Enter Student Name to get Marks: ")
#     marks=d.get(name,-1)
#     if marks ==-1:
#         print("Student Not Found")
#     else:
#         print("The Marks of",name,"are",marks)
#     option=input("Do you want to find another student marks[Yes | No ]")
#     if option=="No":
#         break
# print("Thanks for using our application")




#Write a program to access each character of string in forward and backward direction by using while loop?
#i/p- "Learning Python is very easy"
# s = "Learning Python is very easy !!!"
# n=len(s)
# i = 0
# while i < n:
#     print(s[i], end=" ")
#     i += 1
# print("            Forward direction")
# i=-1
# while i >=- n:
#     print(s[i], end=" ")
#     i -= 1
# print("            Backward direction")


# v=['a','e','i','o','u']
# w= input("Enter the word where we will search the vowel:")
# # w = prashantjha
# found=[]#a
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('Found vowels=',found)
# print('unique vowels',len(found),'from the given word=',w)



# x, y, z = map(int, input().split())

# mylist = []
# for i in range(x):
#     a = int(input())
#     mylist.append(a)

# for j in mylist:
#     if y <= j <= z:
#         print(j, end=' ')



# import datetime 
# #datetime formatting
# date=datetime.datetime.now()
# print("It's now:{:%d/%m/%Y %H:%M:%S}".format(date))




# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x != z)




# val=[2**i for i in range(1,6)]#i=1,2,3,4,5
# print(val)

# s=[i*i for i in range(1,11)]#i=4
# print(s) #s =[1,4,9,16,25,36,49,64,81,100]

#Dictionary Comprehension

# square={x:x*x for x in range(1,6)}
# print(square)

# double={x:2*x for x in range(1,6)}
# print(double)

#=================================================================
#How to read multiple values from the keyboard in a 
#Single line:
# a,b= [int(x) for x in input("Enter 2 number :").split()]
# print("Product is :",a*b)


# a,b,c= [float(x) for x in input("Enter 3 float number :").split(' ')]
# print("The Sum is: ",a+b+c)

#using else block
# mycart=[10,20,800,60,70]
# for item in mycart: 
#     if item>400:
#         print("This is not in my budget")
#         continue
#     print(item)
# else:
#     print("You have purchased everything")


# username="admin"
# password="admin"
# while True:
#     username=input("Enter the username: ")
#     password=input("Enter the password: ")
#     if username == "admin" and password == "admin":
#         print("login")
#         break
#     else:
#         print("Invalid")
#         break
