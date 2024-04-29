''' 
909. Snakes and Ladders
Medium

You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.

Example 1:
Input: 
    board = [[-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,35,-1,-1,13,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.

Example 2:
Input: board = [[-1,-1],[-1,3]]
Output: 1
 

Constraints:
    n == board.length == board[i].length
    2 <= n <= 20
    board[i][j] is either -1 or in the range [1, n2].
    The squares labeled 1 and n2 do not have any ladders or snakes.
'''
from typing import List
from collections import defaultdict, deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        def find_position(row, col, n):
            board_size = n**2 
            curr_row = n * row
            max_row = board_size - curr_row
            position = 0
            row_dir = n - row - 1
            # ascending row (odds)
            if row_dir % 2 == 0:
                position = max_row - (n - col - 1) 
            # descending row (evens)
            else:
                position = max_row - col
            return position

        n = len(board)
        graph = defaultdict(int)
        for i in range(n):
            for j in range(n):
                if board[i][j] != -1:
                    position = find_position(i, j, n)
                    graph[position] = board[i][j]

        q = deque() #(curr_position, count)
        q.append((1, 0)) 
        visited = set()
        visited.add(1)

        print(graph)
        while q:
            curr_pos, count = q.popleft()

            dice_roll = min(n**2 + 1, curr_pos + 7)
            if curr_pos >= n**2:
                return count
            for next_pos in range(curr_pos + 1, dice_roll):
                if next_pos in graph.keys():
                    next_pos = graph[next_pos]
                if next_pos not in visited:
                    visited.add(next_pos)
                    q.append((next_pos, count + 1))
        
        return -1