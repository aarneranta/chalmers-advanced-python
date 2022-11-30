# path visualization with direct colouring of SVG file: DON'T CHANGE

import os
from django.conf import settings

GBG_TRAMNET_SVG = os.path.join(settings.BASE_DIR,
                        'tram/templates/tram/images/gbg_tramnet.svg')

SHORTEST_PATH_SVG = os.path.join(settings.BASE_DIR,
                        'tram/templates/tram/images/shortest_path.svg')

# to color SVG directly; specialized to SVG produced from graphviz

import xml.etree.ElementTree as et

def color_svg_network(
        infile=GBG_TRAMNET_SVG,
        outfile=SHORTEST_PATH_SVG,
        colormap=lambda v: 'white'):
    tree = et.parse(infile)
    root = tree.getroot()
    ns = '{http://www.w3.org/2000/svg}'
    lns = len(ns)
    rg = root.find(ns+'g')
    for g in rg.iter(ns+'g'):
        if g.get('class') == 'node':
            stop = g.find(ns+'title').text
            for p in g.iter():
                if p.tag[-7:] == 'polygon':
                    p.set('fill', colormap(stop))
    xns = '{http://www.w3.org/1999/xlink}'
    lxns = len(xns)
    for elem in root.iter():
        elem.tag = elem.tag[lns:]
        for k, v in elem.items():
            print(k, v)
            if k[:lxns] == xns:
                elem.set(k[lxns:], v)
#                del elem[k]

    tree.write(outfile)

"""
<!-- Svingeln -->
<g id="node10" class="node">
  <title>Svingeln</title>
  <g id="a_node10">
    <a xlink:href="https://avgangstavla.vasttrafik.se/?source=vasttrafikse-stopareadetailspage&amp;stopAreaGid=9021014006480000" xlink:title="Svingeln">
      <polygon fill="white" stroke="black" points="784.38,-511.53 739.38,-511.53 739.38,-494.53 784.38,-494.53 784.38,-511.53"/>
      <text text-anchor="middle" x="761.88" y="-501.13" font-family="Times,serif" font-size="8.00">Svingeln</text>
    </a>
</g>
</g>
"""
