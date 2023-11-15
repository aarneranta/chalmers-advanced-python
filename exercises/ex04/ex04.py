## Question 1: defining classes

class Account:
    # an account has a number and a balance
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

    def get_balance(self):
        # return the actual balance
        return self.balance

    def get_number(self):
        # return the actual balance
        return self.number

    def set_balance(self, b):
        # change the balance to b
        self.balance = b

    def transfer_to(self, account, amount):
        balance1 = self.get_balance()
        if amount > balance1:
            print("Not enough money")
        else:
            self.set_balance(balance1 - amount)
            account.set_balance(account.get_balance() + amount)
            print("OK")


def transfer(account1,account2,amount):
    # transfer amount from account1 to account2
    # report "OK" if successful, i.e. account1 has the required amount
    # "not enough money" otherwise
    balance1 = account1.get_balance()
    if amount > balance1:
        print("Not enough money")
    else:
        account1.set_balance(balance1 - amount)
        account2.set_balance(account2.get_balance() + amount)
        print("OK")


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
        (r, ts) = self.parts()
        es = [(r,t._root) for t in ts]
        for t in ts:
            es = es + t.edges()
        return es
    
    def to_tree(self):
        es = self.edges()
        t = Tree(self._root)
        for (a,b) in es:
            t.add_edge(a,b)
        return t

    # only partially shown in class
    def to_valtree(self):
        num = 1
        vt = ValueTree(num)
        vt.set_value(num, self._root)

        def to_valsubtrees(num, ts):
            for (i, t) in enumerate(ts):
                nnum = int(str(num) + str(i + 1))
                vt.add_edge(num, nnum)
                vt.set_value(nnum, t._root)
                to_valsubtrees(nnum, t._subtrees)

        to_valsubtrees(num, self._subtrees)
        return vt

def atom(a):
    return RecTree(a, [])

import graphviz

# solution from last year, not shown in class
def visualize_vals(graph):
    "Visualize undirected graphs with the dot method of Graphviz."
    dot = graphviz.Graph(engine='dot')
    for v in graph.vertices():
        dot.node(str(v), label=str(graph.get_value(v)))
    for (a,b) in graph.edges():
        dot.edge(str(a),str(b))
    dot.render('mygraph.gv', view=True)

## Question 4: function composition 
# (solution from last year, not shown in class)
class Fun():
    def __init__(self,fun):
        self._fun = fun

    def __mul__(self, other):
        return Fun(lambda x: self._fun(other(x)))

    def __call__(self, *args, **kwargs):
        return self._fun(args[0])