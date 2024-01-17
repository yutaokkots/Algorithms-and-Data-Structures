"""1207. Unique Number of Occurrences"""

"""
1207. Unique Number of Occurrences
Easy

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Constraints:
    1 <= arr.length <= 1000
    -1000 <= arr[i] <= 1000
"""

from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_ct = Counter(arr)
        lst = sorted(arr_ct.values(), key=lambda x: x)
        prev = None
        for ct in lst:
            if prev == ct:
                return False
            prev = ct
        return True

class Solution2:
    """Second attempt at LC1207."""
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ct_dict = Counter(arr)
        set_values = set(ct_dict.values())
        return len(set_values) == len(ct_dict.values())