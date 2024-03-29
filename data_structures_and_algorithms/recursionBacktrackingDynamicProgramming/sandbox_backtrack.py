'''
Playing around with, to understand, backtracking.
from 
    LC 78 - Subsets
    LC 90 - Subsets II
    LC 46 - Permutations
    LC 39 - Combination Sum
    LC 40 - Combination Sum II


'''

from typing import List

###################
## Subsets LC70
###########

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
lst3 = [4,4,4,1,4]
s1 = SolutionSubset()
ans_1_1 = s1.subsets(lst1)
ans_1_2 = s1.subsets(lst3)
## [['a', 'b', 'c'], ['a', 'b'], ['a', 'c'], ['a'], ['b', 'c'], ['b'], ['c'], []]

print(f"Subset: \n    q: {lst1} \n    a:{ans_1_1}")
print(f"Subset: \n    q: {lst1} \n    a:{ans_1_2}")

print("\n")
###################
## Subsets II C90
###########

class SolutionSubsetII:
    def subsetWithDup(self, nums: List[any]) -> List[List[any]]:
        ''' Returns all possible subsets from a list of integers that may contain duplicate integers.

        :type nums: list of numbers
        :rtype: a list of list of subsets 
        '''
        answer = []
        subset = []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                answer.append(subset.copy())
                return
        
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

            # while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            #     i += 1
            backtrack(i + 1)

        backtrack(0)

        return answer

subset_2 = SolutionSubsetII()
ans_2_1 = subset_2.subsetWithDup(lst1)
## [['a', 'b', 'c'], ['a', 'b'], ['a', 'c'], ['a'], ['b', 'c'], ['b'], ['c'], []]
ans_2_2 = subset_2.subsetWithDup(lst3)
## [[1, 4, 4, 4, 4], [1, 4, 4, 4], [1, 4, 4], [1, 4], [1], [4, 4, 4, 4], [4, 4, 4], [4, 4], [4], []]

print(f"Subset II: \n    q: {lst1} \n    a:{ans_2_1}")
print(f"Subset II: \n    q: {lst3} \n    a:{ans_2_2}")

print("\n")
###################
## Permutations LC46
###########

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

print(f"Permutations: \n    q: {lst1} \n    a:{ans2}")

print("\n")
###################
## Combination Sum LC 39
###########


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
print(f"Combination Sum: \n    q: {lst2}, target={t} \n    a:{ans3}")
## [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

print("\n")
###################
## Combination Sum II LC 40
###########

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
                if candidates[idx] == prev:
                    continue
                permutation.append(candidates[idx])
                backtrack(idx + 1)
                permutation.pop()
                prev = candidates[idx]

        backtrack(0)
        return answer


'''

for LC 39 Combination Sum, the state of 'permutation' printed during each loop:

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