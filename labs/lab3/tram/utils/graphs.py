from graphviz.backend.rendering import render
import networkx as nx
import graphviz as gv
class Graph(nx.Graph):

    def __init__(self, start=None):
        super().__init__(start)

    def __len__(self):
        return len(self.vertices())

    def add_vertex(self, v):
        self.add_node(v)

    def get_vertex_value(self, v):
        return self.vertices()[v]["value"]

    def remove_vertex(self, v):
        self.remove_node(v)

    def set_vertex_value(self, v, x):
        self.vertices()[v]["value"] = x

    def vertices(self):
        return self.nodes

class WeightedGraph(Graph):

    def __init__(self, start=None):
        super().__init__(start)

    def get_weight(self, a, b):
        return self[a][b]['weight']

    def set_weight(self, a, b, w):
        self[a][b]['weight'] = w

def dijkstra(graph, source, cost=lambda u,v: 1):

    def costs2attributes(graph, cost, attr='weight'):
        for a, b in graph.edges():
            graph[a][b][attr] = cost(a, b)

    costs2attributes(graph, cost)    
    return nx.shortest_path(graph, source=source, weight='weight')

def visualize(graph, view='dot', name='mygraph', nodecolors={}, engine='dot'):
    g = gv.Graph(engine=engine)
    for v in graph.vertices():
        s = str(v)
        g.node(
            s, 
            style="filled", 
            fillcolor=nodecolors[s] if s in nodecolors else "#ffffffff"
            )
    for (i,j) in graph.edges():
        g.edge(str(i), str(j))
    g.render(name + ".gv", view=True)

def view_shortest(graph, source, target, cost=lambda u,v: 1):
    path = dijkstra(graph, source, cost)[target]
    colormap = {str(v): 'orange' for v in path}
    print(colormap)
    visualize(graph, view='view', nodecolors=colormap)

def demo():
    graph = Graph([(1,2),(1,3),(1,4),(3,4),(3,5),(3,6), (3,7), (6,7)])
    view_shortest(graph, 2, 6)

if __name__ == '__main__':
    demo()