"""Test file for LC2952 - Minimum Number of Coins to be Added"""

"""
Problems % python3 -m unittest leetcode.test.test__2952_min_number_of_coins_to_be_added
"""
from unittest import TestCase
from leetcode._2952_min_number_of_coins_to_be_added import Solution, Solution2

TEST_CASES = [
    {
        "coins": [1,4,10],
        "target": 19,
        "answer": 2     # [1,2,4,8,10]
    },
    {
        "coins": [1,4,10,5,7,19],
        "target": 19,
        "answer": 1     # [1,2,4,5,7,10,19]
    },
    {
        "coins": [1,1,1],
        "target": 20,
        "answer": 3     # [1,1,1,4,8,16]
    },
    {
        "coins": [1],
        "target": 19,
        "answer": 4     # [1,2,4,8,16]
    },
    {
        "coins": [1,1,1,1],
        "target": 25,
        "answer": 3     # [1,1,1,1,5,10,20]
    },
]

class TestLC2952(TestCase):
    """TestCase class for LC 2956"""

    def setUp(self):
        self.test_cases = TEST_CASES
        self.sol = Solution()
        self.sol2 = Solution2()

    def test_cases(self):
        for case in self.test_cases:
            self.assertEqual(self.sol.minimumAddedCoins(case["coins"],case["target"]),case["answer"])
            self.assertEqual(self.sol2.minimumAddedCoins(case["coins"],case["target"]),case["answer"])