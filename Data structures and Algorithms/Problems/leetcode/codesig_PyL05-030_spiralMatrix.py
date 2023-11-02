'''
Spiral Matrix


A spiral matrix is a square matrix of size n x n. It contains all the integers in range from 1 to n * n so that number 1 is written in the bottom right corner, and all other numbers are written in increasing order spirally in the counterclockwise direction.

Given the size of the matrix n, your task is to create a spiral matrix.

Example

For n = 3, the output should be

solution(n) = [[5, 4, 3],
               [6, 9, 2],
               [7, 8, 1]]
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

Matrix size, a positive integer.

Guaranteed constraints:
3 ≤ n ≤ 75.

[output] array.array.integer

A spiral matrix of size n.

'''

def solution(n):
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    curDir = 0
    curPos = (n - 1, n - 1)
    res = [[0] * n for _ in range(n)] # '[[0] * n ] * n' is incorrect: creates a list of lists with the same reference

    for i in range(1, n * n + 1):
        res[curPos[0]][curPos[1]] = i
        nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        if not (0 <= nextPos[0] < n and
                0 <= nextPos[1] < n and
                res[nextPos[0]][nextPos[1]] == 0):
            curDir = (curDir + 1) % 4
            nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        curPos = nextPos

    return res

for i in range(6):
    print(solution(i))

# 0: []
# 1: [[1]]
# 2: [[3, 2], 
#     [4, 1]]
# 3: [[5, 4, 3], 
#     [6, 9, 2], 
#     [7, 8, 1]]
# 4: [[ 7,  6,  5, 4], 
#     [ 8, 15, 14, 3], 
#     [ 9, 16, 13, 2], 
#     [10, 11, 12, 1]]
# 5: [[ 9,  8,  7,  6, 5], 
#     [10, 21, 20, 19, 4], 
#     [11, 22, 25, 18, 3], 
#     [12, 23, 24, 17, 2], 
#     [13, 14, 15, 16, 1]]

