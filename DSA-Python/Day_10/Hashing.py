# Hashing is a technique used to convert data inot a fixed size value called hash value or hash Code
#This hash value helps us store and retrieve data efficiently in a hash table

# #example-
# 10 student - easy to search
# 10 lakh student- searching becomes true without hashing searching becomes slow

# Hashing Time Complexity- O(1) constant time

#Hash Function-
#hash function converts input --> fixed index
#example-  hash("apple") -> might produce-> 2531547955

class HashTable:
    def __init__(self,size):
        self.size = size
        self.table= [[] for _ in range(size)]
    
    def hash_function(self,key):
        return key % self.size
    
    def insert(self,key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def display(self):
        print(self.table)
    
    
