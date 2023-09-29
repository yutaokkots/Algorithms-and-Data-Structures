'''
Sandbox to test the serialize and deserialize methods from LC 297

                7
              /   \
            4       9      
          /  \     /  \
        2     5   8    12
      /  \     \     /   \
     1    3     6   10    13    

'''
from TreeNode import TreeNode 
from typing import Optional

n_13 = TreeNode(val=13)
n_10 = TreeNode(val=10)
n_06 = TreeNode(val=6)
n_03 = TreeNode(val=3)
n_01 = TreeNode(val=1)
n_08 = TreeNode(val=8)
n_12 = TreeNode(val=12, left=n_10, right=n_13)
n_05 = TreeNode(val=5, right=n_06)
n_02 = TreeNode(val=2, left=n_01, right=n_03)
n_09 = TreeNode(val=9, left=n_08, right=n_12)
n_04 = TreeNode(val=4, left=n_02, right=n_05)
n_07 = TreeNode(val=7, left=n_04, right=n_09)
head = n_07

class SerDeser:
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

s = SerDeser()
serialized_tree = s.serializer(head)
print(serialized_tree)
# 7,4,2,1,N,N,3,N,N,5,N,6,N,N,9,8,N,N,12,10,N,N,13,N,N

deserialized_tree = s.deserializer("7,4,2,1,N,N,3,N,N,5,N,6,N,N,9,8,N,N,12,10,N,N,13,N,6,N,N")
print(deserialized_tree)

serialized_tree2 = s.serializer(deserialized_tree)
print(serialized_tree2)