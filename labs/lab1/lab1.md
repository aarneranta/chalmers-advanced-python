# Lab 1: Information Extraction

Advanced Python Course, Chalmers DAT515, 2021

by Aarne Ranta

Version 1.2, 18 November

Added a hint about the command-line argument `init`.

Version 1.1, 12 November

We now provide an alternative, easier way to define geographical distance.
Solving it in the original way is worth 2 extra points, which count toward a higher grade.
This change is in a paragraph marked "New in version 1.1"

Version 1.0, 9 November 2021

Work that satisfies the specification in this version will be
considered valid, even if we have to make changes after Version 1.0. So feel
confident to start you work, but keep an eye on possible changes: we
will not add tasks, but may have to explain some things more clearly.


## Purpose

The purpose of Lab 1 is to read information from different formats and combine it to useful data structures.
We will consider two different data formats:
- JSON, processed by the Python library `json`,
- plain text, processed by indices `[0]`, slices `[1:5]`, and standard
string methods such as `split()`, `strip()`, `join()`.

The data collected from these files is saved in a new JSON file,
`tramnetwork.json`, which is ready to be used in applications - including Labs 2 and 3.
The command `python3 tramdata.py init` produces this file.

The target data structures are dictionaries, which enable efficient queries about the data.
If run with the command `python3 tramdata.py`, the program will enable the following kind of dialogue:

    $ python3 tramdata.py 
    > via Chalmers
    ['6', '7', '8', '10', '13']
    > between Chalmers and Valand
    ['7', '10']
    > time with 6 from Chalmers to Järntorget
    10
    > distance from Chalmers to Järntorget
    1.628

These structures and queries are preparation for the later labs, where
they are embedded in an object-oriented hierarchy (Lab 2) and used in
the back-end of a web application (Lab 3).

An integral part of the lab is also a set of **tests**, which you will submit together with your solutions.
These tests must be written by using the `unittest` standard library of Python.

The solution will be submitted via [GitHub classroom](https://classroom.github.com/classrooms/148326473-dat515-dit515-2023-lp2) but graded on [Canvas](https://chalmers.instructure.com/courses/26551).

Learning outcomes:

- main constructs of Python, reaching the level of the introductory
Python course:
  - string manipulation
  - input and output
  - reading and writing files
  - lists and dictionaries
  - mathematical formulas and the `math` library

- the JSON data format and the `json` library

- testing and the `unittest` library

- version control and Git


### Testing

You should create your own tests by using the `unittest` standard library.
The file [`test_tramdata.py`](./test_tramdata.py) helps you to get started.
Copy this file and add your own tests at the same time as you are
writing each of the functions.
The file is a part of the solution you have to submit.


## Task

The task is to write three functions that build dictionaries, four functions that extract information from them, and a dialogue function that answers to queries.
The dialogue function should be divided into two parts to enable more accurate testing.

### Dictionary building functions

`build_tram_stops(jsonobject)`, building a **stop dictionary**, where

* keys are names of tram stops
* values are dictionaries with
    * the latitude
	* the longitude

Here is a part of the stop dictionary, showing just one stop:

    {
      'Majvallen': {
        'lat': 57.6909343,
	'lon': 11.9354935
       }
    }

An input file in the expected format is [`tramstops.json`](../data/tramstops.json).
The function involves an easy conversion using the `json` library.

`build_tram_lines(lines)`, building a **line dictionary**, where

- keys are names (usually consisting of digits, but to be treated as strings)
- values are lists of stop names, in the order in which the tram runs

Here is an example:

    {
      "9": [
        "Angered Centrum",
        "Storås",
        "Hammarkullen",
	    # many more stops in between
        "Sandarna",
        "Kungssten"
      ]
    }
	
An input file in the expected format is
[`tramlines.txt`](../data/tramlines.txt).
It is a textual representation of timetables for each line, looking as
follows:
```
  1:
  Östra Sjukhuset           10:00
  Tingvallsvägen            10:01
  Kaggeledstorget           10:03
  Ättehögsgatan             10:03
```
Thus, for each tram line, there is a section starting with the line number
and a colon.
After that, the stops are given together with times.
For simplicity, each line starts from time 10:00.
We are not interested in these times as such, but in the **transition times** between stops.
Thus, for instance, the transition time between Tingvallsvägen and Kaggeledstorget is 2 minutes.
We want to store the transition times in a non-redundant way, under the following assumptions:

- transition times are independent of line, departure time and direction:
  - the transition time from A to B is the same for all lines and departures
  - the transition time from B to A is always the same as from A to B

Hence, we don't want to add transition times to the line dictionary, because this would lead to storing redundant information.
Instead, from the file [`tramlines.txt`](../data/tramlines.txt), we also build a **time dictionary**, where

  - keys are stop names
  - values are dictionaries from stop names to numbers of minutes

Here is an example of a time dictionary entry:

    {
      "Tingvallsvägen": {
         "Kaggeledstorget": 2
      }
    }

To summarize, the general idea with these data structures and functions is to **avoid redundancy**: every piece of information is given only once in the dictionaries.
In particular,

- the location of each stop is given only once, in the stop dictionary,
- the time between any two stops is given only once, in the time dictionary.

Moreover,

- the text file that gives lines and their stops and times is read only once.

`build_tram_network(somefiles)` puts everything together. It reads the two input files and writes a
third one, entitled `tramnetwork.json`.
This JSON file represents a dictionary that contains the three dictionaries
built:

    {
    "stops": {
        "Östra Sjukhuset": {
            "lat": 57.7224618,
            "lon": 12.0478166
			},  # and so on, the entire stop dict			
		}
      },
    "lines": {
        "1": [
            "Östra Sjukhuset",
            "Tingvallsvägen",
			# and so on, all stops on line 1
			],  # and so on, the entire line dict
		},
    "times": {
        "Tingvallsvägen": {
            "Kaggeledstorget": 2
            },  # and so on, the entire time dict
        }
    }


### Tests for dictionary building

The file `test_tramdata-py` already tests if all stops associated with lines in `linedict` also exist in `stopdict`.
You should add at least the following tests:

- that all tram lines listed in the original text file ``tramlines.txt`` are included in ``linedict``,
- that the list of stops for each tramline is the same in ``tramlines.txt`` and ``linedict``,
- that all distances are "feasible", meaning less than 20 km (test this test with a smaller number to see it fail!),
- that the time from *a* to *b* is always the same as the time from *b* to *a* along the same line.



### Query functions

The following functions may use any of the three kinds of dictionaries - it is your task to decide which ones.

`lines_via_stop(somedicts, stop)` lists the lines that go via the given stop.
The lines should be sorted in their numeric order, that is, '2' before '10'.

`lines_between_stops(somedicts, stop1, stop2)` lists the lines that go from stop1 to stop2.
The lines should be sorted in their numeric order, that is, '2' before '10'.
Notice that each line is assumed to serve in both directions - the direction listed explicitly for it, and the opposite direction.

`time_between_stops(somedicts, line, stop1, stop2)` calculates the time from `stop1` to `stop2` along the given `line`. This is obtained as the sum of all distances between adjacent stops. If the stops are not along the same line, an error message is printed.

`distance_between_stops(somedicts, stop1, stop2)` calculates the geographic distance between any two stops, based on their latitude and longitude.
The distance is hence not dependent on the tram lines.
Use the formula from [this Wikipedia description](https://en.wikipedia.org/wiki/Geographical_distance#Spherical_Earth_projected_to_a_plane), and notice that the `math` library is needed in the Python code.

**New in version 1.1**. You can define this function easily by using the library [Haversine](https://pypi.org/project/haversine/).
If you do it without the library, as in the original version, it will give you extra points.


### The dialogue function

The `dialogue(jsonfile)` function implements a dialogue about tram information.
It starts by reading the data from the JSON file `tramnetwork.json`,
which has been produced by your program.
Then it takes user input and answers to any number of questions by using your query functions.
Following kinds of input are interpreted:

- `via <stop>`, answered by `lines_via_stop()`
- `between <stop1> and <top2>`, answered by `lines_between_stops()`
- `time with <line> from <stop1> to <top2>`, answered by `time_between_stops()`
- `distance from <stop1> to <top2>`, answered by `distance_between_stops()`
- `quit` - terminating the program
- input with non-existing line or stop names results in the message "unknown arguments" and a new prompt
- any other input results in the message "sorry, try again" and a new prompt
- the prompt is `> `.

The main challenge is to deal correctly with stop names that consist of more than one word.
A hint for this is to locate the positions of keywords such as "and", which can appear between stop names, and consider slices starting or ending at them.
The simplest method is the standard `index()` method of strings.
Also the regular expression library `re` could be used, but is probably more complicated to learn unless you already know it from before.

For the purpose of testing, and more generally to cleanly separate input and output from processing, the `dialogue()` function should be divided into two separate functions:

- `answer_query(tramdict, query)`, which takes the query string and returns the answer as a value (list or integer or float, or `False` if the query cannot be interpreted);

- `dialogue(jsonfile)` itself, which reads the file into a dictionary, loops by asking for input, and for each input prints the value returned by `answer_query()`, except for input `quit` (terminating the loop) and for uninterpreted input (asking the user to try again).


### Tests for the dialogue

Testing a complete dialogue is trickier than ordinary, value-returning functions. 
But you can easily test `answer_query()`.
What you should test, then, is that the answer printed for any query
(in a format written by the user) is the same as the expected answer.
What you really test then is that queries are parsed and interpreted correctly.




### The main function

At the end of your file, make a conditional call under

    if __name__ == '__main__':

calling `build_tram_network()` if the argument `init` is present, `dialogue()` otherwise.
**Hint**: You can check the presence of this argument by using `sys.argv`:
```
    if __name__ == '__main__':
        if sys.argv[1:] == ['init']:
            build_tram_network("tramlines.txt", "tramstops.json")
        else:
            dialogue("tramnetwork.json")			
```
You also need to import `sys`.			



## Submission

You should create a GitHub repository for this course and **make it private**.
You may only - ever - share it with

- your lab partner
- the teachers of the course

The submission is via Canvas, where you post a link to your repository.
Your Lab1 solution must be in two files in that repository, in the main branch:

- `tramdata.py`
- `test_tramdata.py`

They must be usable in the following ways:

- `python3 tramdata.py init` to produce the file `tramnetwork.json`,
- `python3 tramdata.py` to start the query dialogue,
- `import tramdata` from another Python file or the Python shell, without starting the dialogue or printing anything,
- `python3 test_tramdata.py` to run your tests.

We will test all these functionalities.
We will also run some tests of our own.
We may fetch the files at any point after the submission deadline, so make sure that they remains correct at all times!
You can use other branches for your private experimentation.

The same GitHub repository will be extended with your Lab 2 and 3
solutions later.






