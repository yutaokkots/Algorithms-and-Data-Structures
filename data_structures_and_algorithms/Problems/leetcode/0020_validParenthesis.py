q01 = "()"
q02 = "()[]{}"
q03 = "({[]})"
q04 = "[()]{}"
q05 = "{[}]"
q06 = "({[})"
q07 = "(]"
q08 = "["
q09 = "]"
q10 = ""
q11 = "(("
q12 = "))"
q13 = "([]))"
q14 = "{(})"
q15 = "([)]"
q16 = "{([])}"
q17 = "{{{{}}"
q18 = "(((({{))"
q19 = "{[()]"
q20 = "(())[]{}"

q_list = [q01,q02,q03,q04,q05,q06,q07,q08,q09,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20]


class Solution:
    def isValid(self, s: str) -> bool:
        # edge case:
        if len(s) % 2 == 1:
            return False   

        if s == "":
            return True   

        stack = []
        dict = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        for letter in s:
            if letter in dict:
                if stack and stack[-1] == dict[letter]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(letter)
        return True if not stack else False




sol = Solution()

q = p = 1
for question in q_list:
    print(f"Q{q}) " +  f"{sol.isValid(question)}" + f" {q_list[q-1]}")
    q += 1

class Solution2():
    def isValid(self, s: str) -> bool:
        #edge case
        
        if len(s) % 2 == 1:
            return False
        if s == "":
            return True
        
        o_bracket = ("(", "[", "{") #use the index of the tuple to check 
        c_bracket = (")", "]", "}")
        stack = []

        for letter in s:
            if letter in c_bracket:
                if stack and o_bracket.index(stack[-1]) == c_bracket.index(letter):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(letter)
        return True if not stack else False


sol2 = Solution2()

print(" - - - - ")
for question in q_list:
    print(f"Q{p}) " +  f"{sol2.isValid(question)}" + f" {q_list[p-1]}")
    p += 1


# q01: "()",        Output: True
# q02: "()[]{}",    Output: True
# q03: "({[]})",    Output: True
# q04: "[()]{}",    Output: True
# q05: "{[}]",      Output: False
# q06: "({[})",     Output: False
# q07: "(]",        Output: False
# q08: "[",         Output: False
# q09: "]",         Output: False
# q10: "",          Output: True
# q11: "((",        Output: False
# q12: "))",        Output: False
# q13: "([]))",     Output: False
# q14: "{(})",      Output: False
# q15: "([)]",      Output: False
# q16: "{([])}",    Output: True
# q17: "{{{{}}",    Output: False
# q18: "(((({{))",  Output: False
# q19: "{[()]",     Output: False
# q20: "(())[]{}",  Output: True