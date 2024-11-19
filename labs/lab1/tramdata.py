import json
from pprint import pprint
from haversine import haversine


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
        values.append(next_name)
        linedict[key] = values
    
    return (linedict, timedict)
def build_tram_network(stopfile, linefile):

    outdict = {"stops": build_tram_stops(stopfile), "lines": build_tram_lines(linefile)[0], "times": build_tram_lines(linefile)[1]}


    with open("labs/data/tramnetwork.json", "w") as file:
        json.dump(outdict, file)


def lines_via_stop(linedict, stop):

    stoplist = []

    for key in linedict:
        if stop in linedict[key]:
            stoplist.append(key)

    return stoplist

#print(lines_via_stop(build_tram_lines(lines)[0], "Valand"))

def lines_between_stops(linedict, stop1, stop2):

    stoplist = []

    for key in linedict:
        if stop1 in linedict[key] and stop2 in linedict[key]:
            stoplist.append(key)

    return stoplist
#print(lines_between_stops(build_tram_lines(lines)[0], "Ullevi Norra", "Chalmers"))
def time_between_stops(linedict, timedict, line, stop1, stop2):
       
       
    if linedict[str(line)].index(stop1) < linedict[str(line)].index(stop2):
        index_1 = linedict[str(line)].index(stop1)
        index_2 = linedict[str(line)].index(stop2) + 1
    else:
        index_1 = linedict[str(line)].index(stop2)
        index_2 = linedict[str(line)].index(stop1) + 1

    stoplist = linedict[str(line)][index_1:index_2]

    time = 0
    for i in range(len(stoplist) - 1):
        if stoplist[i+1] in timedict[stoplist[i]]:
            time += timedict[stoplist[i]][stoplist[i+1]]
            
        elif stoplist[i] in timedict[stoplist[i+1]]:
            time += timedict[stoplist[i+1]][stoplist[i]]

    return str(time)
       

   
#time_between_stops(build_tram_lines(lines)[0],build_tram_lines(lines)[1], 11,  "Centralstationen", "Majvallen")
def distance_between_stops(stopdict, stop1, stop2):
    location_1 = (float(stopdict[stop1]["lat"]),float(stopdict[stop1]["lon"]))
    location_2 = (float(stopdict[stop2]["lat"]),float(stopdict[stop2]["lon"]))
    
    return haversine(location_1, location_2)

#print(distance_between_stops(build_tram_stops(data), "Centralstationen", "Ullevi Norra"))


def dialogue(tramfile):
    pass