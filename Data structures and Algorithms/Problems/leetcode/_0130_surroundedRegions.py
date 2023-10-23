'''
130. Surrounded Regions
Medium

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:

Input: board = [["X"]]
Output: [["X"]]
'''
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        o_s = set()
        def dfs(r, c, visited):
            if (r not in range(rows) or
                    c not in range(cols) or
                    board[r][c] == "X" or
                    (r, c) in visited):
                return 

            visited.add((r,c))
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col, visited)

        for row in range(rows):
            dfs(row, 0, o_s)
            dfs(row, cols-1, o_s)
        for col in range(cols):
            dfs(0, col, o_s)
            dfs(rows-1, col, o_s)

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in o_s and board[row][col] == "O":
                    board[row][col] = "X"