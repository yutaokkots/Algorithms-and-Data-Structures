# implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

class Solution:
    def isUnique(self, input_string:str) -> bool:
        # naive solution
        dct = {}
        for letter in input_string:
            if letter not in dct.keys():
                dct[letter] = 1
            else:
                return False
        return True
    
    def isUnique2(self, input_string:str) -> bool:
        # using a set
        new_set = "".join((set(input_string)))
        return len(new_set) == len(input_string)


test_strings = ["abcdefgh", "mamamia", "que paso","que pasa"]
# expected: True, False, True, False

sol = Solution()
answer = []
answer2 = []
for test in test_strings:
    answer.append(sol.isUnique(test))
    answer2.append(sol.isUnique2(test))
print(answer)
print(answer2)

