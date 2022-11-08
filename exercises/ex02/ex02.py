# Question 1

import csv # https://docs.python.org/3/library/csv.html

def convert_value(file):
    pass

def tsv2list(file):
    pass

# Question 2

def tsv2dict(file, key=None):
    pass

# Question 3

import json # https://docs.python.org/3/library/json.html

def data2json(data, file):
    with open(file, 'w') as f:
        json.dump(data, f)

def json2data(file):
    pass

def test_json_data(file, key=None):
    pass

# Question 4

def data2txt(data):
    pass

# Question 5

def n_countries(data):
    pass

def most_common_currency(data):
    pass

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