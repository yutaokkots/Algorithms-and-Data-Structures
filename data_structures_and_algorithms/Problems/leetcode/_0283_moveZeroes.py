"""283. Move Zeroes"""

"""
283. Move Zeroes
Easy

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

Constraints:
    1 <= nums.length <= 10^4
    -2^31 <= nums[i] <= 2^31 - 1
"""
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                popped_zero = nums.pop(i)
                nums.append(popped_zero)

class Solution2:
    """Previous solution - 2023-07-23"""
    def moveZeroes(self, nums: list[int]) -> list[int]:
        counter = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[counter] == 0:
                nums[i], nums[counter] = nums[counter], nums[i]
            if nums[counter] != 0:
                counter += 1
        return nums

class Solution3:
    """Previous solution - 2023-07-23"""
    def moveZeroes(self,nums:list[int]) -> list[int]:
        counter = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != 0:
                nums[counter] = nums[i]
                counter += 1
        while counter < length:
            nums[counter] = 0
            counter += 1
        return nums