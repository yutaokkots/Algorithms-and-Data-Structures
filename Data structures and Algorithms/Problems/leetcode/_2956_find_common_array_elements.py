"""2956. Find Common Elements Between Two Arrays"""

"""
2956. Find Common Elements Between Two Arrays
Easy
"""
from typing import List
from collections import Counter
from operator import countOf

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = [0] * 2
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        set01 = set(nums1)
        set02 = set(nums2)
        
        intersect = set01 & set02

        for inter in intersect:
            answer[0] += (count1[inter])
            answer[1] += (count2[inter])
        return answer
    
class Solution2:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = [0] * 2

        set01 = set(nums1)
        set02 = set(nums2)
        
        intersect = set01 & set02

        for inter in intersect:
            answer[0] += countOf(nums1, inter)
            answer[1] += countOf(nums2, inter)
        return answer