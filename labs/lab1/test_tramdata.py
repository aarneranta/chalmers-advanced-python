import unittest
from tramdata import *

TRAM_FILE = 'labs/data/tramnetwork.json'

class TestTramData(unittest.TestCase):

    def setUp(self):
        with open(TRAM_FILE) as trams:
            tramdict = json.loads(trams.read())
            self.stopdict = tramdict['stops']
            self.linedict = tramdict['lines']

    def test_stops_exist(self):
        stopset = {stop for line in self.linedict for stop in self.linedict[line]}
        for stop in stopset:
            self.assertIn(stop, self.stopdict, msg = stop + ' not in stopdict')

    def test_all_stops_included(self):
        pass
    def test_stops_in_line(self):
        pass
    def test_distance_feasible(self):
        pass
    def test_times_beetween_stops(self):
        pass

    


if __name__ == '__main__':
    unittest.main()

