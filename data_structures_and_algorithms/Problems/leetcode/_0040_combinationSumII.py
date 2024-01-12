'''
40. Combination Sum II
Medium

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[ [1,1,6], [1,2,5], [1,7], [2,6] ]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[ [1,2,2], [5] ]

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

'''

from typing import List


class Solution1:
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer = []
        permutation = []

        def backtrack(i):
            if sum(permutation) == target:
                answer.append(permutation.copy())
            if sum(permutation) >= target:
                return
            
            prev = -1
            for idx in range(i, len(candidates)):
                if candidates[idx] == prev:
                    continue
                permutation.append(candidates[idx])
                backtrack(idx + 1)
                permutation.pop()
                prev = candidates[idx]

        backtrack(0)
        return answer


class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(i, current, target):
            if target == 0:
                result.append(current.copy())
            if target <= 0:
                return
            prev = -1
            for idx in range(i, len(candidates)):
                if candidates[idx] == prev:
                    continue
                current.append(candidates[idx])
                backtrack(idx + 1, current, target - candidates[idx])
                current.pop()
                prev = candidates[idx]    

        backtrack(0, [], target)

        return result
    

sol1 = Solution1()
ans1 = sol1.combinationSum1([10,1,2,7,6,1,5], 8)
print(ans1)
# [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

sol2 = Solution2()
ans2 = sol2.combinationSum2([10,1,2,7,6,1,5], 8)
print(ans2)
# [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

