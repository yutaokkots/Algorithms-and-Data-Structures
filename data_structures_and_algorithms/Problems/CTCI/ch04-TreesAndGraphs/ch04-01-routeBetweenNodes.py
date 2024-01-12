# Given a directed graph, design an algorithm to find out there is a route between two nodes

# hint: two well known algorithms can do this. What are the trade-offs between them?
from ch0400creatingGraph import Graph, Node

g = Graph()
g.add_node(0)
g.add_node(1)
g.add_edge(0,1)

for n in g.nodes:
    print(n.value)
    print(n.neighbors)

class Solution():
    def bfs(self, ):
        pass