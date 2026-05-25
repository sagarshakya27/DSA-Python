#Example Graph-
# consider this graph
# text
#   A------B
#   |      |  
#   |      |
#   C------D
# Connection:
# A->B
# A->C
# B->D
# C->D
#Adjacency Matrix Representation
# |   | A | B | C | D |
# | - | - | - | - | - |
# | A | 0 | 1 | 1 | 0 |
# | B | 0 | 0 | 0 | 1 |
# | C | 0 | 0 | 0 | 1 |
# | D | 0 | 0 | 0 | 0 |


class Graph:
    def __init__(self,vertices):
    #Total number of vertices
        self.v=vertices

        #create adjacency matrix with all 0s
        self.matrix = [[0 for _ in range(vertices)]
                       for _ in range(vertices)]
        ## Add edge between two vertices
        # def add_edge(self,u,v):

    #Display matrix
    def display(self):
        for row in self.matrix:
            print(row)

    def add_edge(self,u,v):
        self.matrix[u][v] =1
        self.matrix[v][u] =1 #For undirected graph

    #remove edge
    def remove_edge(self,u,v):
        self.matrix[u][v] =0
        self.matrix[v][u] =0


#Create graph with 4 vertices
g = Graph(4)



#Add edge
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(2,3)

#Remove edge
g.remove_edge(0,1)
g.remove_edge(0,2)
g.remove_edge(1,3)
g.remove_edge(2,3)


print("Adjacency Matrix")
g.display()
