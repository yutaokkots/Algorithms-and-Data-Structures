'''
383. Ransom Note
Easy

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 
Constraints:
    1 <= ransomNote.length, magazine.length <= 10^5
    ransomNote and magazine consist of lowercase English letters.
'''
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = Counter(magazine)

        for letter in ransomNote:
            mag_dict[letter] -= 1
            if mag_dict[letter] < 0:
                return False
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        chars = [0] * 26
        for m in magazine:
            chars[ord(m) - ord("a")] += 1
    
        for r in ransomNote:
            chars[ord(r) - ord("a")] -=1
            if chars[ord(r) - ord("a")] < 0:
                return False
        return True
'''
Java Solution:

    class Solution {
        public boolean canConstruct(String ransomNote, String magazine) {
            HashMap<Character, Integer> magDict = new HashMap<>();
            
            // char[] mag = magazine.toCharArray();
            // for (int i = 0; i < mag.length; i++){
            //     char c = mag[i];
            //     System.out.println(c);
            // }

            for (char c: magazine.toCharArray()){
                if (magDict.containsKey(c)){
                    magDict.put(c, magDict.get(c) + 1);
                } else {
                    magDict.put(c, 1);
                }
            }
            for (char d: ransomNote.toCharArray()){
                if (magDict.containsKey(d)){
                    magDict.put(d, magDict.get(d) - 1);
                    if (magDict.get(d) < 0){
                        return false;
                    }
                } else {
                    return false;
                }
            }
            System.out.println(magDict);
        return true;
        }
    }
'''