def isPalindrome(string): #'awesome' #'tacocat'
    if len(string) == 0:
        return True
    if string[0] != string[len(string)-1]:  # a != e  #t != t
        return False
    return isPalindrome(string[1:-1])

print(isPalindrome('awesome')) #False
print(isPalindrome('foobar')) #False
print(isPalindrome('tacocat')) #True
print(isPalindrome('amanplanacanalpanama')) #False
print(isPalindrome('aluula')) #True
