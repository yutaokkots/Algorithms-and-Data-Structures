"""5. Longest Palindromic Substring"""

'''
5. Longest Palindromic Substring
Medium

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
    1 <= s.length <= 1000
    s consist of only digits and English letters.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            for l, r in ((i,i), (i,i+1)): 
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if (r - l + 1) > len(result):
                        result = s[l:r + 1]
                    l -= 1
                    r += 1

        return result
    
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        result_length = 0 
        
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result_length:
                    result = s[l:r + 1]
                    result_length = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result_length:
                    result = s[l:r + 1]
                    result_length = r - l + 1
                l -= 1
                r += 1
        return result
    
n = 5
for i in range(n):
    print(f"{i=}")
    for l, r in ((i,i), (i,i+1)):
        print(l, r)

