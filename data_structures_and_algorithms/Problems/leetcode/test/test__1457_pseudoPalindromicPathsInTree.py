from unittest import TestCase
from leetcode._1457_PseudoPalindromicPathsInTree import Solution
from leetcode.TreeNode import TreeNode


root = TreeNode(2)
root.right = TreeNode(val=1, right=TreeNode(val=1))
root.left = TreeNode(val=3, left=TreeNode(val=3),right=TreeNode(val=1))


"""Input: root = [2,3,1,3,1,null,1]
        2
      /   \
     3     1
    /  \    \
   3    1    1
"""

class TestLC1457(TestCase):
    def setUp(self):
        self.test_case01 = root
        self.sol = Solution()

    def test_case01(self):
        self.assertEqual(self.sol.pseudoPalindromicPaths(self.test_case01), 2)


