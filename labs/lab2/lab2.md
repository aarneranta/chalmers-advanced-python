# Lab2: Graphs and transport networks

Advanced Python Course, Chalmers DAT515, 2021

by Aarne Ranta

DRAFT, TO BE COMPLETED BY 18 November 2021

## Purpose

The purpose of this lab is to build a system of classes and algorithms for graphs.
The intended application is transport networks, which will be built on top of the graph classes.
But the graphs can be applied in many other ways as well, as will be shown in exercises and extra labs.

The main learning outcomes are:

- Python's data model for classes
- class definitions with private instance variables, public methods, and "hidden" methods
- inheritance between classes
- representations of undirected, directed, and weighted graphs
- Dijkstra's shortest path algorithm with different cost functions
- visualization of graphs and paths in them, the ``graphviz`` library
- property-based testing with randomized input data, the ``hypothesis`` library


## The task: file `graphs.py`

### The Graph class

The class `Graph` can be initialized in three ways:

- from `None` (the default)

or optionally from either

- from an adjacency dictionary
- from a list of edges

The ``__init__()`` function also takes optional

- boolean stating if the graph is **directed**; its default is `False`
- value dictionary, assigning values to vertices; its default is `None`

The class builds internally a data structure that supports different graph operations.
This data structure is kept hidden, and we leave it to everyone to choose among the various equivalent representations.
The public methods to be implemented are:

- `neighbours(vertex)` (same as `successors(vertex)` for directed graphs)
- `predecessors(vertex)` (same as `neighbours(vertex)` for undirected graphs)
- `successors(vertex)` (same as `neighbours(vertex)` for undirected graphs)
- `vertices()`
- `edges()` (only given in one direction for undirected graphs)
- `__len__()`, the number of vertices
- `add_vertex(vertex)`
- `add_edge(vertex, vertex)` 
- `remove_vertex(vertex)` (also removing the edges with this vertex)
- `remove_edge(vertex, vertex)`
- `is_directed()`
- `get_vertex_value(vertex)`
- `set_vertex_value(vertex)`


### The WeightedGraph class

`WeightedGraph` is a subclass of `Graph`, which stores **edge weights** - which can be objects of any type.
It stores these weights internally (e.g. in a dictionary) and supports two public methods:

- `get_weight(vertex, vertex)`
- `set_weight(vertex, vertex, weight)`


### The shortest path algorithm

The function

  dijkstra(graph, source, cost=lambda u,v: 1, step=lambda e: e)

computes the shortest path from `source` vertex to all other vertices, as a dictionary.
What is shortest is calculated by the minimum sum of ``cost`` function applied to each step on the path.
For example, if `graph` is a `WeightedGraph`, its ``get_weight()`` method can be used.
The ``step`` function defines what information about each step on the shortest path is shown.
A suggested implementation of `dijkstra` follows the pseudocode in
[this Wikipedia article](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm).


### Visualization

A very simple visualization function is expected in Lab2; we will make it more sophisticated in Lab3.
The function

    visualize(graph, view='dot', name='mygraph', nodecolors={})

uses the `graphviz` library, whose documentation can be found [here](https://graphviz.readthedocs.io/en/stable/api.html).
The first intended use of `nodecolors` is to show the nodes along the shortest path in a different colour.
You can append the following code to your file to demonstrate this:

    def view_shortest(G, source, target, cost=lambda u,v: 1):
        path = dijkstra(G, source, cost)[target]['path']
        print(path)
        colormap = {str(v): 'orange' for v in path}
        print(colormap)
        visualize(G, view='view', nodecolors=colormap)

    def demo():
        G = Graph([(1,2),(1,3),(1,4),(3,4),(3,5),(3,6), (3,7), (6,7)])
        view_shortest(G, 2, 6)

    if __name__ == '__main__':
        demo()


## The task: file `trams.py`

This file needs to import from two other files of your own

- ``graphs.py`` from Lab 2
- ``tramdata.py`` from Lab 1

as well as from the standard libraries ``sys`` and ``json``.


### The TramStop class

The class `TramStop` reflects the data stored in the stop dictionary in Lab 1, plus some more information.
It has to store

- the name of the stop
- its position (latitude and longitude)
- the list of lines that serve the stop (not in Lab 1)

Its ``__init__()`` method needs the name as a required argument, whereas the position and line list are optional.
The public methods should enable

- getting and setting the position
- getting the list of lines
- adding lines to the list

This time, we leave it to you to decide what methods exactly there are.


### The TramLine class

The class ``TramLine`` reflects exactly the line dictionary of Lab 1.
Thus it should store internally, and make publicly available,

- the name (usually number) of the line
- the list of stops in order, in one direction

The detailed design is left to you.


### The TramNetwork class

The class ``TramNetwork`` is a ``WeightedGraph`` (i.e. inherits from it).
It stores internally

- a list (dictionary) of stops and their positions (of class ``TramStop``)
- a list (dictionary) of lines and their stops (of class ``TramLine``)
- edges, which are transitions between consecutive stops 
- weights, which are the transition times between adjacent stops

Most of the public methods are getters:

- the position of a stop
- the transition time between two subsequent stops
- the geographical distance between any two stops (from Lab 1!)
- list the lines through a stop
- list the stops along a line
- list all stops
- list all lines

However, there is one setter method, which is a bit more tricky:

- remove a line, together with all stops that are only served by that line

This function will be needed in Lab 3 where we want to focus on a subset of lines.


### Reading a TramNetwork

The JSON file `tramnetwork.json` produced in Lab 1 contains all information needed for building an instance of `TramNetwork`.
The function

    readTramNetwork(tramfile=TRAM_FILE)

should do this, defaulting to that JSON file.
It should return an object of class ``TramNetwork`.


### A demo

You can paste the following code to your `trams.py` file to demonstrate and test it:

    def demo():
        G = readTramNetwork()
        a, b = input('from,to ').split(',')
        gr.view_shortest(G, a, b)

    if __name__ == '__main__':
        demo()

When you run the code, it asks you to enter two tram stop names separated by a comma (no spaces between).
Then displays the whole tram network, with the shortest path (as the number of stops) coloured.


### Testing and documentation

Draw a UML diagram (details TODO)

Use `hypothesis` for testing the graph algorithms (details TODO)

Submit the files

- `graphs.py`
- `trams.py`
- `test_graphs.py`
- `test_trams.py`

via the same Git repository as in Lab 1.
Do this by reporting in Canvas that your lab is ready to be graded.

