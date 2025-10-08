import json

# imports added in Lab 3 version
import math
import os
from .graphs import WeightedGraph
from django.conf import settings


# path changed from Lab 2 version
# TODO: copy your json file from Lab 1 here
TRAM_FILE = os.path.join(settings.BASE_DIR, 'static/tramnetwork.json')


# TODO: use your Lab 2 class definition, but add one method
# class TramNetwork(WeightedGraph):    
    # def extreme_positions(self):
        # stops = self._stopdict.values()
        # minlat = min([s._position[0] for s in stops])
        # etc
        # return minlon, minlat, maxlon, maxlat


def readTramNetwork():
    # TODO: your own trams.readTramNetwork()
    pass


def specialize_stops_to_lines(network):
    # TODO: write this function as specified
    return network


def specialized_transition_time(spec_network, a, b, changetime=10):
    # TODO: write this function as specified
    return changetime


def specialized_geo_distance(spec_network, a, b, changedistance=0.02):
    # TODO: write this function as specified
    return changedistance


