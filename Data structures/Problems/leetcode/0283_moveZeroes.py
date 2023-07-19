# Given an integer array nums, move all 0's to the end of it while 
# maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        counter = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[counter] == 0:
                nums[i], nums[counter] = nums[counter], nums[i]
            if nums[counter] != 0:
                counter += 1
        return nums

questions = {
    "q1": [[0,1,0,3,12],[1,3,12,0,0]],
    "q2": [[0],[0]],
    "q3": [[2,1],[2,1]],
    "q4": [[1,0,1],[1,1,0]]
}

sol = Solution()
for key, question in questions.items():
    a = sol.moveZeroes(question[0])
    print(f"{key}) q: {question[0]} answer: {a} correct: {a == question[1]}")

