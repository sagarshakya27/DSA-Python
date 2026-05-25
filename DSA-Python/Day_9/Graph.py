#                               Graph
#                         /                    \
#             Directed                               Undirected
#            /          \                          /             \
#      Weighted          Unweighted         Weighted                 Unweighted
#       /      \                         /         \
#   Positive   Negative                 Positive   Negative


#If a graph is complete or alomost complete we should use Adjacency Matrix
#If the number of edges are few then we should use Adjacency List


#ex-
#  { A: [B, C, D],
#    B: [A, E],
#    C: [A, D],
#    D: [A,C,E],
#    E: [B,D]
#  }



class Graph:
    def __init__(self):
        self.adjacency_list = {} 

    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])

    def add_edge(self,vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            #self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():

        # Remove vertex from all adjacency lists
            for other_vertex in self.adjacency_list.keys():
                if vertex in self.adjacency_list[other_vertex]:
                    self.adjacency_list[other_vertex].remove(vertex)

        # Remove the vertex itself
            self.adjacency_list.pop(vertex)
            return True

        return False
    
    

    

my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")
my_graph.add_edge("A","B")
my_graph.add_edge("A","C")
my_graph.add_edge("A","D")
my_graph.add_edge("B","A")
my_graph.add_edge("B","E")
my_graph.add_edge("C","A")
my_graph.add_edge("C","D")
my_graph.add_edge("D","A")
my_graph.add_edge("D","C")
my_graph.add_edge("D","E")
my_graph.add_edge("E","B")
my_graph.add_edge("E","D")
my_graph.print_graph()
my_graph.remove_vertex("E")
my_graph.print_graph()
