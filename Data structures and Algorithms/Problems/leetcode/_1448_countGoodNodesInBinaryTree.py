'''
1448. Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.path_max = root.val    
        self.good = 0

        def dfs(node, path_max):
            if not node:
                return 0
            if node.val >= path_max:
                self.good += 1


            path_max = max(path_max, node.val)

            left_side = dfs(node.left, path_max)
            right_side = dfs(node.right, path_max)

            return left_side + right_side + 1

        dfs(root, root.val)

        return self.good 
    
    def goodNodes2(self, root: TreeNode) -> int:
        self.path_max = root.val    
        good_nodes = []


        def dfs(node, path_max):
            if not node:
                return 0
            if node.val >= path_max:
                good_nodes.append(node.val)

            path_max = max(path_max, node.val)

            left_side = dfs(node.left, path_max)
            right_side = dfs(node.right, path_max)

            return left_side + right_side + 1

        dfs(root, root.val)

        return len(good_nodes)