# q1

(lambda x, y: y**x)(5, 2)
# Value: 32
# Type: int

[n % n for n in range(1, 4)]
# Value: [0, 0, 0]
# Type: list

{max(n, 5) for n in range(10)}
# Value: {5, 6, 7, 8, 9}
# Type: set


# q2
## {1, 2, 3}.append(2)
# Error: AttributeError
# Reason: set has no append

## {1, 2, 3}.add([])
# Error: TypeError
# Reason: list is unhashable

## [1, 2, 3].append(4, 5)
# Error: TypeError
# Reason: add() takes only one argument


# q3

# these definitions enable testing with the full data from the lab
import json

with open('tramnetwork.json') as file:
    tramnetwork = json.load(file)


stoplines = {s: {k for k in tramnetwork['lines'] if s in tramnetwork['lines'][k]} for s in tramnetwork['stops']}

print(stoplines)

q3b = max(tramnetwork['stops'], key=lambda s: len(stoplines[s]))

print(q3b)

# q4
class Graph:
    def __init__(self):
        self.adjdict = {}

    def add_edge(self, a, b):
        "add b as neighbour of a and a as neighbour of b"
        self.adjdict[a] = self.adjdict.get(a, set())
        self.adjdict[a].add(b)
        self.adjdict[b] = self.adjdict.get(b, set())
        self.adjdict[b].add(a)

    def get_edges(self):
        "return the set of edges, not including (a, b) if (b, a) is included"
        edges = set()
        for a in self.adjdict:
            for b in self.adjdict[a]:
                # if (b, a) not in edges:    ## line 1/2 to be added
                    edges.add((a, b))
        # return edges                       ## line 2/2 to be added


G = Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(2, 2)

print(G.adjdict) # prints: {1: {2}, 2: {1, 2, 3}, 3: {2}}

print(G.get_edges()) # prints: None

# after corrections, it prints {(2, 3), (1, 2), (2, 2)} but this does not need to be mentioned


# q5


class ConnectedGraph(Graph):
    
    def add_edge(self, a, b):
        if not self.adjdict or a in self.adjdict or b in self.adjdict:
            super().add_edge(a, b)
    # idea: if a new edge is added to a graph, one of its vertices must be in the graph already
    # except if the old graph is empty: then one must be able to start with two completely new vertices
            
G = ConnectedGraph()

G.add_edge(1, 2)
G.add_edge(3, 4)

print(G.get_edges())  # {(1, 2)}

G.add_edge(1, 3)
G.add_edge(3, 4)

print(G.get_edges())  # {(1, 2), (1, 3), (3, 4)}



