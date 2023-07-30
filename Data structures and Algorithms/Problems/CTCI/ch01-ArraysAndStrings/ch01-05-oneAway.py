# One Away: There are three types of edits that can be performed on strings.
# insert a character, 
# remove a character,
# replace a character.
# given two strings, write a function to check if they are one edit (or zero edits) away.

questions = {
    "q1": ["pale", "ple"],
    "q2": ["pales", "pale"],
    "q3": ["pale", "bale"],
    "q4": ["pale", "bake"],
    "q5": ["pale", "pale"],
    "q6": ["pale", "ale"]
}

class Solution:
    def oneAway(self, str1: str, str2: str) -> bool:
        pass


sol = Solution()
for k, v in questions.items():
    answer = sol.oneAway(v[0], v[1])
    print(f"{k}: {v[0]}, {v[1]} -> {answer}")