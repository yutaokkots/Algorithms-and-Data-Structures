'''

217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

'''

class Solution:
    def containsDuplicate_1(self, nums: list[int]) -> bool:
        memo = {}
        for n in nums:
            if n not in memo.keys():
                memo[n] = 1
            else:
                return True
        return False

    def containsDuplicate_2(self, nums: list[int]) -> bool:
        nums.sort()
        for index, num in enumerate(nums):
            if index == 0:
                continue
            if num == nums[index - 1]:
                return True
        return False
    
    def containsDuplicate_3(self, nums: list[int]) -> bool:
        return not len(nums) == len(set(nums))

    ###############
    # Solution 4
    ###############
    # return not len(nums) == len(set(nums))

    ###############
    # Solution 1
    ###############
    # memo = {}
    # for n in nums:
    #     if n not in memo.keys():
    #         memo[n] = 1
    #     else:
    #         return True
    # return False

    ###############
    # Solution 2
    ###############
    # nums.sort()
    # for index, num in enumerate(nums):
    #     if index == 0:
    #         continue
    #     if num == nums[index - 1]:
    #         return True
    # return False

    ###############
    # Solution 3
    ###############
    # return not len(nums) == len(set(nums))