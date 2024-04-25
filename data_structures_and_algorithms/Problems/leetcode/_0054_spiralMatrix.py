'''
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: 
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: 
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
'''

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """First attempt solution"""
        row, col= len(matrix), len(matrix[0])
        i, j = 0, 0
        visited = set()
        directions = ((0,1), (1,0), (0,-1), (-1,0))
        dir_index = 0   
        answer = [] 
        while (-1 < i < row and
                -1 < j < col and
                (i, j) not in visited):
            visited.add((i, j))
            answer.append(matrix[i][j])
            next_row = directions[dir_index][0] + i
            next_col = directions[dir_index][1] + j
            if (-1 < next_row < row and
                    -1 < next_col < col and
                    (next_row, next_col) not in visited):
                i = next_row
                j = next_col
            else:
                dir_index = (dir_index + 1) % 4
                i = directions[dir_index][0] + i
                j = directions[dir_index][1] + j
        return answer
    