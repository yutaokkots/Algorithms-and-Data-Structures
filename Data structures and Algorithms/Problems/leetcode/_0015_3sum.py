from typing import List

class Solution:
    """ Class for solving the common three-sum solution.

    Methods
    -------
    threeSum(self, nums:List[int]):
        One method for solving the three-sum problem. 
    """

    def threeSum(self, nums:List[int]) -> List[List[int]]:
        """Method for a solution for three-sum algorithm."""
        output = []
        nums.sort()
        
        for left in range(len(nums)):
            if nums[left] == nums[left - 1] and left > 0:
                continue
            mid, right = left + 1, len(nums) - 1
            while mid < right:
                summation = nums[left] + nums[mid] + nums[right]
                if summation > 0:
                    right -= 1
                elif summation < 0:
                    mid += 1
                else:
                    output.append([nums[left], nums[mid], nums[right]])
                    mid += 1
                    right -= 1
        return output
    