'''
All Longest Strings

Given an array of strings, return another array containing all of its longest strings.

Example 1:
input: ["aba", "aa", "ad", "vcd", "aba"]
output: ["aba", "vcd", "aba"]
'''

def solution(inputArray):
    sorted_input = sorted(inputArray, key=lambda n: len(n), reverse=True)
    size = len(sorted_input[0])
    answer = []
    for word in sorted_input:
        if len(word) != size:
            break
        answer.append(word)
    return answer