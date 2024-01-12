"""Test Case for LC300 - Longest Increasing Subsequence"""
"""
Problems % python3 -m unittest leetcode.test.test__0300_longestIncreasingSubsequence
"""
from unittest import TestCase
from leetcode._0300_longestIncreasingSubsequence import Solution

TEST_CASES = [
    {
        "nums": [10,9,2,5,3,7,101,18],
        "answer": 4
    },
    {
        "nums": [0,1,0,3,2,3],
        "answer": 4
    },
    {
        "nums": [7,7,7,7,7,7,7],
        "answer": 1
    },
    {
        "nums": [10,9,5,3,7,2,101,18],
        "answer": 3
    },
    {
        "nums": [10,9,2,5,3,4,7,101,1,4,9,18],
        "answer": 6
    },
    {
        "nums": [10,9,4,5,8,3],
        "answer": 3
    },
    {
        "nums": [2,3,4,8,25,81,1,4,54,16,7,8,9,10,11],
        "answer": 8
    },
]

class TestLC0300(TestCase):
    def setUp(self) -> None:
        self.test_cases = TEST_CASES
        self.sol = Solution()

    def test_cases(self):
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"Subtest no. {i + 1}"):
                self.assertEqual(self.sol.lengthOfLIS(case["nums"]), case["answer"])