import json
import networkx as nx
import graphviz as gv



TRAMDATA_FILE = 'tramnetwork.json'

with open(TRAMDATA_FILE) as file:
    tramdata = json.load(file)

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

# print(stoplines)

for stop, lines in stoplines.items():
    for line1 in lines:
        for line2 in lines:
            if line1 != line2:
                trams.add_edge((stop, line1), (stop, line2))




viz = gv.Graph('trams')
for node in trams.nodes():
    viz.node(str(node))
for a, b in trams.edges():
    viz.edge(str(a), str(b))

viz.render(view=True)
