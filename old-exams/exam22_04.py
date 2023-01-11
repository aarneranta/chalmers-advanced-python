# 1

"""
'python'.append('3')
AttributeError

['p', 'y', 't', 'h', 'o', 'n'].append(3)
None

['p', 'y', 't', 'h', 'o', 'n'] + [3]
['p', 'y', 't', 'h', 'o', 'n', 3]

{c: c.upper() for c in 'typhoon'}
{'t': 'T', 'y': 'Y', 'p': 'P', 'h': 'H', 'o': 'O', 'n': 'N'}

['x' for x in 'python']
['x', 'x', 'x', 'x', 'x', 'x']

lambda x, y: x//y
<function>

[(lambda x: 10/x)(x) for x in range(5)]
ZeroDivisionError

'pdf2html'.split(2)
TypeError: must be str or None, not int

2 > 3 or 'False'
'False'
"""


# 2

def alpha_sort(strings):
    return sorted(strings, key=lambda s: s.lower())


# 3

f = lambda x, y, s: s[x:][:-y]


# 4

countries = {
   'Afghanistan': {'capital': 'Kabul', 'area': 652230, 'population': 36643815, 'continent': 'Asia', 'currency': 'afghani'}, 
   'Albania': {'capital': 'Tirana', 'area': 28748, 'population': 3020209, 'continent': 'Europe', 'currency': 'lek'},
   'Algeria': {'capital': 'Algiers', 'area': 2381741, 'population': 41318142, 'continent': 'Africa', 'currency': 'dinar'}
  }

q4a = len({countries[c]['currency'] for c in countries if countries[c]['continent'] == 'Europe'})


q4b = {curr: [c for c in countries if countries[c]['currency'] == curr]
           for curr in {countries[c]['currency'] for c in countries}}


# 5

adj_g = {
    1: {2, 3, 4},
    2: {1, 4},
    3: {1, 4, 5, 6, 7},
    4: {1, 2, 3, 5},
    5: {3, 4},
    6: {3, 7},
    7: {3, 6}
    }

# 6

class Vehicle:
    def __init__(self, brand):
        self._brand = brand

    def get_brand(self):
        return self._brand

    def __str__(self):
        return 'brand: ' + self._brand


class Car(Vehicle):
    def __init__(self, brand, acceleration):
        Vehicle.__init__(self, brand)
        self._acceleration = acceleration

    def __str__(self):
        return super().__str__() + ', acceleration:' + str(self._acceleration)

class Electric(Vehicle):
    def __init__(self, brand, range):
        Vehicle.__init__(self, brand)
        self._range = range

    def __str__(self):
        return super().__str__() + ', range:' + str(self._range)


class ElectricCar(Car, Electric):
    def __init__(self, brand, acceleration, range):
        super().__init__(brand, acceleration)
        self._range = range



# bonus colouring

# order: 7, 6, 5, 3, 4, 2, 1

# colours: 1 R, 2 B, 4 Y, 3 B, 5 R, 6 R, 7 Y



# bonus clustering

# weights from above left to right: 1, 2, 3, 2, 3, 4

# k=2: remove 3-7
# k=3: also remove 3-6 or 1-4
# k=4: remove 3-6 or 1-4 depending on which one is left




