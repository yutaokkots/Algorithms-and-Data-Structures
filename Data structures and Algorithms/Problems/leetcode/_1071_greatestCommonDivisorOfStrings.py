'''
1071. Greatest Common Divisor of Strings
Easy

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

Example 4:

Input: str1 = "ABABABAB", str2 = "ABAB"
Output: "ABAB"
'''

class Solution1:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smaller = str1 if str1 < str2 else str2
        larger = str1 if str1 > str2 else str2
        
        gcd = ""
        for i in range(len(smaller), 0, -1):
            div = int(len(larger) / len(smaller[0:i]))
            div2 = int(len(smaller) / len(smaller[0:i]))
            if (len(larger) % len(smaller[0:i]) == 0 and 
                div * smaller[0:i] == larger and
                div2 * smaller[0:i] == smaller):
                if len(smaller[0:i]) > len(gcd):
                    gcd = smaller[0:i]
        return gcd

class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDivisor(length):
            if len1 % length or len2 % length:
                return False
            f1, f2 = len1 // length, len2 // length
            return str1[:length] * f1 == str1 and str1[:length] * f2 == str2

        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ""