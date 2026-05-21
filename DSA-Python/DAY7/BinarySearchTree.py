class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
newBST = BSTNode(None)

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
           rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)    

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data,end=" ")
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data,end=" ")
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data,end=" ")
    

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")    
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
           print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)


newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)
insertNode(newBST, 10)
preOrderTraversal(newBST)
print("===>Pre order Traversal")
inOrderTraversal(newBST)
print("===>In order Traversal")
postOrderTraversal(newBST)
print("===>In order Traversal")

searchNode(newBST, 20)



#(pre order traversal  (root----> left-----> right))===> 70 50 30 20 10 40 60 90 80 100
#(inorder traversal    (left----> root-----> right))===> 10 20 30 40 50 60 70 80 90 100
#(post order traversal (left----> right-----> root))===> 10 20 40 30 60 50 80 100 90 70