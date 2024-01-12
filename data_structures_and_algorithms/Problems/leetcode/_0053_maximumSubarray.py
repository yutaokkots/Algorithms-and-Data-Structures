'''
53. Maximum Subarray
Medium

Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.



'''
from typing import List

class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = nums[0]
        current_sum = 0

        for i in range(len(nums)):
            if current_sum < 0:
                current_sum = 0

            current_sum += nums[i]
            max_value = max(max_value, current_sum)

        return max_value

class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            if current_sum < 0:
                current_sum = 0
            current_sum += nums[i]
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum
    
class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0] 

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum