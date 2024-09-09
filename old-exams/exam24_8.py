# 1
(lambda x, y: y-x)(5, 2)  # -3, int

len({n % n for n in range(1, 4)}) > 2  # False, bool

{x: min(x, 5) for x in range(2, 8)}  # {2: 2, 3: 3, 4: 4, 5: 5, 6: 5, 7: 5}, dict

# 2

# [1, 2, 3].append(4, 5)  TypeError: list.append() takes exactly one argument (2 given)

# {1, 2, 3} + {4, 5} TypeError: unsupported operand type(s) for +: 'set' and 'set'

# (lambda x: x(x))(1)  TypeError: 'int' object is not callableç∂


# 3
import json
with open('tramnetwork.json') as file:
    tramnetwork = json.load(file)

def q3a(A, B):
    return {
        line for line in tramnetwork['lines']
          if A in tramnetwork['lines'][line] and
             B in tramnetwork['lines'][line]
          }

print(q3a('Chalmers', 'Brunnsparken'))  # {'10', '6', '7'}
    
q3b = max({stop for stop in tramnetwork['stops']},
          key = lambda x: len([line for line in tramnetwork['lines']
                               if x in tramnetwork['lines'][line]]))

print(q3b)  # Brunnsparken

# 4

class Graph:
    def __init__(self):
        self.adjdict = {}

    def add_edge(self, a, b):
        "add b as neighbour of a and a as neighbour of b"
        self.adjdict[a] = self.adjdict.get(a, set())
        self.adjdict[a].add(b)
        self.adjdict[b] = self.adjdict.get(b, set())
        self.adjdict[b].add(a)

    def delete_edge(self, a, b):
        "delete the edge between a and b if it exists"
        self.adjdict[a] = {x for x in self.adjdict[a] if x != b}
        # TO ADD:
        # self.adjdict[b] = {x for x in self.adjdict[b] if x != a}

G = Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(2, 2)

print(G.adjdict) # prints: {1: {2}, 2: {1, 2, 3}, 3: {2}}

G.delete_edge(2, 3)

print(G.adjdict) # prints: {1: {2}, 2: {1, 2}, 3: {2}}


# 5

class WeightedGraph(Graph):
    
    def __init__(self):
        super().__init__()
        self.weightdict = {}

    def set_weight(self, a, b, w):
        self.weightdict[(a, b)] = w 
        self.weightdict[(b, a)] = w

    def get_weight(self, a, b):
        return self.weightdict.get((a, b), 1)


W = WeightedGraph()
W.add_edge(1, 2)
W.add_edge(2, 3)
W.set_weight(1, 2, 100)

print(W.get_weight(2, 1))  # 100
print(W.get_weight(2, 3))  # 1
print(W.get_weight(1, 3))  # 1


