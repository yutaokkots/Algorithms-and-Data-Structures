'''

Examples of BFS vs DFS

Breadth-First Search / Depth-First Search

100. Same Tree -> https://leetcode.com/problems/same-tree/
101. Symmetric Tree -> https://leetcode.com/problems/symmetric-tree/
104. Maximum Depth of Binary Tree -> https://leetcode.com/problems/maximum-depth-of-binary-tree/
110. Balanced Binary Tree -> https://leetcode.com/problems/balanced-binary-tree/
111. Minimum Depth of Binary Tree -> https://leetcode.com/problems/minimum-depth-of-binary-tree/


             F <-root
           /    \
          D      J
         / \    / \
        B   E  G   K
       / \     \
      A   C     I
               /
              H 

'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

a_node = TreeNode(val="A")
c_node = TreeNode(val="C")
b_node = TreeNode(val="B", left=a_node, right=c_node)
e_node = TreeNode(val="E")
d_node = TreeNode(val="D", left=b_node, right=e_node)

h_node = TreeNode(val="H")
i_node = TreeNode(val="I", left=h_node)
g_node = TreeNode(val="G", right=i_node)
k_node = TreeNode(val="K")
j_node = TreeNode(val="J", left=g_node, right=k_node)

f_node = TreeNode(val="F", left=d_node, right=j_node)

# Breadth-First; level-order
# F -> D -> J -> B -> E -> G -> K -> A -> C -> I -> H

#Depth-First; 
# F -> D -> B -> A -> C -> E -> J -> G -> I -> H -> K

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.min_depth = float('inf')
        # DFS function
        def dfs(node, depth):
            if not node:
                return 
            if not node.left and not node.right:
                self.min_depth = min(self.min_depth, depth)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)
        return self.min_depth
    
    def isBalanced(self, root:Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]

sol = Solution()
max_depth = sol.maxDepth(f_node)
min_depth = sol.minDepth(f_node)
is_balanced = sol.isBalanced(f_node)
print(f"max_depth: {max_depth}\nmin_depth: {min_depth}\nis_balanced: {is_balanced}")
