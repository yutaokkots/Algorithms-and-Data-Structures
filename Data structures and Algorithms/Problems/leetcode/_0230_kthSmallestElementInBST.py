'''
230. Kth Smallest Element in BST
Medium

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

'''
from typing import Optional
import collections

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # breadth-first-search
        self.record = []
        self.q = collections.deque() ## declares queue
        self.q.append(root) ## [root(5)]
        
        def bfs():
            while len(self.q) > 0:
                popped_item = self.q.popleft()
                self.record.append(popped_item.val)
                if popped_item.left:
                    self.q.append(popped_item.left)
                if popped_item.right:
                    self.q.append(popped_item.right)

        bfs()

        self.record.sort()
        return self.record[k-1]
    

class Solution2:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # depth-first-search
        self.record = []
        def dfs(node):
            if not node:
                return 
            self.record.append(node.val)
            dfs(node.left)
            dfs(node.right)
            return 
        
        dfs(root)

        self.record.sort()
        return self.record[k-1]