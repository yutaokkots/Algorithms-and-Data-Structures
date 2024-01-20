"""907. Sum Of Subarray Minimums"""

"""
907. Sum Of Subarray Minimums
Medium

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:
Input: arr = [11,81,94,43,3]
Output: 444

Constraints:
    1 <= arr.length <= 3 * 10^4
    1 <= arr[i] <= 3 * 10^4
"""

from typing import List
class Solution:
    """Solution for LC907, adapted from code by @MarkSPhilip31."""

    def sumSubarrayMins(self, arr: List[int]) -> int:
        """Monotonic Stack solution (increasing or non-increasing values)."""
        MOD = 10**9 + 7
        stack = []
        sum_of_mins = 0
        for i in range(len(arr) + 1):
            while (stack and 
                    (i == len(arr) or arr[stack[-1]] >= arr[i])):
                mid = stack.pop()
                left_bound = stack[-1] if stack else -1
                right_bound = i
                count = (mid - left_bound) * (right_bound - mid) % MOD
                sum_of_mins += (count * arr[mid]) % MOD
                sum_of_mins %= MOD
            stack.append(i)
        return int(sum_of_mins)