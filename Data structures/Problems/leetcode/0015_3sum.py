###############
# 3SUM question


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


question_list = [q1 ,q2 ,q3 ,q4 ,q5 ,q6 ,q7 ,q8 ,q9 ,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19]


# [-1, 0, 1, 2, -1, -4]
# [-4, -1, -1, 0, 1, 2]

class Solution:
    def threeSum(self, nums:list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = num + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[i] == nums[i - 1]:
                        left += 1

        return result


soln = Solution()


for q in question_list:
    print(soln.threeSum(q))