"""
15. 3sum

q1 = [-1, 0, 1, 2, -1, -4]
# Answer: [[-1, 0, 1], [-1, -1, 2]]
q2 = [0, 0, 0]
# Answer: [[0, 0, 0]]
q3 = [-2, 0, 1, 1, 2]
# Answer: [[-2, 0, 2], [-2, 1, 1]]
q4 = [1, 2, -2, -1]
# Answer: []
q5 = [3, -2, 1, 0]
# Answer: []
q6 = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
# Answer: [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [0, 0, 0]]
q7 = [1, -1, 0]
# Answer: [[-1, 0, 1]]
q8 = [0, 0, 0, 0]
# Answer: [[0, 0, 0]]
q9 = [1, -1, -1, 0, 2, -1, -4]
# Answer: [[-1, -1, 2], [-1, -1, 2], [-1, 0, 1]]
q10 = [2, 2, 2, 2, 2]
# Answer: []
q11 = [1, 1, -2]
# Answer: [[-2, 1, 1]]
q12 = [-3, -1, 2, 4, 5]
# Answer: [[-3, -1, 4]]
q13 = [0, 0, 0, 1, -1, 2, -2]
# Answer: [[0, 0, 0], [-1, 0, 1], [-2, 0, 2], [-1, 1, 0], [-2, 1, 1], [-2, -1, 3]]
q14 = [1, -1, 1, -1, 1, -1]
# Answer: []
q15 = [1, -1, 2, -2]
# Answer: []
q16 = [5, -5, 0, 0]
# Answer: [[-5, 0, 5]]
q17 = [3, 0, -2, -1, 1, 2]
# Answer: [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
q18 = [4, 2, -1, 0, -2, -1, -4]
# Answer: [[-4, 0, 4], [-2, 0, 2], [-1, -1, 2]]
q19 = [-1, -2, -3, -4, -5]
# Answer: []
"""

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
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
        return output
    