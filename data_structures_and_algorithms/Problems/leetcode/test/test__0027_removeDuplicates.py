"""Test for LC0027"""
from unittest import TestCase
from leetcode._0027_removeDuplicates import Solution

'''
Problems % python3 -m unittest leetcode.test.test__0027_removeDuplicates
'''

TEST_CASES = [
    {
        "nums": [3,2,2,3],
        "val": 3,
        "output": 2,
        "nums_output": [2,2]
    },
    {
        "nums": [0,1,2,2,3,0,4,2],
        "val": 2,
        "output": 5,
        "nums_output": [0,1,4,0,3]
    },
    {
        "nums": [2,5,4,6,8,3,1,2,9,-2,2,3,5,7,9],
        "val": 2,
        "output": 12,
        "nums_output": [5,4,6,8,3,1,9,-2,3,5,7,9]
    },
]

class TestLC0027(TestCase):
    def setUp(self) -> None:
        self.test_cases = TEST_CASES
        self.sol = Solution()

    def test_cases_01(self):
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"Method01 Subtest No. {i + 1}"):
                self.assertEqual(self.sol.removeElement(nums=case["nums"], val=case["val"]), case["output"])

    def test_cases_02(self):
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"Method02 Subtest No. {i + 1}"):
                self.assertEqual(self.sol.removeElement02(nums=case["nums"], val=case["val"]), case["output"])

    def test_cases_03(self):
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"Method03 Subtest No. {i + 1}"):
                self.assertEqual(self.sol.removeElement03(nums=case["nums"], val=case["val"]), case["output"])
