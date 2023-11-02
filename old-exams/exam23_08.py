import math


# Q1

# solved by evaluating each expression and its type() in the Python shell


# Q2

# to add:

e = lambda x, f: f(f(x))

# to test:
if __name__ == '__main__':
    print(e(42, print))
    print(e(42, lambda x: x + x))
    print(e(16, math.sqrt))

    print(e('abc', list))
    print(e(7, lambda x: x + 2))



# Q3

# given:

numbers = {
    1: {'sv': 'ett', 'en': 'one'},
    10: {'sv': 'tio'},
    42: {'sv': 'fyrtiotvå', 'en': 'forty-two'},
    3: {'sv': 'tre', 'en': 'three'},
    6: {'sv': 'sex', 'en': 'six'},
    20: {'sv': 'tjugo', 'en': 'twenty'},
    7: {'sv': 'sju'}
    }


# to add:

q3a = [numbers[n]['sv'] for n in range(1, 21)
       if n in numbers and 'sv' in numbers[n] and 'en' not in numbers[n]]

q3b = sorted([n for n in numbers
       if 'sv' in numbers[n] and 'en' in numbers[n]
         and len(numbers[n]['sv']) == len(numbers[n]['en'])])

# to test:
if __name__ == '__main__':
    print(q3a)
    print(q3b)


# Q4

# given:

class Expr:
    pass

class Stm:
    pass


class AddExpr(Expr):
    def __init__(self, a, b):
        self.expr1 = a
        self.expr2 = b

    def show(self):
        return self.expr1.show() + ' + ' + self.expr2.show()


class IntExpr(Expr):
    def __init__(self, n):
        self.expr = str(n)

    def show(self):
        return self.expr


# to add:

class AssignStm(Stm):
    def __init__(self, var, val):
        self.var = var
        self.expr = val

    def show(self):
        return self.var + ' = ' + self.expr.show()
        
class VarExpr(Expr):
    def __init__(self, x):
        self.expr = x

    def show(self):
        return self.expr


class MulExpr(Expr):
    def __init__(self, a, b):
        self.expr1 = a
        self.expr2 = b

    def show(self):
        return self.expr1.show() + ' * ' + self.expr2.show()

    

# to test:

ex1 = AssignStm('x', AddExpr(MulExpr(IntExpr(5), VarExpr('x')), IntExpr(3)))

if __name__ == '__main__':
    print(ex1.show())

    
# Extra colouring

"""
two colours are enough

simplify: 9, 8, 7, 6, 5, 4, 3, 2, 1
select: 1 red, 2 blue, 3 blue, 4 blue, 5 red, 6 red, 7 red, 8 red, 9 red

"""

# Extra clustering

"""
k=2: remove (4, 9)
k=3: also remove (2, 7)
k=4: also remove (1, 2)
"""
