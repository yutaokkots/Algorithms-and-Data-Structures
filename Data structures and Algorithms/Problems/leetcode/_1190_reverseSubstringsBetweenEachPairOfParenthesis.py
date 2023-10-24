'''
1190. Reverse Substrings Between Each Pair of Parentheses
Medium

You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

Example 1:

Input: s = "(abcd)"
Output: "dcba"

Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string. 

Constraints:

1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.

'''

class Solution:
    def reverseParentheses(self, s: str) -> str:
        str_lst = list(s)
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
                continue
            if s[i] == ")":
                opening_index = stack.pop()
                sublst = str_lst[opening_index: i+ 1]
                sublst.reverse()
                str_lst[opening_index: i + 1] = sublst
        answer = []
        for n in str_lst:
            if n != '(' and n != ')':
                answer.append(n)
        return "".join(answer)