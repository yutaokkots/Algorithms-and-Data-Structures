"""Quick Sort algorithm.
uses Divide and Conquer -> recursive
partition
swap
quicksort

"""
from typing import List

case01 = [10, 5, 2, 3, 4, 7]

class QuickSort():
    def quickSort01(self, nums:List) -> List:
        if len(nums) <= 1:
            return nums

        pivot = nums[0]
        less = []
        for n in nums[1:]:
            if n <= pivot:
                less.append(n)
        # less = [n for n in nums[1:] if n<= pivot]
        greater=[]
        for n in nums[1:]:
            if n > pivot:
                greater.append(n)
        # greater = [n for n in nums[1:] if > pivot]
        return self.quickSort01(less) + [pivot] + self.quickSort01(greater)