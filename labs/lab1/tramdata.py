import json 

TRAM_STOP_FILE = 'labs/data/tramstops.json'
with open(TRAM_STOP_FILE, 'r') as fromFile:
    data = json.load(fromFile)


with open ("labs/data/tramlines.txt", "r") as file:
    lines = file.read().replace(":","").strip().split("\n\n")

    lines = [line[:-4] for line in lines]



lines = [line.split("\n") for line in lines]

    


    
        
    
#print(tramlines)
def build_tram_stops(jsonobject):

    stopdict = {x: {"lat":jsonobject[x]['position'][0], "lon":jsonobject[x]['position'][1]} for x in jsonobject}

    return stopdict



def build_tram_lines(lines):

    linedict = {}

    for line in lines:
        key = line[0]
        values=[]
        line.pop(0)
        for x in line:
            values.append(x[:-4].strip())  
        linedict[key] = values
            
        
  
   
    
            
        
    return linedict


print(build_tram_lines(lines)["9"])


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