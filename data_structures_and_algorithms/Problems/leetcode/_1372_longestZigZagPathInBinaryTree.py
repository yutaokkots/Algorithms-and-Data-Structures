"""1372. Longest ZigZag Path in a Binary Tree"""

"""
1372. Longest ZigZag Path in a Binary Tree
Medium

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:
Input: root = [1]
Output: 0
 
Constraints:
    The number of nodes in the tree is in the range [1, 5 * 10^4].
    1 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from TreeNode import TreeNode

class Solution:
    """Solution class for LC1372, adapted from @aryan_0077."""
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_zigzag = 0
        def dfs(node, deep, direction):
            self.max_zigzag = max(self.max_zigzag, deep)
            if node.left is not None:
                dfs(node.left, deep + 1, 'left') if direction != 'left' else dfs(node.left, 1, 'left')
            if node.right is not None:
                dfs(node.right, deep + 1, 'right') if direction != 'right' else dfs(node.right, 1, 'right')
            
        dfs(root, 0, "")
        return self.max_zigzag