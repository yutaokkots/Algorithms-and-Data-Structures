"""455. Assign Cookies"""

"""
455. Assign Cookies
Easy 

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Example 1:
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:
Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.

Constraints:
    1 <= g.length <= 3 * 10^4
    0 <= s.length <= 3 * 10^4
    1 <= g[i], s[j] <= 2^31 - 1
"""
from typing import List, Dict
from collections import Counter

class Solution:
    """Optimized solution for LC0455

    Big-O
    -----
    time: O(m * log(m) + n * log(n))
    space: O(1).
    """

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        count = 0
        for greedy in g:
            if i >= len(s):
                break
            while i < len(s) and greedy > s[i]:
                i += 1
            if i < len(s) and greedy <= s[i]:
                count += 1
                i += 1
        return count

class Solution2:
    """Naive solution for LC0455.

    Big-O
    -----
    time: O(m + n + m * n) 
    space: O(m + n)
    """

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        greed_counter = Counter(g)
        size_counter = Counter(s)
        size_max = max(s)
        counter = 0
        for size in g: 
            if (size in size_counter.keys() and 
                    greed_counter[size] > 0 and
                    size_counter[size] > 0):
                greed_counter[size] -= 1
                size_counter[size] -= 1
                counter += 1
                continue
            s_num = self.linear_search(s, size_counter, size, size_max)
            if s_num > -1:
                greed_counter[s_num] -= 1
                size_counter[s_num] -= 1
                counter += 1
        return counter

    def linear_search(self, lst:List[int], dict:Dict[int, int], target:int, target_max:int) -> int:
        for t in range(target, target_max + 1):
            if t in lst and self.available(dict, t):
                return t
        return -1

    def available(self, dict:Dict[int, int], target:int) -> bool:
        return dict[target] > 0
