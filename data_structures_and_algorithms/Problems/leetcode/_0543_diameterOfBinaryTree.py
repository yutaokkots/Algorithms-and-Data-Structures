'''
543. Diameter of Binary Tree
Easy

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(root):
            if not root:
                return -1

            left_side_height = dfs(root.left)
            right_side_height = dfs(root.right)
            result[0] = max(result[0], left_side_height + right_side_height + 2)

            return max(left_side_height, right_side_height) + 1
        
        dfs(root)
        return result[0]
    
class Solution2:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        self.recursive(root)
        return self.max

    def recursive(self, node):
        if not node:
            return 0

        left_depth = self.recursive(node.left)
        right_depth = self.recursive(node.right)

        self.max = max(self.max, left_depth + right_depth)

        return 1 + max(left_depth, right_depth)