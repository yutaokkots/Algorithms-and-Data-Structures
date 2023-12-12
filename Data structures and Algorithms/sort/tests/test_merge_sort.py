"""Test for merge sort

To run test, run:
    sort % python3 -m unittest -v tests.test_merge_sort
"""
import unittest
from merge_sort import MergeSort

class MergeSortTest(unittest.TestCase):
    def setUp(self):
        self.case01 = [[10, 5, 2, 3, 4, 7], [2,3,4,5,7]]
        self.sort = MergeSort()

    def test_merge_sort(self):
        answer01 = self.sort.mergeSort01(self.case01[0])
        self.assertEqual(answer01, self.case01[1])
