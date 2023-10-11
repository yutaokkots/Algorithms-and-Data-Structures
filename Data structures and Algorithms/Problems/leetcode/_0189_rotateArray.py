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
        ## Solution 2 - O(k) time complexity; O(k) space complexity.
        #########
        if k:                   # if k is non-zero
            k = k % len(nums)   # adjusts value of k, in case input k is greater than len(nums).
            shift = nums[-k:]   # creates a shallow copy, 'shift', from -k index to end.
            nums[-k:] = []      # deletes from -k index to end, in the 'nums' list.
            nums[0:0] = shift   # at index 0 to index 0 of 'nums', inserts the shallow copy, 'shift'. 

    def rotate3(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #################
        ## Solution 3 (slice)
        #########
        if k != 0:
            size = len(nums)
            move = (size + k) % size

            shift = nums[-move:]
            nums[-move:] = []
            nums[0:0] = shift
