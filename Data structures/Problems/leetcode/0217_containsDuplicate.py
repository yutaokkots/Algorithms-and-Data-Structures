class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo = {}
        for n in nums:
            if n not in memo.keys():
                memo[n] = 1
            else:
                memo[n] += 1
            if memo[n] > 1:
                return True
        return False