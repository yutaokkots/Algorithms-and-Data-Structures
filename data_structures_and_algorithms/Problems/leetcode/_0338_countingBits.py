"""338. Counting Bits"""

"""
338. Counting Bits
Easy

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 
Constraints:
    0 <= n <= 10^5
"""

from typing import List

class Solution:
    """Solution for LC0338 with dynamic programming."""
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]
        dp_array = [0] *  (n + 1)E3
        dp_array[1] = 1

        for x in range(2, n+1):
            if x % 2 == 0:
                dp_array[x] = dp_array[x // 2]
            else:
                dp_array[x] = dp_array[x // 2] + 1
            print(dp_array)

        return dp_array

class Solution2:
    """Solution for LC0338 with O(n log n) runtime."""
    def countBits(self, n: int) -> List[int]:
        a = []
        for number in range(n+1):
            a.append(bin(number)[2:].count("1"))
        return a
    
sol = Solution()
a = sol.countBits(20)
print(a)
"""
[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 2, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 2, 1, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 2, 1, 2, 2, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 0, 0, 0, 0, 0]
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 0, 0, 0, 0]
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 0, 0, 0]
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 0, 0]
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 0]
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2]
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2]
"""