# Given an integer array nums and an integer k, 
# return the k most frequent elements. You may return the answer in any order.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

from typing import List

class Solution:
    # first solution using hashmap
    def topKFrequentHashmap(self, nums: List[int], k: int) -> List[int]:
        memo = {}
        answer = []
        for v in nums:
            if v not in memo.keys():
                memo[v] = 1
            else:
                memo[v] += 1
        
        sorted_memo = dict(sorted(memo.items(), reverse=True, key=lambda item: item[1]))
        
        for key, value in sorted_memo.items():
            if k > 0:
                answer.append(key)
            k -= 1
        return answer

nums = [1,1,1,2,2,3]
k = 2

sol = Solution()
answer_1 = sol.topKFrequentHashmap(nums, k)

print(answer_1)