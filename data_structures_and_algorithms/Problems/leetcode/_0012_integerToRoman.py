'''
12. Integer to Roman
Medium


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
    
sol = Solution()

sol.integerToRoman(3395)

