# Question 1

import os # https://docs.python.org/3/library/os.html

# useful functions:
# - os.listdir()
# - os.path.isdir() and os.path.isfile()
# - os.path.join()
# - bonus: os.path.basename()


def dir2dict(path='.'):
    if os.path.isfile(path):
        return os.path.basename(path)
    else: # dir
        d = {}
        d[os.path.basename(path)] = []
        for sub in os.listdir(path):
            if os.path.isfile(sub):
                d[os.path.basename(path)].append(sub)
            else: 
                d[os.path.basename(path)].append(dir2dict(os.path.join(path, sub)))
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
    # init
    table = []
    n = len(adj)
    for _ in range(n):
        table.append([False] * n)
    # update
    for (src, trgs) in adj.items():
        for trg in trgs:
            table[src][trg] = True
    return table
            

def matrix2adjacency(matrix):
    adj = {}
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]:
                if i in adj:
                    adj[i].append(j) 
                else: 
                    adj[i] = [j]
    return adj


# Question 3

def equal(e1,e2):
    def sort_graph(es):
        return sorted([sorted(e) for e in es])
    return sort_graph(e1) == sort_graph(e2)

# Question 4

''' PSEUDOCODE FROM WIKIPEDIA
    procedure DFS(G, v) is
        label v as discovered
        for all directed edges from v to w that are in G.adjacentEdges(v) do
            if vertex w is not labeled as discovered then
                recursively call DFS(G, w)
'''

adj_list = {0: [1, 2], 1: [0, 2], 2: [1, 0, 3], 3: [2]}

def dfs(g, v, discovered=[]):
    print(v)
    discovered.append(v)
    for w in g[v]:
        if w not in discovered:
            dfs(g, w, discovered)

def bfs(graph, current_node, visit_complete=[]):
    visit_complete.append(current_node)
    queue = []
    queue.append(current_node)
 
    while queue:
        s = queue.pop(0)
        print(s)
 
        for neighbour in graph[s]:
            if neighbour not in visit_complete:
                visit_complete.append(neighbour)
                queue.append(neighbour)

# Question 5 

multi_adj_list = {0: [1, 1, 2], 1: [0, 0, 2], 2: [1, 0, 3], 3: [2]}

''' MATRIX REPRESENTATION OF A GRAPH
      0 1 2 3
    0 0 2 1 0
    1 2 0 1 0
    2 1 1 0 1
    3 0 0 1 0
'''

def multi_adjacency2matrix(adj):
    # init
    table = []
    n = len(adj)
    for _ in range(n):
        table.append([0] * n)
    # update
    for (src, trgs) in adj.items():
        for trg in trgs:
            table[src][trg] += 1
    return table

    # bonus: implement multi_matrix2adjacency