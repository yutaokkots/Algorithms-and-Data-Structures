'''
73. Set Matrix Zeroes
Medium
=
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
Constraints:
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -2^31 <= matrix[i][j] <= 2^31 - 1
'''

class Solution(object):
    def setZeroes(self, matrix):
        """First attempt solution."""

        row, col = len(matrix), len(matrix[0])
        zero_row_set = set()
        zero_col_set = set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zero_row_set.add(i)
                    zero_col_set.add(j)
        
        for i in range(row):
            for j in range(col):
                if i in zero_row_set:
                    matrix[i][j] = 0
                if j in zero_col_set:
                    matrix[i][j] = 0
