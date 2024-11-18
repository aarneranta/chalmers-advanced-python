import json
from pprint import pprint


TRAM_STOP_FILE = 'labs/data/tramstops.json'
with open(TRAM_STOP_FILE, 'r') as fromFile:
    data = json.load(fromFile)



with open ("labs/data/tramlines.txt", "r", encoding= "UTF-8") as file:
    lines = file.read().replace(":","").strip().split("\n\n")
    lines = [line.split("\n") for line in lines]

    

def build_tram_stops(jsonobject):

    stopdict = {x: {"lat":jsonobject[x]['position'][0], "lon":jsonobject[x]['position'][1]} for x in jsonobject}

    return stopdict


def build_tram_lines(lines):

    linedict = {}
    timedict = {}

    for line in lines:
        values=[]
        key = line[0]
        for i in range(1, len(line) - 1):
            name, time = [item.strip() for item in line[i].split("  ") if item]
            next_name, next_time = [item.strip() for item in line[i+1].split("  ") if item]
            time_diff = int(next_time) - int(time)
            values.append(name)
            if name not in timedict:
                timedict[name] = {}
            if next_name not in timedict:
                timedict[next_name] = {}
            if name not in timedict[next_name]:
                timedict[name][next_name] = time_diff
        linedict[key] = values
    
    return (linedict, timedict)


def build_tram_network(stopfile, linefile):

    outdict = {"stops": build_tram_stops(stopfile), "lines": build_tram_lines(linefile)[0], "times": build_tram_lines(linefile)[1]}

    with open("labs/data/tramnetwork.json", "w") as file:
        json.dump(outdict, file)


def lines_via_stop(linedict, stop):
    pass

def lines_between_stops(linedict, stop1, stop2):
    pass

def time_between_stops(linedict, timedict, line, stop1, stop2):
    pass

def distance_between_stops(stopdict, stop1, stop2):
    pass

def dialogue(tramfile):
    pass