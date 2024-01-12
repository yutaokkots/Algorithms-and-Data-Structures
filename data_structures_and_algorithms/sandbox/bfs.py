import collections
from typing import Optional
'''
Examples of breadth-first-search algorithms

(1) Define a binary tree:

                7
              /    \
            4       9      
          /  \     /  \
        2     5   8   12
      /  \     \     /  \
     1    3     6   10  13     
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

'''
(2) Undergo BFS on the tree by printing out the value at each level


'''

def bfs(node: Optional[TreeNode]) -> list[int]:
    q = collections.deque()
    q.append(node)
    all_nodes = []
    while len(q) > 0:
        node = q.popleft()
        if node:
            all_nodes.append(node.val)
            q.append(node.left)
            q.append(node.right)
    return all_nodes

answer = bfs(head)
print(answer)

# >>> answer
# >>> [7, 4, 9, 2, 5, 8, 12, 1, 3, 6, 10, 13]