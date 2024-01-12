# Graphs

A tree is actually a type of graph, but not all graphs are trees. 
A tree is a connected graph without cycles. 

## Two common ways to represent a graph -> (1) Adjacency List; (2) Adjacency Matrix

### Adjacency List

Every vertex or node stroes a list of adjacent vertices
In an undireced graph, and edge (a, b) would be stored twice,
once in a's adjacent vertices, and one in b's adjacent vertices. 

```
a simple class definition for a graph node can look similar to a tree node

>>> Python

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

class Graph:
    def __init__(self):
        self.nodes = []
```

Also, an array, or a hash table, of lists (arrays, arraylists, linked lists, etc) can store the adjacency list. 

Example:
```
0: 1, 2
1: 2
2: 0
3: 2
4: 6
5: 4
6: 5

    [6]         [0] - [1]
   /   \            \\ |
 [5] - [4]      [3] - [2]

```

### Adjacency Matrix

An adjacency matrix is an N x N boolean matrix (where N is the number of nodes)
where a true value at matrix[i][j] indicates anedge from node 'i' to node 'j'

