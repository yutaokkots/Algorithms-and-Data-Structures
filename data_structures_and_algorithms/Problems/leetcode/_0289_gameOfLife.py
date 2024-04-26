'''
289. Game Of Life
Medium

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. 
Given the current state of the m x n grid board, return the next state.

Example 1:
Input: 
    board = [[0,1,0],       [[0,0,0],
             [0,0,1], -->    [1,0,1],
             [1,1,1],        [0,1,1],
             [0,0,0]]        [0,1,0]]
Output: 
            [[0,0,0],
             [1,0,1],
             [0,1,1],
             [0,1,0]]

Example 2:
Input: 
    board = [[1,1],
             [1,0]]
Output: 
            [[1,1],
             [1,1]]

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 25
    board[i][j] is 0 or 1.
'''
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """First attempt solution."""
        directions = ((-1, -1), (-1,0), (-1, 1),
                (0, -1), (0, 1),
                (1, -1), (1,0), (1, 1))
        row, col = len(board), len(board[0])
        board_copy = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                count = 0
                curr_value = board[i][j]
                for r, c in directions:
                    if (-1 < i + r < row and
                            -1 < j + c < col and
                            board[i+r][j+c] == 1):
                        count += 1
                if curr_value == 0 and count == 3:
                    curr_value = 1
                elif (curr_value == 1 and 
                        count == 2 or count == 3):
                    curr_value = 1
                elif (curr_value == 1 and
                        count != 2 and count != 3):
                    curr_value = 0
                board_copy[i][j] = curr_value
                
        for i in range(row):
            for j in range(col):
                board[i][j] = board_copy[i][j]

    def gameOfLife2(self, board: List[List[int]]) -> None:
        """Second attempt solution with O(1) space complexity."""
        directions = ((-1,-1), (-1,0), (-1,1),
                        (0,-1), (0,1),
                        (1,-1), (1,0), (1,1))
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                count = 0
                for r, c in directions:
                    if (-1 < i+r < rows and
                            -1 < j+c < cols and
                            board[i+r][j+c] == 1 or
                            -1 < i+r < rows and
                            -1 < j+c < cols and
                            board[i+r][j+c] == 3):
                        count += 1
                curr_value = board[i][j]
                if (board[i][j] == 0 and
                    count == 3):
                    curr_value = 2
                elif (board[i][j] == 1 and count < 2 or 
                        board[i][j] == 1 and count > 3):
                    curr_value = 3
                board[i][j] = curr_value

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0

        # states:
        #       0: dead
        #       1: live
        #       2: dead -> live
        #       3: live -> dead

'''
Java Solution:

        class Solution {
            public void gameOfLife(int[][] board) {
                int row = board.length;
                int col = board[0].length;
                int[][] boardCopy = new int[row][col];
                for (int i = 0; i < row; i ++){
                    for (int j = 0; j < col; j++){
                        boardCopy[i][j] = 0;
                    }
                }
                int[][] directions = {
                        {-1,-1},{-1,0},{-1,1},
                        {0,-1},{0,1},
                        {1,-1},{1,0},{1,1}
                    };
                int dirIndex = 0;

                for (int i = 0; i < row; i++){
                    for (int j = 0; j < col; j++){
                        int count = 0;
                        for (int k = 0; k < directions.length; k++){
                            int r = directions[k][0] + i;
                            int c = directions[k][1] + j;
                            if (r > -1 && r < row && 
                                c > -1 && c < col && 
                                board[r][c] == 1){
                                    count ++;
                            }
                        }
                        int curr_cell = board[i][j];
                        if (curr_cell == 0 && count == 3){
                            curr_cell = 1;
                        } else if (curr_cell == 1 && count < 2 || 
                                curr_cell == 1 && count > 3){
                            curr_cell = 0;
                        } else if (curr_cell == 1 && count == 2 ||
                                curr_cell == 1 && count == 3){
                            curr_cell = 1;
                        }
                        boardCopy[i][j] = curr_cell;                
                    }
                }
                for (int i = 0; i < row; i++){
                    for (int j = 0; j < col; j++){
                        board[i][j] = boardCopy[i][j];
                    }
                }
            }
        }

'''