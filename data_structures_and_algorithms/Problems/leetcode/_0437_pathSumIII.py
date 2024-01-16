"""437. Path Sum III"""

"""
437. Path Sum III
Medium


"""
from typing import Optional
from TreeNode import TreeNode
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """Solution class for LC437, and modified from user @u2agarwal99."""
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.values = defaultdict(int)
        self.values[0] = 1

        def dfs(node, total):
            count = 0
            if not node:
                return count
            total += node.val
            count = self.values[total - targetSum]

            self.values[total] += 1
            
            left = dfs(node.left, total)
            right = dfs(node.right, total)
            count += left + right

            self.values[total] -= 1
            return count

        answer = dfs(root, 0)   
        return answer