"""11. Container With Most Water"""

"""
11. Container With Most Water
Medium
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
    n == height.length
    2 <= n <= 10^5
    0 <= height[i] <= 10^4

"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # given integer array represents height
        # Purpose: find two lines that form largest container/box 
        # output -> maximum container value, as int
        # 
        # area = ((i + x) - i) * min(height[i+x], height[i])
        #
        # [1,8,6,2,5,4,15,3,7]
        #
        # two-pointer approach:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            area = (right - left) * h
            max_area = max(max_area, area)   
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return max_area