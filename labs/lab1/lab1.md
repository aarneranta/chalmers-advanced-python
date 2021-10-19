# Lab 1: Information Extraction

Advanced Python Course, Chalmers DAT515, 2021

by Aarne Ranta


## Purpose

The purpose of Lab 1 is to read information from different formats and combine it to useful data structures.
We will consider two different data formats:
- JSon, processed by the Python library `json`,
- plain text, processed by indices `[0]`, slices `[1:5]`, and standard string methods such as `split()`, `strip()`, `join()`.


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

These structures and queries are preparation for the later labs, where they are embedded in an object-oriented hierarchy (Lab 2) and used in the back-end of a web application (Lab 3).


## Task

The task is to write two functions that build dictionaries, four functions that extract information from them, and a dialogue function that answers to queries.

### Dictionary building functions

`build_tram_stops(jsonobject)`, building a **stop dictionary**, where

* keys are names of tram stops
* values are dictionaries with
    * the name of the town
    * the latitude
	* the longitude

Here is a part of the stop dictionary, showing just one stop:

    {
      'Majvallen': {
        'town': 'Göteborg',
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
The conversion needs a bit more processing than the previous function.
Notice that some stop names are followed by numbers indicating the transition time from the previous stop.
These numbers are ignored by this function, but will be used in the next one.

The same function will use the same file to build, at the same time, a
**time dictionary**, where

  - keys are stop names
  - values are dictionaries from stop names to numbers of minutes

Here is an example:

    {
      "Vasaplatsen": {
         "Kapellplatsen": 2
      }
    }

This information is extracted from the text lines

    Vasaplatsen
    Kapellplatsen 2
    Chalmers

The meaning of this is:

- the trip from Vasaplatsen to Kapellplatsen takes 2 minutes,
- the trip from Kapellplatsen to Chalmers takes 1 minute (the default, when no number is given).

It is enough to collect times in one direction, and only for transition times other than one minute.
Thus no time *from* Kapellplatsen is needed, since the only possibilities are to Vasaplatsen (already covered) and to Chalmers (the default).

The general idea with these data structures and functions is to **avoid redundancy**: every piece of information is given only once in the dictionaries.
In particular,

- the location of each stop is given only once, in the stop dictionary,
- the time between two stops is given only once, in the time dictionary.

Moreover,

- the text file that gives lines and their stops and times is read only once.



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

The `dialogue(somefiles)` function implements a dialogue about tram information.
It starts by reading the data from files, using the dictionary-building functions that you have written.
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





