"""Test case for LC0392 - Is Subsequence"""

"""
Problems % python3 -m unittest leetcode.test.test__0392_isSubsequence
"""
from unittest import TestCase
from leetcode._0392_isSubsequence import Solution

TEST_CASES = [
    {
        "s": "abc", 
        "t": "ahbgdc",
        "answer": True
    },
    {
        "s": "axc", 
        "t": "ahbgdc",
        "answer": False
    },
    {
        "s": "ahc", 
        "t": "ahbgdc",
        "answer": True
    }
]

class TestLC0392(TestCase):
    def setUp(self) -> None:
        self.test_cases = TEST_CASES
        self.sol = Solution()

    def test_cases(self):
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"Test {i + 1}"):
                self.assertEqual(self.sol.isSubsequence(case["s"], case["t"]), case["answer"])

