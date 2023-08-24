# 1523. Count Odd Numbers in an Interval Range
# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high - low == 1:
            return 1
        if (low % 2 == 1 and high % 2 == 1 
            or low % 2 == 1 
            or high % 2 == 1):
            return (high - low) // 2 + 1
        else:
            return (high - low) // 2 
        
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2
    

low = 3
hight = 7
low = 8
hight = 10
low = 0
hight = 10
low = 13
hight = 18
