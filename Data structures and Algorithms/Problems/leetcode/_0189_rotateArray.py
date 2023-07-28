from typing import List

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]


class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #################
        ## Solution 1 (O(N) time)
        #########

        size = len(nums)
        move = (size + k) % size
        for i in range(move):
            element = nums.pop()
            nums.insert(0,element)

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #################
        ## Solution 2 (slice)
        #########
        if k != 0:
            size = len(nums)
            move = (size + k) % size

            shift = nums[-move:]
            nums[-move:] = []
            nums[0:0] = shift