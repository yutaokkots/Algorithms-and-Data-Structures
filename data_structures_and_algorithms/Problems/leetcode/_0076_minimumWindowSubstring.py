"""76. Mininum Window Substring"""

"""
76. Mininum Window Substring
Hard

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 
Constraints:
    m == s.length
    n == t.length
    1 <= m, n <= 10^5
    s and t consist of uppercase and lowercase English letters.
"""
from collections import defaultdict

class Solution:
    """Solution class for LC76, based on @sumit4199."""
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_dict = defaultdict(int)
        for char in t:
            t_dict[char] += 1
        
        left = 0
        min_length = float('inf')
        min_left = 0
        count = len(t)

        for right in range(len(s)):
            current_char = s[right]

            if current_char in t_dict:
                t_dict[current_char] -= 1
                if t_dict[current_char] >= 0:
                    count -= 1
            while count == 0:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left
                left_char = s[left]
                if left_char in t_dict:
                    t_dict[left_char] += 1
                    if t_dict[left_char] > 0:
                        count += 1
                left += 1

        return "" if min_length == float('inf') else s[min_left:min_left + min_length]