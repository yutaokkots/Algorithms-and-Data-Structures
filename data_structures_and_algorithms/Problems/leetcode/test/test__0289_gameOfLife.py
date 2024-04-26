'''Unittest for LC0289 - Game of Life'''

from unittest import TestCase
from leetcode._0289_gameOfLife import Solution
from leetcode.time_measure import timer
import copy

TEST_CASES = [
    {
        "input": [[0,1,0],[0,0,1],[1,1,1],[0,0,0]],
        "output": [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    },
    {
        "input": [[1,1],[1,0]],
        "output": [[1,1],[1,1]]
    }
]

class Test0054(TestCase):
    def setUp(self) -> None:
        self.test_cases = TEST_CASES
        self.sol = Solution()
    
    @timer
    def test01(self) -> None:
        case01 = copy.deepcopy(self.test_cases)
        for i, case in enumerate(case01):
            with self.subTest(f"Test 01 case {i+1}"):
                board = case["input"].copy()
                self.sol.gameOfLife(board=board)
                self.assertEqual(board, case["output"])

    @timer
    def test02(self) -> None:
        case02 = copy.deepcopy(self.test_cases)
        for i, case in enumerate(case02):
            with self.subTest(f"Test 02 case {i+1}"):
                board2 = case["input"].copy()
                self.sol.gameOfLife2(board=board2)
                self.assertEqual(board2, case["output"])