# Data Structures overview

1) ***Arrays*** - contiguous memory locations. Collection of elements of the same type. 

    (1) ***Array*** - An Array in Java is a fixed-size, ordered collection of elements of the same data type. The elements in an array are stored in contiguous memory locations, and each element is accessed using an index or a subscript. 

    (2) ***Array*** - An Array in JavaScript array can consist of different data types. JavaScript is dynamically typed, so the types of elements within the array are flexible.

    (3) ***ArrayList*** - An ArrayList in Java is a dynamic, ordered collection that can hold elements of different types. Java is statically typed, so the type of elements in the ArrayList is specified when it is declared.

    (4) ***List*** - A List in Python is a dynamic, ordered collection in which elements can be of different data types. Lists are more flexible compared to arrays as they can grow or shrink in size during runtime. Elements in a list are also accessed using an index, but the list allows for more operations, such as appending, inserting, and removing elements

2) ***Hash Tables*** - Typically uses a contiguous data structure such as an array/list that holds buckets, but elements stored in the array are non-contiguous. Each bucket holds one or more key-value pairs. A hash function is designed to generate a unique key for the key-value pairs, and a value corresponds to that unique key. Basic functions for hash tables are search, insertion, and deletion of values.

    e.g. Valid Anagram -> use memo/hashmap

    e.g. Two-sum -> use memo/hashmap

    e.g. Group Anagrams -> use memo/hashmap

3) ***Stacks*** - typically contiguous memory locations. Collection of elements, where elements can only be inserted or removed from the top (***Last in first out (LIFO)***). Follows 'push' and 'pop' operations. Stacks are represented either as an array (contiguous memory locations) or a linked list (non-contiguous memory locations). 

4) ***Queues*** - Can be contiguous or non-contiguous memory locations, and is a linear data structure. Queues are typically represented as arrays/lists. Collection of elements where, elements are inserted on one end, and removed at the other end (***First in first out (FIFO)***). Insertion at one end is typically called enqueue, while removal at the other end is called dequeue.

5) ***Heaps*** - contiguous memory locations. Typically stored as lists/arrays, but represents a tree (usually a binary tree). 'Heapify' is the term that describes creating a heap (binary tree) from an array. Useful when inserting, removing, or retrieving objects with the highest or lowest priority (priority queue). Heaps are generally represented as Max-heap (where the root node is the largest value among the keys present at all of its chidren, and this property is recursively true for all of its children), or as a Min-heap (where the root node is the smallest value among the keys present at all of its chidren, and this property is recursively true for all of its children). The purpose of heaps is to perform the operations with O(logN) time complexity.

6) ***Sets*** - A data type that represents an unordered collection of unique elements. The elements in a set must be immutable (unchangeable), and the set itself is mutable (elements can be added or deleted). Sets are commonly used for tasks that involve testing membership, eliminating duplicate entries, and performing set operations like union, intersection, difference, and symmetric difference.

7) ***Linked lists*** - a node contains data and a reference to the next node. Collection of nodes. linked data structure. Allows for dynamic size and efficient insertion and deletion, but slower access time. 

8) ***Trees*** - Data in a tree are non-linear, but can be created from contiguous or non-contiguous memory locations. Trees can be createdin a number of ways, including 

    (1) array-based representation (each element of the array corresponds to a node in the tree, and the parent-child relationships are determined by the indices of the array elements); 

    (2) linked structures (an object contains the nodes value and points to references another, child node); 

    (3) hybrid approach like a binary heap. 

9) ***Graphs*** - Non-linear, non-coniguous memory locations. Graphs are a collection of nodes (vertices) that are connected by edges. Each vertex represents an object, and can further contain additional information. Edges are the connections between pairs of indices, and represent the relationship between the objects. Edges can be directed (having a specific direction and indicating a flow of the relationship) or undirected (having no specific direction). Edges can also have weights or costs associated with them. Two approaches to represent Graphs are 

    (1) **Adjacency lists** - each vertex is associated with an array (list) that contains its adjacent vertices (i.e. an array of linked list or a hash map that stores adjacenct lists); 

    (2) **Adjacency matrix** - a two-dimensional matrix to represent the connection between vertices.
    