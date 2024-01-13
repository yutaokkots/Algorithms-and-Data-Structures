"""2299. Strong Password Checker II"""

"""
2299. Strong Password Checker II
Easy

A password is said to be strong if it satisfies all the following criteria:

It has at least 8 characters.
It contains at least one lowercase letter.
It contains at least one uppercase letter.
It contains at least one digit.
It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false.

Example 1:
Input: password = "IloveLe3tcode!"
Output: true
Explanation: The password meets all the requirements. Therefore, we return true.

Example 2:
Input: password = "Me+You--IsMyDream"
Output: false
Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.

Example 3:
Input: password = "1aB!"
Output: false
Explanation: The password does not meet the length requirement. Therefore, we return false.
 
Constraints:
    1 <= password.length <= 100
    password consists of letters, digits, and special characters: "!@#$%^&*()-+".
"""

class Solution:
    """Solution class for checking password LC2299."""
    
    def strongPasswordCheckerII(self, password: str) -> bool:
        if not self.check_char_length(password, 8):
            return False
        if not self.check_upper(password):
            return False
        if not self.check_lower(password):
            return False
        if not self.check_digit(password):
            return False
        if not self.check_special(password):
            return False
        if not self.not_adj(password):
            return False
        return True

    def check_char_length(self, password:str, length:int) -> bool:
        return len(password) >= length
        
    def check_upper(self, password:str) -> bool:
        return True if any(char.isupper() for char in password) else False

    def check_lower(self, password:str) -> bool:
        return True if any(char.islower() for char in password) else False

    def check_digit(self, password:str) -> bool:
        return True if any(char.isnumeric() for char in password) else False

    def check_special(self, password:str) -> bool:
        special = "!@#$%^&*()-+"
        return True if any(char in special for char in password) else False

    def not_adj(self, password:str) -> bool:
        for i in range(1, len(password)):
            if password[i - 1] == password[i]:
                return False
        return True