"""Merge Sort algorithm.
uses Divide and Conquer -> recursive
"""
from typing import List

case01 = [10, 5, 2, 3, 4, 7]

class MergeSort():
    def merge(self, lst1: List[int], lst2: List[int]) -> List[int]:
        results = []
        i, j = 0, 0
        while i < len(lst1) and j < len(lst2):
            if lst1[i] < lst2[j]:
                results.append(lst1[i])
                i += 1
            else:
                results.append(lst2[j])
                j += 1
        while i < len(lst1):
            results.append(lst1[i])
            i += 1
        while j < len(lst2):
            results.append(lst2[j])
            j += 1
        return results

    def mergeSort01(self, nums:List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        l, r = nums[:mid], nums[mid:]
        left = self.mergeSort01(l)
        right = self.mergeSort01(r)
        return self.merge(left, right)
    