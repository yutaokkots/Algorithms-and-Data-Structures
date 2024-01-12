# You have a set of integers s, which originally contains all the numbers from 1 to n. 
# Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, 
# which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.

# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]

# Example 2:
# Input: nums = [1,1]
# Output: [1,2]


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        nums.sort()

        counter = 1
        duplicate = None
        if len(nums) == 2:
            return [1, 2]
        
        for i in range(len(nums)):
            if counter != nums[i]:
                duplicate = nums[i]
                if duplicate == nums[i - 1]:
                    return [duplicate, duplicate + 1 ] 
                else:
                    return [duplicate, duplicate - 1 ] 
            counter += 1

            # "q1": [[1,2,*2,4], [2,3]],
            # "q2": [[1,1], [1,2]],
            # "q3": [[2, 2], [2, 1]],
            # "q4": [[1, 2, *2], [2, 3]],
            # "q5": [[1, 2, 3, 4, *4], [4, 5]],
            # "q6": [[1, 2, 3, 5, *5, 6], [4, 5]]

    # def findErrorNums_2(self, nums: list[int]) -> list[int]:
    #     # [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5]
    #     # [1, 2, 3, 4, 4] -> [1, 2, 3, 4]; 14 vs 10 -> 4\\

    #     # [1, 2, 3, 4, 4, 6] -> [1, 2, 3, 5, 6]; 22 vs 17 -> 5
          # [0, 1, 2, 3, 4, 5] <- i
          # [1, 2, 3, 4, 5]    

    #     # [1, 2, 3, 5, 5, 6] -> [1, 2, 3, 5, 6]; 22 vs 17 -> 5
          # [0, 1, 2, 3, 4, 5] <- i
          # [1, 2, 3, 4, 5]               <- counter
    #     nums_list = list(set(nums))
    #     diff = sum(nums) - sum(nums_list)
    #     for n in nums():
    #         pass

                
# [X, X, 3, 4]
# [1, X, X, 4]
# [1, 2, X, X]

question_list = {
    "q1": [[1,2,2,4], [2,3]],
    "q2": [[1,1], [1,2]],
    "q3": [[2, 2], [2, 1]],
    "q4": [[1, 2, 2], [2, 3]],
    "q5": [[1, 2, 3, 4, 4], [4, 5]],
    "q6": [[1, 2, 3, 5, 5, 6], [4, 5]]
}

sol = Solution()

for k, q in question_list.items():
    #print(sol.findErrorNums(q[0]))
    print(k)
    print(sol.findErrorNums(q[0]))
    print("\n")
