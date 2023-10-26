'''
String Rearrangement


Given an array of equal-length strings, check if it is possible to rearrange the strings in such a way that after the rearrangement the strings at consecutive positions would differ by exactly one character.

Example 1:

For inputArray = ["aba", "bbb", "bab"], the output should be stringsRearrangement(inputArray) = false;
All rearrangements dont satisfy the description condition.

    There are 6 possible arrangements for these strings:

    ["aba", "bbb", "bab"]
    ["aba", "bab", "bbb"]
    ["bbb", "aba", "bab"]
    ["bbb", "bab", "aba"]
    ["bab", "bbb", "aba"]
    ["bab", "aba", "bbb"]
    
    None of these satisfy the condition of consecutive strings differing by 1 character

Example 2:

For inputArray = ["ab", "bb", "aa"], the output should be stringsRearrangement(inputArray) = true.
Strings can be rearranged in the following way: "aa", "ab", "bb".

'''

def solution(inputArray):
    result = [False]
    answer = []
    
    def backtrack():
        for i in range(len(inputArray)):
            if result[0]:
                break
            answer.append(inputArray.pop(i))
            if len(inputArray) == 0:
                result[0] = result[0] or solution()
            else:
                backtrack()
            inputArray.insert(i, answer.pop())                  
            
    def solution():
        for i in range(len(answer) - 1):
            difference = 0
            for j in range(len(answer[i])):
                if answer[i][j] != answer[i + 1][j]:
                    difference += 1
            if difference != 1:
                return False
        return True
        
    backtrack()
    return result[0]