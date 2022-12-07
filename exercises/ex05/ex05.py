from trams import readTramNetwork # trams.py and all the files it needs are exepected to be in the same folder
import sys
sys.path.append("../../examples")
from htmlgen import table

# Relies on a TramNetwork implementation that uses TramLine objects but represents a line's tram stops as strings, and not as TramStop objects. 
# Adjust to your own implementation if needed
def tramtable(tn):
    header = ["Line n.", "Stretch", "Length", "N. stops", "Travel time", "Avg. speed"]
    data = []
    lines = tn.all_lines()
    for line in lines:
        stops = line.get_stops()
        start = stops[0]
        end = stops[-1]

        n = line.get_number()
        stretch = start + "-" + end
        length = tn.geo_distance(start, end)
        n_stops = len(stops)
        t_time = tn.transition_time(n, start,end)
        avg_speed = length / t_time

        row = list(map(str, [n, stretch, length, n_stops, t_time, avg_speed]))
        data.append(row)
    return table(header,data)

from urllib.request import urlopen
from bs4 import BeautifulSoup
from trees import Graph, visualize

def hypergraph(url, depth=2):
    g = Graph()

    def hypergraph_r(url, depth):
        if depth:
            content = urlopen(url if url.startswith("https://") else "https://" + url).read()
            soup = BeautifulSoup(content, 'html.parser')
            links = filter(lambda link: link != None, [a.get('href') for a in soup.find_all('a')])
            hlinks = list(filter(lambda link: link.endswith(".html"), links))
            nonrel_hlinks = list(filter(lambda hlink: hlink.startswith("https://"), hlinks))
            for hlink in nonrel_hlinks:
                src = url.replace("https://", "")
                trg = hlink.replace("https://", "")
                g.add_edge(src, trg)
                print("adding edge ", src, "->", trg)
                hypergraph_r(trg, depth - 1)

    hypergraph_r(url, depth)
    return g

if __name__ == "__main__":
    # print(tramtable(readTramNetwork("tramnetwork.json")))
    visualize(hypergraph("https://docs.python.org/3/library/urllib.request.html#module-urllib.request"))
