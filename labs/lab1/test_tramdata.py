import unittest
from tramdata import *
import haversine as hs
TRAMFILE = 'labs/data/tramnetwork.json'

class TestTramData(unittest.TestCase):

    def setUp(self):
        with open(TRAMFILE) as trams:
            tramdict = json.loads(trams.read())
            self.stopdict = tramdict['stops']
            self.linedict = tramdict['lines']
            self.timedict = tramdict['times']
            self.tramdict = tramdict
    def teststopsexist(self):
        stopset = {stop for line in self.linedict for stop in self.linedict[line]}
        for stop in stopset:
            self.assertIn(stop, self.stopdict, msg = stop + ' not in stopdict')

    def test_all_stops_included(self):
        test1 = ['1','2','3','4','5','6','7','8','9','10','11','13']
        for i in range(len(test1)):
            self.assertIn( test1[i], self.linedict.keys(), msg = "didnt work")

    def test_stops_in_line(self):
        test2 = ["Ullevi Norra", "Chalmers", "Angered Centrum", "Saltholmen", "Hagen", "Rambergsvallen"]
        for i in range(len(test2)):
                self.assertIn(test2[i], [item for sublist in list(self.linedict.values()) for item in sublist], msg = "didnt work")

    def test_distance_feasible(self):

        for stop1 in self.stopdict:
            for stop2 in self.stopdict:
                self.assertLess(distance_between_stops(self.stopdict, stop1, stop2), 20, msg = "didnt work")
                    

    def test_times_beetween_stops(self):
        
        for line in self.linedict:
            for stop1 in self.linedict[line]:
                for stop2 in self.linedict[line]:
                    self.assertEqual(time_between_stops(self.linedict, self.timedict, line, stop1, stop2),time_between_stops(self.linedict, self.timedict, line, stop2, stop1) , msg = "didnt work")
    
    def test_query(self):
        test3 = ["between norrköping and linköping", "via chalmers", "between chalmers and ullevi norra", "time with 8 from chalmers to ullevi", "distance from Hagen to Rambergsvallen", "quit", "hejehjehejehje"]
        x = 0
        for i in test3:
            if answer_query(self.tramdict, i) ==  str or int or list or float:
                x+=1
        print(f'query {x} passed test ouf of {len(test3)}')

if __name__ == '__main__':
    unittest.main()

