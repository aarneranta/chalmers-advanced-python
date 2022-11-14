# Question 1

import os # https://docs.python.org/3/library/os.html

# useful functions:
# - os.listdir()
# - os.path.isdir() and os.path.isfile()
# - os.path.join()
# - bonus: os.path.basename()


def dir2dict(path='.'):
    pass 

# Question 2

adj_list = {0: [1, 2], 1: [0, 2], 2: [1, 0, 3], 3: [2]}

''' MATRIX REPRESENTATION OF A GRAPH
      0 1 2 3
    0   * *
    1 *   *
    2 * *   *
    3     *
'''

def adjacency2matrix(adj):
    pass

def matrix2adjacency(matrix):
    pass

# Question 3

def equal(e1,e2):
    pass

# Question 4

''' PSEUDOCODE FROM WIKIPEDIA
    procedure DFS(G, v) is
        label v as discovered
        for all directed edges from v to w that are in G.adjacentEdges(v) do
            if vertex w is not labeled as discovered then
                recursively call DFS(G, w)
'''

def dfs(g, v, discovered=[]):
    pass

# Question 5 