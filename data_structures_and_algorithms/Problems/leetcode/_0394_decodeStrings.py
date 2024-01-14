"""394. Decode Strings."""

"""
394. Decode Strings.
Medium
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:
    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets '[]'.
    s is guaranteed to be a valid input.
    All the integers in s are in the range [1, 300].
"""

        # "s" : "2[abc]ef3[c2[k]d]",
        # "answer": "abcabcefckkdckkdckkd"
        #
        #   [2, a, b]
        #   "a","b"
        # s = "2[ab]"
        ##     "abab"

from typing import List

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                result = ""
                while stack[-1] != "[":
                    result += stack.pop()
                stack.pop()
                num = ""
                while stack and stack[-1].isnumeric():
                    num += stack.pop()
                stack.append(result * int(num[::-1]))

        return "".join([letter[::-1] for letter in stack])