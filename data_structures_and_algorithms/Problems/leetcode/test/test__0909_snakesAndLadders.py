'''Test cases for 909. Snakes and Ladders'''

from unittest import TestCase
from leetcode._0909_snakesAndLadders import Solution

TEST_CASES = [
    {
        "input": [[-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1],
                  [-1,35,-1,-1,13,-1],
                  [-1,-1,-1,-1,-1,-1],
                  [-1,15,-1,-1,-1,-1]],
        "output": 4
    },
    {
        "input": [[-1,-1],
                  [-1, 3]],
        "output": 1
    },
    {
        "input": [[-1,-1,-1],
                  [-1,-1,-1],
                  [-1,-1,-1]],
        "output": 2
    },
    {
        "input": [[-1,-1,19,10,-1],
                  [ 2,-1,-1, 6,-1],
                  [-1,17,-1,19,-1],
                  [25,-1,20,-1,-1],
                  [-1,-1,-1,-1,15]],
        "output": 2
    },
    {
        "output":[[-1,-1,27,13,-1,25,-1],
                  [-1,-1,-1,-1,-1,-1,-1],
                  [44,-1,8,-1,-1,2,-1],
                  [-1,30,-1,-1,-1,-1,-1],
                  [3,-1,20,-1,46,6,-1],
                  [-1,-1,-1,-1,-1,-1,29],
                  [-1,29,21,33,-1,-1,-1]],
        "input":4
    }
]

class TestLC0909(TestCase):

    def setUp(self) -> None:
        self.test_cases = TEST_CASES
        self.sol = Solution()
        return super().setUp()
    
    def tests(self):
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"Test {i+1}"):
                self.assertEqual(self.sol.snakesAndLadders(case["input"]), case["output"])