from random import randint

# Question 1: Analysing treebank files and computing simple statistics
PATH = "en_pud-ud-test.conllu"

# read a file and return a list of non-empty paragraphs
def paragraphs(file):
    with open(file) as f:
        text = f.read()
    return [par for par in text.split("\n\n") if len(par) >=1]

FIELDS = {0: "id", 1 : "word", 3: "pos", 6: "head", 7: "rel"}

# convert a paragraph into a structure that represents the words of a sentence
# hint: define a Token class or use a list of dicts like in yesterday's lecture
def sentence(para):
    lines = para.split("\n")
    tokens = []
    for line in lines:
        if not line.startswith("#"):
            token_dict = {}
            for (i,info) in enumerate(line.split("\t")):
                if i in FIELDS.keys():
                    token_dict[FIELDS[i]] = info
            tokens.append(token_dict)
    return tokens

# return a structure that says how many times each part of speech occurs in the file
def posfreqs(sentences):
    freq_dict = {}
    for sentence in sentences:
        for token in sentence:
            pos = token["pos"]
            if pos not in freq_dict.keys():
                freq_dict[pos] = 1
            else:
                freq_dict[pos] += 1
    return freq_dict


# Question 2: visualizing dependency graphs
# convert a sentence to an image that pops up when the function is called
from graphviz import Digraph

def visualize(sentence):
    dot = Digraph(engine='dot')
    dot.node("0")
    for trg_tok in sentence:
        src = trg_tok["id"] + " " + trg_tok["word"]
        head_id = int(trg_tok["head"])
        src_tok = sentence[head_id - 1]
        trg = (src_tok["id"] + " " + src_tok["word"]) if head_id != 0 else "0"
        dot.node(src)
        dot.edge(trg, src, label=trg_tok["rel"])
    dot.render('mygraph.gv', view=True)

# Question 3: a main function
import random

if __name__ == "__main__":
    paras = paragraphs(PATH)
    n_sents = len(paras)
    print(n_sents)
    sentences = [sentence(para) for para in paras]
    freq_dict = posfreqs(sentences)
    sorted_pairs = sorted(freq_dict.items(), key=lambda keyval: keyval[1], reverse=True)
    for (key,val) in sorted_pairs:
        print(key, val)
    r = randint(0, n_sents)
    visualize(sentences[r])
