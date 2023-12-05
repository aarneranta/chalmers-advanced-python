# Question 1: Analysing treebank files and computing simple statistics
PATH = "en_pud-ud-test.conllu"

# read a file and return a list of non-empty paragraphs
def paragraphs(file):
    pass

# convert a paragraph into a structure that represents the words of a sentence
# hint: define a Token class or use a list of dicts like in yesterday's lecture
def sentence(para):
    pass

# return a structure that says how many times each part of speech occurs in the file
def posfreqs(sentences):
    pass


# Question 2: visualizing dependency graphs
# convert a sentence to an image that pops up when the function is called
from graphviz import Digraph

def visualize(sentence):
    pass

# Question 3: a main function
import random

if __name__ == "__main__":