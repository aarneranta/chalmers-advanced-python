# lecture 5

class Graph:
    def __init__(self, adj=None):
        if adj:
            self._adjlist = adj
        else:
            self._adjlist = {}
        # format: {1: {2}, 2: {1}}
        
    def add_edge(self, a, b):
        if a in self._adjlist:
            self._adjlist[a].add(b)
        else:
            self._adjlist[a] = {b}
        if b in self._adjlist:
            self._adjlist[b].add(a)
        else:
            self._adjlist[b] = {a}

    def get_edges(self):
        edges = set()
        for a in self._adjlist:
            for b in self._adjlist[a]:
                edges.add(frozenset({a, b}))
                
        edges = [tuple(fs) for fs in edges]
        return edges

    def __str__(self):
        return str(self._adjlist)

if __name__ == '__main__':
    G = Graph()
    print(G)
    G.add_edge(1, 2)
    print(G)
    G.add_edge(2, 3)
    print(G)
    G.add_edge(2, 1)
    print(G)
    print(G.get_edges())
    H = Graph()
    print(H)
    


            

