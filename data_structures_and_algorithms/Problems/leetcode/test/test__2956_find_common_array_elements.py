"""Test file for LC2956 - Find Common Elements Between Two Arrays"""
from unittest import TestCase
from leetcode._2956_find_common_array_elements import Solution, Solution2
"""
Problems % python3 -m unittest leetcode.test.test__2956_find_common_array_elements
"""

TEST_CASES = [
    {
        "nums1":[4,3,2,3,1],
        "nums2":[2,2,5,2,3,6], 
        "answer": [3,4]
    },
    {
        "nums1":[3,4,2,3], 
        "nums2":[1,5], 
        "answer": [0,0]
    },
    {
        "nums1":[5,6,6,7,4,2], 
        "nums2":[2,5,6,8,9], 
        "answer": [4,3]
    }
]

class TestLC2956(TestCase):
    """TestCase class for LC 2956"""

    def setUp(self):
        self.test_cases = TEST_CASES
        self.sol = Solution()
        self.sol2 = Solution2()

    def test_cases(self):
        for test in self.test_cases:
            self.assertEqual(self.sol.findIntersectionValues(test["nums1"],test["nums2"]), test["answer"])
            self.assertEqual(self.sol2.findIntersectionValues(test["nums1"],test["nums2"]), test["answer"])
        