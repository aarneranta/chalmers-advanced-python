edges = [(1,2), (2,0), (0,1), (2,3)]

# Copied from ex01 but also useful here ######################################
def edges2adjacency(edges):

    def add_edge(adj,src,dst):
        if not src in adj:
            adj[src] = [dst]
        else:
            adj[src].append(dst)

    adj = {}
    for (src,dst) in edges:
        add_edge(adj, src, dst)
        add_edge(adj, dst, src)
    
    return adj

def adjacency2edges(adj):
    edges = []
    for (src,dsts) in adj.items():
        for dst in dsts:
            if not (src,dst) in edges and not (dst,src) in edges: 
                edges.append((src,dst))
    return edges

# Question 1 #################################################################
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

# Question 2 #################################################################
def equal(edges1, edges2):
    set1 = set([frozenset(edge) for edge in edges1])
    set2 = set([frozenset(edge) for edge in edges2])
    return set1 == set2

# another approach can be checking that all elements of edges1, disregarding 
# the order of nodes of each edge, belong to edges2 and vice versa

# another approach can be sorting both the lists of edges and each pair of 
# nodes and see if the resulting lists are equal to each other

# Question 3 #################################################################
''' PSEUDOCODE FROM WIKIPEDIA
procedure DFS(G, v) is
    label v as discovered
    for all directed edges from v to w that are in G.adjacentEdges(v) do
        if vertex w is not labeled as discovered then
            recursively call DFS(G, w)
'''

def dfs(g, v, discovered=[]): # g as an adjacency list (dictionary)
    discovered.append(v)
    print(v)
    for w in g[v]:
        if not w in discovered:
            dfs(g, w, discovered)

# Question 4 #################################################################
# a multigraph can be represented as a weighted graph, using an int to 
# represent the number of edges (instead of the weight)

# the adjacency list representation becomes a nested dictionary in this format
# {source1: {target1: n_edges, target2: m_edges, ...}, source2: {...}, ... }

 # adjacency2edges conversion left as individual exercise
def multi_edges2adjacency(edges):

    # only this function was modified wrt edges2adjacency
    def add_edge(adj,src,dst): 
        if not src in adj:
            adj[src] = {dst: 1}
        else:
            if dst in adj[src]:
                adj[src][dst] += 1
            else:
                adj[src][dst] = 1

    adj = {}
    for (src,dst) in edges:
        add_edge(adj, src, dst)
        add_edge(adj, dst, src)
    
    return adj

# the matrix representation is just modified so that instead 1s are replaced 
# with any int representing the number of edges between two nodes

 # matrix2adjacency conversion left as individual exercise
def multi_adjacency2matrix(adj):
    n = len(adj.keys())
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if j in adj[i]:
                # only this line was modified wrt adjacency2matrix
                row.append(adj[i][j]) 
            else:
                row.append(0)
        matrix.append(row)
    return matrix