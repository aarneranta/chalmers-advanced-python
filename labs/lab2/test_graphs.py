import unittest

from networkx.exception import NetworkXError, NodeNotFound
import hypothesis

from graphs_basic import * 
# from graphs_bonus import *

class TestGraphs(unittest.TestCase):

    def setUp(self):
        self.start = [(0,1), (1,2), (1,3)]
        self.g = WeightedGraph(self.start)

    def test_len(self):
        assert len(self.g) == 4
        assert len(WeightedGraph()) == 0

    def test_edges(self):
        assert set(self.g.edges()) == set(self.start)
        self.g.add_edge(1,4)
        assert (1,4) in self.g.edges()
        assert (4,1) in self.g.edges()
        self.g.remove_edge(1,4)
        assert (1,4) not in self.g.edges()

    def test_vertices(self):
        assert set(self.g.vertices()) == set([0,1,2,3])
        self.g.add_vertex(5)
        assert 5 in self.g.vertices()
        self.g.remove_vertex(5)
        assert 5 not in self.g.vertices()

    def test_neighbors(self):
        assert set(self.g.neighbors(1)) == set([0,2,3])
        assert set(self.g.neighbors(0)) == set([1])
        with self.assertRaises(NetworkXError):
            set(self.g.neighbors(5))

    def test_values(self):
        v = 0
        x = "value"
        self.g.set_vertex_value(v, x)
        assert self.g.get_vertex_value(v) == x
        
    def test_weights(self):
        self.g.set_weight(0,1,3)
        assert self.g.get_weight(0,1) == 3
        assert self.g.get_weight(1,0) == 3
        with self.assertRaises(KeyError):
            self.g.set_weight(0,0,3)

    def test_dijkstra(self):
        assert len(dijkstra(self.g, 0)[0])
        assert dijkstra(self.g, 0)[3] == [0,1,3]
        with self.assertRaises(NodeNotFound):
            dijkstra(self.g, 5)
        self.g.add_vertex(5)
        with self.assertRaises(KeyError):
            dijkstra(self.g, 0)[5]


if __name__ == '__main__':
    unittest.main()