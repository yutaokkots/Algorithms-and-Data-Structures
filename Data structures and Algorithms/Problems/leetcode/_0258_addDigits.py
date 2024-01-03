"""258. Add Digits"""

"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:

Input: num = 0
Output: 0
 
Constraints:

0 <= num <= 231 - 1

Follow up: Could you do it without any loop/recursion in O(1) runtime?
"""

class Solution:
    """Solution class for adding up all of the digits."""

    def addDigits(self, num: int) -> int: 
        while num >= 10:
            num = sum(map(int, str(num)))
        return num
    
class Solution2:
    """Second solution class for adding up all of the digits."""

    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            new_num = 0
            for s in str(num):
                new_num += int(s)
            num = new_num
        return num  
    
class Solution3:
    """Third solution class for adding up all of the digits."""

    def addDigits(self, num: int) -> int: 
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9