# A phrase is a palindrome if, after converting all uppercase letters into 
# lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters 
# include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:        
        if len(s) == 1 or len(s) == 1:
            return True
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if not s[l].lower() == s[r].lower():
                    return False
                l += 1
                r -= 1

        return True