# Reverse a string using recursion

def reverse(string): #'python' 'pytho'
    if len(string) <= 1: #6<=1  5<=1
        return string 
    return string[len(string)-1] + reverse(string[0:len(string)-1])  #6-1=5    #5-1=4               
                                                                     #n pytho  #no pyth                
print(reverse('python')) #'nohtyp'
print(reverse('appmillers')) #'srellimppa'