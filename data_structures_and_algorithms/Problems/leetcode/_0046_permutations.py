'''
46. Permutations
Medium

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #backtracking
        result = []
        
        #base-case
        if (len(nums) == 1):
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)

            result.extend(perms)
            nums.append(n)
        return result   
    

class Solution3:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        def backtrack(i):
            if i == len(nums):
                output.append(nums[:])
                return

            for idx in range(i, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                backtrack(i + 1)
                nums[i], nums[idx] = nums[idx], nums[i]

        backtrack(0)
        return output
    
class Solution4:
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
    
class Solution5:
    def permute(self, nums: List[any]) -> List[List[any]]: 
        output = []
        self.backtrack(nums, [], output)
        return output
    
    def backtrack(self, nums, subset, result):
        if not nums:
            result.append(subset.copy())
            return
        for i in range(len(nums)):
            subset.append(nums[i])
            self.backtrack(nums[:i] + nums[i + 1:], subset, result)
            subset.pop() 

class Solution6:
    def permute(self, nums: List[any]) -> List[List[any]]: 
        result = []
        
        def backtrack(nums_list, current_permutation):
            if not nums_list:
                result.append(current_permutation[:])
                return

            for i in range(len(nums_list)):
                n = nums_list[i]
                current_permutation.append(n)
                backtrack(nums_list[:i] + nums_list[i+1:], current_permutation)
                current_permutation.pop()

        backtrack(nums, [])
        return result