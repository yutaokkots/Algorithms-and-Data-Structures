'''
100. Same Tree
Easy

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false


'''

# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result = [True, 0]

        def dfs(node1, node2):
            if not node1 and node2 or node1 and not node2:
                result[0] = False
                return result
            if not node1 and not node2:
                return result
            if node1.val != node2.val:
                result[0] = False
                return result
                
            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)
            if left[0] == False or right[0] == False:
                result[0] = False
            return result

        dfs(p, q)

        return result[0]

class Solution2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.result = True
        self.dfs(p, q)

        return self.result

    def dfs(self, node1, node2):
        if not node1 and node2 or node1 and not node2:
            self.result = False
            return self.result
        if not node1 and not node2:
            return self.result
        if node1.val != node2.val:
            self.result = False
            return self.result
            
        left = self.dfs(node1.left, node2.left)
        right = self.dfs(node1.right, node2.right)
        if not left or not right:
            self.result = False
        return self.result
