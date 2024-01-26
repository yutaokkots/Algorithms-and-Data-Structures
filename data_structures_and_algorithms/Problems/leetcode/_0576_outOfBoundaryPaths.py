"""576. Out of Boundary Paths"""

"""
576. Out of Boundary Paths
Medium

There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

Example 1:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12

Constraints:
    1 <= m, n <= 50
    0 <= maxMove <= 50
    0 <= startRow < m
    0 <= startColumn < n
"""

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        modulo = 10**9 + 7
        memo = {}

        def recursive(x: int, y: int, move:int) -> int:
            if move > maxMove:
                return 0
            if (x not in range(m) or
                    y not in range(n)):
                return 1
            if (x, y, move) in memo:
                return memo[(x, y, move)] % modulo
            memo[(x, y, move)] = recursive(x, y - 1, move + 1) + recursive(x - 1, y, move + 1) + recursive(x, y + 1, move + 1) + recursive(x + 1, y, move + 1)

            return memo[(x,y,move)] % modulo
        return recursive(startRow, startColumn, 0) % modulo