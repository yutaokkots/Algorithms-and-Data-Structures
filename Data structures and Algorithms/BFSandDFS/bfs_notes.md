# Breadth-First-Search (BFS) & Depth-First-Search (DFS)

Breadth-First-Search (BFS) can be used to fulfill the following:
1) Is there a path from node A to ndoe B?
2) What is the shortest path from node A to node B?

## Breadth-First Search
Points:
1) Start BFS from any vertex. 
2) When at a vertex, visit adjacent vertex in any order.
3) When visiting a vertex, you must visit all adjacent vertices, before going to next vertex for exploration
4) Select the next vertex to explore using a **queue**.

## Depth-First Search
Points:
1) Start BFS from any vertex. 
2) When visiting a new vertex, suspend the exploration of the current vertex, and explore that new vertex first. 
3) Use a **stack** to keep track of next vertext to explore.