# 567. Permutation in String

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.


class Solution:
    def checkInclusion1(self, s1: str, s2: str) -> bool:
        s1_const = 0
        for letter in s1:
            s1_const += ord(letter)
            
        s1_lst = list(s1)
        s1_lst.sort()
        left = 0
        counter = 0
        for right in range(len(s2)):
            if right - left == len(s1):
                left += 1
            if s2[right] in s1:
                pointer = left
                while pointer <= right:
                    counter += ord(s2[pointer])
                    if counter == s1_const:
                        s2_sub = list(s2[left:right+1])
                        s2_sub.sort()
                        if s2_sub == s1_lst:
                            # print(s1_const, counter)
                            # print(right)
                            return True
                    pointer += 1
                counter = 0

        return False
    
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dict = {}
        s2_dict = {}
        for n in range(26):
            s1_dict[chr(97+n)] = 0
            s2_dict[chr(97+n)] = 0
        for s in s1:
            s1_dict[s] += 1

        left = 0
        s1_length = len(s1)

        for right in range(len(s2)):         
            if right - left == s1_length:
                s2_dict[s2[left]] -= 1
                left += 1
            s2_dict[s2[right]] += 1
            if s1_dict == s2_dict:
                return True   

        return s1_dict == s2_dict

s1 = "ab"
s2 = "eidbaooo"
s1 = "ab"
s2 = "eidboaoo"
s1 = "a"
s2 = "ab"
s1 = "abc"
s2 = "ccccbbbbaaaa"