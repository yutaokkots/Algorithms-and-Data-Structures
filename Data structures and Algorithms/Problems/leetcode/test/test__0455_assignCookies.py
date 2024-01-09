"""Testcase for LC455 - Assign Cookies"""

from unittest import TestCase
from leetcode._0455_assignCookies import Solution

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
    }
]


class TestLC455(TestCase):
    """Test class for LC455 """

    def setUp(self) -> None:
        self.test_cases = TEST_CASES    
        self.sol = Solution()

    def test_cases(self):
        for case in self.test_cases:
            self.assertEqual(self.sol.findContentChildren(g=case["g"], s=case["s"]), case["answer"])