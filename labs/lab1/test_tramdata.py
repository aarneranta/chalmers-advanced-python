import unittest
from tramdata import *
import haversine as hs
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
        with open ("labs/data/tramlines.txt", "r", encoding= "UTF-8") as file:
            tramtest = file.read().replace(":","").strip().split("\n\n")
            tramtest = [line.split("\n") for line in tramtest]
        #print(tramtest)
        test1 = []
        newtestlist =[] 
        for line in tramtest:
            test1.append(line[0])
            newtestlist += line; newtestlist.remove(line[0])

        x = 0 
        for i in range(len(test1)):    
            if test1[i] in self.linedict:
                x+=1
        print(f'{x} ouf of {len(test1)} passed')
        
        test2 = []
        for i in newtestlist:
            a = i.rsplit(' ', 1)
            test2.append(a[0].rstrip(" "))
        k =0
        for t in range(len(test2)):
            for e in self.linedict.values():
                if test2[t] in e:
                    k+=1
                    break
        print(f'{k} ouf of {len(test2)} passed')    

    def test_stops_in_line(self):
        pass
    
    def test_distance_feasible(self):
        print(self.stopdict)
        
        pass
    def test_times_beetween_stops(self):
        pass

TestTramData.test_all_stops_included
if __name__ == '__main__':
    unittest.main()

