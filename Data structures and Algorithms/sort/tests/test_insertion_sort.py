import unittest
from insertion_sort import InsertionSort

class InsertionSortTest(unittest.TestCase):
    """Testing for InstionSort class."""
    
    def setUp(self):
        """Set-up method for InsertionSort class."""
        self.case01 = [[9, 3, 6, 2, 1, 11],     [1, 2, 3, 6, 9, 11]]
        self.case02 = [[12, 16, 14, 1, 2, 3],   [1, 2, 3, 12, 14, 16]]
        self.case03 = [
            [(5, "apple"), (2, "banana"), (9, "cherry")], 
            [
                [(5, "apple"), (2, "banana"), (9, "cherry")], 
                [(2, "banana"), (5, "apple"), (9, "cherry")], 
                [(2, "banana"), (5, "apple"), (9, "cherry")]
            ]]
        self.case04 = [
            [(3, "cat"), (3, "bird"), (2, "dog")], 
            [
                [(3, "cat"), (3, "bird"), (2, "dog")], 
                [(3, "cat"), (3, "bird"), (2, "dog")],
                [(2, "dog"), (3, "cat"), (3, "bird")]
            ]]
        self.sorter = InsertionSort()

    def test_insertion_sort(self):
        """Test for 'insertionSort01' method."""
        answer1 = self.sorter.insertionSort01(self.case01[0])
        self.assertEqual(answer1, self.case01[1])
        answer2 = self.sorter.insertionSort01(self.case02[0])
        self.assertEqual(answer2, self.case02[1])

    def test_insertion_sort_snapshot(self):
        """Test for 'insertionSort02' method."""
        answer3 = self.sorter.insertionSort02(self.case03[0])
        self.assertEqual(answer3, self.case03[1])
        answer4 = self.sorter.insertionSort02(self.case04[0])
        self.assertEqual(answer4, self.case04[1])
        