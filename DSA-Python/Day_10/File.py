#write a python program to extract all mobile
#input.txt where numbers are mixed with normal
# import re

# f1 = open("input.txt", "r")
# f2 = open("output.txt", "w")
# content = f1.read()
# numbers = re.findall("[7-9]\d{9}", content)
# for num in numbers:
#     f2.write(num + "\n")
# f1.close()
# f2.close()
# print("Mobile numbers extracted successfully")

#=================================================================================================

#Program to print the number of lines, words and characters present in the given file?
# import os,sys
# fname = input("enter file name: ")
# if os.path.isfile(fname):
#     print("File exists:",fname)
#     f=open(fname,"r")
# else:
#     print("File does not exist:",fname)
#     sys.exit(0)
# lcount=wcount=ccount=0
# for line in f:
#     lcount=lcount+1
#     ccount=ccount+len(line)
#     words=line.split()
#     wcount=wcount+len(words)
# print("The number of Lines:",lcount)
# print("The number of Words:",wcount)
# print("The number of Characters:",ccount)
