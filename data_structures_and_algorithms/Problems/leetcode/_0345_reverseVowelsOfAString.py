'''
345. Reverse Vowels of a String
Easy

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"

'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1

        lst_s = list(s)
        v = ("A", "a", "E", "e", "I", "i", "O", "o", "U", "u")
        while left < right:
            if lst_s[right] in v and lst_s[left] in v:
                lst_s[right], lst_s[left] = lst_s[left], lst_s[right]
                right -= 1
                left += 1

            if lst_s[right] not in v:
                right -= 1
            if lst_s[left] not in v:
                left += 1

        return "".join(lst_s)