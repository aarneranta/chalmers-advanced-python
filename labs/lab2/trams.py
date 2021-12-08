import sys
import json
from networkx.generators import line
sys.path.append('../../labs/lab1/')
import tramdata as td
import graphs_basic as basic
import graphs_bonus as bonus

TRAM_FILE = 'tramnetwork.json'

class TramNetwork(basic.WeightedGraph):

    def __init__(self, lines, stops, times, start=None):
        super().__init__(start=start)
        self._linedict = lines
        self._stopdict = stops
        self._timedict = times

    def all_lines(self):
        return [TramLine(n, ss) for (n,ss) in self._linedict.items()]

    def all_stops(self):
        return self._stopdict.keys()

    def extreme_positions(self):
        pass

    def geo_distance(self, a, b):
        return td.distance_between_stops(self._stopdict, a, b)

    def line_stops(self, line):
        return self._linedict[line]

    def remove_lines(self, lines):
        pass

    def stop_lines(self, a):
        return td.lines_via_stop(self._linedict, a)

    def stop_position(self, a):
        pass

    def transition_time(self, n, a, b):
        return td.time_between_stops(self._linedict, self._timedict, n, a, b)

class TramLine():

    def __init__(self, number, stops):
        self._number = number
        self._stops = stops

    def get_number(self):
        return self._number

    def get_stops(self):
        return self._stops

class TramStop():
    
    def __init__(self, name, lines=None, lat=None, lon=None):
        self._name = name
        self._position = (lat,lon)
        self._lines = lines

    def add_line(self, line):
        self._lines.append(line)
    
    def get_lines(self):
        return self._lines

    def get_name(self):
        return self._name

    def get_position(self):
        return self._position

    def set_position(self, lat, lon):
        self._position = (lat,lon)

def readTramNetwork(file=TRAM_FILE):
    with open(file) as f:
        network_dict = json.load(f)

    linedict = network_dict["lines"]
    stopdict = network_dict["stops"]
    timedict = network_dict["times"]

    edges = []
    weights = []
    for (src, dsts) in network_dict["times"].items():
        for (dst,time) in dsts.items():
            edges.append((src,dst))
            weights.append(time)
    
    network = TramNetwork(
        linedict, 
        stopdict,
        timedict,
        start=edges
        )

    for (i,(a,b)) in enumerate(edges):
        network.set_weight(a,b,weights[i])
    
    return network

def demo():
    G = readTramNetwork()
    a, b = input('from,to ').split(',')
    basic.view_shortest(G, a, b)

if __name__ == '__main__':
    demo()
