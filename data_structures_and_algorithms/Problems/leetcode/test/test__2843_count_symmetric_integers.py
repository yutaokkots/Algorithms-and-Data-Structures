"""Unit-testing for LC2843."""
from unittest import TestCase
from leetcode._2843_count_symmetric_integers import Solution
"""
Problems % python3 -m unittest leetcode.test.test__2843_count_symmetric_integers
"""

class Test2843(TestCase):
    """Test Case class for LC2843 - count symmetric integers."""
    
    def setUp(self) -> None:
        "Set-up class for LC2843"
        self.testcase01 = {"low":1, "high":100}
        self.testcase02 = {"low":1200, "high":1230}
        self.testcase03 = {"low":121, "high":151}
        self.testcase04 = {"low":1, "high":9}
        self.testcase05 = {"low":22, "high":89}
        self.testcase06 = {"low":22, "high":121}
        self.testcase07 = {"low":11, "high":1123}
        self.soln = Solution()

    def testcase01(self):
        """Method for testcase 01."""
        ans01 = self.soln.countSymmetricIntegers(self.testcase01["low"], self.testcase01["high"])
        self.assertEqual(type(ans01), int)
        self.assertEqual(ans01, 9)  #11, 22, 33, 44, 55, 66, 77, 88, 99

    def testcase02(self):
        """Method for testcase 02."""
        ans02 = self.soln.countSymmetricIntegers(self.testcase02["low"], self.testcase02["high"])
        self.assertEqual(type(ans02), int)
        self.assertEqual(ans02, 4)  # 1203, 1212, 1221, 1230

    def testcase03(self):
        """Method for testcase 03."""
        ans03 = self.soln.countSymmetricIntegers(self.testcase03["low"], self.testcase03["high"])
        self.assertEqual(type(ans03), int)
        self.assertEqual(ans03, 0)  # no solutions

    def testcase04(self):
        """Method for testcase 04."""
        ans04 = self.soln.countSymmetricIntegers(self.testcase04["low"], self.testcase04["high"])
        self.assertEqual(type(ans04), int)
        self.assertEqual(ans04, 0)  # no solutions

    def testcase05(self):
        """Method for testcase 05."""
        ans05 = self.soln.countSymmetricIntegers(self.testcase05["low"], self.testcase05["high"])
        self.assertEqual(type(ans05), int)
        self.assertEqual(ans05, 7)  # 22, 33, 44, 55, 66, 77, 88

    def testcase06(self):
        """Method for testcase 06."""
        ans06 = self.soln.countSymmetricIntegers(self.testcase06["low"], self.testcase06["high"])
        self.assertEqual(type(ans06), int)
        self.assertEqual(ans06, 8)  # 22, 33, 44, 55, 66, 77, 88, 99,  

    def testcase07(self):
        """Method for testcase 07, "low":11, "high":1123."""
        ans07 = self.soln.countSymmetricIntegers(self.testcase07["low"], self.testcase07["high"])
        self.assertEqual(type(ans07), int)
        self.assertEqual(ans07, 14) # 11, 22, 33, 44, 55, 66, 77, 88, 99 (9)    -> 100, 999 :: 10000
                                    # 1001, 1010, 1102, 1111, 1120 (5) => 14    -> 
