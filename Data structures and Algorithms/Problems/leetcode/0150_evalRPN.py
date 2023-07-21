questions = {
    "q1":[["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22], 
    "q2":[["2","1","+","3","*"], 9], 
    "q3":[["4","13","5","/","+"], 6] 
}

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operator = ("+","-","*","/")

        for t in tokens:
            if t not in operator:
                stack.append(int(t))
            else:
                if t == "+":
                    stack.append(stack.pop(-2) + stack.pop(-1))
                elif t == "-":
                    stack.append(stack.pop(-2) - stack.pop(-1))
                elif t == "*":
                    stack.append(stack.pop(-2) * stack.pop(-1))
                elif t == "/":
                    stack.append(int(stack.pop(-2) / stack.pop(-1)))

        return stack[0]


soln = Solution()

for key, value in questions.items():
    answer = soln.evalRPN(value[0])
    print(f"{key}) a: {answer} -> correct: {answer == value[1]}")