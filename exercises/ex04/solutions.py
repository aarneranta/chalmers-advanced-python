import sys
import graphviz as gv
sys.path.append("../../examples/")
from trees import *

# Question 1 #################################################################
class Account:
        # an account has a number and a balance
        def __init__(self, number, balance=0):
            self._number = number
            self._balance = balance

        def get_number(self):
            return self._number

        def get_balance(self):
            # return the actual balance
            return self._balance

        def set_balance(self, b):
            # change the balance to b
            self._balance = b
    
def transfer(account1,account2,amount):
    balance1 = account1.get_balance()
    if balance1 >= amount:
        # transfer
        account1.set_balance(balance1 - amount)
        account2.set_balance(account2.get_balance() + amount)
        print("OK")
    else:
        print("not enough money")
    


# Questions 2-3 ##############################################################

class RecTree:

    def __init__(self, r, ts):
        self._root = r
        self._subtrees = ts

    def parts(self):
        return self._root, self._subtrees

    def edges(self):
        pass

    def to_tree(self):
        pass

    def to_valtree(self):
        pass

def atom(l):
    pass 

extree1 = RecTree(
    1, 
    [RecTree(11, [atom(111), atom(112)]), atom(12)]
    )

extree2 = RecTree('+', [atom('2'), atom('2')])

# Question 4 #################################################################
class Fun():
    pass

##############################################################################

# for free
if __name__ == '__main__': 
    visualize(extree1.to_tree())
    #visualize_valtree(extree2.to_valtree())

    # TODO: convert to test
    #f = Fun(lambda x: x+1)
    #g = Fun(lambda x: 3*x)
    #print(9, f(8))
    #print(24, g(8))
    #print(27, (g*f)(8)) #
    #print(30, (g*f*f)(8)) #
    #print(81, (g*g*f)(8)) #
    #print(28, (f*g*f)(8))

