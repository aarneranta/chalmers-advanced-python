
# 1: paste each of these to Python shell to see the value
"""
'python'.reverse()
'python'[-1::-2]
[str(x) for x in range(3)]
{c: list(c) for c in 'typhoon'}
{'x' for x in range(120)}
1 > 2 and x > 1
[print(x) for x in range(3)]
2 * False
2 * 'False'
lambda x: range(x)
[x for x in range(3) if x < x**2 < x**3]
{{}}
"""



# 2

alphasort = lambda s: ''.join(sorted(s, key=lambda c: c.upper()))

print(alphasort('bAdC'))



# 3

# do the following if you want to test; the data is in ex02
import csv

COUNTRY_FILE = 'countries.tsv'

with open(COUNTRY_FILE) as file:
    creader = csv.reader(file, delimiter='\t')
    cdict = {}
    creader.__next__()
    for c in creader:
        cdict[c[0]] = {
            'capital': c[1],
            'area': float(c[2]),
            'population': int(c[3]),
            'continent': c[4],
            'currency': c[5]
            }

# and now the questions themselves:

# How many countries in Europe have a population over ten million?
q3a = len({c for c in cdict
               if (cdict[c]['continent'] == 'Europe' and
                   cdict[c]['population'])
               > 10000000
               })
# print(q3a)

# to each continent, the total population of its countries
q3b = {cont: sum([cdict[c]['population']
                      for c in cdict
                      if cdict[c]['continent'] == cont])
            for cont in {cdict[c]['continent'] for c in cdict}
           }
# print(q3b)


# 5

adjlist = {
    1: {2, 5, 3},
    2: {1, 4, 5},
    3: {1, 5},
    4: {2, 5},
    5: {2, 4, 1, 3}
    }

# 6

class Work:
    def __init__(self, title, author):
        self._title = title
        self._author = author


class Book(Work):
    def __init__(self, title, author, pages):
        Work.__init__(self, title, author)
        self._pages = pages


class Recording(Work):
    def __init__(self, title, author, duration):
        super().__init__(title, author)
        self._duration = duration
        

class Audiobook(Book, Recording):
    def __init__(self, title, author, pages, duration):
        Book.__init__(self, title, author, pages)
        self._duration = duration


if __name__ == '__main__':
    w = Work('Kniv', 'Jo Nesbø')
    b = Book('Kniv', 'Jo Nesbø', 758)
    r = Recording('Kniv', 'Jo Nesbø', 21.2)
    a = Audiobook('Kniv', 'Jo Nesbø', 758, 21.2)
    print(w._title)
    print(b._title)
    print(r._title)
    print(a._title)
#    print(w._pages)
    print(b._pages)
    print(r._duration)
    print(a._pages)
    print(a._duration)

    
# coloring:
    
# remove 3, 1, 2, 4, 5
# color 5r, 4b, 2g, 1b, 3g
        

# clustering:

# k=2: remove any of 7-4, 6-3, 4-1
# k=3: remove any two of these
# k=4: remove all of these 


                    
            
