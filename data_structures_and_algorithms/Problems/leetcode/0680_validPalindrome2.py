# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution:
    def validPalindrome(self, s: str) -> bool:

        # bc d eed a cb
        # 01 2 345 6 78
        #    d eed a
        #    d eed    -> dee d
        #      eed a  -> a dee

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                left_slice = s[l:r]     
                right_slice = s[l+1:r+1]
                return left_slice == left_slice[-1::-1] or right_slice == right_slice[-1::-1]
            else: # if s[l] == s[r]
                l += 1
                r -= 1
        
        return True 