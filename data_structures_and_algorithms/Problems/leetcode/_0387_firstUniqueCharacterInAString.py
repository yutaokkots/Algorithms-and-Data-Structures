""" 387. First Unique Character In A String. """

"""
387. First Unique Character In A String. 
Easy

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
    1 <= s.length <= 10^5
    s consists of only lowercase English letters.
"""
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter_dict = Counter(s)
        for i, char in enumerate(s):      
            if counter_dict[char] - 1 == 0:
                return i
        return -1