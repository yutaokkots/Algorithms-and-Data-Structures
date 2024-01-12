# notes from leetcode problem 2381

# Given an initial string, 's', and the directions for shift, 'shifts'
# where 'shifts' comprises an array of arrays, 
# where each subarray includes [start_index, end_index, backward/forward]
# where start_index and end_index are inclusive
# and backward/forward is binary, where backward is 0, forward is 1
#
# example 1:
# s = 'abc'
# shifts = [[0,1,0],[1,2,1],[0,2,1]]
# example 2:
# s = 'blue'
# shifts = [[0,1,0],[1,3,1],[0,2,1],[1,1,0]]
#
# How to best record the shfits in the string? 

s = 'blue'
shifts = [[0,1,0],[1,3,1],[0,2,1],[1,1,0]]
str_length = len(s) + 1
record = [0] * str_length #create a list with number of elements 1 greater than 
#                           length of string, 's'

for start, end, direction in shifts:
    if direction == 0:
        record[start] -= 1
        record[end+1] += 1
    else:
        record[start] += 1
        record[end+1] -= 1
    print(record)
# record after each iteration:   
#     [ 0, 0, 0,  0,  0]
#     [-1, 0, 1,  0,  0]
#     [-1, 1, 1,  0, -1]
#     [ 0, 1, 1, -1, -1]
#     [ 0, 0, 2, -1, -1]

cumulative_sum = 0
for i in range(len(s)):
    cumulative_sum += record[i]
    print(cumulative_sum)
# cumulative_sum over the iteration:
# 0
# 0
# 2
# 1

# how does the 'record' variable, 
# translate to the 'cumulative_sum' containing the number of elements to shift?

# this works because when each index, 'i' in the word, 's', is iterated over in the
# second part of the algorithm, 
# the 'cumulative_sum' keeps track of how to move the current index as well as the
# subsequent index, AS LONG AS the change in the index (+ or -) is not negated
# by the end index. 