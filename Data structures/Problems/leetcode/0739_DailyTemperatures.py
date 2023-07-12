
# remember the previous temperature
# use a stack

# monotonic decreasing stack

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

