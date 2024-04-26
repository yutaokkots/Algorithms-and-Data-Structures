'''
205. Isomorphic Strings
Easy 

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
    1 <= s.length <= 5 * 10^4
    t.length == s.length
    s and t consist of any valid ascii character.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        memo = {}
        for i, j in zip(s, t):
            letter = memo.get(i)
            if (letter == None and
                    j not in memo.values()):
                memo[i] = j
            elif letter != j:
                return False
        return True

        # s = "foo", t = "bar"
        # starts to create memo, but 'letter != j' returns False. 
        #   memo =  {
        #             'f': 'b', 
        #             'o': 'a'
        #   }

    def isIsomorphic2(self, s: str, t: str) -> bool:
        ''' First attempt. '''
        if len(t) != len(s):
            return False
        set_s = []
        set_t = []

        length = len(s)
        for i in range(length):
            if s[i] not in set_s:
                set_s.append(s[i])
            if t[i] not in set_t:
                set_t.append(t[i])

        s_lst = []
        t_lst = []

        for i in range(length):
            s_lst.append(set_s.index(s[i]))
            t_lst.append(set_t.index(t[i]))

        return s_lst == t_lst