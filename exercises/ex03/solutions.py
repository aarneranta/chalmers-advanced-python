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

# Question 2 #################################################################
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

# Question 3 #################################################################

# Question 4 #################################################################