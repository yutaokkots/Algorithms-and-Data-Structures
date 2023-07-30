# write a method to replace all spaces in a string with '%20':
# you may assume that the string has sufficient space at the end to hold the additional characters, 
# and that you are given the "true" length of the string. 

# Example:

# input =  "Mr John Smith      " 13
# output = "Mr%20John%20Smith"

questions = {
    "q1" :  "Mr John Smith      ",
    "q2" :  "I'm Never Gonna Give You Up",
    "q3" :  "    panda jackson  ",
}

class Solution():
    def urlify(self, test_string: str) -> str:
        trimmed_str = test_string.strip().split()
        return "%20".join(trimmed_str)


sol = Solution()
for k, q in questions.items():
    answer = sol.urlify(q)
    print(answer)