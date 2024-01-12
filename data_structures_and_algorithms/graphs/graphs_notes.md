# Graphs

## Graphs are basically nodes and connections.

Graph data structure, each vertex can be connected to multiple other vertices via edges, and some vertices may not have any edges connected to them. 

Graphs can be used to represent a wide range of real-world problems, such as social networks, transportation systems, and communication network

**Graph Traversal**:
> Graphs can be directed, where the edges have a direction and represent a one-way relationship between nodes, or undirected, where the edges have no direction and represent a two-way relationship between nodes.
> 
> Depth-First Search (DFS): DFS is a recursive algorithm that starts at a node and visits all the connected nodes, exploring as far as possible along each branch before backtracking. It can be used to detect cycles in a graph, check if a path exists between two nodes, or find connected components.
> 
> Breadth-First Search (BFS): BFS is an algorithm that visits all the nodes at the current depth before moving on to the next level. It is often used to find the shortest path between two nodes, or to explore the graph in a systematic way.

**Shortest Path Algorithms**:
> Dijkstra's Algorithm: Dijkstra's algorithm is a greedy algorithm that finds the shortest path between two nodes in a weighted graph. It works by starting at the source node, and iteratively adding the closest unvisited node to the set of visited nodes. The algorithm terminates when the destination node is reached, or when all reachable nodes have been visited.
> 
> Bellman-Ford Algorithm: The Bellman-Ford algorithm is another algorithm that finds the shortest path between two nodes in a weighted graph. It can handle graphs with negative edge weights, unlike Dijkstra's algorithm. The algorithm works by relaxing each edge in the graph V-1 times, where V is the number of nodes in the graph.
> 
> A **Search Algorithm: A** is a heuristic search algorithm that finds the shortest path between two nodes in a weighted graph. It uses a heuristic function to estimate the distance to the destination node, which helps to guide the search towards the goal. A* is often used in pathfinding applications, such as in video games or robotics.
sparse data: Sparse data is a variable in which the cells do not contain actual data within data analysis. Sparse data is empty or has a zero value.

How to store data
Adjacency Graphs

https://en.wikipedia.org/wiki/Adjacency_matrix

Adjacency Lists

Example 1.

Undirected graph
Suppose you have an undirected graph with 5 nodes: A, B, C, D, and E. The edges and their weights are as follows:

    A-B: 4
    A-C: 1
    B-C: 2
    B-D: 5
    C-D: 1
    C-E: 6
    D-E: 3

    graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 1, 'B': 2, 'D': 1, 'E': 6},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'C': 6, 'D': 3}
    }

    Each key in the outer dictionary represents a node in the graph, and the corresponding value is another dictionary that represents the edges and their weights that connect that node to its neighbors.


Example 2.

Directed graph
Suppose you have a directed graph with 4 nodes: A, B, C, and D. The edges and their weights are as follows:
    A->B: 5
    A->D: 1
    B->C: 2
    C->A: 3
    C->D: 4

    graph = {
    'A': {'B': 5, 'D': 1},
    'B': {'C': 2},
    'C': {'A': 3, 'D': 4},
    'D': {}
    }

    Each key in the outer dictionary represents a node in the graph, and the corresponding value is another dictionary that represents the edges and their weights that go out from that node to its neighbors.

Example 3. 

Weighted graph with self-loops
Suppose you have a directed graph with 4 nodes: A, B, C, and D. The edges and their weights are as follows:
    A->A: 2
    A->B: 5
    A->C: 1
    B->A: 3
    B->C: 2

    graph = {
    'A': {'A': 2, 'B': 5, 'C': 1},
    'B': {'A': 3, 'C': 2},
    'C': {}
    }

    Each key in the outer dictionary represents a node in the graph, and the corresponding value is another dictionary that represents the edges and their weights that go out from that node to its neighbors, including self-loops.

|      |            Adjacency List 	                | 	        Adjacency Matrix               |
| :--: |      :--------------------------------:    | :--------------------------------------: |
| Pros |	Can take up less space (in sparse graph)|	Faster to lookup specific edge         |
| Pros |	Faster to iterate over all edges		|                                          |
| Cons |	Can be slower to lookup specific edge	|	Takes up more space (in sparse graph)  |
| Cons |			                                |   Slower to iterate over all edges       |