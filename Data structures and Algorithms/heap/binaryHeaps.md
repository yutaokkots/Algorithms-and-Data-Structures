# Binary Heaps (min-heaps and max-heaps)

A min-heaps(and max-heaps) is a complete binary tree. (see /trees/trees_notes.md in this repository)

The root is the minimum element in the tree

## Two key operations on a min-heap -> (1) insert; (2) extract_min

### 1. insert

```
             4
          /     \
        50        7
      /   \     /  
    55    90   87  
```  

When inserting into a min-heap, always insert the element at the bottom. 
1. Insert at the right-most spot to maintain the 'complete tree' property. 
2. fix the tree by swapping the new element with its parent, until an appropriate spot is found. 

```
step 1: insert 2
             4
          /     \
        50        7
      /   \     /   \
    55    90   87    [2]

step 2: swap 2 and 7
             4
          /     \
        50       [2]
      /   \     /   \
    55    90   87    7   

step 3: swap 2 and 4
            [2]
          /     \
        50        4
      /   \     /   \
    55    90   87    7   
```

Time complexity of the insertion/swap is O(logN), where N is number of nodes in heap

### 2. Extract Minimum Element

Finding minimum element in min-heap is EASY -> top node

```
             4
          /     \
        50        23
      /   \     /   \
    88    90   32    74
   /
  96  
```  

When extracting from a min-heap
1. Remove the minimum element
2. Swap the minimum element with the last element in the heap (the bottom-most, right-most element)
3. Bubble down the element



```
step 1: replace min with 96
            [96]
          /     \
        50        23
      /   \     /   \
    88    90   32    74
   /

step 2: swap 23 and 96
             23
          /     \
        50       [96]
      /   \     /   \
    88    90   32    74

step 3: swap 32 and 96
             23
          /     \
        50        32
      /   \     /   \
    88    90  [96]   74


```  
