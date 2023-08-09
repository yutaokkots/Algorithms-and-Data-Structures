# Trees vs Binary Trees

A binary tree is a tree in which each node has up to two children.
Not all trees are binary trees.

Ex. This might be considered a Tree, or a Ternary Tree. 
            8
          / | \
         4  6  10
       /  \      \
      2    1      20

## Binary Tree vs Binary Search Tree

A binary search tree is a binary tree in which every node fits
as specific ordering property. This property must be true for each node, n.

binary search tree
            8
           / \
          4   10
         / \    \
        2   6    20
not a binary search tree
            8
           / \
          4   10
         / \    \
        2   12    20

## Balanced vs unbalanced

Not all trees are balanced. A "balanced" tree really means 
"not terribly imbalanced", and is "balanced enough to ensure
O(logn) times for insert and find

### Complete Binary Tree - a binary tree in which every level is fully filled, except the last level

not Complete                complete
             10                  10
           /   \               /    \            
          5      20           5      20   
        /   \      \        /  \    /  
       3     7      30     3    7  15

### Full Binary Tree - a binary tree in which every node has either zero or two children

not a full binary tree      a full binary tree
             10                   10
           /    \               /    \            
          5       20           5      20   
           \     /  \               /   \  
            12  3    7             3     7
               / \                / \ 
              9   18             9   18
https://leetcode.com/problems/all-possible-full-binary-trees/

### Perfect Binary Trees - a binary tree that is both full and complete. 

All perfect binary tree must have exactly (2^k - 1) nodes, where k is the number of levels. 
perfect binary trees are rare - do not assume a binary tree is perfect. 

             10
           /    \
          5      20
        /  \    /  \
       9   18  3    7

