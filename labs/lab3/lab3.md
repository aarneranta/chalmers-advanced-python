# Lab3: A web application for tram network

Advanced Python Course, Chalmers DAT515, 2021

by Aarne Ranta


DRAFT, to be finalized 7 December


## Purpose

The purpose is to build a web application replicating some functionalities of apps such as [Västtrafik](https://www.vasttrafik.se/reseplanering/reseplaneraren/).
Your application will

- display the complete map of tram lines
- highlight shortest paths in terms of time and geographical distance
- bonus part 1: make the calculations more precise by taking changes into account
- bonus part 2: show actual departures from any stops by clicking at it on the map


Here is an example screenshot:

![shortest-path](../images/app-shortest.png)

Unlike the official app, ours will not have access to the actual timetables, but just to the distances and times as defined in Labs 1 and 2.
This is of course a severe simplification - but, on the other hand,
our app will be usable for any transport system that can be
represented by the class `TramNetwork`.
In addition, the bonus part will give access to actual traffic information from Västtrafik.

Another difference from the official app is that we only run ours in a safe `localhost` environment.
Thereby we do not have to cope with security issues, and it will also be much easier for all groups to finish the project.

The learning outcomes include:

- visualization with more details on positions and colours
- simple front-end construction with HTML
- putting everything together by using a web application framework, Django
- more details of `graphviz` library, various libraries belonging to the `flask` framework
- virtual environments (`venv`)


The basic lab gives 10 points and each bonus part 4 points.
Thus the maximum is 18 points.


## The task

We will follow a standard line of work for the `django` network.
There are several tutorials available, for instance,

- [Django Girls Tutorial](https://tutorial.djangogirls.org/en/)
- [Official Django Tutorial](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)



### The virtual environment

1. Create a `lab3` directory in your GitHub repository for the course.
2. Follow [the tutorial](https://tutorial.djangogirls.org/en/installation/#virtualenv) to build a **virtual environment** (`venv`) for your application.
3. Activate the environment and install `django` and other libraries that you need (in this case, `graphviz`)


**Notice**. In Step 3, you can install the latest version of Django, 3.2, instead of 2.4 as in the Django Girls Tutorial.


It is advisable to follow the tutorial exactly before you start with your own project.
We will do this during Lecture 9 and also have an exercise on it.
In this way, you can make sure that everything works as required.
But do not include this experiment in your course GitHub repository!


### Files to write

The final structure will look as follows, in my case.
Most of these files are created automatically (unmarked in the diagram).
Some of these have to be edited slightly (marked `?`).
Some have to be written by you (marked `??`).
Some can be copied from [here](./files/) (marked `!`).
```
lab3
├── db.sqlite3
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── settings.py ?
│   ├── urls.py
│   └── wsgi.py
├── myvenv
│   └── ...
├── requirements.txt ?
├── static
│   ├── gbg_trams.json ??
│   ├── shortest_path.svg
│   └── tram-url.json ??
└── tram
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py ?
    ├── migrations
    │   └── __init__.py
    ├── models.py ?
	├── templates ??
    │  └── tram
    │      ├── find_route.html !
    │      ├── home.html !
	│      ├── images
    │      │   ├── gbg_tramnet.svg
    │      │   └── shortest_path.svg -> ../../../../static/
	│      ├── route_detail.html !
    │      └── static
    ├── tests.py
    ├── urls.py ?
    ├── utils
    │   ├── __init__.py
    │   ├── graphs.py ?? 
    │   ├── trams.py ??
    │   └── tramviz.py ??
    └── views.py !
```
Most part of the actual work will happen in ``tramviz.py``, which we will describe in a separate section.
However, you may actually spend much of your time just to make this all work so that you can see the app in action in your web browser.


### The file `tram/utils/graphs.py`

The simplest solution is just to copy your Lab 2 file here.


### The file `tram/utils/trams.py`

The import from `graphs` is now to its local version, marked by prefixing ``.`` (without a slash):
```
    from .graphs import WeightedGraph, dijkstra
```
In addition, you need to modify `readTramNetwork()` in a way that works in Django.
TODO

In order to position the stops well on the map, we need to know the extreme points of the network - that is, the minimum and maximum latitude and longitude.
To this end, we add a function (or a class method in `TramNetwork`)

    def extreme_positions(network):
        # code to compute the extreme positions
        return minlon, minlat, maxlon, maxlat


#### Bonus part 1

In Lab2 shortest path, we ignored the effect of changing from one line to the other.
This effect is that major factor that can make "shortest time" and "shortest distance" differ.
Its implementation requires that we recognize when a change must be made and add a suitable number of minutes or meters to the cost.

One way to do this with the existing algorithms is simply to build a new graph for the network, where

- vertices are pairs `(stop, line)` for each `stop` in the original graph and each `line` than passes through it,
- every edge `(a, b)` of the original graph is multiplied to edges `((a, line), (b, line))` for every `line` that serves both `a` and `b`,
- edges are added between all vertices that have the same `stop`,
- distances and transfer time between different stops are the same as in the original graph,
- a special change distance and change time is added between vertices that have the same stop but different times - for instance, 20 metres and 10 minutes, respectively.



### The file `tramviz.py`

This is the file that makes most of the work in the app.
You can start from the [example file](../../examples/tramviz.py).

The function used in the app is

- `show_shortest(dep, dest)`, displaying the shortest path on the map

A baseline implementation could use `graphs.visualize` from Lab 2.
But here we want more (some of it already given in the example file):

- the stops should be put into positions that correspond to their longitude and latitude;
- there should be separate, coloured edges for each tramline that serves the same edge;
- two possibly different shortest paths should be shown: the temporally and geographically shortest.

Moreover, there is a technical difference:

- the map should be generated in the SVG format (Scalable Vector Graphics) and piped directly to the app.

This, however, is easy to implement: as the last steps of visualization, use

    dot.format = 'svg'
    return dot.pipe().decode('utf-8')

TODO: more details on how to use this in Django.

The most complex part of this file - and the whole Lab 3 - is to make sure that the positions and colours come out right.
Here is a possible sequence of steps to follow:

- use `graphs.extreme_positions()` to compute the corners, the width, and the height of the map in geographic degrees;
- calculate `x` coordinates from *longitudes* by subtracting the minimal longitude from the actual longitude, and multiplying with a suitable constant (500 works well for me);
- calculate `y` coordinates similarly from latitudes;
- create a canvas of suitable size for the map, by for instance

    dot = graphviz.Graph(engine='fdp', graph_attr={'size': '12,12'})

which works fine for me (the engine 'fdp' is needed to preserve absolute positions);
- compute the shortest paths, with respect to both distance and time;
- print the nodes of the map, displaying the name of each tram stop and colouring it in three of different colours depending on if it appears on the shortest time path, shortest distance path, or both (see the picture at the beginning of this document, using yellow, cyan, and lightgreen, respectively);
- draw edges corresponding to each line with their colors - the following color map is an approximation of what is actually used

    {1: 'gray', 2: 'yellow', 3: 'blue', 4: 'green', 5: 'red',
     6: 'orange', 7: 'brown', 8: 'purple', 9: 'blue',
     10: 'lightgreen', 11: 'black', 13: 'pink'}

- print the listing of the quickest path and its duration, and the shortest (if different) and its length.



### Bonus part 2: links to actual traffic information

This bonus part can be submitted even if you have not done Bonus part 1.

The challenge is to find the URLs corresponding to each stop name.
They are given as numerical codes, for instance, Nordstan is
```
https://www.vasttrafik.se/reseplanering/hallplatser/9021014004945000/
```
and its timetable is in
```
https://avgangstavla.vasttrafik.se/?source=vasttrafikse-stopareadetailspage&stopAreaGid=9021014004945000
```
The full list of stop identifiers can be found in
```
https://www.vasttrafik.se/reseplanering/hallplatslista/
```
The algorithm is as follows:

1. Investigate where and how Gids are given in the HTML document.
2. Extract the Gids of all tram stops from the document.
3. Create URLs for every stop.
4. Include the URLs in the generated map.

The standard library for parsing HTML is
```
https://docs.python.org/3/library/html.parser.html
```
A slightly more convenient third party library can also be used:
```
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
```


## Submission

Via a GitHub link in Canvas, as usual.

Indicate in your Canvas message whether you claim bonus points for Bonus task 1 or 2 or both.




