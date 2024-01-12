# Given a string, write a function to check to see if it is a permutation of a palindrome
# Example
# input: "Tact Coa"
# output: True
#       permuations-> "taco cat", "atco cta" are palindromes

questions = {
    "q1": "Tact Coa",
    "q2": "raarcce",
    "q3": "raarccet",

}

class Solution:
    def palindrome_permutation(self, phrase:str) -> bool:
        phrase_lst = list(phrase)
        memo = {}
        for n in phrase_lst:
            if not n.isalnum():
                continue
            n = n.lower()
            if n not in memo.keys():
                memo[n] = 1
            else:
                memo[n] += 1
        odd = 0
        print(memo)
        for v in memo.values():
            if v % 2 != 0:
                odd += 1
            if odd > 1:
                return False
        return True

str1 = "Tact Coa"

sol = Solution()
for k, v in questions.items():
    answer = sol.palindrome_permutation(v)
    print(f"{k}: {v} -> {answer}")   
