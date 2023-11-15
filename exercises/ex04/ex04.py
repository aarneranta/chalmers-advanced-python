## Question 1: defining classes

class Account:
    # an account has a number and a balance

    def get_balance(self):
        # return the actual balance
        pass

    def set_balance(self, b):
        # change the balance to b
        pass

def transfer(account1,account2,amount):
    # transfer amount from account1 to account2
    # report "OK" if successful, i.e. account1 has the required amount
    # "not enough money" otherwise
    pass

## Question 2 and 3: trees
import sys
sys.path.append("../../examples")
from trees import *

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

def atom(a):
    pass

import graphviz

def visualize_vals(graph):
    pass

## Question 4: function composition
