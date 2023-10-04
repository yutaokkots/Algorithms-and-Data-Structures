'''
79. Word Search
Medium

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

| A | B | C | E |
| S | F | C | S |
| A | D | E | E |

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
'''
from typing import List

class Solution1:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def backtrack(row, col, index):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[index]:
                return False
            if index == len(word) - 1:
                return True

            original_char, board[row][col] = board[row][col], "#"

            if (backtrack(row + 1, col, index + 1) or
                backtrack(row - 1, col, index + 1) or
                backtrack(row, col + 1, index + 1) or
                backtrack(row, col - 1, index + 1)):
                return True

            board[row][col] = original_char

            return False

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True

        return False

class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
            word[i] != board[r][c] or (r, c) in path):
                return False
            path.add((r, c))
            res = (backtrack(r + 1, c, i + 1) or
                    backtrack(r - 1, c, i + 1) or
                    backtrack(r, c + 1, i + 1) or
                    backtrack(r, c - 1, i + 1))
            path.remove((r, c))
            return res
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0): return True
        return False 

