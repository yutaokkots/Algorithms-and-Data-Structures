# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    def longestConsecutive(self, nums):
        #edge case:
        if nums == []:
            return 0
        # sort the nums list -> O(N)
        nums.sort()

        # memo and counter
        memo = {"init": 1}
        counter = 1
        index_counter = 0

        # for loop that runs through the sorted 'nums' list 
        for i, n in enumerate(nums):
            # in the case where nums[i] is 0, skip
            if i == 0:
                pass
            elif n == nums[i - 1]:
                pass
            elif n - nums[i - 1] == 1:
                counter += 1
            elif n - nums[i - 1] > 1:
                counter = 1
            if counter > 1:
                memo[index_counter] = counter
            elif counter == 1:
                index_counter += 1
        
        return max(list(memo.values()))

list_A = [100,4,200,1,3,2]
list_B = [0,3,7,2,5,8,4,6,0,1]
list_C = [0,3,-7,2,5,-8,4,6,0,1,7, 9, 12, 10, 11]

solution = Solution()

print(solution.longestConsecutive(list_A))
print(solution.longestConsecutive(list_B))
print(solution.longestConsecutive(list_C))