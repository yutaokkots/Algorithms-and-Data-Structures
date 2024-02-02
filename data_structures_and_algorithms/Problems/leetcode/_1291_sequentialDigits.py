"""1291. Sequential Digits"""

"""
1291. Sequential Digits
Medium

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
Input: low = 100, high = 300
Output: [123,234]

Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 
Constraints:
    10 <= low <= high <= 10^9
"""
from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        for digit in range(1, 10):
            num = digit
            next_digit = num + 1
            while next_digit <= 9 and num <= high:
                num = num * 10 + next_digit
                if num >= low and num <= high:
                    result.append(num)
                next_digit += 1
        return sorted(result)
    
class Solution2:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        range_lst = [12, 23, 34, 45, 56, 67, 78, 89,
            123, 234, 345, 456, 567, 678, 789,
            1234, 2345, 3456, 4567, 5678, 6789,
            12345, 23456, 34567, 45678, 56789,
            123456, 234567, 345678, 456789,
            1234567, 2345678, 3456789,
            12345678, 23456789,
            123456789]

        answer_lst = []
        for n in range_lst:
            if n < low:
                continue
            elif low <= n <= high:
                answer_lst.append(n)
            else:
                break
        return answer_lst