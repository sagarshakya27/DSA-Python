import logging
logging.basicConfig(filename="newfile.txt",level=logging.DEBUG)
try:
    a=int(input("Enter first integer no:"))
    b=int(input("Enter second integer no:"))
    print(a/b)
except(ZeroDivisionError,ValueError) as message:
    print(message)
    logging.exception(message)
print("Logging Level is set up. Check 'newfile.txt' fro log details.")