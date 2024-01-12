'''
17. Letter Combinations of a Phone Number
Medium

'''
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keys = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        answer = []

        def backtrack(i, permutation):
            if len(digits) == len(permutation):
                answer.append("".join(permutation))
                return

            curr_number = int(digits[i]) - 2
            choices = keys[curr_number]
            for letter in choices:
                backtrack(i + 1, permutation + [letter])

        if digits:
            backtrack(0, [])
        return answer
    
class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        keys = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        answer = []

        def backtrack(i, permutation):
            if len(digits) == len(permutation):
                answer.append("".join(permutation))
                return
            key_choices = keys[digits[i]]
            for k in key_choices:
                backtrack(i + 1, permutation + [k])

        if digits:
            backtrack(0, [])

        return answer
    

sol = Solution()
answer = sol.letterCombinations("2223218632")
print(answer)

## time complexity = O(n * 4^n)
print(len(answer))