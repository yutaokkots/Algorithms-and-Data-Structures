'''
avoid obstacles

You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
solution(inputArray) = 4.
'''

def solution(inputArray):
    max_val = max(inputArray) + 2
    for i in range(1, max_val):
        jump = True
        for j in inputArray:
            if j % i == 0:
                jump = False
                
        if jump:
            return i

# @andrew_pudge
def solution2(inputArray): 
    c = 2
    while True:
        if sorted([i % c for i in inputArray])[0] > 0:
            return c
        c += 1