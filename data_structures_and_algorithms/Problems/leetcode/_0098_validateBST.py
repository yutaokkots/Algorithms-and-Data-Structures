'''
98. Validate Binary Search Tree
Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_valid = True
        lower = float("-inf")
        upper = float("inf")
        
        def dfs(node, left_lower, right_upper):
            if not node:
                return 0
            
            if not left_lower < node.val < right_upper:
                self.is_valid = False
                
            left = dfs(node.left, left_lower, node.val)
            right = dfs(node.right, node.val, right_upper)
            return left + right + 1

        dfs(root, lower, upper)

        return self.is_valid

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return (dfs(node.left, left, node.val) and 
                dfs(node.right, node.val, right))
        
        return dfs(root, float("-inf"), float("inf"))