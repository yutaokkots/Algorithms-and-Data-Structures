# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.

class Solution:
    def firstPalindrome_1(self, words: list[str]) -> str:
        possible_pali = []
        for word in words:
            if word[0] == word[-1]:
                possible_pali.append(word)
        if len(possible_pali) == 0:
            return ""

        for word in possible_pali:
            l = 0
            r = len(word) - 1
            not_palindrome = False
            while l < r and not not_palindrome:
                if word[l] == word[r]:
                    l += 1
                    r -= 1
                else: #not a palindrome
                    not_palindrome = True
            if not_palindrome:    
                continue
            else: 
                return word

        return ""
    
    def firstPalindrome_2(self, words: list[str]) -> str:
        for word in words:
            if word[0] == word[-1]:
                l = 0
                r = len(word) - 1
                not_palindrome = False
                while l < r and not not_palindrome:
                    if word[l] == word[r]:
                        l += 1
                        r -= 1
                    else: 
                        not_palindrome = True
                if not_palindrome:    
                    continue
                else: 
                    return word

        return ""
    
    def firstPalindrome_3(self, words: list[str]) -> str:
        pass