'''
Backtracking sandbox with for-loop
from 
    LC 40 - Combination Sum II

Example 1:
    candidates = [10,1,2,7,6,1,5]
    target = 8

    answer = [
        [1,1,6],
        [1,2,5],
        [1,7],
        [2,6]]
'''
from typing import List

class SolutionCombinationSumII:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                if prev == candidates[idx]:
                    continue
                permutation.append(candidates[idx])
                backtrack(idx + 1)
                permutation.pop()
                prev = candidates[idx]

        backtrack(0)
        return answer

lst_csII = [10,1,2,7,6,1,5] 
t_8 = 8
comboSumII = SolutionCombinationSumII()
ans_comboSumII = comboSumII.combinationSum2(lst_csII, t_8)

print(f"Subset II: \n    q: {lst_csII} t: {t_8} \n    a:{ans_comboSumII}")
## [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
