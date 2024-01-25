"""1457. Pseudo-Palindromic Paths in a Binary Tree"""

"""
1457. Pseudo-Palindromic Paths in a Binary Tree
Medium

Given a binary tree where node values are digits from 1 to 9. 
A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Example 1:
Input: root = [2,3,1,3,1,null,1]
        2
      /   \
     3     1
    /  \    \
   3    1    1

Output: 2 
Explanation: The figure above represents the given binary tree. 
There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. 
Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:
Input: root = [9]
Output: 1
 
Constraints:
    The number of nodes in the tree is in the range [1, 10^5].
    1 <= Node.val <= 9
"""

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from .TreeNode import TreeNode

class Solution:
    """A solution class for LC1457 adapted from user @anwendeng"""
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def dfs(node, path):
            if not node:
                return
            node_val = node.val
            path ^= (1 << node_val) 
            # 1 << x; calculates 2 raised to the power of x.
            #  ^= ; bitwise XOR assignment operation. Takes the current value of path, performs a bitwise XOR with the result of 1 << x, and assigns the result back to path.
            if (not node.left) and (not node.right):
                if path.bit_count() <= 1:
                    self.result += 1
                    return
            dfs(node.left, path)
            dfs(node.right, path)
        dfs(root, 0)
        return self.result
