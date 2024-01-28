"""1074. Number of Submatrices that Sum to Target"""

"""
1074. Number of Submatrices that Sum to Target
Hard

Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

Example 1:
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
    [[0,1,0],
     [1,1,1],
     [0,1,0]]
     
Example 2:
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
    [[ 1,-1],
     [-1, 1]]

Example 3:
Input: matrix = [[904]], target = 0
Output: 0
    [[904]]

Constraints:
    1 <= matrix.length <= 100
    1 <= matrix[0].length <= 100
    -1000 <= matrix[i] <= 1000
    -10^8 <= target <= 10^8

"""
from typing import List
from collections import defaultdict

class Solution:
    """Solution class adapted from user @nitanshritulon"""
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range (1, n):
                matrix[i][j] += matrix[i][j - 1]
            matrix[i] = [0] + matrix[i]
        answer = 0
        memo = defaultdict(int)
        for col_01 in range(n):
            for col_02 in range(col_01 + 1, n + 1):
                temp = 0
                memo[0] = 1
                for row in range(m):
                    temp += matrix[row][col_02] - matrix[row][col_01]
                    if temp - target in memo:
                        answer += memo[temp - target]
                    memo[temp] += 1
                memo.clear()
        return answer 