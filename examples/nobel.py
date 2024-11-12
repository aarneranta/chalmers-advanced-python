import json

# query: https://w.wiki/3tEM

NOBEL_FILE = 'nobel.json'

with open(NOBEL_FILE) as file:
    nobel = json.load(file)


# print(json.dumps(nobel, indent=2, ensure_ascii=False))

print('number of laureates:', len(nobel))

print('number of unique persons:', len({n['person'] for n in nobel}))

print('number of women:', len([n for n in nobel if n['sexLabel'] == 'female']))

categories = {n['awardLabel'] for n in nobel}
print(categories)

winners_by_category = {c: [n for n in nobel if n['awardLabel'] == c] for c in categories}

women_by_category = {
    cat: len([w['personLabel'] for w in winners if w['sexLabel'] == 'female'])
        for cat, winners in winners_by_category.items()
  }

print(women_by_category)

def winner_age(winner):
    date = int(winner['date'][:4])
    birth = int(winner['birthDate'][:4])
    return date-birth


age_statistics = {
    age: len([n for n in nobel if winner_age(n) == age])
    for age in range(10, 120)}

print(age_statistics)

# example of list item showing the structure

alice_munro = {
    "person": "http://www.wikidata.org/entity/Q234819",
    "personLabel": "Alice Munro",
    "sexLabel": "female",
    "award": "http://www.wikidata.org/entity/Q37922",
    "awardLabel": "Nobel Prize in Literature",
    "date": "2013-01-01T00:00:00Z",
    "birthDate": "1931-07-10T00:00:00Z",
    "birthPlace": "http://www.wikidata.org/entity/Q4249510",
    "birthPlaceLabel": "Wingham",
    "country": "http://www.wikidata.org/entity/Q16",
    "countryLabel": "Canada",
    "deathDate": "2024-05-13T00:00:00Z"
  }


