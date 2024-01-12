"""2843. Count Symmetric Integers"""

"""
2843. Count Symmetric Integers
Easy.

You are given two positive integers low and high.

An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.

Return the number of symmetric integers in the range [low, high].

Example 1:

Input: low = 1, high = 100
Output: 9
Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.

Example 2:

Input: low = 1200, high = 1230
Output: 4
Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.
 
Constraints:
1 <= low <= high <= 104
"""

class Solution:
    """Solution class for LC2843 - Count Symmetric Integers."""

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """First solution method."""
        counter = 0
        for n in range(low, high + 1):
            if 99 < n < 1000:
                continue
            str_n:str = str(n)
            str_length:int = len(str_n)
            if str_length % 2 != 0:
                continue
            else:
                if  self.digit_symmetry(str_n, str_length / 2):
                    counter += 1
        return counter
    
    def digit_symmetry(self, number_str:str, middle:int) -> bool:
        first = 0
        second = 0
        for i, n in enumerate(number_str):
            if i < middle:
                first += int(n)
            else:
                second += int(n)
        return first == second

    def countSymmetricIntegers02(self, low: int, high: int) -> int:
        """A solution method contributed on LC2843.
        
        map() function applies the int() function to the substring.
        """
        counter = 0
        for i in range(low, high + 1):
            s = str(i)
            if len(s) % 2 == 1:
                continue
            if sum(map(int, s[:len(s) // 2])) == sum(map(int, s[len(s) // 2:])):
                counter += 1
        return counter
    