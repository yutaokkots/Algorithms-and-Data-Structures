'''Unit tests for LC0012, Integer to Roman '''
from unittest import TestCase
from leetcode._0012_integerToRoman import Solution

'''
Problems % python3 -m unittest leetcode.test.test__0012_integerToRoman
'''

TEST_CASES = [
    {
        "input": 3,
        "output": "III",
    },
    {
        "input": 87,
        "output": "LXXXVII",   
    },
    {
        "input": 3924,
        "output": "MMMCMXXIV",          
    },
    {
        "input": 1014,
        "output": "MXIV",          
    },
    {
        "input": 994,
        "output": "CMXCIV",          
    },
]

class TestLC0012(TestCase):
    def setUp(self) -> None:
        self.test_cases = TEST_CASES
        self.sol = Solution()
    
    def tests(self) -> None:
        for i, case in enumerate(self.test_cases):
            input = case["input"]
            output = case["output"]
            with self.subTest(f"Test {i+1}"):
                self.assertEqual(self.sol.integerToRoman(input), output)
