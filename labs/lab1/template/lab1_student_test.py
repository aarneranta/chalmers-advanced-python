# DO NOT MODIFY THIS FILE

# TEST lab 1

import os.path
import sys
import json
from haversine import haversine


try:
    assert os.path.exists('tramdata.py')
    assert os.path.exists('tramnetwork.json')
except:
    print('You need to submit both tramdata.py and tramnetwork.json')



with open('tramnetwork.json') as file:
    tramdict = json.load(file)

from tramdata import answer_query

outcome = True

answers = {'via Jaegerdorffsplatsen': ['3', '9'],
           'via Aprilgatan': ['6'], 
           'via Scandinavium': ['2', '6', '8', '13'], 
           'via Botaniska Trädgården': ['1', '2', '7', '8', '13'], 
           'via Chalmers': ['6', '7', '8', '10', '13'], 
           'between Temperaturgatan and Sahlgrenska Huvudentré': ['6'], 
           'between Domkyrkan and Scandinavium': ['2', '6'],
           'between Bellevue and Positivgatan': ['7'], 
           'between Saltholmen and Medicinaregatan': ['13'], 
           'between Medicinaregatan and Saltholmen': ['13'], 
           'time with 3 from Hagakyrkan to Mariaplan': 16, 
           'time with 3 from Mariaplan to Hagakyrkan': 16,
           'time with 5 from Munkebäckstorget to Sankt Sigfrids Plan': 9, 
           'time with 7 from Allhelgonakyrkan to Komettorget': 6, 
           'time with 10 from Wavrinskys Plats to Hjalmar Brantingsplatsen': 15, 
           'time with 13 from Scandinavium to Korsvägen': 1, 
           'distance from Jaegerdorffsplatsen to Tranered': 3.003, 
           'distance from Sahlgrenska Huvudentré to Kortedala Torg': 8.781, 
           'distance from Temperaturgatan to Lackarebäck': 10.092, 
           'distance from Rymdtorget Spårvagn to Hagakyrkan': 8.841, 
           'distance from Vasaplatsen to Doktor Sydows Gata': 2.223}

for query, answer in answers.items():
    if type(answer) == float:
        try:
            assert round(answer_query(tramdict, query), 3) == answer
        except:
            print(f"Error in {query}, your result is {round(answer_query(tramdict, query), 3)}, but the expected is {answer}")
            outcome = False
    else:
        try:
            assert answer_query(tramdict, query) == answer
        except:
            print(f"Error in {query}, your result is {answer_query(tramdict, query)}, but the expected is {answer}")
            outcome = False

#-----------------------------
#final result
assert outcome == True
