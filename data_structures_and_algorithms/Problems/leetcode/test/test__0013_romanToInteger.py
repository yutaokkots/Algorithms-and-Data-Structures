'''Unit Test for Roman to Integer'''
from unittest import TestCase
from leetcode._0013_romanToInteger import Solution

'''
Problems % python3 -m unittest leetcode.test.test__0013_romanToInteger
'''

TEST_CASES = [
    {
        "input": 'III',
        "output": 3,
    },
    {
        "input": 'LVIII',
        "output": 58,
    },
    {
        "input": 'MCMXCIV',
        "output": 1994,
    },
    {
        "input": 'MMMDCCCXCIX',
        "output": 3899,
    },
    {
        "input": 'MMMCMXCIX',
        "output": 3999,
    }
]

class TestLC0013(TestCase):
    def setUp(self) -> None:
        self.test_cases = TEST_CASES
        self.sol = Solution()

    def test_case(self):
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"Test {i + 1}"):
                input = case["input"]
                output = case["output"]
                self.assertEqual(self.sol.romanToInt(input), output)