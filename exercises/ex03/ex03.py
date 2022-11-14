# Question 1

import os # https://docs.python.org/3/library/os.html

# useful functions:
# - os.listdir()
# - os.path.isdir() and os.path.isfile()
# - os.path.join()
# - bonus: os.path.basename()


def dir2dict(path='.'):
    d = {}
    d[path] = []
    for sub in os.listdir(path):
        joint = os.path.join(path, sub)
        if os.path.isfile(joint):
            d[path].append(sub)
        else:
            d[path].append(dir2dict(joint))
    return d 

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
    n = len(adj.keys())
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if j in adj[i]:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def matrix2adjacency(matrix):
    adj = {}
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                if not i in adj:
                    adj[i] = [j]
                else:
                    adj[i].append(j)
    return adj

# Question 3

def equal(e1,e2):
    return sorted([sorted(pair) for pair in e1]) == sorted([sorted(pair) for pair in e2])

# Question 4

''' PSEUDOCODE FROM WIKIPEDIA
    procedure DFS(G, v) is
        label v as discovered
        for all directed edges from v to w that are in G.adjacentEdges(v) do
            if vertex w is not labeled as discovered then
                recursively call DFS(G, w)
'''

def dfs(g, v, discovered=[]):
    discovered.append(v)
    print(v)
    for w in g[v]:
        if not w in discovered:
            dfs(g, w, discovered)

# Question 5