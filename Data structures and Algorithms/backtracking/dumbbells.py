'''
Given a plate of weights, return a list of pair that which is combination left and right sides have equal weights.

Example 1:
input = [1,1,1,2,3]
output = [[1,1,2],[3,1]]

Example 2:
input = [1,1,1,2,3,1]
output = [[1,1,2],[3,1]]

'''
from typing import List
      
class Solution():
    def dumbbell(self, weights: List[int]):
        if sum(weights) % 2 == 1:
            return []

        answer = []
        target = sum(weights) // 2
        combo = {0: []}

        for weight in weights:
            temp = dict(combo)
            for key, value in combo.items():
                if key + weight == target:
                    answer.append(value + [weight])
                elif key + weight < target and key + weight not in temp:
                    temp[key + weight] = value + [weight]
            combo = temp
        return answer

w = [1,1,1,2,3]
x = [1,5,11,5]
y = [7,7,7,7,8]
y = [7,7,7,7,8]

sol = Solution()
answer = sol.dumbbell(w)
print(answer)
answer2 = sol.dumbbell(x)
print(answer2)

sol2 = Solution()
answer = sol2.dumbbell(y)
print(answer)
