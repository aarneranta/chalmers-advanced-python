import os # https://docs.python.org/3/library/os.html

## Question 1: directory structure
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
    
## Question 2: graph representations
adj_list = {
    0: [1, 3, 2], 
    1: [0, 2], 
    2: [1, 0, 3], 3: [2]}

def adj2mat(adj):
    n = len(adj.items())
    mat = []
    for _ in range(n):
        mat.append([False] * n)
    for (key, vals) in adj.items():
        for val in vals:
            mat[key][val] = True
    return mat

# bonus: write a func that checks that the resulting mat is n*n

def mat2adj(mat, vertices):
    adj = {}
    for key in vertices:
        row = mat[key]
        for val in range(len(row)):
            if mat[key][val]:
                if key in adj:
                    adj[key].append(val)
                else: 
                    adj[key] = [val]
    return adj

## Question 3: equality between graphs


def equal(edges1, edges2):

    def included(edges1, edges2):
        for (src,trg) in edges1:
            if (not (src,trg) in edges2) and (not (trg,src) in edges2):
                return False 
        return True

    if len(edges1) != len(edges2):
        return False
    if included(edges1, edges2) and included(edges2, edges1):
        return True
    return False
    

## Question 4: depth-first search
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

''' PSEUDOCODE FROM WIKIPEDIA
    procedure DFS(G, v) is
        label v as discovered
        for all directed edges from v to w that are in G.adjacentEdges(v) do
            if key w is not labeled as discovered then
                recursively call DFS(G, w)
'''

def dfs(graph, current_node, visit_complete=[]):
    print(current_node)
    visit_complete.append(current_node)
    for neighbour in graph[current_node]:
        if not neighbour in visit_complete:
            dfs(graph, neighbour, visit_complete)

# bonus: implement dfs iteratively

## Question 5: multigraphs
multi_edgelist = [(0, 2), (1, 2), (2, 1)]

def edges2adj(edges):
    adj = {}
    for (src,trg) in edges:
        if src in adj:
            adj[src].append(trg)
        else:
            adj[src] = [trg]
    return adj

def multi_adj2mat(adj):
    n = len(adj.items())
    mat = []
    for _ in range(n):
        mat.append([0] * n)
    print(mat)
    for key in range(len(adj)):
        vals = adj[key]
        for val in range(len(vals)):
            mat[key][val] += 1 
    return mat