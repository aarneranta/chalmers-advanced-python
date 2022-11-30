# visualization of shortest path in Lab 3, modified to work with Django

from .trams import readTramNetwork
from .graphs import dijkstra
import os
from django.conf import settings

def show_shortest(dep, dest):
    # TODO: uncomment this when it works with your own code
    network = readTramNetwork()

    # TODO: replace this mock-up with actual computation using dijkstra.
    # First you need to calculate the shortest and quickest paths, by using appropriate
    # cost functions in dijkstra().
    # Then you just need to use the lists of stops returned by dijkstra()
    #
    # If you do Bonus 1, you could also tell which tram lines you use and where changes
    # happen. But since this was not mentioned in lab3.md, it is not compulsory.
    timepath = 'The quickest route from ' + dep + ' to ' + dest
    geopath = 'The shortest route from ' + dep + ' to ' + dest

    # TODO: run this with the shortest-path colors to update the svg image
    # network_graphviz(network, SHORTEST_PATH_SVG, colors=...):
    
    return timepath, geopath

