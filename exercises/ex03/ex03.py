## Question 1: directory structure
import os # https://docs.python.org/3/library/os.html

## Question 2: graph representations
adj_list = {0: [1, 2], 1: [0, 2], 2: [1, 0, 3], 3: [2]}

def adj2mat(adj):
    pass

def mat2adj(mat):
    pass

## Question 3: equality between graphs
def equal(edges1, edges2):
    pass

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

def bfs():
    pass

## Question 5: multigraphs
