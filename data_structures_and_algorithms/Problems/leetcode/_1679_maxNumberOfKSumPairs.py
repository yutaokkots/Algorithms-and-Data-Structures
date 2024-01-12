"""1679. Max Number of K-Sum Pairs"""

"""
1679. Max Number of K-Sum Pairs
Medium

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= 10^9
"""

from typing import List

class Solution:
    """More optimal solution for LC1679.
    
    Big-O
    -----
    time: O(n log-n) 
    space: O(n)
    """
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            summation = nums[left] + nums[right]
            if summation < k:
                left += 1
            elif summation > k:
                right -= 1
            else:
                count +=1
                left += 1
                right -= 1
        return count

class Solution2:
    """Naive solution for LC1679.

    Big-O
    -----
    time: O(n^2) 
    space: O(n)
    """
    def maxOperations(self, nums: List[int], k: int) -> int:
        right = 0
        count = 0
        seen = set()
        for left in range(len(nums)):
            while (right < len(nums)):
                if right in seen:
                    right += 1
                if left in seen or right >= len(nums):
                    break
                if (nums[left] + nums[right] == k and 
                        left != right and
                        right not in seen and 
                        left not in seen):
                    seen.add(left)
                    seen.add(right)
                    count += 1
                right += 1
            right = left
            right += 1
            if left < len(nums) - 2:
                right += 1
        return count
    