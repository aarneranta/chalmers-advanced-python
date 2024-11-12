import json 

TRAM_STOP_FILE = 'labs/data/tramstops.json'
with open(TRAM_STOP_FILE, 'r') as fromFile:
    data = json.load(fromFile)

#print(json.dumps(data, indent=2, ensure_ascii=False))

def build_tram_stops(jsonobject):

    stopdict = {x: {"lat":jsonobject[x]['position'][0], "lon":jsonobject[x]['position'][1]} for x in jsonobject}

    return stopdict

print(build_tram_stops(data))

def build_tram_lines(lines):
    pass

def build_tram_network(stopfile, linefile):
    pass

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