# Given n pairs of parentheses, write a function 
# to generate all combinations of well-formed parentheses.
# constraints
# 1 <= n <= 8

#e.g. n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        #use 'backtracking', which is a technique to explore all possible solutions
        #backtracking is done recursively
        #three types of backtracking:
        # 1. Decision Problem – search for a feasible solution.
        # 2. Optimization Problem – search for the best solution.
        # 3. Enumeration Problem – find all feasible solutions.

        stack = []
        answer = []

        #define a backtrack function
        #openN is the number of open parenthesis that is counted, and passed as an argument
        #closedN is the number of closed parenthesis that is counted, and passed as an argument
        def backtrack(openN, closedN):
            # when the number of open parentheses and closed parentheses are the same as input n,
            # then make the 'join' list into a single string, and append to the 'answer' list
            if openN == closedN == n:
                answer.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return answer

soln = Solution()
print(soln.generateParenthesis(1))
print(soln.generateParenthesis(2))
print(soln.generateParenthesis(3))
print(soln.generateParenthesis(4))
print(soln.generateParenthesis(5))
#print(soln.generateParenthesis(6))
#print(soln.generateParenthesis(7))
#print(soln.generateParenthesis(8))