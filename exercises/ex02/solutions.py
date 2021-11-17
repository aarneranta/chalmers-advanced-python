import json
import csv
import os

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
def data2txt(data): # data in tsv2list format
    names = data[0].keys() # get column names
    # build a dictionary with column names as keys, lengths as values
    lendict = {}
    for name in names:
        lendict[name] = max([len(str(d[name])) for d in data])
    for d in data:
        string = ""
        for name in names:
            chars = str(d[name])
            spaces = (2 + (lendict[name] - len(chars))) * " "
            string += chars + spaces
        print(string)

# Question 5 #################################################################

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

def least_diff_in_pop(d):
    pop_name_list = sorted(
        [(d['population'],name) for (name, d) in d.items()])
    c1 = pop_name_list[0][1]
    c2 = pop_name_list[1][1]
    min_diff = pop_name_list[1][0] - pop_name_list[0][0]
    for (i, (pop, name)) in enumerate(pop_name_list[:-1]):
        (next_pop, next_name) = pop_name_list[i + 1]
        diff = next_pop - pop  
        if diff < min_diff:
            min_diff = diff
            c1 = name
            c2 = next_name
    return c1, c2

def countries_by_density(d):
    return sorted(
        [(d['population'] / d['area'] ,name) for (name, d) in d.items()], 
        reverse=True)

def query_test():
    d = tsv2dict('countries.tsv', key='country')
    print("How many countries are there?")
    print(n_countries(d))
    print("What is the most common name of a currency?")
    print(most_common_curr(d))
    print("Which two countries have the smallest difference in population?")
    print(least_diff_in_pop(d))
    print("List the 20 countries with the highest population density" 
    + " population divided by area), together with the densities, in a " 
    + "descending order of density.")
    print(countries_by_density(d)[:20])

# Question 6 #################################################################
def dir2dict(path='.'):
    if os.path.isfile(path):
        return None
    else: # os.path.isdir(path)
        d = {}
        d[os.path.basename(path)] = {}
        for el in os.listdir(path):
            d[os.path.basename(path)][el] = dir2dict(os.path.join(path,el))
            print(d)
        return d
