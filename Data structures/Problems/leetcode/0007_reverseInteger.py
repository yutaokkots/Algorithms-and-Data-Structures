# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

class Solution:
    def reverse(self, x: int) -> int:
        str_number = str(x)
        minus = False
        bank = []
        for n in str_number:
            if n == "-":
                minus = True
                continue
            bank.append(n)
        bank.reverse()
        str_new_number = "".join(bank)
        answer = int(str_new_number)
        if answer > 2147483647:
            answer = 0
        return -answer if minus else answer