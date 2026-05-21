# # ProductOfArray Solution

def productOFArray(arr):#[1,2,3]  [2,3]   [3]     []
    if len(arr) == 0:    #3==0     2==0    1==0   0==0
        return 1
    return arr[0] * productOFArray(arr[1:])

print(productOFArray([1,2,3])) #1*2*3*1=6  
print(productOFArray([1,2,3,10])) #60