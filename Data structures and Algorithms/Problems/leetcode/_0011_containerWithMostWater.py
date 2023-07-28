from typing import List

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

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