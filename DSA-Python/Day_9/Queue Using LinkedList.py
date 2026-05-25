class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    def enqueue(self,value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
    
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode
        
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.linkedList.head
        
    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None

    # def display(self):
    #     if self.isEmpty():
    #         print("Queue is Empty")
    #     else:
    #         print("Display Queue again")
    #         temp = self.LinkedList.head
    #         while temp is not None:
    #             print(temp.value)
    #             temp = temp.next
    #         print()

custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue)
print("Display top value :")
print(custQueue.peek())
print("Delete FIFO ")
print(custQueue.dequeue())
print("display Queue Again")
print(custQueue)
print("Delete FIFO")
print(custQueue.dequeue())
print("display Queue again")
print(custQueue)