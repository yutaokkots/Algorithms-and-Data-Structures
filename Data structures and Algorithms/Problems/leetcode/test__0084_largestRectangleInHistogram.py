"""Test for LC84, Largest Rectangle in Histogram using unittest"""

import unittest, pytest
from _0084_largestRectangleInHistogram import Solution
unittest.TestCase.maxDiff = None

class TestLargestRectangleInHistogram(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLargestRectangleInHistogram, self).__init__(*args, **kwargs)

        self.sol = Solution()

    def test_LargestRectangle(self):
        with self.subTest():
            self.assertEqual(self.sol.largestRectangleArea([2,1,5,6,2,3]), 10)
        with self.subTest():
            self.assertEqual(self.sol.largestRectangleArea([2,4]), 4)

if __name__ == '__main__':
    unittest.main()