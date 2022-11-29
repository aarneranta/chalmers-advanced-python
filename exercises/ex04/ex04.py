# Question 1

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

# Question 2

import sys
sys.path.append("../../examples")
from trees import *

class RecTree:
    def __init__(self, r, ts):
        self._root = r
        self._subtrees = ts

    def parts(self):
        return self._root, self._subtrees
    
    # a list of edges from which a Graph can be constructed  
    def edges(self):
        pass

    # conversion to the Tree class of Lecture 6
    def to_tree(self):
        pass

    # conversion to the ValTree class of Lecture 6
    def to_valtree(self):
        pass

# a helper function to construct atomic trees
def atom(r):
    pass

# Question 4


if __name__ == '__main__':
    # for Q2-3
    extree = RecTree(1, [RecTree(11, [atom(111), atom(112)]), atom(12)]) 
    visualize(extree.to_tree())

    syntree = RecTree('+', [atom('2'), atom('2')]) 

    # for Q4
    # f = Fun(lambda x: x+1)
    # g = Fun(lambda x: 3*x)
    # print(9, f(8))
    # print(24, g(8))
    # print(27, (g*f)(8)) #
    # print(30, (g*f*f)(8)) #
    # print(81, (g*g*f)(8)) #
    # print(28, (f*g*f)(8))