#When the main problem can be divivded into similar sub problem then you use Recursion
#Recursion used the stack memory

#Factorial Solution
def factorial(num):#num=1
    if num <=1:# base condition
        return 1
    return num * factorial(num-1)
print(factorial(4))

#4*factorial(3)
#3*factorial(2)
#2*factorial(1)
#4*3*2*1=24