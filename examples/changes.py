import json
import networkx as nx
import graphviz as gv



TRAMDATA_FILE = 'tramnetwork.json'

STOPID_FILE = 'stopids.json'



with open(TRAMDATA_FILE) as file:
    tramdata = json.load(file)

with open(STOPID_FILE) as file:
    stopids = json.load(file)

lines = tramdata['lines']


# print(tramdata)

trams = nx.Graph()

for line, stops in lines.items():
    for stop in stops:
        node = (stop, line)
        trams.add_node(node)

stoplines = {
    stop: {line for line, stops in lines.items()
           if stop in stops}
    for stop in tramdata['stops']}

for line, stops in lines.items():
    for i in range(len(stops)-1):
        trams.add_edge((stops[i], line), (stops[i+1], line))
    

# print(stoplines)

for stop, lines in stoplines.items():
    for line1 in lines:
        for line2 in lines:
            if line1 != line2:
                trams.add_edge((stop, line1), (stop, line2))

def color(v):
    if v[0] == 'C':
        return 'orange'
    else:
        return 'white'


def nodepos(node):
    return (tramdata['stops'][node]['lon'],           
            tramdata['stops'][node]['lat'])


viz = gv.Graph('trams', engine='circo')
for node, _ in trams.nodes():
    x, y = nodepos(node)
    viz.node(str(node),
             style='filled',
             fillcolor=color(node),
             pos=str(x) + ',' + str(y) + '!',
             URL = stopids[node]
             )
for (a, line), (b, _) in trams.edges():
    if a != b:
        viz.edge(str(a), str(b), label=str(line))

viz.render(view=True)
