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
from typing import Optional

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serializer(self, root:Optional[TreeNode]) -> str:
        ''' Encodes a tree to a string
        
        :type root: TreeNode
        :rtype: str
        '''

        self.serialized_lst:list = []
        self.dfs_serializer(root)
        return ",".join(self.serialized_lst)
    
    def dfs_serializer(self, node:Optional[TreeNode]) -> None:
        ''' Recursive function that visits each node and saves the node value to a global list.
        
        :type node: TreeNode
        :rtype: None
        '''

        # if node does not exist, then append "N" to indicate None type. 
        if not node:
            self.serialized_lst.append("N")
            return
        node_value = str(node.val)
        self.serialized_lst.append(node_value)
        self.dfs_serializer(node.left)
        self.dfs_serializer(node.right)

    def deserializer(self, str_data):
        ''' Decodes a string to a tree.
        
        :type str_data: str
        :rtype: TreeNode
        '''

        self.deserialized_lst = str_data.split(",")
        self.index = 0
        return self.dfs_deserializer()
    
    def dfs_deserializer(self) -> TreeNode:
        ''' Recursive function that increments through a list, and creates a new node. 

        :rtype: TreeNode
        '''

        # Edge case that increments the index if there is "N" in the string
        if self.deserialized_lst[self.index] == "N":
            self.index += 1
            return None
        node_value = self.deserialized_lst[self.index]
        node = TreeNode(node_value)
        self.index += 1
        # Recursive portion that turns the left node or right node the result of the function. 
        node.left = self.dfs_deserializer()
        node.right = self.dfs_deserializer()
        return node
        