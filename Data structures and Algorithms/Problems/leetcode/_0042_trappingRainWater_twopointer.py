# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.

from typing import List
##              ∏
##    ∏ @ @ @ @ ∏
##    ∏ @ @ ∏ @ ∏
##    ∏ ∏ @ ∏ ∏ ∏
##    ∏ ∏ @ ∏ ∏ ∏
q2 = [4,2,0,3,2,5]

questions = {
    "q1": {"q":[0,1,0,2,1,0,1,3,2,1,2,1], "a":6},
    "q2": {"q":[4,2,0,0,3,2,5], "a":13},
    "q3": {"q":[2,8,3,4,1,3,7,2,1,1,3], "a":22},
}

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        accum = []

        while left < right:
            if height[left] < left_max:
                accum.append(left_max - height[left])
            if height[right] < right_max:
                accum.append(right_max - height[right])
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])           

            if height[left] >= height[right]:
                right -= 1
            elif height[right] > height[left]:
                left += 1
        return sum(accum)

sol = Solution()
for k, v in questions.items():
    answer = sol.trap(v["q"])
    print(f"{k}) q: {v['q']}\na: {answer} \n{answer == v['a']} \n")