'''
224. Basic Calculator
Hard

Given a string s representing a valid expression, implement a basic calculator to evaluate it, 
and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings 
as mathematical expressions, such as eval().

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Constraints:
    1 <= s.length <= 3 * 10^5
    s consists of digits, '+', '-', '(', ')', and ' '.
    s represents a valid expression.
    '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
    '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
    There will be no two consecutive operators in the input.
    Every number and running calculation will fit in a signed 32-bit integer.
'''

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        ans_sum = 0
        curr_sum = 0
        pos_neg = 1

        for str_s in s:
            if str_s.isdigit():
                curr_sum = (curr_sum * 10) + int(str_s)
            elif str_s in '-+':
                ans_sum += pos_neg * curr_sum
                curr_sum = 0
                if str_s == "+":
                    pos_neg = 1
                else:
                    pos_neg = -1
            elif str_s == '(':
                stack.append(ans_sum)
                stack.append(pos_neg)
                pos_neg = 1
                ans_sum = 0
            elif str_s == ')':
                ans_sum += curr_sum * pos_neg
                ans_sum *= stack.pop()
                ans_sum += stack.pop()
                curr_sum = 0
        return ans_sum + (curr_sum * pos_neg)
