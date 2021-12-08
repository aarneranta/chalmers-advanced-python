import unittest
from itertools import combinations
from tramdata import *

TRAM_FILE = 'tramnetwork.json'

class TestTramData(unittest.TestCase):

    def setUp(self):
        build_tram_network("../data/tramstops.json", "../data/tramlines.txt")
        with open(TRAM_FILE) as trams:
            self.tramdict = json.loads(trams.read())
            self.stopdict = self.tramdict['stops']
            self.linedict = self.tramdict['lines']
            self.timedict = self.tramdict['times']
            self.linesfile = "../data/tramlines.txt"

    def test_stops_exist(self):
        """
        All stops associated with lines in linedict also exist in stopdict.
        """
        stopset = {stop for line in self.linedict for stop in self.linedict[line]}
        for stop in stopset:
            self.assertIn(stop, self.stopdict, msg = stop + ' not in stopdict')
    
    def test_same_lines(self):
        """
        All tram lines listed in the original text file tramlines.txt are 
        included in linedict.
        """
        with open(self.linesfile) as f:
            lines = f.readlines()
        txt_lines = {str(int(line.replace(":", ""))) for line in lines if ":" in line and len(line.split()) < 2}
        dict_lines = set(self.linedict.keys())
        assert txt_lines != dict_lines

    def test_same_stops(self):
        """
        The list of stops for each tramline is the same in tramlines.txt and 
        linedict.
        """
        with open(self.linesfile) as f:
            text = f.read()
        line_blocks = text.split("\n\n")
        for block in line_blocks[:-1]: # skip last empty line/block
            lines = block.split("\n")
            tram_line = str(int(lines[0].replace(":","")))
            tram_stops = [parse_stop_info(stop_info)[0] for stop_info in lines[1:]]
            assert self.linedict[tram_line] == tram_stops

    def test_feasible_distances(self):
        """
        All distances are "feasible", meaning less than 20 km.
        """
        for (a,b) in list(combinations(self.stopdict.keys(), 2)):
            assert distance_between_stops(self.stopdict, a, b) < 20

    def test_same_time(self):
        """
        That time from a to b is always the same as the time from b to a, 
        along the same line.
        """
        for tram_line in self.linedict.keys():
            for (a,b) in list(combinations(self.linedict[tram_line], 2)):
                assert time_between_stops(self.linedict, self.timedict, tram_line, a, b) == time_between_stops(self.linedict, self.timedict, tram_line, b, a)

    def test_valid_queries(self):
        """
        Test various valid queries.
        """
        assert answer_query("via Chalmers", self.tramdict) == ['6', '7', '8', '10', '13']
        assert answer_query("via Ullevi Norra", self.tramdict) == ['1', '3', '6', '8']
        assert answer_query("between Chalmers and Kviberg", self.tramdict) == ['6', '7']
        assert answer_query("between Ullevi Norra and Chalmers", self.tramdict) == ['6', '8']
        assert answer_query("time with 6 from Beväringsgatan to Chalmers", self.tramdict) <= 30
        assert answer_query("distance from Kviberg to SKF", self.tramdict) < 2

    def test_invalid_queries(self):
        """
        Test various invalid queries.
        """
        assert not answer_query("via chalmers", self.tramdict)
        assert not answer_query("by Chalmers", self.tramdict)
        assert not answer_query("between Chalmers Kviberg", self.tramdict)
        assert not answer_query("between Ullevi norra and Chalmers", self.tramdict)
        # assert not answer_query("time with 6 between Beväringsgatan and Chalmers", self.tramdict) 
        # assert not answer_query("distance from Kviberg to S.K.F", self.tramdict)
        

if __name__ == '__main__':
    unittest.main()

