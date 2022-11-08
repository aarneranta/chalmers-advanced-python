import json
import csv
import statistics as st
import sys

COUNTRY_TSV_FILE = 'countries.tsv'
COUNTRY_JSON_FILE = 'countries.json'

# a special case of exercise Question 1
def get_data(file):
    with open(file) as file:
        rows = csv.reader(file, delimiter='\t')
        rows.__next__()
        data = {row[0]: dict(
                  capital = row[1],
                  area = float(row[2]),
                  population = int(row[3]),
                  continent = row[4],
                  currency = row[5]
                  )
                for row in rows
                }
    return data

def query_list(data):
    print("All continents")
    conts = [data[c]['continent']  for c in data]
    print(conts)
    
    print("All distinct continents")
    conts = {data[c]['continent']  for c in data}
    print(conts)
    
    print("How many continents?")
    lconts = len({data[c]['continent']  for c in data})
    print(lconts)

    print("Average area?")
    avarea = st.mean([data[c]['area'] for c in data])
    print(avarea)
    
    print("How many countries on each continent?")
    contcounts = {c: len({k for k in data if data[k]['continent'] == c}) for c in conts}
    print(contcounts)

    print("The currency of Sweden")
    swec = data['Sweden']['currency']
    print(swec)
    
    print("The currency of Denmark")
    swec = data['Denmark']['currency']
    print(swec)
    
    print("The currency of Norway")
    swec = data['Norway']['currency']
    print(swec)
    
    print("How many different currencies in Europe?")
    contcounts = len({data[c]['currency']
                      for c in data
                        if data[c]['continent'] == 'Europe'})
    print(contcounts)

    print("Countries for currencies")
    currencies = {data[c]['currency']  for c in data}
    swec = {cu: [c for c in data if data[c]['currency'] == cu] for cu in currencies}
    [print(s, swec[s]) for s in swec]

    
if __name__ == '__main__':
    if sys.argv[1:] == ['init']:
        data = get_data(COUNTRY_TSV_FILE)        
        with open(COUNTRY_JSON_FILE, 'w') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=4) 
    else:
        with open(COUNTRY_JSON_FILE, 'r') as infile:
            data = json.load(infile)
            query_list(data)

