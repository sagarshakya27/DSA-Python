def power(base,exponent): #2,0
    if exponent == 0:  # 0 == 0
        return 1
    return base * power(base,exponent-1)

print(power(2,0)) #1
print(power(2,2)) #4
print(power(2,4)) #16

#2*2*1