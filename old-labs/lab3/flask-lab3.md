# Lab3: A web application for tram network

Advanced Python Course, Chalmers DAT515, 2021

by Aarne Ranta


Version 1.0, 8 December 2021

NOTICE: if you have already started working in Flask, in accordance
with the earlier draft, you can continue with this specification.
The directories `static` and `templates` belong the the Flask version.

If you have not started yet, we strongly recommend building the Django
version as specified in `lab3.md`.
The instructions there are much more detailed.

The task, including the bonus parts, is exactly the same in the Flask
and Django versions.

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

We will follow a standard line of work for the `flask` network.
There are several tutorials available, for instance, the one by [Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world), whose chapters 1 to 3 cover most of the things we need.


### The virtual environment

1. Create a `lab3` directory in your GitHub repository for the course.
2. Follow [the tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) to build a **virtual environment** (`venv`) for your application.
3. Activate the environment and install `flask` and other libraries that you need.

It is advisable to follow the tutorial, chapters 1 to 3, exactly before you start with your own project.
In this way, you can make sure that everything works as required.
But do not include this experiment in your course GitHub repository!


### Python files

Directly the `app` directory, you need to create the following files:

- `__init__.py`, standard
- `forms.py`, standard
- `routes.py`, standard
- `graphs.py`, a copy from Lab 2, with import paths set to `app` 
- `trams.py`, a copy from Lab 2, with import paths set to `app` 
- `tramviz.py`, a new file
- directory `static`, where you just copy
  - `auto.css` from [./static/]
  - `auto.js` from [./static/]
  - `tramnetwork.json` as created in Lab 1

- directory `templates`, where you put
  - `base.html` copied from [./templates/], inherited by most other pages
  - `route.html` copied from [./templates/], for searching for a route
  - `lines.html` which you create yourself, for just showing the network or restricting it to certain lines
  - `index.html` which you create yourself and where you can put whatever you want, but it must give links to `route.html` and `lines.html` 

Most part of the actual work will happen in ``tramviz.py``, which we will describe in a separate section.
However, you may actually spend much of your time just to make this all work so that you can see the app in action in your web browser.


### Changes to `trams.py`

The imports of Lab 2 files are now from their app versions:

    import json
    from app import graphs as g
    from urllib.request import urlopen

In `readTramNetwork()`, the JSON file is read from a URL, pointing to the `static` subdirectory of the app.
The URL that can be used is

    http://127.0.0.1:5000/static/gbg_trams.json

Instead of `open` on a file, the content is loaded by

    urlopen(url-of-tramfile).read().decode('utf8')

In order to position the stops well on the map, we need to know the extreme points of the network - that is, the minimum and maximum latitude and longitude.
To this end, we add a function (or a class method in `TramNetwork`)

    def extreme_positions(network):
        # code to compute the extreme positions
        return minlon, minlat, maxlon, maxlat


### The file `tramviz.py`

This file can be modified from [the Django version file](files/tramviz.py).
You have to change the imports and the file paths read and generated to match Flask conventions.
```
   from app import graphs
   from app import trams
```
The function imported to the app is still

- `show_shortest(dep, dest)`, displaying the shortest path on the map



### Autocompletion

(Optional, since the Django version does not require this)

The route finding page helps users with autocompletion of tram stop names:

![autocompletion](../images/find-auto.png)

We provide ready-made Javascript and CSS files, given in the [static](./static) directory.
These files are copied and slightly modified from [W3Schools](https://www.w3schools.com/howto/howto_js_autocomplete.asp).
Since this kind of communication is not directly covered in Grinberg's tutorial, we also provide the HTML template file [route.html](./templates/route.html).


## Bonus part 1

In Lab2 shortest path, we ignored the effect of changing from one line to the other.
This effect is that major factor that can make "shortest time" and "shortest distance" differ.
Its implementation requires that we recognize when a change must be made and add a suitable number of minutes or meters to the cost.

One way to do this with the existing algorithms is simply to build a new graph for the network, where

- vertices are pairs `(stop, line)` for each `stop` in the original graph and each `line` than passes through it,
- every edge `(a, b)` of the original graph is multiplied to edges `((a, line), (b, line))` for every `line` that serves both `a` and `b`,
- edges are added between all vertices that have the same `stop`,
- distances and transfer time between different stops are the same as in the original graph,
- a special change distance and change time is added between vertices that have the same stop but different times - for instance, 20 metres and 10 minutes, respectively.


## Bonus part 2: links to actual traffic information

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

