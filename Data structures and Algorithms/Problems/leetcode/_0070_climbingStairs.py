'''
70. Climbing Stairs
Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
'''

class Solution1:
    def climbStairs(self, n: int) -> int:
        dpset = [-1] * (n + 2)

        def dynamic(i):
            if i == 0 or i == 1:
                return 1
            if dpset[i] != -1:
                return dpset[i]
            left = dynamic(i - 1)
            right = dynamic(i - 2)
            dpset[i]= left + right
            return left + right
        return dynamic(n)

class Solution2:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


class Solution3:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
    
        # Create a table to store results for subproblems.
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1
        dp[1] = 1
        
        # Fill in the table iteratively
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # The final result is in dp[n]
        return dp[n]
    
class Solution4:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

sol1 = Solution1()
answer1 = sol1.climbStairs(8)
print(answer1)

sol2 = Solution2()
answer2 = sol2.climbStairs(8)
print(answer2)