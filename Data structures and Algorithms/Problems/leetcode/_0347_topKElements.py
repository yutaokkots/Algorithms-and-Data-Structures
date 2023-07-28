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
        
        for key in sorted_memo.keys():
            if k > 0:
                answer.append(key)
            k -= 1
        return answer
    
    # second solution using max-heap
    def topKFrequentHeap(self,nums: List[int], k: int) -> List[int]:
        import heapq
        import collections
        heap = []
        # creates a hashtable of counted items in 'nums' list
        count = collections.Counter(nums)
        # iterate over set of nums

        # iterates over the values in the set(nums)
        for n in set(nums):
            # to the 'heap' heap, create a max-heap (as indicated by multiplying by negative number)
            print((-1 * count[n], n))
            # add the tuple, (-1 * count[i], i)  <-- (-frequency, value)
            heapq.heappush(heap, (-1 * count[n], n))
        # pop out the k number of items from the max-heap, specifically the [1] index of the tuple
        answer = [heapq.heappop(heap)[1] for _ in range(k)]
        return answer


nums = [1,1,1,2,2,3,4,5,3,3,2,5,5,5,1,5,12]
k = 2

sol = Solution()
answer_1 = sol.topKFrequentHashmap(nums, k)

print(answer_1)

answer_2 = sol.topKFrequentHeap(nums,k)

print(answer_2)