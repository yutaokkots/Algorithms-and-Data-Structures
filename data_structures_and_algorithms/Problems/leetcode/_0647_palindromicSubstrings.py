'''
647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 
Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = []

        for i in range(len(s)):
            for left, right in ((i,i), (i,i+1)):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    answer.append(s[left:right+1])
                    left -= 1
                    right += 1
        
        return len(answer)

class Solution2:
    def countSubstrings(self, s: str) -> int:
        ans = 0 
        n=len(s)
        for center in range(2*n-1):
            left = center//2
            right = left + center%2
            while left>=0 and right<n and left<=right and s[left]==s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans