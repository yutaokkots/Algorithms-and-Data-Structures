'''Test for LC0032 - Longest Valid Parentheses'''
from unittest import TestCase
from leetcode._0032_longestValidParentheses import Solution

TEST_CASES = [
    {
        "input": "(()",
        "output": 2
    },
    {
        "input": ")()())",
        "output": 4
    },
    {
        "input": "",
        "output": 0
    },
    {
        "input": "))(()))()",
        "output": 4
    },
    {
        "input": "))(())(()()()",
        "output": 6
    },
    {
        "input": "()(()",
        "output": 2
    },
]

class TestLC0032(TestCase):
    def setUp(self) -> None:
        self.test_cases = TEST_CASES
        self.sol = Solution()
        return super().setUp()
    
    def tests(self):
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"Test {i + 1}"):
                self.assertEqual(self.sol.longestValidParentheses(case["input"]), case["output"])
