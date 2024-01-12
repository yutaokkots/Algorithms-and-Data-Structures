"""1235. Maximum Profit in Job Scheduling"""

"""
1235. Maximum Profit in Job Scheduling
Hard

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.

Example 3:
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
 

Constraints:
    1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
    1 <= startTime[i] < endTime[i] <= 10^9
    1 <= profit[i] <= 10^4

"""
from typing import List
import bisect

class Solution:
    # Incorrect solution:
    # def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    #     length = len(startTime)
    #     start_end_profit = list(zip(startTime, endTime, profit))
    #     dp = [0] * length

    #     for i in range(length):
    #         dp[i] = start_end_profit[i][2]
    #         max_value = 0
    #         for j in range(0, i):
    #             if (start_end_profit[j][1] <= start_end_profit[i][0] and 
    #                 start_end_profit[j][0] <= start_end_profit[i][1]):
    #                 max_value = max(dp[j], 0)           
    #         dp[i] = max_value + dp[i]
    #     print(dp)
    #     return max(dp)

    # "startTime": [6,15,7,11,1,3,16,2],
    # "endTime": [19,18,19,16,10,8,19,8],
    # "profit": [2,9,1,19,5,7,3,19],
    # "answer": 41

    #   0   4   8   12  16  20
    #   |   |   |   |   |   |
    #1         *************    2 
    #2                 ****     9 
    #3         *************    1      
    #4             ******       19  
    #5   **********     |       5  
    #6     ******       |       7  
    #7                  ****    3  
    #8    *******               19     

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        start_end_profit = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        sorted_end_times = [x[1] for x in start_end_profit]
        length = len( start_end_profit)
        
        dp = [0] * length
        dp[0] = start_end_profit[0][2]

        for i in range(1, length):
            current_start, current_profit = start_end_profit[i][0], start_end_profit[i][2]  
            j = bisect.bisect_right(sorted_end_times, current_start) - 1
            if j >= 0:
                current_profit += dp[j]
            dp[i] = max(current_profit, dp[i - 1])

        return dp[-1]