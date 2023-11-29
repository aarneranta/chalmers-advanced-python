import sys
sys.path.append("../../examples")
from trees import Graph
from hypothesis.strategies import lists, integers, tuples
from hypothesis import given

def easy_complete(G):
    n = len(G.vertices())
    non_self_loops = list(filter(lambda edge: edge[0] != edge[1], G.edges()))
    return len(non_self_loops) == (n*(n-1)) // 2

def complete(G):
    for v in G.vertices():
        for u in G.vertices():
            if v != u:
                if (v,u) not in G.edges() and (u,v) not in G.edges():
                    return False
    return True

#complete_g = Graph()
#edges = [(1,2), (2,3), (3,1)]
#for (src,trg) in edges:
#    complete_g.add_edge(src,trg)
#
#incomplete_g = Graph()
#for (src,trg) in edges[:2]:
#    incomplete_g.add_edge(src,trg)
#
#print(complete_g, easy_complete(complete_g), complete(complete_g))
#print(incomplete_g, easy_complete(incomplete_g), complete(incomplete_g))

@given(lists(tuples(integers(min_value=1, max_value=5), integers(min_value=1, max_value=5)), min_size=5, max_size=25, unique=True))
def test_completes(edges):
    graph = Graph()
    for (src,trg) in edges:
        graph.add_edge(src,trg)
    #print(graph, "complete: ", complete(graph), "easy complete: ", easy_complete(graph))
    assert(complete(graph) == easy_complete(graph))