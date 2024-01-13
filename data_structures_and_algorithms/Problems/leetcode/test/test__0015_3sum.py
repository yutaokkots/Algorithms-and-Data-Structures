""" Unit tests for Three-sum problem (LC15)
Created a single unit-test that contains multiple asserts, for simplicity.
"""
import pytest, unittest
from _0015_3sum import Solution

@pytest.fixture
def solution():
    return Solution()

def test_3sum(solution):
    case = unittest.TestCase()
    case.assertCountEqual(solution.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])
    case.assertCountEqual(solution.threeSum([0, 0, 0]), [[0, 0, 0]])
    case.assertCountEqual(solution.threeSum([-2, 0, 1, 1, 2]), [[-2, 0, 2], [-2, 1, 1]])
    case.assertCountEqual(solution.threeSum([1, 2, -2, -1]), [])
    case.assertCountEqual(solution.threeSum([3, -2, 1, 0]), [])
    case.assertCountEqual(solution.threeSum([-1, -1, -1, 0, 0, 0, 1, 1, 1]), [[-1, 0, 1], [0, 0, 0]])
    case.assertCountEqual(solution.threeSum([1, -1, 0]), [[-1, 0, 1]])
    case.assertCountEqual(solution.threeSum([0, 0, 0, 0]), [[0, 0, 0]])
    case.assertCountEqual(solution.threeSum([1, -1, -1, 0, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
    case.assertCountEqual(solution.threeSum([2, 2, 2, 2, 2]), [])
    case.assertCountEqual(solution.threeSum([1, 1, -2]), [[-2, 1, 1]])
    case.assertCountEqual(solution.threeSum([-3, -1, 2, 4, 5]), [[-3, -1, 4]])
    case.assertCountEqual(solution.threeSum([0, 0, 0, 1, -1, 2, -2]), [[0, 0, 0], [-1, 0, 1], [-2, 0, 2]])
    case.assertCountEqual(solution.threeSum([1, -1, 1, -1, 1, -1]), [])
    case.assertCountEqual(solution.threeSum([1, -1, 2, -2]), [])
    case.assertCountEqual(solution.threeSum([5, -5, 0, 0]), [[-5, 0, 5]])
    case.assertCountEqual(solution.threeSum([3, 0, -2, -1, 1, 2]), [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]])
    case.assertCountEqual(solution.threeSum([4, 2, -1, 0, -2, -1, -4]), [[-4, 0, 4], [-2, 0, 2], [-1, -1, 2]])
    case.assertCountEqual(solution.threeSum([-1, -2, -3, -4, -5]), [])
