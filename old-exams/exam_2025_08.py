import json

-- 1

"""
>>> [1, 2, 3].append(3)
None, NoneType

>>> len({1, 2, 3}.add(3))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'NoneType' has no len()

>>> set('python') == set('typhoon')
True

>>> [n*'2' for n in range(4)]
['', '2', '22', '222']

>>> {x % 3 for x in range(20)}
{0, 1, 2}

>>> [] is []
False

>>> print((lambda x, y: x + y)(5, 6))
None, NoneType

>>> (lambda x, y: x + y)(5, 6)
11

>>> len({x%2: x for x in range(100)})
2

>>> {x: x ** x for x in range(4)}.get(4, 63)
63
"""

with open('tramnetwork.json') as file:
    tramnetwork = json.load(file)

-- 2

set2a = {line for line, stops in tramnetwork['lines'].items()
         if 'Chalmers' in stops and 'Korsvägen' not in stops}

print(set2a)

longest2 = max([(t, a, b) for a, bts in tramnetwork['times'].items()
                for b, t in bts.items()])[1:3]

print(longest2)

-- 3

class Graph:
    
    def __init__(self):
        self.vertices = set()
        self.edges = set()
        
    def add_vertex(self, a):
        self.vertices.add(a)

    def add_edge(self, a, b):
        "add edge only once, smaller vertex first"
        a, b = sorted((a, b))
        self.edges.add((a, b))
        self.vertices.add(a)
        self.vertices.add(b)

    def adjacency(self):
        return {a: {b for c, b in self.edges if c == a} for a in self.vertices}

    def add_graph(self, other):
        "add the vertices and edges of other to self"
        self.vertices.update(other.vertices)
        self.edges.update(other.edges)
        
G = Graph()
G.add_edge(2, 1)
G.add_edge(1, 2)
G.add_vertex(3)

print(G.adjacency())
# {3: set()}, should be {1: {2}, 2: set(), 3: set()}

G.add_graph(G)
print(G.adjacency())

3 notice: adjacency() as above stores neighbours only in one direction
# solutions that change it so that both directions are included were also accepted

-- 4

class Tree:
    def __init__(self, node, trees):
        self.root = node
        self.subtrees = trees


def tree2graph(tree):
    graph = Graph()
    graph.add_vertex(tree.root)
    for subtree in tree.subtrees:
        graph.add_edge(tree.root, subtree.root)
        graph.add_graph(tree2graph(subtree))
    return graph

def atom(a):
    return Tree(a, [])

T = Tree(1, [Tree(2, [atom(3), atom(4)]), Tree(5, [Tree(6, [atom(7)]), atom(8)])])

print(tree2graph(T).adjacency())
# {1: {2, 5}, 2: {3, 4}, 3: set(), 4: set(), 5: {8, 6}, 6: {7}, 7: set(), 8: set()}



            
    


