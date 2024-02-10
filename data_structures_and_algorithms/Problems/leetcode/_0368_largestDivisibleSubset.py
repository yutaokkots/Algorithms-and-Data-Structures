"""368. Largest Divisible Subset"""

"""
368. Largest Divisible Subset
Medium

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Example 1:
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:
Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 
Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 2 * 10^9
All the integers in nums are unique.
"""
from typing import List

test_case = [5,9,18,54,108,540,90,180,360,720]

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        subsets = {-1: set()}
        nums.sort()
        for n in nums:
            subsets[n] = max([subsets[k] for k in subsets if n % k == 0], key=len) | {n}
        
        return list(max(subsets.values(), key=len))