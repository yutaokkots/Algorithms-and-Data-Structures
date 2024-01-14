"""687. Longest Univalue Path"""

"""
687. Longest Univalue Path
Medium
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [5,4,5,1,1,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 5).

Example 2:
Input: root = [1,4,5,4,4,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 4).
 
Constraints:
    The number of nodes in the tree is in the range [0, 10^4].
    -1000 <= Node.val <= 1000
    The depth of the tree will not exceed 1000.
"""
from typing import Optional
from TreeNode import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def dfs(node, node_prev):
            if not node:
                return 0 
            left_val = dfs(node.left, node)
            right_val = dfs(node.right, node)
            self.longest = max(self.longest, left_val + right_val)
            if node_prev and node.val == node_prev.val:
                return 1 + max(left_val, right_val)
            return 0
        dfs(root, None)
        return self.longest