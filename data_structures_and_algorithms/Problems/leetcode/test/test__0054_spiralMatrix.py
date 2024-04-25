'''Test code for LC0054 Spiral Matrix'''

from unittest import TestCase
from leetcode._0054_spiralMatrix import Solution

TEST_CASES = [
    {
        "input": [[1,2,3],[4,5,6],[7,8,9]],
        "output": [1,2,3,6,9,8,7,4,5]
    },
    {
        "input": [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
        "output": [1,2,3,4,8,12,11,10,9,5,6,7]
    },
    {
        "input": [[2,3,5,4],
                  [0,4,2,1],
                  [2,8,9,4],
                  [8,5,1,7]],
        "output": [2,3,5,4,1,4,7,1,5,8,2,0,4,2,9,8]
    },

]
class Test0054(TestCase):
    def setUp(self) -> None:
        self.test_cases = TEST_CASES
        self.sol = Solution()
    
    def tests(self):
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"Test {i+1}"):
                self.assertEqual(self.sol.spiralOrder(matrix=case["input"]), case["output"])