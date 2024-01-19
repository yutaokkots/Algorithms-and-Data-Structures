"""931. Mininum Falling Path Sum."""

"""
931. Mininum Falling Path Sum.
Medium

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
    [[2,1,3],   <-  1       1   
     [6,5,4],   <-  5       4
     [7,8,9]]   <-  7       8
                    13      13
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

Example 2:
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
 
Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 100
    -100 <= matrix[i][j] <= 100
"""

from typing import List

class Solution:
    """First attempt at LC931, naive solution."""
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix)
        self.min_sum = 10000
        permutation: List[int] = []
        possibilities = ((1, -1), (1, 0), (1, 1))

        def backtrack(i, j):
            if i == rows and len(permutation) == rows and 0 <= j < cols:
                self.min_sum = min(self.min_sum, sum(permutation))
                return  
            if (i < 0 or i >= rows or j < 0 or j >= cols):
                return 
            permutation.append(matrix[i][j])
            for row, col in possibilities:
                backtrack(i + row, j + col)
            permutation.pop()
            for row, col in possibilities:
                backtrack(i + row, j + col)

        for k in range(cols):
            backtrack(0, k)

        return self.min_sum