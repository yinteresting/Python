'''
Longest and shortest path for a directed acyclic graph

SSSP on DAG:
single source shortest path problem solved in O(V+E) with weights

Find the shortest path from Node A to all other nodes:

The beauty of topological ordering is that it always explore the furthest nodes from source node
that is it already maintained a sequence of visiting the nodes in a graph, that is we always need visit
all the nodes to the left hand side to reach the right hand side nodes.

So we visit the graph again and search all the edges connected to another node and save the smallest value
to each destination, that value will be the shortest value for the source node to reach the destination nodes.

graph =
    [ "A" : [ ("B" , 3), ("C" , 5) ],

    ]

Second question:
Longest path for Node A to all other nodes? This is a NP-Hard problem
But for DAG directed acyclic graph, O(V+E)
The trick is multiply all edge values by -1 then find the shortest path and then multiply the edge
values by -1 again


'''
import math
from collections import deque


class SSSP:
    def __init__(self, graph, source):
        self.graph = graph
        self.source = source
        self.n = len(graph)
        self.visited = {key: False for key in self.graph}

    def find_all_shortest_paths(self):
        res = {key : math.inf for key in self.graph}
        paths = {key : deque() for key in self.graph}

        # we need generate a topological order of the graph
        arbitrary_topological_order = deque()
        for node in self.graph:
            if not self.visited[node]:
                self.dfs(node, arbitrary_topological_order)

        # now iterate through the topological order and update the res for each node
        index = 0
        while index < len(arbitrary_topological_order):
            if self.source == arbitrary_topological_order[index]:
                break
            index += 1
        res[self.source] = 0
        paths[self.source].appendleft(self.source)

        while index < len(arbitrary_topological_order):

            for neighbor in self.graph[arbitrary_topological_order[index]]:
                if res[arbitrary_topological_order[index]] + neighbor[1] < res[neighbor[0]]:
                    res[neighbor[0]] = res[arbitrary_topological_order[index]] + neighbor[1]
                    paths[neighbor[0]] = deque(list(paths[arbitrary_topological_order[index]]) + [neighbor[0]])

            index += 1

        return res, paths

    def dfs(self, at, top_order):
        self.visited[at] = True

        for neighbor in self.graph[at]:
            if not self.visited[neighbor[0]]:
                self.dfs(neighbor[0], top_order)

        top_order.appendleft(at)

graph = { 'A' : [('B', 3), ('C', 6) ],
          'B' : [('C', 4), ('D', 4), ('E', 11)],
          'C' : [('D', 8), ('G', 11)],
          'D' : [('E',-4), ('F', 5), ('G', 2)],
          'E' : [('H', 9)],
          'F' : [('H', 1)],
          'G' : [('H', 2)],
          'H' : []
          }

test = SSSP( graph, 'B')
arr, p = test.find_all_shortest_paths()
print(arr)
print(p)

'''
Dijkstra's Algorithm: single source shorest path SSSP algorithm 
for graphs with non-negative edge weight.
Typically O(E*log(V))

The constraint is imposed to ensure that once a node has been visited its optimal 
distance cannot be improved

This property is especially important because it enables Dijkstra's algorithm to act in
a greedy manner by always selecting the next most promising nodee. 


Lazy Dijkstra's algorithm VS Eager Dijksstra's algorithm

Overview:
1. Maintain a 'dist' array where distance to every node is positive infinity. Mark the distance to 
the start node 's' to be 0
2. Maintain a PQ of key-value pairs of (node index, distance) which tell you which node to visit next
based on sorted min value
3. Inseret (s, 0) into the PQ and loop while PQ is not empty pulling out the next most promising 
(node index, distance) pair
4. Iterate over all edges outwards from the current node and relax each edge appending a new (node index, distance)
pair to the PQ for every relaxation. 

'''

class Dijkstra_shortest_path:
    def __init__(self, graph, source):
        self.graph = graph