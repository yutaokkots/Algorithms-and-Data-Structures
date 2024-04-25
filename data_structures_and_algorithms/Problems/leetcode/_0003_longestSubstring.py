'''
3. Longest substring without repeating characters
Given a string s, find the length of the longest 
substring
without repeating characters.


Example 1
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4
# "pwwkew"
output = 3
'''

from collections import defaultdict

class Solution():
    # solution does not work 
    def lengthOfLongestSubstring1(self, s: str) -> int:
        ## Brute force method:
        left, right = 0, 0
        memo = {}
        counter = 0
        max_value = 0
        while right < len(s) - 1:
            memo.setdefault(counter, [])
            if s[right] in memo[counter]:
                # increment counter to create a new key
                max_value = max(max_value, len(memo[counter]))
                counter += 1
                left += 1
                right = left
            else:
                memo[counter].append(s[right])
                max_value = max(max_value, len(memo[counter]))
                right += 1
        return max_value
    
    def lengthOfLongestSubstring2(self, s: str) -> int:
        left = 0
        max_str = 0
        str_set = set()
        for right in range(len(s)):
            while s[right] in str_set:
                str_set.discard(s[left])
                left += 1
            str_set.add(s[right])
            max_str = max(max_str, right-left+1)
        return max_str

    def lengthOfLongestSubstring3(self, s: str) -> int:
        if not s: 
            return 0
        dict_seen = defaultdict(int)
        left = 0
        max_substring = 0
        for right in range(len(s)):
            curr_letter = s[right]
            dict_seen[curr_letter] += 1
            while dict_seen[curr_letter] > 1:
                dict_seen[s[left]] -= 1
                left += 1
            max_substring = max(max_substring, right + 1 - left)
        return max_substring
    
str_1 = "abcabcbb"
str_2 = "bbbbb"
str_3 = "wwkew"

sol = Solution()
a1 = sol.lengthOfLongestSubstring2(str_1)
a2 = sol.lengthOfLongestSubstring2(str_2)
a3 = sol.lengthOfLongestSubstring2(str_3)

print(a1)
print(a2)
print(a3)






