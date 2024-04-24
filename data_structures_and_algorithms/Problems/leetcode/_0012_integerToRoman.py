'''
12. Integer to Roman
Medium

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.
'''

class Solution:
    def integerToRoman(self, num: int) -> str:
        roman_nums = (
            ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
            ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
            ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),
            ("", "M", "MM", "MMM")
        )
        divisor = 1000
        digit_val = 0
        str_roman = ""
        while divisor >= 1:
            digit_place = len(str(int(num))) - 1
            digit_val = int(num // divisor)
            rom_val = roman_nums[digit_place][digit_val]
            str_roman += rom_val
            num = num % divisor
            divisor = divisor / 10
        return str_roman
    
    def integerToRoman02(self, num:int) -> str:
        ones = ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")
        tens = ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC")
        hund = ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM")
        thou = ("", "M", "MM", "MMM")

        return thou[num // 1000] + hund[(num % 1000) // 100] + tens[(num % 100) // 10] + ones[num % 10]
        
sol = Solution()

sol.integerToRoman(3395)

