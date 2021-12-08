class Graph():

    _adjlist = {}
    _valuelist = {}

    def __init__(self, edgelist=None):
        pass

    def __len__(self):
        pass

    def add_edge(self, a, b):
        pass

    def add_vertex(self, a):
        pass

    def edges(self):
        pass

    def get_vertex_value(self, b):
        pass

    def neighbours(self, v):
        pass

    def remove_edge(self, a, b):
        pass

    def remove_vertex(self, v):
        pass

    def set_vertex_value(self, v):
        pass

    def vertices(self):
        pass

class WeightedGraph(Graph):
    _weightlist = {}

    def __init__(self, start, edgelist=None):
        super().__init__(edgelist=edgelist)

    def get_weight(self, a, b):
        pass

    def set_weight(self, a, b, w):
        pass

def dijkstra(graph, source, cost=lambda u,v: 1):
    pass

def visualize(graph, view='dot', name='mygraph', nodecolors={}, engine='dot'):
    pass