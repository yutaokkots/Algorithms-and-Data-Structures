'''
114. Flatten Binary Tree to Linked List
Medium

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 
Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]
 
Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from TreeNode import TreeNode
from typing import Optional

class Solution:
    """Solution class for LC0114. return None"""

    def flatten(self, root: Optional[TreeNode]) -> None:
        self.end_node = root

        def dfs(node):
            if not node:
                return None
            if not node.left and not node.right:
                self.end_node = node
                return node
            left = dfs(node.left)
            left_branch = self.end_node
            right = dfs(node.right)
            if left:
                node.right = left
                left_branch.right = right
            else:
                node.right = right
            node.left = None
            return node

        dfs(root)

    def flatten(self, root: Optional[TreeNode]) -> None:
        """First attempt at LC0114"""

        self.head_node = self.end_node = root
        def dfs(node):
            if not node:
                return None
            if not node.left and not node.right:
                self.end_node = node
                return node

            temp_left = node.left
            node.left = None
            temp_right = node.right
            node.right = None
            
            left = dfs(temp_left)
            left_branch = self.end_node
            
            right = dfs(temp_right)
            
            if left:
                node.right = left
                left_branch.right = right
            else:
                node.right = right
            return node

        dfs(root)

        return self.head_node

