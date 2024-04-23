"""Test Case for LC0122."""
from unittest import TestCase
from leetcode._0122_bestTimeToBuySellStockII import Solution

"""
Problems % python3 -m unittest leetcode.test.test__0122_bestTimeToBuySellStockII
"""

TEST_CASES = [
    {
        "prices": [7,1,5,3,6,4],
        "output": 7
    },
    {
        "prices": [1,2,3,4,5],
        "output": 4
    },
    {
        "prices": [7,6,4,3,1],
        "output": 0
    }
]

class TestLC0122(TestCase):
    """TestLC0122 class is an Abstraction of TestCase."""
    def setUp(self) -> None:
        self.test_cases = TEST_CASES
        self.sol = Solution()

    def test_cases(self) -> None:
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"Test {i + 1}"):
                self.assertEqual(self.sol.maxProfit(case["prices"]), case["output"])
            
