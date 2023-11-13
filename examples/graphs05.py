# live coding on lecture 5, 2023
# an alternative to lecture05.py in the same directory

class Graph:
    "a class of undirected graphs"

    def __init__(self):
        "creates an empty graph"
        # storing list of edges, rather than adjecency list
        # only undirected lists are covered
        self._edges = set()

    def add_edge(self, a, b):
        "adds an edge from a to b"
        # storing edges as frozensets, to avoid duplicate a-b, b-a
        # also avoiding the need for testing this
        self._edges.add(frozenset({a, b}))

    def get_edges(self):
        "returns edges as pairs of nodes"
        # easier to work with than frozensets
        # notice: if an edge is a-a, need to convert {a} to (a, a)
        # we can use the minimum and maximum functions
        # they will do the job for both 1- and 2-element sets
        return {(min(e), max(e)) for e in self._edges}
        
    def adjacency_dict(self):
        "a dictionary from nodes to sets of adjacent nodes"
        dict = {}
        for (a, b) in self.get_edges():
            dict[a] = dict.get(a, set())
            dict[a].add(b)
            dict[b] = dict.get(b, set())
            dict[b].add(a)
        return dict

    def __str__(self):
        "show the expression for the adjacency dictionary"
        return str(self.adjacency_dict())
    

if __name__ == '__main__':
    G = Graph()
    print(G)
    print(G.get_edges())
    G.add_edge(1, 2)
    print(G)
    print(G.get_edges())
    
    G.add_edge(1, 2)
    print(G.get_edges())
    
    G.add_edge(2, 1)
    print(G.get_edges())
    print(G.adjacency_dict())
    
    G.add_edge(2, 2)
    print(G.get_edges())
    print(G.adjacency_dict())

    G.add_edge(3, 2)
    print(G)    

