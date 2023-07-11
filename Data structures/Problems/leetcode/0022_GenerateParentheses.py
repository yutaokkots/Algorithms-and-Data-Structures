# Given n pairs of parentheses, write a function 
# to generate all combinations of well-formed parentheses.
# constraints
# 1 <= n <= 8

#e.g. n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        #use 'backtracking', which is a technique to explore all possible solutions
        stack = []
        answer = []
        def generator(openN, closedN):
            if openN == closedN == n:
                answer.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                generator(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                generator(openN, closedN + 1)
                stack.pop()
        generator(0, 0)
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