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
    """Dynamic Programming solution, via user @prodonik"""
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1:
            return matrix[0][0]
        rows = cols = len(matrix)
        dp = [[0] * rows for _ in range(rows)]
        dp = matrix.copy()
        result = 100000

        for i in range(rows - 2, -1, -1):
            for j in range(cols):
                min_path = dp[i + 1][j]
                if j > 0:
                    min_path = min(min_path, dp[i + 1][j - 1])
                if j < cols - 1:
                    min_path = min(min_path, dp[i + 1][j + 1])
                dp[i][j] += min_path
                
        for num in dp[0]:
            result = min(result, num)
        
        return result

class Solution2:
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
    
matrix = [[36,62,4,57,-62,57,-11,52,-9,58],[-85,-92,87,-3,81,89,33,14,-57,-82],[64,78,56,40,-16,-39,-78,-15,13,85],[88,-17,-81,55,47,-94,-11,37,-94,84],[93,45,-85,-86,-28,-95,-31,-98,95,64],[-86,79,-59,-59,35,88,-76,-99,-26,-96],[21,72,-63,-78,-31,92,-74,94,-28,-5],[-42,88,92,27,-64,99,-80,16,-69,80],[90,61,-37,-52,51,-42,-16,-91,-74,-96],[-85,-86,-16,10,48,-72,-16,28,-84,-11]]

sol = Solution()
a = sol.minFallingPathSum(matrix)
print(a)