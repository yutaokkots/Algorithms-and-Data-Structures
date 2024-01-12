# 239 Sliding Window Maximum
# You are given an array of integers nums, 
# there is a sliding window of size k 
#which is moving from the very left of the array to the very right. Y
#ou can only see the k numbers in the window. 
# Each time the sliding window moves right by one position.

# Return the max sliding window.
from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
    
nums1 = [1,3,-1,-3,5,3,6,7]