# Question 1

import csv # https://docs.python.org/3/library/csv.html

def convert_value(s):
    try:
        converted = int(s)
    except ValueError:
        converted = s
    return converted

def tsv2list(file):
    with open(file) as tsv:
        dictlist = list(csv.DictReader(tsv, delimiter="\t"))
    for dict in dictlist:
        for (key,val) in dict.items():
            dict[key] = convert_value(val)
    return dictlist

# Question 2

def tsv2dict(file, key=None):
    dictlist = tsv2list(file)
    if not key:
        return dictlist
    else:
        if key not in dictlist[0].keys():
            print("invalid key")
            return None
        else:
            nested_dict = {}
            for dict in dictlist:
                keyval = dict.pop(key)
                if keyval in nested_dict:
                    print("non-unique key")
                    return None
                else:
                    nested_dict[keyval] = dict
    return nested_dict

# Question 3

import json # https://docs.python.org/3/library/json.html

def data2json(data, file):
    with open(file, 'w') as f:
        json.dump(data, f)

def json2data(file):
    with open(file) as f:
        return json.load(f)

def test_json_data(file, key=None):
    obj = tsv2dict(file, key)
    json_path = "countries.json"
    data2json(obj, json_path)
    return json2data(json_path) == obj


# Question 4

def data2txt(data):
    # bonus: add col names, make more efficient
    lengths_dict = {} 
    for key in data[0].keys():
        lengths_dict[key] = len(key)
    for dict in data:
        for (key,val) in dict.items():
            length = len(str(val))
            if length > lengths_dict[key]:
                lengths_dict[key] = length
    for dict in data:
        line = ""
        for (key,val) in dict.items():
            line += str(val) + (" " * (2 + (lengths_dict[key] - len(str(val)))))
        print(line)

# Question 5

def n_countries(data):
    return len(data)

def most_common_currency(data):
    curr_dict = {}
    for (_, dict) in data.items():
        if dict["currency"] not in curr_dict:
            curr_dict[dict["currency"]] = 1
        else:
            curr_dict[dict["currency"]] += 1
    currencies = [(val,key) for (key,val) in list(curr_dict.items())]
    currencies.sort(reverse=True)
    return currencies[0][1]


def least_population_difference(data):
    pass

def countries_by_density(data):
    pass

def query_test():
    d = tsv2dict('countries.tsv', key='country')
    print("How many countries are there?")
    print(n_countries(d))
    print("What is the most common name of a currency?")
    print(most_common_currency(d))
    print("Which two countries have the smallest difference in population?")
    print(least_population_difference(d))
    print("List the 20 countries with the highest population density" 
    + " population divided by area), together with the densities, in a " 
    + "descending order of density.")
    print(countries_by_density(d)[:20])