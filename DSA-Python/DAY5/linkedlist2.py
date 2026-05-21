##Dynamically created linked list-
class Node:
    def __init__(self,data):
        self.data = data #instance variable(5)(10)
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,value):#5
        self.node = Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else:
            self.tail.next = self.node
            self.tail      = self.node
    
    #display node
    def displayNode(self):
        while self.head != None:   
            print(self.head.data, "|",'->', end=" ")
            self.head = self.head.next  
        print() 

    
    def addNodeBiginning(self,value):
        print("Add node begining")
        self.node  = Node(value)
        if self.head is None:
            self.head=self.node
            self.tail=self.node
        else:
            self.node.next=self.head
            self.head=self.node

if __name__ =="__main__":
    object = LinkedList() # Linkedlist object created
    #Menu driven options
    while True:
        print('1. Add Node Linkedlist :')
        print('2. Add Node in begining :')
        print('3. Add Node Between :')
        print('4. Add Node End :')
        print('5. Display Linkedlist :')
        print('6. Exit :')
        ch = int(input('Enter your choice:'))
        if ch ==1:
            value = int(input('Enter value for node:'))#5
            object.addNode(value)
            print('Node added successfully in single Linkedlist: ')
        elif ch ==2:
        
            value = int(input('Enter value for node:'))
            object.addNodeBiginning(value)
        elif ch ==2:
            value = int(input('Enter value for node:'))
            object.addNodeBiginning(value)
        elif ch ==5:
            object.displayNode()
    