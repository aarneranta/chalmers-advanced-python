# 1

"""
1.5 points per question. The total sum is rounded upwards: 7.5 gives 8

'madam'.reverse()
AttributeError: : 'str' object has no attribute 'reverse'
TypeError also accepted
value None is not accepted

list(range(1, 10, 2))
[1, 3, 5, 7, 9]

{{n} for n in range(5)}
TypeError: unhashable type: 'set'

{n: {n} for n in range(5)}
{0: {0}, 1: {1}, 2: {2}, 3: {3}, 4: {4}}

len({print(n) for n in range(5)})
1
If the solution shows the printing, it is OK, but it must be clear that 1 is the value.

{1, 2, 1} != {1, 2}
False

[] is []
False

{} == set()
False
"""


# 2

e = lambda xs, ys: set(xs + ys)
# it is not necessary to include "e = ": the lambda expression itself is enough

# 3

countries = {
   'Afghanistan': {'capital': 'Kabul', 'area': 652230, 'population': 36643815, 'continent': 'Asia', 'currency': 'afghani'}, 
   'Albania': {'capital': 'Tirana', 'area': 28748, 'population': 3020209, 'continent': 'Europe', 'currency': 'lek'},
   'Algeria': {'capital': 'Algiers', 'area': 2381741, 'population': 41318142, 'continent': 'Africa', 'currency': 'dinar'}
  }

q3a = {c for c in countries if countries[c]['continent'] != 'Europe'}


q3b = len({c for c in countries if countries[c]['continent'] != 'Europe' and countries[c]['currency'] == 'euro'})
# also OK to use the first expression as a part
q3b2 = len({c for c in q3a if countries[c]['currency'] == 'euro'})
# in both cases, it is also OK to use lists rather than sets, because dict keys are unique

# 4

adj_g = {
    1: {2, 3, 4, 5},
    2: {1, 6},
    3: {1, 6},
    4: {1, 6},
    5: {1, 6},
    6: {2, 3, 4, 5}
    }
# it is OK for the values to be lists

# 5
# the example is from https://realpython.com/python-super/#an-overview-of-pythons-super-function
# 3p for the class definition, 3p in total for the use examples
    
# the class Rectangle was given
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# the class Square is to be defined
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        
        # also Rectangle.__init__(self, side, side) is OK
        # and so is explicitly defining length and width as side,
        # because __init__() has to be overwritten
# The important thing is that area() and perimeter() are not redefined but inherited


R = Rectangle(3, 2)

R.area()

S = Square(4)

S.area()



# bonus colouring

# order: 7, 3, 4, 5, 1, 6
# many other orders are also valid, as long as the removed vertices always have less than 3 edges

# colours: 6 R, 1 R, 5 B, 4 B, 3 B, 2 B
# in fact two colours are enough, but the simplify-select algorithm cannot get started with 2



# bonus clustering

# for each key, remove k-1 edges with the longest distances
# k=2: remove Chalmers-Korsvägen
# k=3: also remove Stenpiren-Brunnsparken
# k=4: also remove Järntorget-Hagakyrkan




