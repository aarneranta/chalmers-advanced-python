# visualization of shortest path in Lab 3, modified to work with Django

from .trams import readTramNetwork
from .graphs import dijkstra
from .color_tram_svg import color_svg_network
import os
from django.conf import settings

def show_shortest(dep, dest):
    network = readTramNetwork()

    # TODO: replace this mock-up with actual computation using dijkstra.
    # First you need to calculate the shortest and quickest paths,
    # by using appropriate cost functions in dijkstra().
    # Then you just need to use the lists of stops returned by dijkstra()
    # You sould also tell which tram lines you use and where changes happen.

    quickest = [dep, 'Chalmers', dest]
    shortest = [dep, 'Chalmers', dest] 
    
    timepath = 'Quickest: ' + ', '.join(quickest) + ', 5 minutes'
    geopath = 'Shortest: ' + ', '.join(shortest) + ', 100 km'

    def colors(v):
        if v in shortest:
            return 'cyan'
        else:
            return 'white'
            

    # this part should be left as it is:
    # change the SVG image with your shortest path colors
    color_svg_network(colormap=colors)
    # return the path texts to be shown in the web page
    return timepath, geopath

