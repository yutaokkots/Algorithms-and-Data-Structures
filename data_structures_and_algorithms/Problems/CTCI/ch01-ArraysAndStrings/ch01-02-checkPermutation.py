# given two strings, write a method to decide if one is a permutation of the other. 


questions = {
    "q1": ["seashell", "shellsea"],
    "q2": ["abba", "baab"],
    "q3": ["TAGCTA", "tagcta"],
    "q4": ["star", "rats"],
    "q5": ["neoph", "phones"],
    "q6": ["read", "deer"]
}

class Solution:
    def checkPermutation(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        str1 = list(str1.lower())
        str2 = list(str2.lower())
        str1.sort()
        str2.sort()
        return str1 == str2


sol = Solution()

for k, v in questions.items():
    answer = sol.checkPermutation(v[0], v[1])
    print(f"{k}: {answer}")