"""1456. Maximum Number of Vowels in a Substring of Given Length"""

"""
1456. Maximum Number of Vowels in a Substring of Given Length
Medium

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:
    1 <= s.length <= 10^5
    s consists of lowercase English letters.
    1 <= k <= s.length
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ("a", "e", "i", "o", "u")
        s_lst = [1 if char in vowels else 0 for char in s ]
        left:int = 0
        prev:int = 0
        max_value = curr_value = s_lst[left:k].count(1)

        for right in range(k, len(s_lst)):
            if right > 0:
                curr_value = curr_value - s_lst[prev] + s_lst[right] 
                prev += 1
            max_value = max(max_value, curr_value)
            left += 1
            
        return max_value