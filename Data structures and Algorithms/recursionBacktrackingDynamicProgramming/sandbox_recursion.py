'''
Playing around with, to understand, backtracking.
from 
    LC 78 - Subsets
    LC 39 - Combination Sum
    LC 46 - Permutations

'''

from typing import List

class SolutionSubset:
    def subsets(self, nums: List[any]) -> List[List[any]]:
        ''' Returns all possible subsets from a list of unique integers.

        :type nums: list of unique numbers
        :rtype: a list of list of subsets 
        '''
        answer = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                answer.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)

        backtrack(0)

        return answer

lst1 = ["a", "b", "c"]
s1 = SolutionSubset()
ans = s1.subsets(lst1)
## [['a', 'b', 'c'], ['a', 'b'], ['a', 'c'], ['a'], ['b', 'c'], ['b'], ['c'], []]

print(ans)

class SolutionPermutations:
    def permute(self, nums: List[any]) -> List[List[any]]: 
        answer = []
        permutation = []

        def backtrack():
            if len(permutation) == len(nums):
                answer.append(permutation.copy())
                return

            for num in nums:
                if num not in permutation:
                    permutation.append(num)
                    backtrack()
                    permutation.pop()

        backtrack()

        return answer
    
s2 = SolutionPermutations()
ans2 = s2.permute(lst1)
## [['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b'], ['c', 'b', 'a']]

print(ans2)

class SolutionCombinationSum:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        permutation = []

        def backtrack(i):
            if sum(permutation) == target:
                answer.append(permutation.copy())
                return
            if i >= len(candidates) or sum(permutation) > target:
                return
            permutation.append(candidates[i])
            backtrack(i)

            permutation.pop()
            backtrack(i + 1)
        backtrack(0)
        return answer
    
lst2 = [2, 3, 5]
t = 8
s3 = SolutionCombinationSum()
ans3 = s3.combinationSum(lst2, t)
print(ans3)
## [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

'''
[]
[2]
[2, 2]
[2, 2, 2]
[2, 2, 2, 2]
[2, 2, 2]
[2, 2, 2, 3]
[2, 2, 2]
[2, 2, 2, 5]
[2, 2, 2]
[2, 2]
[2, 2, 3]
[2, 2, 3, 3]
[2, 2, 3]
[2, 2, 3, 5]
[2, 2, 3]
[2, 2]
[2, 2, 5]
[2, 2]
[2]
[2, 3]
[2, 3, 3]
[2, 3]
[2, 3, 5]
[2, 3]
[2]
[2, 5]
[2, 5, 5]
[2, 5]
[2]
[]
[3]
[3, 3]
[3, 3, 3]
[3, 3]
[3, 3, 5]
[3, 3]
[3]
[3, 5]
[3]
[]
[5]
[5, 5]
[5]
[]

'''