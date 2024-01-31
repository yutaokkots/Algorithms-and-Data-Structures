"""739. Daily Temperatures"""

"""
739. Daily Temperatures
Medium

Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
 
Constraints:
    1 <= temperatures.length <= 10^5
    30 <= temperatures[i] <= 100
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = []  #pair: [temp,index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = (i - stackInd)
            stack.append([t, i])
        return result
    
    def dailyTemperatures2(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = [] # [temperature, index]

        for i in range(len(temperatures) - 1):
            while stack and temperatures[i] > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                result[stackIndex] = (i - stackIndex)
            stack.append([temperatures[i], i])
        return result
    
    def dailyTemperatures3(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, value in enumerate(temperatures):
            while stack and value > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                result[stackIndex] = (i - stackIndex)

            stack.append([value, i])
        return result
    



sol = Solution()

temperatures = [73,74,75,71,69,72,76,73]

print(sol.dailyTemperatures(temperatures))
print(sol.dailyTemperatures2(temperatures))
print(sol.dailyTemperatures3(temperatures))

