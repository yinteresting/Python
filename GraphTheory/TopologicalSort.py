'''
Top sort:

Prerequisite:
Some real world applications can be modelled as a graph with directed edges where some events must happen
before others.

. School class prerequisites
. Program dependencies
. Event scheduling
. Assembly instructions

Find ordering in O(V+E) time
Top orderings are not unique

Given a dependcy graph, print a top order to build the all the program
Note: not all graph can have a top ordering, a graph with cycles can't.
How to verify if your graph has cycle, only  directed acyclic graph has a top order


Torjon's strong component algorithm to detect.
ALl rooted trees have a top ordering.

Solution:
The dfs will make sure that all the higher priority nodes after current node will
be placed after current node.

    we pick a random node, apply dfs on that node,
    when backtrack, we add the call stack nodes to the back of our result.

    repeat above process until all nodes are visited

    directed graph with adjacency list as representation
'''
from collections import deque

class ToplogicalSort:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
        self.visited = {key: False for key in self.graph}
        self.visiting = set()
        self.has_cycle = False

    def findtoporder(self):
        res = deque()
        for node in self.graph:
            if not self.visited[node]:
                self.dfs(node, res)
            if self.has_cycle:
                raise ValueError("Graph has a cycle!")
        return list(res)

    def dfs(self, at, res):
        if at in self.visiting:
            self.has_cycle = True
            return
        if self.visited[at]:
            return

        self.visiting.add(at)

        for child in self.graph[at]:
            self.dfs(child, res)

        self.visiting.remove(at)

        self.visited[at] = True
        res.appendleft(at)


if __name__ == '__main__':
    graph = {
        "A": ["C"],
        "B": ["C", "D"],
        "C": ["E"],
        "D": ["F"],
        "E": ["F"],
        "F": []
    }
    test = ToplogicalSort(graph)
    print(test.findtoporder())