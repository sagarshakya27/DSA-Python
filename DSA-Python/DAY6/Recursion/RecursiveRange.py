# recursiveRange Solution

def recursiveRange(num):#6
    if num <= 0: #6<=0
        return 0
    return num + recursiveRange(num-1)
    #6+5+4...
print(recursiveRange(6))