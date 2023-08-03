# Topics overview

<table>
    <tr>
        <th>Data Structures</th>
        <th>Algorithms</th>
        <th>Concepts</th>
    </tr>
    <tr>
        <td>Linked Lists</td>
        <td>Breadth-First Search</td>
        <td>Bit Manipulation</td>
    </tr>
    <tr>
        <td>Trees, Tries, and Graphs</td>
        <td>Depth-First Search</td>
        <td>Memory (stack vs heap</td>
    </tr>
    <tr>
        <td>Stacks and Queues</td>
        <td>Binary Search</td>
        <td>Recursion</td>
    </tr>
    <tr>
        <td>Heaps</td>
        <td>Merge Sort</td>
        <td>Dynamic Programming</td>
    </tr>
    <tr>
        <td>Vector / ArrayLists</td>
        <td>Quick Sort</td>
        <td> Big O Time and Space</td>
    </tr>
    <tr>
        <td>Hash Tables</td>
        <td></td>
        <td></td>
    </tr>
</table>

# Data Structures overview

1) Arrays - contiguous memory locations. Collection of elements of the same type. 
    e.g. Valid Anagram -> use memo/hashmap
    e.g. Two-sum -> use memo/hashmap
    e.g. Group Anagrams -> use memo/hashmap

2) Linked lists - a node contains data and a reference to the next node. Collection of nodes. linked data structure. Allows for dynamic size and efficient insertion and deletion, but slower access time. 

3) Stacks - typically contiguous memory locations. Collection of elements, where elements can only be inserted or removed from the top (Last in first out (LIFO)). Follows 'push' and 'pop' operations. Stacks are represented either as an array (contiguous memory locations) or a linked list (non-contiguous memory locations). 

4) Heaps - contiguous memory locations. Typically stored as lists/arrays, but represents a tree (usually a binary tree). 'Heapify' is the term that describes creating a heap (binary tree) from an array. Useful when inserting, removing, or retrieving objects with the highest or lowest priority (priority queue). Heaps are generally represented as Max-heap (where the root node is the largest value among the keys present at all of its chidren, and this property is recursively true for all of its children), or as a Min-heap (where the root node is the smallest value among the keys present at all of its chidren, and this property is recursively true for all of its children). The purpose of heaps is to perform the operations with O(logN)

5) Queues - Can be contiguous or non-contiguous memory locations, and is a linear data structure. Queues are typically represented as arrays/lists. Collection of elements where, elements are inserted on one end, and removed at the other end (First in first out (FIFO)). Insertion at one end is typically called enqueue, while removal at the other end is called dequeue.

6) Trees - Data in a tree are non-linear, but can be created from contiguous or non-contiguous memory locations. Trees can be createdin a number of ways, including 
    (1) array-based representation (each element of the array corresponds to a node in the tree, and the parent-child relationships are determined by the indices of the array elements); 
    (2) linked structures (an object contains the nodes value and points to references another, child node); 
    (3) hybrid approach like a binary heap. 


7) Graphs - Non-linear, non-coniguous memory locations. Graphs are a collection of nodes (vertices) that are connected by edges. Each vertex represents an object, and can further contain additional information. Edges are the connections between pairs of indices, and represent the relationship between the objects. Edges can be directed (having a specific direction and indicating a flow of the relationship) or undirected (having no specific direction). Edges can also have weights or costs associated with them. Two approaches to represent Graphs are 
    (1) Adjacency lists - each vertex is associated with an array (list) that contains its adjacent vertices (i.e. an array of linked list or a hash map that stores adjacenct lists); 
    (2) Adjacency matrix - a two-dimensional matrix to represent the connection between vertices
    
8) Hash Tables - Typically uses a contiguous data structure such as an array/list that holds buckets, but elements stored in the array are non-contiguous. Each bucket holds one or more key-value pairs. A hash function is designed to generate a unique key for the key-value pairs, and a value corresponds to that unique key. Basic functions for hash tables are search, insertion, and deletion of values.

9) Sets