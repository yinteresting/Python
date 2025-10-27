'''
Depth first search
 start as the starting vertex to search
 graph as input: we use an adjacency list
 visited will print out the dfs path of visiting the graph

DFS works in a cursive way, to avoid a cycle or re-visit the node that is being visited
simply check if the next node is already in the visited path.
'''

def depth_first_search(start, graph):
    visited = []
    dfs(start, visited, graph)
    print(visited)


def dfs(at, visited, graph):
    if visited is None:
        visited = []
    visited.append(at)

    neighbors = graph[at]
    for next in neighbors:
        if next not in visited:
            dfs(next, visited, graph)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'

graph2 = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}
depth_first_search(start_node, graph2)
