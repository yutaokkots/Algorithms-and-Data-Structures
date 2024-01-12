"""Test Case for 1235 -  Maximum Profit in Job Scheduling"""

"""
Problems % python3 -m unittest leetcode.test.test__1235_maximumProfitInJobScheduling
"""
from unittest import TestCase
from leetcode._1235_maximumProfitInJobScheduling import Solution

TEST_CASES = [
    {
        "startTime": [1,2,3,3],
        "endTime": [3,4,5,6],
        "profit": [50,10,40,70],
        "answer": 120
    },
    {
        "startTime": [1,2,3,4,6],
        "endTime": [3,5,10,6,9],
        "profit": [20,20,100,70,60],
        "answer": 150
    },
    {
        "startTime": [1,1,1],
        "endTime": [2,3,4],
        "profit": [5,6,4],
        "answer": 6
    },
    {
        "startTime": [6,15,7,11,1,3,16,2],
        "endTime": [19,18,19,16,10,8,19,8],
        "profit": [2,9,1,19,5,7,3,19],
        "answer": 41
    },
    {
        "startTime": [24,24,7,2,1,13,6,14,18,24],
        "endTime": [27,27,20,7,14,22,20,24,19,27],
        "profit": [6,1,4,2,3,6,5,6,9,8],
        "answer": 20
    },
]

class TestLC1235(TestCase):
    def setUp(self):
        self.test_cases = TEST_CASES
        self.sol = Solution()

    def test_cases(self):
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"Test {i + 1}"):
                """Testing each test-case as a Sub-test"""
                self.assertEqual(
                    self.sol.jobScheduling(
                        startTime=case["startTime"],
                        endTime=case["endTime"],
                        profit=case["profit"]), 
                    case["answer"])