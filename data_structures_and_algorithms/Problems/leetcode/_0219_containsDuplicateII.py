'''
219. Contains Duplicate
Easy

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    0 <= k <= 10^5
'''

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap and i - hashmap[nums[i]] <= k:
                return True
            else:
                hashmap[nums[i]] = i
        return False

    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        min_diff = float('inf')
        for i in range(len(nums)):
            hash_key = hashmap.get(nums[i])
            if (hash_key == None):
                hashmap[nums[i]] = i
            elif (nums[i] in hashmap.keys()):
                min_diff = min(min_diff, abs(hashmap[nums[i]] - i))
                hashmap[nums[i]] = i

        return k >= min_diff 