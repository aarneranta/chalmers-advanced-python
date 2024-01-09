# 1

"""
[1, 2, 3].append(3)
Value: None
Type: NoneType

len({n % 7 for n in range(678)})
Value: 7
Type: int

{n % 2: n for n in range(10)}
Value: {0: 8, 1: 9}
Type: dict
"""

# 2

"""
{1//n for n in range(5)}
Error: ZeroDivisionError
Reason: 1//0 because 0 is in range(5)

{{}}
Error: TypeError (AttributeError also accepted)
Reason: {} is unhashable (a dict)

{'1': 'one', '2': 'two'}[2]
Error: KeyError
Reason: 2 is not in dict
"""

# 3
tramnetwork = {
    "stops": {
        "Östra Sjukhuset": {
            "lat": 57.7224618,
            "lon": 12.0478166
        }
    # the positions of every stop
    },
    "lines": {
        "1": [
            "Östra Sjukhuset",
            "Tingvallsvägen",
            # and the rest of the stops along line 1
            ]
    # the sequence of stops on every line
    },    
    "times": {
        "Östra Sjukhuset": {},
        "Tingvallsvägen": {
            "Östra Sjukhuset": 1
        }
    # the times from each stop to its alphabetically later neighbours
    }
  }

# a dictionary that to each stop assigns its latitude (lat)
# Answer:
latitudes = {stop: tramnetwork['stops'][stop]['lat']
                for stop in tramnetwork['stops']}

# the name of the southernmost tram stop
#Answer:
min([stop for stop in latitudes], key=lambda stop: latitudes[stop])


# 4

class Graph:
    def __init__(self):
        self.adjdict = {}

    def add_edge(self, a, b):
        self.adjdict[a] = self.adjdict.get(a, set())
        self.adjdict[a].add(b)
        
# this must be added so that adjdict[b] is also updated
#        self.adjdict[b] = self.adjdict.get(b, set())
#        self.adjdict[b].add(a)

    def get_vertices(self):
        return {a for a in self.adjdict}

    def get_edges(self):
        edges = set()
        for a in self.adjdict:
            for b in self.adjdict[a]:
                if (b, a) not in edges:
                    edges.add((a, b))
        return edges

    def get_neighbours(self, a):
        return self.adjdict.get(a, set())
    

G = Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(2, 2)
print(G.get_vertices())  # Answer: {1, 2}
print(G.get_edges())     # Answer: {(2, 3), (1, 2), (2, 2)}


# 5

class NoSelfLoopsGraph(Graph):
    # your code, can just make super().add_edge() conditional:
    def add_edge(self, a, b):
        if a != b:
            super().add_edge(a, b)

            
def without_self_loops(G):
    # your code, can just loop over G's edges with NG.add_edge():
    NG = NoSelfLoopsGraph()
    for (a, b) in G.get_edges():
        NG.add_edge(a, b)
    return NG


print(without_self_loops(G).get_edges())  #Answer: {(2, 3), (1, 2)}

    
