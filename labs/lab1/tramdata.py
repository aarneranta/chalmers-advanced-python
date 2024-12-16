import sys
import json
from haversine import haversine
from pprint import pprint




STOP_FILE = './data/tramstops.json'

LINE_FILE = './data/tramlines.txt'

TRAM_FILE = './tramnetwork.json'

def build_tram_stops(jsonobject):
    with open(STOP_FILE, 'r') as fromFile:
        jsonobject = json.load(fromFile)
    

    stopdict = {x: {"lat":jsonobject[x]['position'][0], "lon":jsonobject[x]['position'][1]} for x in jsonobject}

    return stopdict

def build_tram_lines(lines):
    with open (LINE_FILE, "r", encoding= "UTF-8") as file:
        lines = file.read().replace(":","").strip().split("\n\n")
        lines = [line.split("\n") for line in lines]

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

    with open("./tramnetwork.json", "w") as file:
        json.dump(outdict, file)


def lines_via_stop(linedict, stop):

    return [key for key in linedict if stop in linedict[key]]

def lines_between_stops(linedict, stop1, stop2):
    
    return [key for key in linedict if stop1 in linedict[key] and stop2 in linedict[key]]

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

    return time

def distance_between_stops(stopdict, stop1, stop2):
     
    loc_1 = (float(stopdict[stop1]["lat"]),float(stopdict[stop1]["lon"]))
    loc_2 = (float(stopdict[stop2]["lat"]),float(stopdict[stop2]["lon"]))
    
    return haversine(loc_1, loc_2)

def answer_query(tramdict, query):

    query = query.lower().title().split()

    if query[0] == "Via":
        stop = " ".join(query[query.index("Via") + 1:])
        return lines_via_stop(tramdict["lines"], stop)
        
    if query[0] == "Between":
        stop1 = " ".join(query[query.index("Between") + 1: query.index("And")])
        stop2 = " ".join(query[query.index("And") + 1:])

        return lines_between_stops(tramdict["lines"], stop1, stop2) 
    
    if query[0] == "Time":
        line = query[2]
        stop1 = stop1 = " ".join(query[query.index("From") + 1: query.index("To")])
        stop2 = " ".join(query[query.index("To") + 1:])
        return time_between_stops(tramdict["lines"], tramdict["times"], int(line), stop1, stop2)
        
    if query[0] == "Distance":

        stop1 = " ".join(query[query.index("From") + 1: query.index("To")])
        stop2 = " ".join(query[query.index("To") + 1:])
        return distance_between_stops(tramdict["stops"], stop1, stop2)

    return query

def dialogue(tramfile=TRAM_FILE):
   
    with open(tramfile, "r") as file:
        tramdict = json.load(file)

    while True:
        try:
            print("Choose option:\n via <stop>\n between <stop1> and <top2\n time with <line> from <stop1> to <top2>\n distance from <stop1> to <top2>\n quit")
            query = input("")
            

            answer = answer_query(tramdict, query)
            if answer[0] == "Quit":
                break

            if answer:
                print(answer)
            else: 
                print("unknown arguments")   
        except:
            print("sorry, try that again")

if __name__ == '__main__':
    if sys.argv[1:] == ['init']:
        build_tram_network(STOP_FILE,LINE_FILE)
    else:
        dialogue()
