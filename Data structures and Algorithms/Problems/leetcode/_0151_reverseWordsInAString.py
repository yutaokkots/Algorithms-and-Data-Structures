'''
151. Reverse Words in a String
Medium

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

'''

class Solution1:
    def reverseWords(self, s: str) -> str:
        left = 0
        word_lst = []
        for right in range(len(s)):
            if right == len(s)-1 and s[right] != " ":
                word_lst.append(s[left:right+1])
                break
            if s[right] == " " and left == right:
                left += 1
                continue
            elif s[right] == " ":
                word_lst.append(s[left:right])
                left = right + 1
        return " ".join(word_lst[::-1])
    
class Solution2:
    def reverseWords(self, s:str) -> str:
        words = s.split()
        return ' '.join(words[::-1])