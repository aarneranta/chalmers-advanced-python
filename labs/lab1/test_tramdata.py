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
    def teststopsexist(self):
        stopset = {stop for line in self.linedict for stop in self.linedict[line]}
        for stop in stopset:
            self.assertIn(stop, self.stopdict, msg = stop + ' not in stopdict')

    def test_all_stops_included(self):
        test1 = ['1','2','3','4','5','6','7','8','9','10','11','13']
        x = 0 
        for i in range(len(test1)):
            if test1[i] in self.linedict:
                x+=1

        print(f'{x} passed test out of {len(test1)} passed')

    def test_stops_in_line(self):
        test2 = ["Ullevi Norra", "Chalmers", "Angered Centrum", "Saltholmen", "Hagen", "Rambergsvallen"]
        x =0
        for i in range(len(test2)):
            for k in self.linedict.values():
                if test2[i] in k:
                    x+=1
                    break
        print(f'{x} passed test out of {len(test2)} passed')

    def test_distance_feasible(self):
        x = 0
        if distance_between_stops(self.stopdict, "Ullevi Norra", "Chalmers") < 20:
            x+=1
        if distance_between_stops(self.stopdict, "Angered Centrum", "Saltholmen") < 20:
            x+=1
        if distance_between_stops(self.stopdict, "Hagen", "Rambergsvallen") < 20:
            x+=1
        print(f'{x} passed test ouf of {3}')

    def test_times_beetween_stops(self):
        pass
        test3 = {"Tingvallsvägen": {"Kaggeledstorget": 2}}

        print(self.timedict) 

if __name__ == '__main__':
    unittest.main()

