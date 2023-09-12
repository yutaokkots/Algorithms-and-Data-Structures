'''
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1

    def search2(self, nums: List[int], target: int) -> int:
        #takes two parameters
        # 1) sorted array
        # 2) an integer ('target')
        # if target exists, then return the index of the target inside the list
        # if not in the list, return '-1'

        #implement a time complexity of O(logN)

        # length of the list is between 1 and 100000
        # values of the integers in the list are -10000 -> 10000
        # values are unique
        # array is sorted. 


        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        # [-1, 0, 3, 5, 9, 12]
        # target 9


        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (right + left) // 2
            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1

        # define a while loop to keep searching for target
        # while len(nums) > 1:
        #     list_index = len(nums) // 2 
        #     if target == nums[list_index]:
        #         return list_index
        #     elif target > nums[list_index]:
        #         nums = nums[list_index:-1]
        #     elif target < nums[list_index]:
        #         nums = nums[0:list_index]

        # if the value is not found:
        

        # if the value is found:
        return -1