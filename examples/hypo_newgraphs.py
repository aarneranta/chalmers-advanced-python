# testing if removing an edge and adding back it gives
# the same set of edges

from hypothesis import given, strategies as st
from newgraphs import *  # your Lab 2 solution

# generate small integers, 0...10
smallints = st.integers(min_value=0, max_value=10)
  
# generate pairs of small integers
twoints = st.tuples(smallints, smallints)
  
# generate non-empty sets of pairs of small integers
st_edge_set = st.sets(twoints, min_size=1)

@given(st_edge_set)
def test_remove_add(eds):
      """
      test that removing an edge and adding it back results
      in the same set of edges as the original
      """
      G = Graph()
      for (a,b) in eds:
          G.add_edge(a, b)
      edge = list(G.edges())[0]
      edges_1 = set(G.edges())
      G.remove_edge(*edge)
      G.add_edge(*edge)
      assert set(G.edges()) == edges_1


test_remove_add()


