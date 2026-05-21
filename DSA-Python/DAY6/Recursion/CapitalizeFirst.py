#capitalizeFirst solution using recurision 

def capitalizeFirst(arr):#['car','taco','banana']
    result = []#empty list
    if len(arr) == 0:
        return result
    
    result.append(arr[0][0].upper()+arr[0][1:])#C+ar=Taco
    return result + capitalizeFirst(arr[1:])
print(capitalizeFirst(['car','taco','banana']))#['Car', 'Taco', 'Banana']


#   row col
#arr[0][0]
#   012
#0='car'  ===>C