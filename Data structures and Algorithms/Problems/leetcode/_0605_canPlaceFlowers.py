'''
605. Can Place Flowers
Easy

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false




'''
from typing import List

class Solution1:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i == 0 or flowerbed[i - 1] == 0:
                    if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        count += 1
            i += 1
        
        return count >= n
    
class Solution2:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]

        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0
    
class Solution3:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ct = 0 if flowerbed[0] else 1

        for f in flowerbed:
            if f:
                n -= int((ct - 1) / 2)
                ct = 0
            else:
                ct += 1

        n -= (ct) // 2
        return n <= 0