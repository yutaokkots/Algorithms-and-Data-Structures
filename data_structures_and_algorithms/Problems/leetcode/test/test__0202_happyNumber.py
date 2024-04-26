'''Test for LC0202 - Happy Number'''

from unittest import TestCase
from leetcode._0202_happyNumber import Solution

TEST_CASES = [
    {
        "input": 16,
        "output": False
    },
    {
        "input": 19,
        "output": True
    },
    {
        "input": 2,
        "output": False
    }
]

class TestLC0202(TestCase):
    ''' Test for LC0202 - Happy Number.

    Write an algorithm to determine if a number n is happy.
    A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum 
        of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), 
        or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

    Return true if n is a happy number, and false if not.

    example:16 -> 1² + 6² ->  37 -> 3² -> 7² -> 58 -> 5² + 8² -> 64+25, 89 -> 8² + 9² -> 64+81, 145 -> 
                    #  1² + 4² + 5² -> 1+16+25, 42 -> 4² + 2² -> 16+4, 20 -> 2² + 0² -> 4 + 0, 4 -> 4² ->  16
                    # 1² + 6² . . . 
    16 repeats

    example: 2 -> 2² -> 4 -> 4² -> 16 -> 1² + 6².. 

    '''
    def setUp(self) -> None:
        self.test_cases = TEST_CASES
        self.sol = Solution()
        return super().setUp()
    
    def tests(self):
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"Test {i + 1}"):
                self.assertEqual(self.sol.isHappy(case["input"]), case["output"])