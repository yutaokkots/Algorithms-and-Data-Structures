"""
125. Valid Palindrome
Easy

A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters 
include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:        
        if len(s) == 1 or len(s) == 1:
            return True
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if not s[l].lower() == s[r].lower():
                    return False
                l += 1
                r -= 1

        return True
    
    def isPalindrome2(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            elif not s[r].isalnum():
                r -= 1
                continue
            elif (not s[l].isalnum() and 
                    not s[r].isalnum()):
                l += 1
                r -= 1
                continue
            elif (s[l].isalnum() and 
                    s[r].isalnum() and 
                    s[l].lower() != s[r].lower()):
                return False
            l += 1
            r -= 1
        return True
