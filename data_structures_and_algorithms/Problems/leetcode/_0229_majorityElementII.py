'''
229. Majority Element II
Medium

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:

Input: nums = [3,2,3]
Output: [3]

Example 2:

Input: nums = [1]
Output: [1]

Example 3:

Input: nums = [1,2]
Output: [1,2]
'''
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # O(N) time and O(1) space
        # majority elements -> up to 2
        
        ## LL? [3,2,3]
        n1 = 0
        n2 = 0
        count1 = 0
        count2 = 0

        for num in nums:
            if num == n1:
                count1 += 1
            elif num == n2:
                count2 += 1
            elif count1 == 0:
                n1 = num
                count1 = 1
            elif count2 == 0:
                n2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = 0
        count2 = 0
        for num in nums:
            if num == n1:
                count1 += 1
            elif num == n2:
                count2 += 1

        result = []
        if count1 > len(nums) / 3:
            result.append(n1)
        if count2 > len(nums) / 3:
            result.append(n2)

        return result