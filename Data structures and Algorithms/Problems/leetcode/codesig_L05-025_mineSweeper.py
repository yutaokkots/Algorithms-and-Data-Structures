'''
Mine Sweeper

In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example 1:
matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
solution(matrix) = [[1, 2, 1],
                    [2, 1, 1],
                    [1, 1, 1]]

Example 2:
matrix = 
 [[true, false,false,true], 
 [false,false,true, false], 
 [true, true, false,true]]
 
solution(matrix) = 
 [[0, 2, 2, 1]
 [3, 4, 3  3]
 [1, 2, 3, 1]]
'''

def solution(matrix):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1,-1),(-1,0),(-1,1),
                (0,-1),(0,1),
                (1,-1),(1,0),(1,1)]
    solution = []   
    for row in range(rows):
        grid_row = []
        for col in range(cols):
            mine_count = 0
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r not in range(rows) or
                    c not in range(cols)):
                    continue
                if matrix[r][c] == True:
                    mine_count += 1
            grid_row.append(mine_count)
        solution.append(grid_row)
        
    return solution
     