import unittest
import json
from newgraphs import *

from hypothesis import given
import hypothesis.strategies as st

TRAM_FILE = './tramnetwork.json'

class TestNewGraphs(unittest.TestCase):

    def setUp(self):
        with open(TRAM_FILE) as trams:
            tramdict = json.loads(trams.read())
            self.timedict = tramdict['times']
        self.G = Graph()
        [self.G.add_edge(a, b)
            for a, bs in self.timedict.items()
               for b in bs.keys()]

    def test_edges_in_vertices(self):
        for a, b in self.G.edges():
            self.assertIn(a, self.G.vertices(),
                          msg = f"edge member {a} not in vertices")

    def test_symmetric_adjacency_dict(self):
        for bs in self.G.adjacency_dict().values():
            for b in bs:
                self.assertIn(b, self.G.adjacency_dict())

    def test_removal_complete(self):
        for removed in self.G.vertices():
            self.G.remove_vertex(removed)
            self.assertNotIn(removed, self.G.vertices(),
                         msg = f"{removed} still in vertices")
            self.assertNotIn(removed, {a for ab in self.G.edges() for a in ab},
                         msg = f"{removed} still in edges")

    def test_nonredundancy(self):
        for a, bs in self.G._adjacency.items():
            for b in bs:
                self.assertNotIn(a, self.G._adjacency[b])
                

if __name__ == '__main__':
    unittest.main()

