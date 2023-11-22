## Question 1
from _trams import readTramNetwork
import sys
sys.path.append("../../examples")
from htmlgen import table

def tramtable(tram_network):
    header = ["Line", "Stretch", "Length", "Stops", "Travel time", "Average speed"]
    lines = tram_network.all_lines()
    data = []
    for line in lines:
        line_n = line.get_number()
        stop_names = line.get_stops()
        start = stop_names[0]
        end = stop_names[-1]
        stretch = "{} - {}".format(start, end)
        length = round(tram_network.geo_distance(start, end),2)
        n_stops = len(stop_names)
        travel_time = tram_network.transition_time(line_n,start,end)
        avg_speed = round(length / (travel_time / 60), 2)
        data.append([line_n, stretch, str(length), str(n_stops), str(travel_time), str(avg_speed)])
    return table(header,data)

## Question 2
from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
from trees import Graph, visualize

def build_hypergraph(url, depth=1, graph=Graph()):
    if depth > 0:
        try:
            content = urlopen("http://" + url).read()
        except:
            return graph
        soup = BeautifulSoup(content, 'html.parser')
        links = soup.find_all("a")
        hrefs = [link.get('href') for link in links]
        proper_hrefs = list(filter(lambda href: href and href.endswith(".html"), hrefs)) # this is a simplification
        for href in proper_hrefs:
            src_url = url.replace("http://", "").replace("https://", "")
            trg_url = href.replace("http://", "").replace("https://", "")
            graph.add_edge(src_url, trg_url)
            print("adding edge {} -> {}".format(src_url, trg_url))
            build_hypergraph(trg_url, depth-1, graph)
    return graph


# lambda href: href.endswith(".html") is the same as
def does_it_end_with_html(href):
    return href.endswith(".html")

if __name__ == "__main__":
    # print(tramtable(readTramNetwork("_tramnetwork.json")))
    visualize(build_hypergraph("www.cse.chalmers.se/~aarne/", depth=3))