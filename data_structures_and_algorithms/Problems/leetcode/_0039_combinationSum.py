'''
39. Combination Sum
Medium

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []

'''
from typing import List

class Solution:
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        permutation = []

        def backtrack(i):
            if sum(permutation) == target:
                answer.append(permutation[:])
                return
            if i >= len(candidates) or sum(permutation) > target:
                return

            permutation.append(candidates[i])
            backtrack(i)

            permutation.pop()
            backtrack(i + 1)

        backtrack(0)

        return answer
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def backtrack(i, current):
            if sum(current) == target:
                answer.append(current[:])
                return
            if i >= len(candidates) or sum(current) > target:
                return

            current.append(candidates[i])
            backtrack(i, current)

            current.pop()
            backtrack(i + 1, current)

        backtrack(0, [])

        return answer

    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def backtrack(i, current, total):
            if total == target:
                answer.append(current.copy())
                return
            if i >= len(candidates) or total > target:
                return

            current.append(candidates[i])
            backtrack(i, current, total + candidates[i])

            current.pop()
            backtrack(i + 1, current, total)

        backtrack(0, [], 0)

        return answer
