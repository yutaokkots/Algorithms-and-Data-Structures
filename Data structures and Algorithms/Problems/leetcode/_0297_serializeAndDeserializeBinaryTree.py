'''
297. Serialize and Deserialize Binary Tree
Hard

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:

Input: root = []
Output: []
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str

        """
        self.result = []
        self.dfs(root)
        return ",".join(self.result)

    def dfs(self, node):
        if not node:
            self.result.append("N")
            return
        self.result.append(str(node.val))
        self.dfs(node.left)   
        self.dfs(node.right)   

    def deserialize(self, data):
        self.values = data.split(",")
        self.i = 0
        return self.des_dfs()

    def des_dfs(self):
        if self.values[self.i] == "N":
            self.i += 1
            return None
        node = TreeNode(int(self.values[self.i]))
        self.i += 1
        node.left = self.des_dfs()
        node.right = self.des_dfs()
        return node
    

        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        