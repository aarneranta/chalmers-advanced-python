import unittest
from tramdata import *

TRAM_FILE = 'labs/data/tramnetwork.json'

class TestTramData(unittest.TestCase):

    def setUp(self):

        with open ("labs/data/tramlines.txt", "r", encoding= "UTF-8") as file:
            lines = file.read().replace(":","").strip().split("\n\n")
            lines = [line.split("\n") for line in lines]
        test1 = []
        test2 =[]
        for line in lines:
            stoplist = []
            test2.append(line[0])
            for i in range(1, len(line)):
                item1, item2= [item.strip() for item in line[i].split("  ") if item]
                stoplist.append((item1))
            test1.append(stoplist)
        self.stoplist = test1
        self.linelist = test2

        with open(TRAM_FILE) as trams:
            tramdict = json.loads(trams.read())
            self.stopdict = tramdict['stops']
            self.linedict = tramdict['lines']
            self.timedict = tramdict['times']

        

    def test_stops_exist(self):
        stopset = {stop for line in self.linedict for stop in self.linedict[line]}
        for stop in stopset:
            self.assertIn(stop, self.stopdict, msg = stop + ' not in stopdict')

    def test_all_stops_included(self):
        "Testar ifall alla spårvagnslinjer finns med"
        for i in range(len(self.linelist)):
            if self.linelist[i] not in self.linedict:
                print(f"{self.linelist[i]} not in tramdict")

    def test_stops_in_line(self):
        "Testar ifall alla hållplatser finns i linjerna"
        x = 0
        for i in range(len(self.stoplist)):
            if self.stoplist[i] != self.linedict[self.linelist[i]]:
                print(f"Stops in line {self.linelist[i]} not ok")
            else:
                x += 1       
        print(f"{x} out of {len(self.stoplist)} tests passed")

    def test_distance_feasible(self):
        pass
    def test_times_beetween_stops(self):
        pass


    


if __name__ == '__main__':
    unittest.main()

