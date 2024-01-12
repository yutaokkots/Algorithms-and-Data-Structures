'''
128. Longest Consecutive Sequence
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

from typing import List

class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums.sort()

        memo = {"init": 1}
        counter = 1
        index_counter = 0

        # for loop that runs through the sorted 'nums' list 
        for i, n in enumerate(nums):
            # in the case where nums[i] is 0, skip
            if i == 0:
                pass
            elif n == nums[i - 1]:
                pass
            elif n - nums[i - 1] == 1:
                counter += 1
            elif n - nums[i - 1] > 1:
                counter = 1
            if counter > 1:
                memo[f"{index_counter}"] = counter
            elif counter == 1:
                index_counter += 1
        
        return max(list(memo.values()))

class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        counter = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set:
                length = 1 
                while nums[i] + length in nums_set:
                    length += 1
                if length > counter:
                    counter = length

        return counter
    
    