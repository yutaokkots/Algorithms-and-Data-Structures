'''
131. Palindrome Partitioning
Medium

Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s. 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

'''

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, partition = [], []

        def backtrack(i):
            if i >= len(s):
                result.append(partition.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    partition.append(s[i : j + 1])
                    backtrack(j + 1)
                    partition.pop()

        backtrack(0)
        return result

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

    #def isPalindrome(self, s, l, r):
    #    return list(s[l:r+1])[::-1] == list(s[l:r+1])
    

sol = Solution()

ans = sol.partition("ababraba")
print(ans)
## [['a', 'b', 'a', 'b', 'r', 'a', 'b', 'a'], ['a', 'b', 'a', 'b', 'r', 'aba'], ['a', 'bab', 'r', 'a', 'b', 'a'], ['a', 'bab', 'r', 'aba'], ['aba', 'b', 'r', 'a', 'b', 'a'], ['aba', 'b', 'r', 'aba']]
