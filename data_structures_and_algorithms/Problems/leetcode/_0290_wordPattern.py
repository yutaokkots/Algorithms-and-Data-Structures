'''
290. Word Pattern
Easy

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:
    1 <= pattern.length <= 300
    pattern contains only lower-case English letters.
    1 <= s.length <= 3000
    s contains only lowercase English letters and spaces ' '.
    s does not contain any leading or trailing spaces.
    All the words in s are separated by a single space.
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_lst = s.split()
        if len(s_lst) != len(pattern):
            return False
            
        hashmap = {}
        for p_letter, word in zip(pattern, s_lst):
            value_p = hashmap.get(p_letter)
            if (value_p == None and 
                    word not in hashmap.values()): 
                hashmap[p_letter] = word
            elif (value_p == None or
                    hashmap[p_letter] != word):
                return False

        return True