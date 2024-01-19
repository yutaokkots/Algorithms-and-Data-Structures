"""1004. Max Consecutive Ones III"""

"""
1004. Max Consecutive Ones III
Medium

#####
Also see: 1493. Longest Subarray of 1's After Deleting One Element"
#####

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 
Constraints:
    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.
    0 <= k <= nums.length
"""

from typing import List

class Solution:
    """Sliding-window solution for LC1004."""
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left + 1

class Solution2:
    """Naive inefficient solution for LC1004."""
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        right = 0
        k_val = k
        for left in range(len(nums)):
            while right < len(nums):
                if not k_val and nums[right] == 0:
                    break
                if k_val and nums[right] == 0:
                    k_val -= 1
                right += 1
                max_length = max(max_length, len(nums[left:right]))
            right = left + 1
            k_val = k
        return max_length