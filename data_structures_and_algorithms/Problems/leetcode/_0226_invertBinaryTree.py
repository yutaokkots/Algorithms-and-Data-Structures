'''
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2
Input: root = [2,1,3]
Output: [2,3,1]

Example 3
Input: root = []
Output: []


Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        left = root.left 
        root.left = root.right
        root.right = left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    

'''
JAVA solution:

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null){
            return null;
        }
        TreeNode rightNode = root.right;
        root.right = root.left;
        root.left = rightNode;
        invertTree(root.right);
        invertTree(root.left);

        return root;

    }
}


'''