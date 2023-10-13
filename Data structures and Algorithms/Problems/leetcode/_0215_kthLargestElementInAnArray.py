'''
215. Kth Largest Element in an Array
Medium

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

import heapq
from typing import List

class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        counter = 0
        j = len(nums) - k
        while counter < j:
            heapq.heappop(nums)
            counter += 1
        
        return nums[0]
    
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        counter = 0
        heapq.heapify(nums)
        while counter < k - 1:
            heapq.heappop(nums)
            counter += 1
        
        return -nums[0]