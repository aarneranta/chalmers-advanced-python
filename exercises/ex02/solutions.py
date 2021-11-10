import json
import csv

# Question 1 #################################################################

FILE = "countries.tsv"

def convert_value(s):
    if s.isdigit():
        return int(s)
    return s

# alternative solution with try/except
def convert_value_alt(v):
    try:
        n = int(v)
    except ValueError:
        return v
    return n

def parse_tsv(FILE):
    with open(FILE) as f:
        return [line.replace("\n", "").split("\t") for line in f.readlines()]

# TODO: alternative solution based on Ulf's comment in the chat:

def tsv2list(FILE):
    dicts = []
    tsv_lines = parse_tsv(FILE)
    names = tsv_lines[0]
    for line in tsv_lines[1:]:
        dict = {}
        for (i,name) in enumerate(names):
            dict[name] = convert_value(line[i])
        dicts.append(dict)
    return dicts

# Question 2 (implemented separaterly for clarity) ###########################

def tsv2dict(FILE, key=None):
    tsv_lines = parse_tsv(FILE)
    names = tsv_lines[0]
    if not key: # as before
        dicts = []
        for line in tsv_lines[1:]:
            dict = {}
            for (i,name) in enumerate(names):
                dict[name] = convert_value(line[i])
            dicts.append(dict)
        return dicts
    elif key in names:
        ki = names.index(key)
        dict = {}
        for line in tsv_lines[1:]:
            if line[ki] in dict:
                print("non-unique key")
                return
            dict[line[ki]] = {}
            for (i,name) in enumerate(names):
                if i != ki:
                    dict[line[ki]][name] = convert_value(line[i])
        return dict
    else:
        print("invalid key")
        return

# Question 3 (freely inspired to, this is what we did in class) ##############

def data2json(data, FILE):
    with open(FILE, 'w') as f:
        json.dump(data, f)

def json2data(FILE):
    with open(FILE, 'r') as f:
        return json.load(f)

def test_json_rw(data):
    path = "countries.json"
    data2json(data, path) # writes json file
    new_data = json2data(path)
    # when implementing tests for the lab, you might prefer to use assert
    return data == new_data 

# Question 3 (a solution that better matches the specifications) #############
def test_json_data(part_path, key=None):
    d1 = tsv2dict(part_path + ".tsv",key)
    data2json(d1, part_path + ".json")
    with open(part_path + ".json") as f:
        d2 = json.load(f)
    return d1 == d2

# Question 4 #################################################################
# to be done next time

# Question 5 (partial solution, the complete one will be provided next time) #

def n_countries(d):
    return len(d)

def most_common_curr(d):
    currdict = {}
    for inner_d in d.values():
        if inner_d["currency"] in currdict:
            currdict[inner_d["currency"]] += 1
        else: 
            currdict[inner_d["currency"]] = 1
    currlist = sorted([(count,name) for (name,count) in currdict.items()])
    return currlist[-1]

def query_test():
    d = tsv2dict('countries.tsv', key='country')
    print("How many countries are there?")
    print(n_countries(d))
    print("What is the most common name of a currency?")
    print(most_common_curr(d))

# Question 6 #################################################################
# to be done next time