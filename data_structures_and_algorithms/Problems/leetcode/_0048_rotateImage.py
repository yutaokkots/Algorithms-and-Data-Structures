"""48. Rotate Image."""

"""
48. Rotate Image.
Medium

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 
Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000
"""
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        for i in range(rows):
            for j in range(i):  # ensure that it reaches index i
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                # temp = matrix[j][i]
                # matrix[j][i] = matrix[i][j]
                # matrix[i][j] = temp
        for i in range(rows):
            matrix[i].reverse()
        return matrix

    def rotate2(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        visited = set()

        for i in range(row):
            for j in range(col):
                if (i, j) not in visited:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                visited.add((i,j))
                visited.add((j,i))
        visited.clear()
        for i in range(row):
            for j in range(col):
                refl_j = col - 1 - j
                if (i, j) not in visited:
                    matrix[i][j], matrix[i][refl_j] = matrix[i][refl_j], matrix[i][j]
                visited.add((i, j))
                visited.add((i, refl_j))