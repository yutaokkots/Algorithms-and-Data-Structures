# Given an array nums of distinct integers, 
# return all the possible permutations. 
# You can return the answer in any order.

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

example = [1,2,3]

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # declare a list that will be used to construct a permutation
        result = []

        if len(nums) == 1:
            return [nums[:]] # return a shallow copy of the nums list, and located inside another list

        for i in range(len(nums)):
            n = nums.pop(0) # pop the 0th element of the list 
            
            perms = self.permute(nums)  # after removing the 0th item, 
                                        # place the rest of the list into the self.permute() function recursively
            for perm in perms:          # this code only runs after only [nums[:]] is returned (above)
                perm.append(n)          # and append the popped element, 'n'

            result.extend(perms)
            # .append() adds a single element to the end of the list 
            #  while .extend() can add multiple individual elements to the end of the list.

            nums.append(n)
            #print(nums)
        return result
    

    
sol = Solution()
print(sol.permute(example))

