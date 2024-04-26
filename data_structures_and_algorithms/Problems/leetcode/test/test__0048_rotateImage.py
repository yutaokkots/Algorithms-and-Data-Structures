'''Unittest for LC0048 Rotate Image'''
from unittest import TestCase
from leetcode._0048_rotateImage import Solution

TEST_CASES = [
    {
    "input": [[1,2,3],
              [4,5,6],
              [7,8,9]],
    "output": [[7,4,1],
               [8,5,2],
               [9,6,3]]
    },
    {
        "input":[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
        "output":[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    }
]

class TestLC0048(TestCase):
    def setUp(self) -> None:
        self.test_cases =TEST_CASES
        self.sol = Solution()

    def tests(self):
        for i, case in range(self.test_cases):
            with self.subTest(f"Test {i + 1}"):
                self.assertEqual(self.sol.rotate(matrix=case["input"]), case["output"])

    