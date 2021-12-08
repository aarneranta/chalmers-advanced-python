# Question 1 #################################################################
import sys

from networkx.classes import graph 
sys.path.append('../../labs/lab2/') # change to wherever you stored you lab2
from trams import *
sys.path.append('../../examples/')
from htmlgen import *


def tram_network2html_table(tn):
    header = ["Number", "Stretch", "Length", "Stops", "Travel time", "Average speed"]
    rows = []
    for line in tn.all_lines():
        stops = line.get_stops()
        first_stop = stops[0] 
        last_stop = stops[-1]

        number = line.get_number()
        stretch = first_stop + "-" + last_stop
        length = tn.geo_distance(first_stop, last_stop)
        n_stops = len(stops)
        travel_time = tn.transition_time(number, first_stop, last_stop)
        average_speed = length / (travel_time / 60)

        # map (in: function, list)
        rows.append(list(map(str, [number, stretch, length, n_stops, travel_time, average_speed])))

    return table(header, rows)

def q1():
    table = tram_network2html_table(readTramNetwork('../../labs/lab1/tramnetwork.json'))
    webpage = html([title("Tram lines")], [table])
    with open("table.html", "w") as f:
        f.write(webpage)

# Question 2 #################################################################
from bs4 import BeautifulSoup
import urllib.request
from graphs_basic import Graph, visualize

def hyperlink_graph(url, depth=4):
    g = Graph()

    def hyperlink_graph_h(url, depth):
        if depth == 0:
            return
        html_doc = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_doc, 'html.parser')
        for new_url in list(map(lambda link: link.get('href'),soup.find_all('a'))):
            if new_url:
                g.add_edge(url,new_url)
                print("adding edge: " + url + " -> " + new_url)
                hyperlink_graph_h(new_url, depth - 1)

    hyperlink_graph_h(url, depth)

    return g

def q2():
    graph = hyperlink_graph("https://fishdraw.glitch.me/")
    postprocessed_graph = Graph(
        list(
            map(
                lambda edge: tuple(map(
                    lambda s: "".join(list(filter(lambda c: c.isalpha(), s))), 
                    edge)),
                graph.edges())
                )
            )
    visualize(postprocessed_graph)

if __name__ == '__main__':
    q1()
    q2()