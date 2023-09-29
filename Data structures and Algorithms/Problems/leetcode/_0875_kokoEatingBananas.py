'''
875. Koko Eating Bananas
Medium

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.


Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

'''
import math
from typing import List

class Solution():
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        while left <= right:
            mid = (left + right) // 2
            banana_time = self.bananaRateCounter(piles, mid)
            if banana_time <= h:
                res = min(mid,res)
                right = mid - 1
            else:
                left = mid + 1
        return res


    def bananaRateCounter(self, piles, bananas):
        counter = 0
        for i in range(len(piles)):
            counter += math.ceil(piles[i] / bananas)
        return counter


'''
    def minEatingSpeed2(self, piles: List[int], h: int) -> int:
        # k is the rate of eating
        # ex 1) piles_1 = [3,6,7,11], h = 8 // [4, 8, 8, 12] -> 32
        # output = 4
        # sum(piles_1) -> 27, 8 hours 
        # len(piles_1) -> 4

        ##  x * h > 27  and related to n piles (piles[i])
        ##  x * h > 27  solve for x, where 
        ## 
        for i in range(0, len(piles)):
            each_hour = piles[i] // x + 1
            h - each_hour
            
        if h == 0:
            return x

        ##///
        len(piles) <= x <= sum(piles) / len(piles) 


        # ex 2) piles_2 = [30,11,23,4,20], h = 5
        # output: 30
        # sum(piles_2) -> 88
        # len(piles_2) -> 5

        # sort the pile
        piles.sort()
        # reverse the pile
        piles.reverse()

        pile_length = len(piles)
        pile_sum = sum(piles)
        
        if h == pile_length:
            return piles[0]
        else: # h > pile_length:
            
        # return k, rate of banana consumption
        return k        
'''