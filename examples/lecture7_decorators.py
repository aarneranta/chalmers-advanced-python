# decorator examples

def do_twice(f):
    def wrap(*args):
        f(*args)
        f(*args)
    return wrap

@do_twice
def hello():
    print("hello")


hello()


def also_print(f):
    def wrap(*args):
        v = f(*args)
        print(v)
        return v
    return wrap

@ also_print
def average(xs):
    return sum(xs)/len(xs)

average(range(10))

import random

def call_with_random(n, k):
    def wrap(f):
        ns = random.choices(range(n), k=k)
        for i in ns:
            f(i)
    return wrap

@call_with_random(100, 5)
def prsq(n):
    print(n**2)

prsq

