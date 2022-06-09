# vertex: node
# edge: connects vertices
# weighted edge: edges can be weighted or nowedge with weight
# bidirectional: edges between two vertices 
# linkedlist can be a tree and tree can be a graph with directional edges.
# linkedlist < tree < graph

# adjacent matrix: respresent a graph with a adjacent matrix. it describes relations between edges in a matrix with 1,0 or weights
# adjacent list: represent a graph with ditionary 

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError: # in case there is no edge between v1 and v2
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
            


    
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.remove_edge('A', 'B')
graph.remove_vertex('A')
graph.print_graph()
