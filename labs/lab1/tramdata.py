import sys
import json
import math
import re

# Network initialization #####################################################

def build_tram_stops(json_file):
    """
    Given a json file describing tram stop, return the corresponding Python
    dictionary, with stop names as keys and latitude and longitude as values.
    """
    
    # read json to python dict 
    with open(json_file) as file:
        basic_dict = json.load(file)
    custom_dict = {}

    # convert to required format (there could be a neater way)
    for key in basic_dict:
        custom_dict[key] = {
            "lat": float(basic_dict[key]["position"][0]),
            "lon": float(basic_dict[key]["position"][1]),
        }
    return custom_dict

def parse_stop_info(line):
    """
    Divides a stop info line into stop name and time, e.g.
    'Liseberg Södra            10:11' -> ("Liseberg Södra","10:11")
    """
    time = line[-6:]
    stop_name = line[:-6].rstrip()
    return (stop_name, time)

def build_tram_lines(lines_file):
    """
    Given a text file describing tram lines, return:
    - a line dict where keys are line names and values are lists of stops
    - a time dict representing transition times from a stop to another 
    """
    line_dict = {}
    time_dict = {}

    with open(lines_file) as file:
        text = file.read()

    def time_diff(s1, s2):
        """
        Given to strings in the form "hh:mm", it returns their time 
        difference in minutes.
        NOTE: this implementation assumes that no tram line takes over 60 
        minutes to travel through. In the input file, hh is in fact always 10.
        TODO: generalize
        """
        return abs(int(s1.replace(":", "")) - int(s2.replace(":", "")))

    def not_redundant(s1, s2, td):
        """
        Given two stops and a time dictionary, it checks whether storing the
        transition time from s1 to s2 in the dictionary would be redundant.
        """
        return (not (s1,s2) in td.items()) and (not (s2,s1) in td.items())

    tram_lines = text.split("\n\n")
    for tram_line in tram_lines[:-1]: # skip last empty line!
        lines = tram_line.split("\n")
        tram_line_n = str(int(lines[0][:-1])) # int removes any spaces
        line_dict[tram_line_n] = []
        for (i,line) in enumerate(lines[1:]):
            (stop, time) = parse_stop_info(line)
            line_dict[tram_line_n].append(stop)
            next_i = i + 2
            if next_i < len(lines):
                (next_stop, next_time) = parse_stop_info(lines[next_i])
                if not_redundant(stop, next_stop, time_dict):
                    if not stop in time_dict:
                        time_dict[stop] = {}
                    time_dict[stop][next_stop] = time_diff(time, next_time)

    return line_dict, time_dict

def build_tram_network(json_file, lines_file):
    """
    Builds a dictionary of the three above generated dictionaries and exports
    it as json, writing it to 'tramnetwork.json'
    """
    stops = build_tram_stops(json_file)
    (lines,times) = build_tram_lines(lines_file)
    tramdict_dict = {
        "stops": stops,
        "lines": lines,
        "times": times
    }
    with open("tramnetwork.json", "w") as file:
        json.dump(tramdict_dict, file)

# Query functions ############################################################

def lines_via_stop(lines_dict, stop):
    """
    Lists the lines that go via the given stop. 
    """
    lines = []
    for (curr_line,curr_stops) in lines_dict.items():
        for curr_stop in curr_stops:
            if curr_stop == stop:
                lines.append(curr_line)
    lines.sort(key=int)
    return lines

def lines_between_stops(lines_dict, stop1, stop2):
    """
    Lists the lines that go from stop 1 to stop 2.
    """
    lines = []
    for (curr_line, curr_stops) in lines_dict.items():
        if stop1 in curr_stops and stop2 in curr_stops: # both directions
            lines.append(curr_line)
    lines.sort(key=int)
    return lines

def time_between_stops(lines_dict, times_dict, line, stop1, stop2):
    """
    Returns the time it takes to go from stop1 to stop2 via the given line. 
    If the stops are not along in the same line, it prints an error message.
    """
    line_stops = lines_dict[line]
    try:
        i = line_stops.index(stop1)
        j = line_stops.index(stop2)
    except ValueError:
        print("Cannot go from {} to {} with line {}.".format(stop1, stop2, line))
        return
    relevant_stops = line_stops[min(i,j):max(i,j)+1]
    time = 0
    for (k,stop) in enumerate(relevant_stops):
        if k + 1 < len(relevant_stops):
            time += times_dict[stop][relevant_stops[k + 1]]
        else: break
    return time


def distance_between_stops(stops_dict, stop1, stop2):
    """
    Calculates the geographic distance between any two stops, based on their 
    latitude and longitude.
    """

    def rad(l):
        """
        Converts degrees to radiants.
        """
        return l * (math.pi / 180)

    (lat1,lon1) = (stops_dict[stop1]["lat"],stops_dict[stop1]["lon"])
    (lat2,lon2) = (stops_dict[stop2]["lat"],stops_dict[stop2]["lon"])
    r = 6371.009 # Earth radius in km
    deltaf = rad(lat2 - lat1) # lat
    deltal = rad(lon2 - lon1) # lon
    fm = (rad(lat1) + rad(lat2)) / 2
    return r * math.sqrt((deltaf ** 2) + ((math.cos(fm) * deltal) ** 2))

# User interaction ###########################################################

def initialize():
    build_tram_network("../data/tramstops.json", "../data/tramlines.txt")

def dialogue(jsonfile):
    with open(jsonfile) as f:
        tramdict = json.load(f)

    while True:
        query = input("> ")
        ans = answer_query(query, tramdict)
        if ans == False:
            print("sorry, try again")
        elif ans == None or ans == []:
            print("invalid arguments")
        else:
            print(ans)
    
def answer_query(query, tramdict):
    via = re.findall(r"via ((?:[a-ö]+ ?)+)", query, flags=re.IGNORECASE)
    if via:
        return lines_via_stop(tramdict['lines'], via[0]) 

    between = re.findall(
        r"between ((?:[a-ö]+ ?)+) and ((?:[a-ö]+ ?)+)", query, flags=re.IGNORECASE)
    if between:
        return lines_between_stops(tramdict['lines'], between[0][0], between[0][1])

    time = re.findall(
        r"time with (\d+) from ((?:[a-ö]+ ?)+) to ((?:[a-ö]+ ?)+)", query, flags=re.IGNORECASE)
    if time:
        return time_between_stops(tramdict['lines'], tramdict['times'], time[0][0], time[0][1], time[0][2])

    distance = re.findall(
        r"distance from ((?:[a-ö]+ ?)+) to ((?:[a-ö]+ ?)+)", query, flags=re.IGNORECASE)
    if distance:
        return distance_between_stops(tramdict['stops'], distance[0][0], distance[0][1])

    if query == "quit":
        exit(0)

    return False

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        dialogue("tramnetwork.json")
    elif len(sys.argv) == 2 and sys.argv[1] == "init":
        initialize()
    else:
        print("Usage: python tramdata.py init for initialization, " 
            + "python tramdata.py for interactive mode.")
        exit(1)