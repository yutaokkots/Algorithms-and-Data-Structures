'''
771. Jewels and Stones

You're given strings jewels representing the types of stones that are jewels, 
and stones representing the stones you have. 
Each character in stones is a type of stone you have. 
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type 
of stone from "A".

Example:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
'''

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int: 
        counter = 0
        for stone in stones:
            if stone in jewels:
                counter += 1
        return counter

    def numJewelsInStones2(self, jewels: str, stones: str) -> int: 
        return len([s for s in stones if s  in jewels])
    