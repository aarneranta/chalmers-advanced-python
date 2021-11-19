class Graph:
    """
    A class of undirected graphs.
    """
    def __init__(self):
        "Start with an empty graph."
        self._adjlist = {}

    def add_edge(self, a, b):
        "Add an edge, and the vertices if needed."
        if a not in self._adjlist:
            self._adjlist[a] = set()
        self._adjlist[a].add(b)
        if b not in self._adjlist:
            self._adjlist[b] = set()
        self._adjlist[b].add(a)

    def vertices(self):
        "Lists all vertices."
        return self._adjlist.keys()
    
    def edges(self):
        "Lists all edges in one direction, a <= b"
        eds = []
        for a in self._adjlist.keys():
            for b in self._adjlist[a]:
                if a <= b:
                    eds.append((a, b))
        return eds

    def __str__(self):
        "Shows the adjacency list."
        return str(self._adjlist)

    def __getitem__(self, v):
        "Gives the neighbours of vertex v."
        return self._adjlist[v]
    

class ValueGraph(Graph):
    "Graph where vertices have values."
    def __init__(self):
        "Initialize with empty graph and no values."
        super().__init__()
        self._valuelist = {}

    def get_value(self, v):
        "The value of vertex v, default None."
        return self._valuelist.get(v, None)
    
    def set_value(self, v, x):
        "Destructive update of value of vertex v."
        if v in self.vertices():
            self._valuelist[v] = x


class Tree(Graph):
    "Trees as graphs with certain restrictions."
    def __init__(self, r):
        "Initialize with a root node r."
        super().__init__()
        self._adjlist = {r: set()}
        
    def add_edge(self, a, b):
        """
        Add an edge from parent a to child b,
        provided that a exists and b does not exist.
        """
        if a not in self._adjlist:
            print('Parent does not exist:', a)
        elif b in self._adjlist:
            print('Child already exists:', b)
        else:
            self._adjlist[a].add(b)
            self._adjlist[b] = set()


class ValueTree(Tree, ValueGraph):
    def __init__(self, r):
        super().__init__(r)


# for experiments and demos
import graphviz

def visualize(graph):
    "Visualize undirected graphs with the dot method of Graphviz."
    dot = graphviz.Graph(engine='dot')
    for v in graph.vertices():
        dot.node(str(v))
    for (a,b) in graph.edges():
        dot.edge(str(a),str(b))
    dot.render('mygraph.gv', view=True)




def demo():
    T = ValueTree(1)
    T.add_edge(1, 11)
    T.add_edge(1, 12)
    T.add_edge(11, 111)
    T.add_edge(111, 11)
    T.add_edge(11, 112)
    T.add_edge(1, 4)
    T.add_edge(3, 4)
    T.add_edge(11, 112)
    T.set_value(1, 'one')
    T.set_value(11, 'eleven')
    print(T)
    print(T._valuelist)
    for v in T.vertices():
        print(T[v])
    visualize(T)
    

if __name__ == '__main__':
    demo()
