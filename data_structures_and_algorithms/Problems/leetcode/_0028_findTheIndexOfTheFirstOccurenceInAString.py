'''
28. Find the index of the first occurence in a string
Easy
Given two string, needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for idx in range(len(haystack) + 1 - len(needle)):
            if haystack[idx : idx + len(needle)] == needle:
                return idx

        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        str_length = len(needle)
        for i in range(str_length, len(haystack)+1):
            if haystack[i-str_length: i] == needle:
                return i-str_length
        return -1