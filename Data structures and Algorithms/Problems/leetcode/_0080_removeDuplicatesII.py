from typing import List
# ##Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        length = len(nums) - 1
        for i in range(length, -1, -1):
            if i == length:
                continue
            if i == 0:
                break
            if i == 1 and nums[i] == nums[i+1] == nums[i-1]:
                nums.pop(i+1)
                break
            else:
                if nums[i] == nums[i+1] == nums[i-1]:
                    nums.pop(i+1)
        return len(nums)
    
    def removeDuplicates2(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        length = len(nums) - 1
        ##
        ## Rewrite of above code for conciseness
        for i in range(length, -1, -1):
            if i == length:
                continue
            if nums[i] == nums[i+1] == nums[i-1]:
                nums.pop(i+1)
            if i == 1:
                break
        return len(nums)