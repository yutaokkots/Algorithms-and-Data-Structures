'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''


from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram -> rearrange letters, and letters are the same
        # anagram rat == tar
        # return Boolean
        if len(s) != len(t):
            return False
        else:
            for idx in set(s):
                if s.count(idx) != t.count(idx):
                    return False
        return True 
    
    def isAnagram2(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        return s_dict == t_dict


    def isAnagram3(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()

        return s_list == t_list


    def isAnagram4(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        else:
            for idx in set(s):
                if s.count(idx) != t.count(idx):
                    return False
        return True


    def isAnagram5(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


        #         Solution 3: 
        #edge case when the input strings are different lengths
        # if len(s) != len(t):
        #     return False
        # return " ".join(sorted(list(s))) == " ".join(sorted(list(t)))


        # list_s = list(s)
        # list_t = list(t)
        # dict_letters = {}
        # for letter in list_s:
        #     if letter == " ":
        #         pass
        #     if letter not in dict_letters.keys():
        #         dict_letters[letter] = 1
        #     else:
        #         dict_letters[letter] += 1
        # for letter in list_t:
        #     if letter == " ":
        #         pass
        #     if letter not in dict_letters.keys():
        #         return False
        #     else:
        #         dict_letters[letter] -= 1
        #         if dict_letters[letter] < 0:
        #             return False

        # return True


        #slow time complexity: O(n^2) or higher
        # list_s = list(s)
        # list_t = list(t)
        # for letter in list_s:
        #     if letter in list_t:
        #         list_t.pop(list_t.index(letter))
        #     else:
        #         return False

        # return True 

"""
Java Solution 1:

    class Solution {
        public boolean isAnagram(String s, String t) {
            HashMap<Character, Integer> charCountS = new HashMap<>();
            HashMap<Character, Integer> charCountT = new HashMap<>();

            for (char sChar: s.toCharArray()){
                if (charCountS.containsKey(sChar)){
                    charCountS.put(sChar, charCountS.get(sChar) + 1);
                } else {
                    charCountS.put(sChar, 1);
                }
            }
            for (char tChar: t.toCharArray()){
                if (charCountT.containsKey(tChar)){
                charCountT.put(tChar, charCountT.get(tChar) + 1);
                } else {
                    charCountT.put(tChar, 1);
                }
            }
            return charCountS.equals(charCountT);
        }
    }

Java Solution 1:

    class Solution {
        public boolean isAnagram(String s, String t) {
            char sArray[] = s.toCharArray();
            char tArray[] = t.toCharArray();

            Arrays.sort(sArray);
            Arrays.sort(tArray);
            
            String sStr = new String(sArray);
            String tStr = new String(tArray);

            return sStr.equals(tStr);
        }
}

"""