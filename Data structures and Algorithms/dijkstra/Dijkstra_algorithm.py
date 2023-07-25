## from chag gpt
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 3, 'B': 1, 'D': 2},
    'D': {'B': 3, 'C': 2}
}

distances = dijkstra(graph, 'A')
print(distances)
# Output: {'A': 0, 'B': 4, 'C': 3, 'D': 5}


# This implementation uses a priority queue (heapq) to keep track of the nodes to visit next. It starts by initializing the distances to all nodes as infinity, except the starting node which has a distance of 0. It then adds the starting node to the priority queue.

# The algorithm continues by visiting the node with the smallest distance in the priority queue. If the distance to the current node is greater than the distance already recorded for that node, it skips the node.

# Otherwise, it updates the distances to all neighbors of the current node, and adds them to the priority queue if they have not been visited before or if their distance can be improved.

# The algorithm terminates when the priority queue is empty, and returns the shortest distances to all nodes from the starting node.

# You can use this implementation by passing in a graph represented as a dictionary of dictionaries, where the keys of the outer dictionary are the nodes, and the keys of the inner dictionaries are the neighbors of each node and their corresponding edge weights. 