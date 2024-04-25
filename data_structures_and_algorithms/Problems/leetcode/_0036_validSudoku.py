'''
36. Valid Sudoku
Medium

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

'''

from typing import List
import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create a function that checks a Sudoku board is valid
        # input, 'board' is a list of list
        # check for validity (1-9 without repetition)
        #   - columns
        #   - rows
        #   - sub-boards of 3 x 3 cells

        # check that values within range of 1-9 is not repeated
        # pattern:
        # [0-2][3-5][6-8] index, i
        # [0-2][3-5][6-8] index, j

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)

        DICT_KEY = {
            0: "A",
            1: "A",
            2: "A",
            3: "B",
            4: "B",
            5: "B",
            6: "C",
            7: "C",
            8: "C"
        }

        dict_board = {
        }

        def validator(input_list):
            check_dict = {}
            for n in input_list:
                if n != ".": 
                    if n not in check_dict.keys():
                        check_dict[n] = 1
                    else:
                        return False
            return True

        def validator_2(input_list):
            return len(set(input_list)) != len(input_list)

        # nested for-loop to go through each row
        for row_idx, row_list in enumerate(board):
            if not validator(row_list):
                return False
            for col_idx, val in enumerate(row_list):
                ## following creates a dict_board with values of sub-boards
                if val == ".":
                    continue
                if f"i{DICT_KEY[row_idx]}j{DICT_KEY[col_idx]}" not in dict_board.keys():
                    dict_board[f"i{DICT_KEY[row_idx]}j{DICT_KEY[col_idx]}"] = []
                dict_board[f"i{DICT_KEY[row_idx]}j{DICT_KEY[col_idx]}"].append(val)
                ## add to dict_board, and add values for the columns
                # 'colA: []'
                if f"col{col_idx}" not in dict_board.keys():
                    dict_board[f"col{col_idx}"] = []
                dict_board[f"col{col_idx}"].append(val)


        for val in dict_board.values():
            print(val)
            if not validator_2(val):
                print('false')
                return False
            else:
                print('true')

        return True
    
    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        dict_sets = collections.defaultdict(set)
        dict_ints = collections.defaultdict(int)
        centers = ((1, 1), (1, 4), (1, 7), 
                (4, 1), (4, 4), (4, 7), 
                (7, 1), (7, 4), (7, 7))
        circle = ((-1,-1), (-1, 0), (-1,1),
                (0,-1), (0,0), (0,1),
                (1,-1), (1,0), (1,1))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    dict_sets[f"row{i}"].add(board[i][j])
                    dict_ints[f"row{i}"] += 1
                    dict_sets[f"col{j}"].add(board[i][j])
                    dict_ints[f"col{j}"] += 1
                if (i, j) in centers:
                    for x, y in circle:
                        if board[i + x][j + y] != ".":
                            dict_sets[f"box{i}{j}"].add(board[i + x][j + y])
                            dict_ints[f"box{i}{j}"] += 1             
             
        for key in dict_sets.keys():
            if len(dict_sets[key]) != dict_ints[key]:
                return False

        return True
    
    def isValidSudoku3(self, board: List[List[str]]) -> bool:
        result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val != ".":
                    result += [(i, val), 
                            (val, j), 
                            (i//3, j//3, val)]
        return len(result) == len(set(result))