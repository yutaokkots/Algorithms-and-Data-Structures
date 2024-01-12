"""
446. Arithmetic Slices II - Subsequence

"""
from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total_count = 0  
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1  
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    total_count += dp[j][diff]

        return total_count

class Solution2:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        permutation = []
        self.counter = 0
        def backtrack(i):
            if i > len(nums) - 1:
                if (len(permutation) > 2 and 
                    self.arithmetric_seq_set(permutation) or
                    self.arithmetric_seq(permutation)):

                    self.counter += 1
                return 
            permutation.append(nums[i])
            backtrack(i + 1)
            permutation.pop()
            backtrack(i + 1)
        backtrack(0)
        return self.counter

    def arithmetric_seq(self, lst: List[int]) -> bool:
        if len(lst) < 3:
            return False
        diff = lst[1] - lst[0]
        for i in range(1, len(lst)):
            if lst[i] - lst[i - 1] != diff:
                return False
        return True

    def arithmetric_seq_set(self, lst:List[int]) -> bool:
        return True if len(set(lst)) == 1 else False
    

class Solution3:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        self.nums = nums
        self.permutation = []
        self.counter = 0
        if self.arithmetric_seq_set(nums):
            self.backtrack2(0)
        else:
            self.backtrack(0)
        return self.counter

    def arithmetric_seq(self, lst: List[int]) -> bool:
        if len(lst) < 3:
            return False
        diff = lst[1] - lst[0]
        for i in range(1, len(lst)):
            if lst[i] - lst[i - 1] != diff:
                return False
        return True

    def arithmetric_seq_set(self, lst:List[int]) -> bool:
        return True if len(set(lst)) == 1 else False

    def backtrack(self, i):
        if i > len(self.nums) - 1:
            if (len(self.permutation) > 2 and 
                    self.arithmetric_seq_set(self.permutation) or
                    self.arithmetric_seq(self.permutation)):
                self.counter += 1
            return 
        self.permutation.append(self.nums[i])
        self.backtrack(i + 1)
        self.permutation.pop()
        self.backtrack(i + 1)

    def backtrack2(self, i):
        if i > len(self.nums) - 1:
            if (len(self.permutation) > 2):
                self.counter += 1
            return 
        self.permutation.append(self.nums[i])
        self.backtrack2(i + 1)
        self.permutation.pop()
        self.backtrack2(i + 1)


lst = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

sol = Solution()
a = sol.numberOfArithmeticSlices(lst)
print(a)
