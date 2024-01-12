"""Test for quick sort

To run test, run:
    sort % python3 -m unittest -v tests.test_quick_sort
"""

import unittest
from quick_sort import QuickSort

class QuickSortTest(unittest.TestCase):
    def setUp(self):
        self.case01 = [[10, 5, 2, 3, 4, 7], [2,3,4,5,7,10]]
        self.sort = QuickSort()

    def test_quick_sort(self):
        answer1 = self.sort.quickSort01(self.case01[0])
        self.assertEqual(answer1, self.case01[1])
