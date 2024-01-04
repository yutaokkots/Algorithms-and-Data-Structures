"""Test case for LC2945"""
from unittest import TestCase
from leetcode._2945_find_max_non_decreasing_array_length import Solution

TEST_CASES2945 = [
    [[5,2,2], 1],
    [[1,2,3,4], 4],
    [[4,3,2,6], 3],
    [[1], 1],
    [[1,4,3,2,1], 3],
    [[1,1,1,1,1], 2],
    [[1,1,1,1,1,1], 3],
    [[1,1,1,1,1,1,1], 3],
    [[5,1,1,1,1,1,1], 2],
    [[4,3,2,6,7], 4],
    [[4,3,2,6,1], 3],
    [[4,3,3,6,1], 3],
    [[4,3,3,3,6,1], 3],
    [[4,3,1,1,6,1,9], 4],
    [[1,2,3,1,5,6], 5],
    [[1,2,3,1,5,6,3,4], 6],
    [[272,482,115,925,983], 4],
    [[2,5,1,9,10,11,3,14], 6],
    [[2,5,1,9,10,8,3,14], 6],
]

TEST_NON_DECREASING = [
    [[1,2,3,4], True],
    [[1,2,3,6], True],
    [[3,4,5,10], True],
    [[1,2,1,2], False],
    [[5,2,3,4], False],
    [[10], True],
]

class Test2945(TestCase):
    """Test class for LC2945."""
    def setUp(self):
        self.soln = Solution()
        self.test_cases = TEST_CASES2945
        self.test_nd = TEST_NON_DECREASING
    
    def test_nondecreasing(self):
        for case, answer in self.test_nd:
            self.assertEqual(self.soln.check_non_decreasing(case), answer)

    def testcases(self):
        for idx, case_set in enumerate(self.test_cases):
            case, answer = case_set
            with self.subTest(f"Subtest {idx+1}"):
                print(f"\nSubtest {idx+1}: {case}")
                self.assertEqual(type(answer),int)
                print(self.soln.findMaximumLength(case))
                self.assertEqual(self.soln.findMaximumLength(case), answer)