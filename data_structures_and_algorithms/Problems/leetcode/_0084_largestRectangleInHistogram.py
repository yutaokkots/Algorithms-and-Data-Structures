"""Solution for LC84 - Largest Rectangle in Histogram
84.  Largest Rectangle in Histogram
Hard

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""
from typing import List

class Solution():
    """Class for the solution(s) for LC84
    
    Methods
    -------
    largestRectangleArea(self, heights)
        returns the largest rectangular area from a list of heights.
    """
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        """class method for solving the largest rectangular area of heights"""
        stack = []
        max_area = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, heights[i]))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
