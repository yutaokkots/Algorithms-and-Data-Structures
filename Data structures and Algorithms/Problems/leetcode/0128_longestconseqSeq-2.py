# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

list_A = [100,4,200,1,3,2]
list_B = [0,3,7,2,5,8,4,6,0,1]
list_C = [0,3,-7,2,5,-8,4,6,0,1,7, 9, 12, 10, 11]

solution = Solution()

print(solution.longestConsecutive(list_A))  # 4
print(solution.longestConsecutive(list_B))  # 9
print(solution.longestConsecutive(list_C))  # 8