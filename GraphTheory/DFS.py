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
#depth_first_search(start_node, graph)

'''
Finding connected components 
Start a dfs at every node except if it's alreeady 
'''
def finding_connected_components(graph_input):
    visited = {key: False for key in graph_input}
    components = {}

    for node in graph_input:
        components[node] = []
        dfs2(node, graph_input, visited, components[node])

    return components

def dfs2(at, g, visited, component):
    if visited[at]:
        return
    visited[at] = True
    component.append(at)
    for neighbor in g[at]:
        dfs2(neighbor, g, visited, component)

graph3 = {
    '0' : ['4','8','13', '14'],
    '8' : ['0', '4', '14'],
    '4' : ['0','8'],
    '14' : ['0', '8','13'],
    '13' : ['0', '14'],
    '6' : ['7','11'],
    '11' : ['6', '7'],
    '7' : ['6', '11'],
    '12' : [],
    '1' : ['5'],
    '5' : ['1', '16', '17'],
    '16' : ['5'],
    '17' : ['5'],
    '15' : ['9','2','10'],
    '10' : ['15'],
    '2' :['9','15'],
    '9' : ['3','15', '2'],
    '3' : ['9']
}

res = finding_connected_components(graph3)
for k in res:
    if len(res[k]) > 0:
        print(res[k])


"""
what can we do using DFS?
1. compute a graph's minimum spanning tree
2. Detect and find cycles in a graph
3. Check if a graph is bipartite
4. Find strongly connected components
5. Topologically sort the nodes of a graph
6. Find bridges and articulation points
7. Find augmenting paths in a flow network
8. Generate mazes.
"""