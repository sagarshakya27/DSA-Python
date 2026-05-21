#In the tree structure --->
#1. There is exactly one root node
#2. Every node (except root) has only one parent
#3. A node can have 0 or more children
#4. There are no cycles
#5. All nodes are connected (reachable from root)
#6. There is exactly one path between any two nodes
#7. A tree with N nodes has N − 1 edges

### Array Representation-
# class Tree:
#     def __init__(self,data):
#         self.data = data #("Drinks") ("Hot")("Cold")
#         self.child =[]

#     def __str__(self,level =0):
#         ret=" "*level+str(self.data)+"\n"
#         for ch in self.child:
#             ret += ch.__str__(level+1)
#         return ret
        

#     def addChild(self, object):
#         self.child.append(object)
#         print("Tree node added")


# rootNode = Tree("Drinks")
# Hot      = Tree("Hot")
# Cold     = Tree("Cold")
# Tea      = Tree("  Tea")
# Coffee   = Tree("    Coffee")
# NonAlcholic = Tree("   Non Alcholic")
# Alcholic = Tree("         Alcholic")

# rootNode.addChild(Hot)    #Left
# rootNode.addChild(Cold)   #Right
# Hot.addChild(Tea)         #Left
# Hot.addChild(Coffee)      #Right
# Cold.addChild(NonAlcholic)#Left
# Cold.addChild(Alcholic   )#Right

# print(rootNode) 



