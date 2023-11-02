# lecture 7

import graphs  # your Lab2 solution
import graphviz

def draw(G):
    dot = graphviz.Graph()
    for v in G.vertices():
        dot.node(str(v))
    for (v, w) in G.edges():
        dot.edge(str(v), str(w))
    dot.render(view=True)
    
def draw_rectangles(G):
    dot = graphviz.Graph()
    for v in G.vertices():
        dot.node(
            str(v),
            shape='rectangle',
            )
    for (v, w) in G.edges():
        dot.edge(str(v), str(w))
    dot.render(view=True)

    
def draw_colored(G, color=lambda v: 'orange'):
    dot = graphviz.Graph()
    for v in G.vertices():
        dot.node(
            str(v),
            fillcolor=color(v),
            style='filled'
            )
    for (v, w) in G.edges():
        dot.edge(str(v), str(w))
    dot.render(view=True)


def wikipedia(v):
    return 'https://en.wikipedia.org/wiki/'+str(v)


def draw_urls(G, url=wikipedia):
    dot = graphviz.Graph()
    for v in G.vertices():
        dot.node(
            str(v),
            URL=url(v)
            )
    for (v, w) in G.edges():
        dot.edge(str(v), str(w))
    dot.render(view=True)


from random import randrange
def randompos(G, v):
    n = len(G)
    return randrange(n), randrange(n)
    
    
def draw_positioned(G, pos=lambda v: randompos(G, v)):
    dot = graphviz.Graph(engine='fdp')
    for v in G.vertices():
        (x, y) = pos(v)
        dot.node(
            str(v),
            pos=str(x) + ',' + str(y) + '!'
            )
    for (v, w) in G.edges():
        dot.edge(str(v), str(w))
    dot.render(view=True)


import matplotlib.pyplot as plt
def draw_matplotlib(G, pos=lambda v: randompos(G, v)):
    plt.figure(figsize=(12, 12))

    posdict = {}
    for v in G.vertices():
        (x, y) = pos(v)
        posdict[v] = (x, y)
        plt.text(x, y, str(v))

    for a, b in G.edges():
        ax, ay = posdict[a]
        bx, by = posdict[b]
        X = [ax, bx]
        Y = [ay, by]
        plt.plot(X, Y)
    plt.show()

    

def mygraph():
    G = graphs.Graph()
    for n in range(2, 11):
        for m in range(2, n):
            if n % m == 0:
                G.add_edge(m, n)
    return G



    
if __name__ == '__main__':
    G = mygraph()
#    draw(G)
#    draw_rectangles(G)
#    draw_colored(G)
#    draw_positioned(G)
#    draw_urls(G)
    draw_matplotlib(G)

