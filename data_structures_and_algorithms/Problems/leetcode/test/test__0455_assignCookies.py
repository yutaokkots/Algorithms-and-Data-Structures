"""Testcase for LC455 - Assign Cookies"""

"""
Problems % python3 -m unittest leetcode.test.test__0455_assignCookies
"""

from unittest import TestCase
from leetcode._0455_assignCookies import Solution
from .lc0455_test_cases import test_case_05, test_case_06

TEST_CASES = [
    {
        "g": [1,2,3],
        "s": [1,1],
        "answer": 1
    },
    {
        "g": [1,2],
        "s": [1,2,3],
        "answer": 2
    },
    {
        "g": [1,2,2],
        "s": [2,1,1],
        "answer": 2
    },
    {
        "g": [2,2],
        "s": [2,1,3],
        "answer": 2
    },
    test_case_05,
    test_case_06,
    {
        "g": [2,3,5],
        "s": [2,1,4,4],
        "answer": 2
    }
]

class TestLC455(TestCase):
    """Test class for LC455 """

    def setUp(self) -> None:
        self.test_cases = TEST_CASES    
        self.sol = Solution()

    def test_cases(self):
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"Test case {i + 1}"):
                self.assertEqual(self.sol.findContentChildren(g=case["g"], s=case["s"]), case["answer"])