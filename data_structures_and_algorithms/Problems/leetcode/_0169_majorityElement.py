from typing import List
import collections

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement1(self, nums: List[int]) -> int:
        #################
        ## Solution 1 (using heap and collections.Counter())
        #########

        import heapq
        heap = []
        count = collections.Counter(nums)
        for v in set(nums):
            heapq.heappush(heap, (-1 * count[v], v))
        return heapq.heappop(heap)[1]
    
    def majorityElement2(self, nums: List[int]) -> int:
        #################
        ## Solution 2 (using collections.Counter() and sorted())
        #########

        count = collections.Counter(nums)
        sorted_dict = sorted(count.items(), key=lambda x: x[1])
        return sorted_dict[-1][0]

        ## one-liner
        # return sorted(collections.Counter(nums).items(), key=lambda x: x[1])[-1][0]
    
    def majorityElement3(self, nums: List[int]) -> int:
        #################
        ## Solution 3
        #########
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        return nums[len(nums) // 2]