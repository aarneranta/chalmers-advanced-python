# showing shortest path in the Wikipedia SVG map

import xml.etree.ElementTree as et
from urllib.request import urlopen

import sys
sys.path.append('../labs/lab2')
sys.path.append('../labs/lab1')
import trams
import graphs

MAP_FILE_URL = 'https://upload.wikimedia.org/wikipedia/commons/7/71/G%C3%B6teborgs_sp%C3%A5rv%C3%A4gsn%C3%A4t.svg'
TRAM_FILE = '../labs/lab1/tramnetwork.json'
OUT_FILE = 'routemap.svg'

def color_xml_tree(tree, tomark):
    if tree.text in tomark:
        print(tree.text)
        tree.attrib['style'] = "font-size:8.23333311px;stroke-width:0.26458332"
    for child in tree:
        color_xml_tree(child, tomark)


def main():
    network = trams.readTramNetwork(tramfile=TRAM_FILE)
    a, b = input('from,to: ').split(',')
    path = graphs.dijkstra(network, a)[b]['path']
    with urlopen(MAP_FILE_URL) as file:
        tree = et.fromstring(file.read())
    color_xml_tree(tree, path)
    et.ElementTree(tree).write(OUT_FILE)


if __name__ == '__main__':
    main()


        
