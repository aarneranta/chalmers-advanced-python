import csv

UD_FILE = "en_pud-ud-test.conllu"


# Question 1

def paragraphs(file):
    with open(file) as f:
        ss = f.read().split('\n\n')
    return [s for s in ss if s]


def sentence(s):
    lines = s.split('\n')
    tabs = csv.reader(lines, delimiter = '\t', quotechar = None)
    return [t for t in tabs if t[0].isdigit()]

# thus ignoring positions with dots
# but solutions that include them will be accepted as well (see assignment FAQ)


def posfreqs(sentences):
    freqs = {}
    for s in sentences:
        for w in s:
            pos = w[3].strip()
            freqs[pos] = freqs.get(pos, 0) + 1
    return freqs


# Question 2

import graphviz as gv

def visualize(s):
    G = gv.Digraph()
    for w in s:
        G.node(w[0], w[0] + ' ' + w[1])
    for w in s:
        G.edge(w[6], w[0], label=w[7])
    G.render('sgraph', view=True)


# Question 3
    
import random

if __name__ == '__main__':
    sts = paragraphs(UD_FILE)
    sentences = [sentence(s) for s in sts]
    
    print(len(sentences))
    
    freqs = posfreqs(sentences)
    for f in sorted(freqs.items(), key = lambda w: -w[1]):
        print(f[0], f[1])

    r = random.randrange(0, len(sentences))
    print(sentences[r])
    visualize(sentences[r])

# you can of course also gather this into a main() function


# Question 4

"""
remove 1
remove 2
remove 3
remove 5
remove 6
remove 4
remove 0
add 0 green
add 4 red
add 6 green
add 5 green
add 3 green
add 2 red
add 1 red

As for the general question: 2 colours are enough for any tree!
Start by colouring the top node green.
Then colour its children red, their children green, and so on.
Each node gets a colour different from its mother and its children.
The mother and the children are the only neighbours of each node.
"""

    
# Question 5

"""
# small tree:
# It turns out that edges with distance >= 2 are to be removed.
# We are then left with:

the
black cat sees us
now
0 

# large tree: 12 clusters

Its struggle
against
the Ottoman Empire
in
the Mediterranean See
put serious limits
0
on the military power
.
it could deploy
against the rebels
in the Netherlands
"""


"""
expected frequency table (when dot positions are not allowed)
NOUN 4040
ADP 2493
PUNCT 2451
VERB 2150   # with dot positions 2156
DET 2086
PROPN 1727
ADJ 1540
PRON 1021
AUX 1014
ADV 848  # with dot positions 849
CCONJ 576
NUM 455
PART 426
SCONJ 290
SYM 42
X 16
INTJ 1
"""

