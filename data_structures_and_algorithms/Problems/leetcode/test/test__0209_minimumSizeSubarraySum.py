'''Unit Test for LC0209 Mininum Size Subarray Sum'''
from unittest import TestCase
from leetcode._0209_minimumSizeSubarraySum import Solution

TEST_CASES = [
    {
        "nums": [2,3,1,2,4,3],
        "target": 7,
        "output": 2
    },
    {
        "nums": [1,4,4],
        "target": 4,
        "output": 1
    },
    {
        "nums": [1,1,1,1,1,1,1,1],
        "target": 11,
        "output": 0
    },
]

class TestLC0209(TestCase):
    def setUp(self) -> None:
        self.test_cases = TEST_CASES
        self.sol = Solution()

    def test_case(self) -> None:
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"Test {i+1}"):
                self.assertEqual(self.sol.minSubArrayLen(target=case["target"], nums=case["nums"]), case["output"])
