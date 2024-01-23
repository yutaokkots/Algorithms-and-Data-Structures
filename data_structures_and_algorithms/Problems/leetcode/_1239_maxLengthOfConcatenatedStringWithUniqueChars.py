"""1239. Maximum Length of a Concatenated String with Unique Characters"""

"""
1239. Maximum Length of a Concatenated String with Unique Characters
Medium

You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
 
Constraints:
    1 <= arr.length <= 16
    1 <= arr[i].length <= 26
    arr[i] contains only lowercase English letters.
"""

from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.max_length = 0
        self.backtrack(arr, "", 0, self.max_length)
        return self.max_length

    def backtrack(self, arr, current, start, max_length):
        if self.max_length < len(current):
            self.max_length = len(current)
        for i in range(start, len(arr)):
            if not self.is_valid(current, arr[i]):
                continue
            self.backtrack(arr, current + arr[i], i + 1, self.max_length)

    def is_valid(self, current_string, new_string):
        char_set = set()
        for char in new_string:
            if char in char_set:
                return False
            char_set.add(char)
            if char in current_string:
                return False
        return True