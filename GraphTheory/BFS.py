"""
BFS: breadth first search
Search breadth first vs depth
runs in O(V+E)
particularly useful for one thing:
finding the shortest path on unweighted graphs.

Data structure used in BFS: a queue to maintain the elements for the same level
to explore before jumping to the next
"""
from collections import deque


class BreadthFirstSearch:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
        self.visited = [False] *  self.n


    def shortest_path(self, start, end):

        prev = self.solve(start)

        return self.reconstructpath(start, end, prev)

    def solve(self, start):
        queue = deque()
        queue.appendleft(start)

        self.visited[start] = True
        prev = [ None ] * self.n

        while len(queue) > 0:
            vertex = queue.pop()
            neighbors = self.graph[vertex]

            for next in neighbors:
                if not self.visited[next]:
                    queue.append(next)
                    self.visited[next] = True
                    prev[next] = vertex
        return prev

    def reconstructpath(self, start, end, prev):
        path = deque()
        while end is not None :
            path.appendleft(end)
            if end == start:
                return path
            end = prev[end]
        return None

graph6 = {
    0: [],
    1: [2],
    2: [0, 3],
    3: [4],
    4: []
}
g = BreadthFirstSearch(graph6)
print(g.shortest_path(0, 0))