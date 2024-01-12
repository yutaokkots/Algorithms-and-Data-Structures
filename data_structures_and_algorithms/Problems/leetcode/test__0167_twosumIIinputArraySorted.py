# import solution class from this function
from _0167_twosumIIinputArraySorted import Solution

def test_can_twoSum():
    sol = Solution()
    assert sol.twoSum([2,7,11,15], 9) == [1, 2]
    assert sol.twoSum([-1,0], -1) == [1, 2]
    assert sol.twoSum([2,3,4], 6) == [1, 3]

# % pytest _0167_twosumIIinputArraySorted_test.py::test_can_twoSum
#
# pytest naming convention:
# '_0167_twosumIIinputArraySorted_test.py'
# or
# 'test__0167_twosumIIinputArraySorted.py'