# Question 1

class Account:
    # an account has a number and a balance
    def __init__(self, n, balance):
        self._n = n
        self._balance = balance 
    
    def get_balance(self):
        # return the actual balance
        return self._balance

    def get_number(self):
        # return the actual number
        return self._n

    def set_balance(self, b):
        # change the balance to b
        self._balance = b
    
def transfer(account1,account2,amount):
    # transfer amount from account1 to account2
    # report "OK" if successful, i.e. account1 has the required amount
    # "not enough money" otherwise
    a1_balance = account1.get_balance()
    a2_balance = account2.get_balance()
    if a1_balance >= amount:
        account1.set_balance(a1_balance - amount)
        account2.set_balance(a2_balance + amount)
        print("OK")
    else:
        print("not enough money")

# Question 2

import sys
sys.path.append("../../examples")
from trees import *

class RecTree:
    def __init__(self, r, ts):
        self._root = r
        self._subtrees = ts

    def parts(self):
        return (self._root, self._subtrees)
    
    # a list of edges from which a Graph can be constructed  
    def edges(self):
        (r, ts) = self.parts()
        es = [(r, t._root) for t in ts]
        for t in ts:
            es += t.edges()
        return es

    # conversion to the Tree class of Lecture 6
    def to_tree(self):
        t = Tree(self._root)
        for (src, trg) in self.edges():
            t.add_edge(src, trg)
        return t

    # conversion to the ValTree class of Lecture 6
    def to_valtree(self):
        # not shown entirely during exercise class
        # TODO: explain "live" during ex05
        numbering = "1"
        vt = ValueTree(int(numbering))
        vt.set_value(int(numbering), self._root)

        def to_valtree_h(ts, vt, numbering):
            for (i,t) in enumerate(ts):
                new_numbering = numbering + str(i + 1)
                vt.add_edge(int(numbering), int(new_numbering))
                vt.set_value(int(new_numbering), t._root)
                to_valtree_h(t._subtrees, vt, new_numbering)

        to_valtree_h(self._subtrees, vt, numbering)
        return vt    

# a helper function to construct atomic trees
def atom(r):
    return RecTree(r, [])

import graphviz

def visualize_vals(graph):
    "Visualize undirected graphs with the dot method of Graphviz."
    dot = graphviz.Graph(engine='dot')
    for v in graph.vertices():
        dot.node(str(v), label=str(graph.get_value(v)))
    for (a,b) in graph.edges():
        dot.edge(str(a),str(b))
    dot.render('mygraph.gv', view=True)

# Question 4 (advanced exercise, not shown in class - 
# happy to explain the code to those interested)
class Fun():
    def __init__(self,fun):
        self._fun = fun

    def __mul__(self, other):
        return Fun(lambda x: self._fun(other(x)))

    def __call__(self, *args, **kwargs):
        return self._fun(args[0])

if __name__ == '__main__':
    # for Q2-3
    extree = RecTree(1, [RecTree(11, [atom(111), atom(112)]), atom(12)])
    print(extree.parts()) 
    visualize(extree.to_tree())

    syntree = RecTree('+', [atom('2'), atom('2')]) 
    visualize_vals(syntree.to_valtree())

    # for Q4
    # f = Fun(lambda x: x+1)
    # g = Fun(lambda x: 3*x)
    # print(9, f(8))
    # print(24, g(8))
    # print(27, (g*f)(8)) #
    # print(30, (g*f*f)(8)) #
    # print(81, (g*g*f)(8)) #
    # print(28, (f*g*f)(8))