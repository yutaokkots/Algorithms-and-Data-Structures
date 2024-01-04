"""
144. Binary Tree Preorder Traversal
Easy

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
 
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
from typing import Optional, List
from TreeNode import TreeNode

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.answer = []
        def traversal(node):
            if node == None:
                return
            self.answer.append(node.val)
            traversal(node.left)
            traversal(node.right)

        traversal(root)
        return self.answer
