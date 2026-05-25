import time

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __iter__(self):
        curNode = self.LinkedList.head   # corrected
        while curNode:
            yield curNode
            curNode = curNode.next
    
    def __str__(self):
        values = [str(x.value) for x in self]   # corrected
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():   # corrected
            return "There is no any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
    
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodevalue = self.LinkedList.head.value
            return nodevalue
        
    def delete(self):
        self.LinkedList.head = None
    
    def display(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Display Stack again")
            temp = self.LinkedList.head
            while temp is not None:
                print(temp.value)
                temp = temp.next
            print()


customStack = Stack()

customStack.push(1)
time.sleep(2)

customStack.push(2)
time.sleep(2)

customStack.push(3)

print(customStack)

print("Display Top Value:")
print(customStack.peek())

print("Pop top element")
print(customStack.pop())   # corrected

print("Now check the stack again")
print(customStack)

print("Pop top element")
print(customStack.pop())

print("Now check the stack again")
print(customStack)
