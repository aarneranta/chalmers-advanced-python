# simplified tram visualization for Lab 3

import graphs as g
import trams as t
import graphviz
import sys

TRAM_FILE = 'central-tramnetwork.json' # stored in course GitHub examples/
FTRAM_FILE = 'tramnetwork.json' # your own complete network

# assign colors to lines, indexed by line number; not quite accurate
gbg_linecolors = {
    1: 'gray', 2: 'yellow', 3: 'blue', 4: 'green', 5: 'red',
    6: 'orange', 7: 'brown', 8: 'purple', 9: 'cyan',
    10: 'lightgreen', 11: 'black', 13: 'pink'}


def scaled_position(network):

    # compute the scale of the map
    minlat, minlon, maxlat, maxlon = network.extreme_positions()
    size_x = maxlon - minlon
    scalefactor = len(network)/3
    x_factor = scalefactor/size_x
    size_y = maxlat - minlat
    y_factor = scalefactor/size_y
    
    return lambda xy: (x_factor*(xy[0]-minlon), y_factor*(xy[1]-minlat))

# to generate https://www.google.com/search?q=Prinsgatan+Gothenburg
import urllib.parse
def stop_url(stop):
    google_url = 'https://www.google.com/search'
    attrs = urllib.parse.urlencode({'q': 'Gothenburg ' + stop})
    return google_url + '?' + attrs


def network_graphviz(network, colors=None, positions=None):
    dot = graphviz.Graph(engine='fdp', graph_attr={'size': '12,12'})

    for stop in network.all_stops():
        
        x, y = network.stop_position(stop)
        if positions:
            x, y = positions((x, y))
        pos_x, pos_y = str(x), str(y)
        
        if colors:
            col = colors(stop)
        else:
            col = 'white'
            
        dot.node(
            stop,
            label=stop,
            shape='rectangle',
#            pos=pos_x + ',' + pos_y +'!',
            fontsize='8pt',
            width='0.4',
            height='0.05',
            URL=stop_url(stop),
            fillcolor=col, style='filled'
            )
        
    for line in network.all_lines():
        stops = network.line_stops(line)
        for i in range(len(stops)-1):
            pass
        
            dot.edge(
                stops[i], stops[i+1],
                color=gbg_linecolors[int(line)],
                penwidth=str(2))
         
    dot.render(view=True)


def graphviz_main():
    network = t.readTramNetwork(FTRAM_FILE)
    positions = scaled_position(network)
    colors = lambda stop: 'orange' if stop[0] == 'C' else 'white'
    network_graphviz(network, colors=colors, positions=positions)


import matplotlib.pyplot as plt

def network_matplotlib(network, linecolors=gbg_linecolors, path=None, focuscolor='orange'):

    # compute the scale of the map
    # scale_x, scale_y = network_scale(network)

    # create a canvas for the map
    plt.figure(figsize=(12, 10))
    unit = 0.00025  # visible distance from a point
    
    # print stop names on the canvas
    for stop in network.all_stops():
        pos = network.stop_position(stop)
        if path and stop in path:
            plt.text(pos[0]+unit, pos[1], stop, fontsize=10, color=focuscolor)
        else:
            plt.text(pos[0]+unit, pos[1], stop, fontsize=8)
        
    for line in network.all_lines():
        stops = network.line_stops(line)
        positions = [network.stop_position(stop) for stop in stops]
        Xs, Ys = [p[0] for p in positions], [p[1] for p in positions]
        plt.scatter(Xs, Ys, c = 'white')
        plt.plot(Xs, Ys, linecolors[int(line)],linewidth=2)

    plt.show()


def matplotlib_main():
    network = t.readTramNetwork(FTRAM_FILE)
    network_matplotlib(network)

    

if __name__ == '__main__':
    graphviz_main()
#    matplotlib_main()
    


