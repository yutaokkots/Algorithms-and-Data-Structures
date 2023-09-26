# Adjacency matrix
'''
    The Node class represents each vertex of the graph
    The attribute value represents the stored data
    The list of neighbors attribute represents the vertices with which exists a connection
'''
class Node:
    def __init__(self, value, neighbors=None):
        self.value = value
        #self.neighbors = []
        self.neighbors = [] if neighbors is None else neighbors
        # if neighbors is None:
        #     self.neighbors = []
        # else:
        #     self.neighbors = neighbors

    def has_neighbors(self):            #returns true if vertex is connected with at least one vertex
        if len(self.neighbors) == 0:
            return False
        return True
    
    def number_of_neighbors(self):      # returns the number of vertices 
        return len(self.neighbors)
    
    def add_neighbor(self, neighbor):   # adds a new connection. 
        self.neighbors.append(neighbor)

'''
    The Graph class represents the graph data structure.
    The Graph class contains a nodes attribute (list) with all nodes of the graph. 
'''

class Graph:
    def __init__(self, nodes=None):
        self.nodes = [] if nodes is None else nodes
        # if nodes is None:
        #     self.nodes = []
        # else:
        #     self.nodes = nodes
    
    def add_node(self, value, neighbors=None):      # adds a new node(vertex) to the graph
        self.nodes.append(Node(value, neighbors))

    def find_node(self, value):                     #returns true if node with given value exists
        for node in self.nodes:
            if node.value == value:
                return node
        return None
    
    def add_edge(self, value1, value2, weight=1):
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)

        if node1 and node2:
            node1.add_neighbor((value2, weight))  
            node2.add_neighbor((value1, weight))  
        else:
            print("Error:one or more nodes were not found")

    def number_of_nodes(self):
        return f"Graph contains {len(self.nodes)} nodes"
    
    def are_connected(self, node_one, node_two):
        node_one = self.find_node(node_one)
        node_two = self.find_node(node_two)

        for neighbor in node_one.neighbors:
            if neighbor[0].value == node_two.value:
                return True
        return False