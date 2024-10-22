import json

# imports added in Lab3 version
import math
import os
from .graphs import WeightedGraph
from django.conf import settings


# path changed from Lab2 version
# TODO: copy your json file from Lab 1 here
TRAM_FILE = os.path.join(settings.BASE_DIR, 'static/tramnetwork.json')


# TODO: use your lab 2 class definition, but add one method
# class TramNetwork(WeightedGraph):    
    # def extreme_positions(self):
        # stops = self._stopdict.values()
        # minlat = min([s._position[0] for s in stops])
        # etc
        # return minlon, minlat, maxlon, maxlat


def readTramNetwork():
    # TODO: your own trams.readTramNetwork()
    pass


# Bonus task 1: take changes into account and show used tram lines

def specialize_stops_to_lines(network):
    # TODO: write this function as specified
    return network


def specialized_transition_time(spec_network, a, b, changetime=10):
    # TODO: write this function as specified
    return changetime


def specialized_geo_distance(spec_network, a, b, changedistance=0.02):
    # TODO: write this function as specified
    return changedistance


