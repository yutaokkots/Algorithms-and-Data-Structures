"""Insertion Sort Algorithm Example"""
from typing import List

case01 = [9, 3, 6, 2, 1, 11]
case02 = [12, 16, 14, 1, 2, 3]
case03 = [(5, "apple"), (2, "banana"), (9, "cherry")]
case04 = [(3, "cat"), (3, "bird"), (2, "dog")]


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class InsertionSort():
    """Class containing various insertion sort algorithms"""

    def insertionSort01(self, nums:List) -> List:
        """Method for basic insertion sort."""
        for i in range(1, len(nums)):
            j = i - 1
            curr = nums[i]
            while j >= 0 and curr < nums[j]:
                nums[j + 1] = nums[j]
                nums[j] = curr
                j -= 1
        return nums

    def insertionSort02(self, pairs: List[Pair]) -> List[List[Pair]]:
        """Method for performing an insertion sort while capturing the sort step."""
        answer = []
        answer.append(pairs.copy())
        for i in range(1, len(pairs)):
            curr = pairs[i]
            j = i - 1
            while j >= 0 and curr[0] < pairs[j][0]:
                pairs[j+1] = pairs[j]
                pairs[j] = curr
                j -= 1
            answer.append(pairs.copy())
        return answer


    def __str__(self):
        return str("How to perform insertion sort.")