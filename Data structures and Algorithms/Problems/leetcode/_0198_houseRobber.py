'''
198. House Robber
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

Other testcases:
        # [2,1,1,2]
        #  ^     ^   
        #  4

        # [2,1,1,1,2]
        #  ^   ^   ^
        #  5

        # [2,1,6,8,5,4]
        #  ^     ^   ^
        #  14

        # [2,1,8,6,5,4]
        #  ^   ^   ^
        #  15
'''
from typing import List

## first attempt:
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

sol = Solution()

questions = [[[2,1,1,2], 4], 
             [[2,7,9,3,1], 12],
             [[2,1,6,8,5,4], 14],
             [[2,1,8,6,5,4], 15]]

for i, v in enumerate(questions):
    answer = sol.rob(v[0])
    print(f"Q{i+1}: houses- {v[0]}; solution- {answer}; {'correct' if answer == v[1] else 'incorrect'}")