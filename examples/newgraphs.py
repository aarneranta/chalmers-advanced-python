"""
A class for undirected graphs for Lecture 5 at Chalmers second course on programming.
"""

import graphviz as gv
import copy

class Graph:
    "Undirected graph, vertices must have an ordering."
    def __init__(self):
        """
        Initialize with an empty graph, represented as empty
        adjacency dictionary. To avoid redundancy, the dictionary
        stores b in the set of neighbors of a if and only if a <= b.
        All vertices have at least an empty set of neighbors stored.
        """
        self._adjacency = {}

    def add_edge(self, a, b):
        "add an edge from a to b, stored for key a if a<=b; also add b as key"
        a, b = sorted((a, b))
        self._adjacency[a] = self._adjacency.get(a, set())
        self._adjacency[a].add(b)
        self._adjacency[b] = self._adjacency.get(b, set())

    def add_vertex(self, a):
        "add a vertex a as a key in the adjecency dict"
        self._adjacency[a] = self._adjacency.get(a, set())

    def neighbors(self, a):
        "return the set of all vertices that have an edge to a"
        ns = {b for b in self._adjacency[a]}
        for b, cs in self._adjacency.items():
            if a in cs:
                ns.add(b)
        return ns

    def edges(self):
        "return all edges as a set of pairs of vertices with a <= b"
        return {(a, b) for a, bs in self._adjacency.items() for b in bs}

    def vertices(self):
        "return the keys of the adjacency dict"
        return {a for a in self._adjacency}
    
    def adjacency_dict(self):
        "return full adjacency dict showing both directiopns"
        return {a: self.neighbors(a) for a in self.vertices()}
    
    def remove_vertex(self, a):
        "remove vertex and also all edges that include it"
        self._adjacency.pop(a)
        for bs in self._adjacency.values():
            if a in bs:
                bs.remove(a)

    def __str__(self):
        "show the adjacency dict"
        return str(self.adjacency_dict())

    def __eq__(self, other):
        "test if adjacency dicts are equal"
        return self.adjacency_dict() == other.adjacency_dict()

    def __copy__(self):
        H = Graph()
        for a, bs in self._adjacency.items():
            H.add_vertex(a)
            [H.add_edge(a, b) for b in bs]
        return H

    def visualize(self):
        "show a picture of the graph in a separate window"
        dot = gv.Graph()
        [dot.node(str(a)) for a in self.vertices()]
        [dot.edge(str(a), str(b)) for a, b in self.edges()]
        dot.render('_graph.gv', view=True)


if __name__ == '__mainz__':
    G = Graph()
    G.add_edge(1, 2)
    G.add_edge(3, 2)
    G.add_edge(2, 1)
    G.add_vertex(4)
    G.add_vertex(2)
    print(1, G.edges())
#    G.visualize()

    print(G.vertices())

    print(G.neighbors(2))

    print(G.adjacency_dict())
    print(2, G.edges())

    print(G)
    print(G.edges())

    H = G.__copy__()
    print(H)
    print(H == G)


if __name__ == '__main__':
    import json
    with open('tramnetwork.json') as file:
        data = json.load(file)
    timedict = data['times']
    T = Graph()
    [T.add_edge(a, b) for a, bs in timedict.items() for b in bs.keys()]
    print(T.neighbors('Chalmers'))
    T.visualize()
    

