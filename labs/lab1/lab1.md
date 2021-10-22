# Lab 1: Information Extraction

Advanced Python Course, Chalmers DAT515, 2021

by Aarne Ranta


## Purpose

The purpose of Lab 1 is to read information from different formats and combine it to useful data structures.
We will consider two different data formats:
- JSON, processed by the Python library `json`,
- plain text, processed by indices `[0]`, slices `[1:5]`, and standard
string methods such as `split()`, `strip()`, `join()`.

The data collected from these file is saved in a new JSON file,
`tramnetwork.json`, which
is ready to be used in applications - including Labs 2 and 3.
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

Learning outcomes:

- main constructs of Python, reaching the level of the introductory
Python course:
  - string manipulation
  - input and output
  - reading and writing files
  - lists and dictionaries
  - mathematical formulas and the `math` library

- the JSON data format and the `json` library


## Task

The task is to write three functions that build dictionaries, four functions that extract information from them, and a dialogue function that answers to queries.

### Dictionary building functions

`build_tram_stops(jsonobject)`, building a **stop dictionary**, where

* keys are names of tram stops
* values are dictionaries with
    * the latitude
	* the longitude

Here is a part of the stop dictionary, showing just one stop:

    {
      'Majvallen': {
        'lat': '57.6909343',
	    'lon': '11.9354935'
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

  1:
  Östra Sjukhuset           10:00
  Tingvallsvägen            10:01
  Kaggeledstorget           10:03
  Ättehögsgatan             10:03

Thus, for each line, there is a section starting with the line number
and a colon.
After that, the stops are given together with times.
For simplicity, each line starts from time 10:00.
We are not interested in these times as such, but in the **transition times** between stops.
Thus, for instance, the transition time between Tingvallsvägen and Kaggeledstorget is 2 minutes.
We want to store these transition times in a non-redundant way, under the following assumptions:

- transition times are independent of line, departure time and direction:
  - the transition time from A to B is the same for all lines and departures
  - the transition time from B to A is the same as from A to B

Hence, we don't want to add transition times to the line dictionary, because this would lead to storing redundant information.
Instead, when reading the file [`tramlines.txt`](../data/tramlines.txt), we simultaneously build a **time dictionary**, where

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
- the time between two stops is given only once, in the time dictionary.

Moreover,

- the text file that gives lines and their stops and times is read only once.

`build_tram_network(somefiles)` puts everything together. It reads the two input files and writes a
third one, entitled `tramnetwork.json`.
This JSON file represents a dictionary that contains the three dictionaries
built:

    {
    "stops": {
        "\u00d6stra Sjukhuset": {
            "lat": 57.7224618,
            "lon": 12.0478166
			},  # and so on, the entire stop dict			
		}
      },
    "lines": {
        "1": [
            "\u00d6stra Sjukhuset",
            "Tingvallsv\u00e4gen",
			# and so on, all stops on line 1
			],  # and so on, the entire line dict
		},
    "times": {
        "Tingvallsv\u00e4gen": {
            "Kaggeledstorget": 2
            },  # and so on, the entire time dict
        }
    }

### Query functions

The following functions may use any of the three kinds of dictionaries - it is your task to decide which ones.

`lines_via_stop(somedicts, stop)` lists the lines that go via the given stop.
The lines should be sorted in their numeric order, that is, '2' before '10'.

`lines_between_stops(somedicts, stop1, stop2)` lists the lines that go from stop1 to stop2.
The lines should be sorted in their numeric order, that is, '2' before '10'.
Notice that each line is assumed to serve in both directions - the direction listed explicitly for it, and the opposite direction.

`time_between_stops(somedicts, line, stop1, stop2)` calculates the time from `stop1` to `stop2` along the given `line`. This is obtained as the sum of all distances between the stops. If the stops are not along the same line, an error message is printed.

`distance_between_stops(somedicts, stop1, stop2)` calculates the geographic distance between any two stops, based on their latitude and longitude.
The distance is hence not dependent on the tram lines.
Use the formula from [this Wikipedia description](https://en.wikipedia.org/wiki/Geographical_distance#Spherical_Earth_projected_to_a_plane), and notice that the `math` library is needed in the Python code.


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


### The main function

At the end of your file, make a conditional call of the `dialogue()` function with the provided data files:

    if __name__ == '__main__':
        dialogue()


### Tests

You should create your own tests.
More about this later.


## Submission

You should create a GitHub repository for this course and **make it private**.
You may only - ever - share it with

- your lab partner
- the teachers of the course

The submission is via Canvas, where you post a link to your repository.
Lab1 solution should be the file `tramdata.py` in that repository, in the main branch.
We may fetch the file at any point after the submission deadline, so make sure that it remains correct at all times!
You can use other branches for experimentation.





