"""Using a for-loop over a zip().

Looking at the use of zip() as an interable for a for-loop.
This question is inpsired by LC-2352, "Equal Row and Column Pairs."

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 2:
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
"""
from typing import List
from collections import Counter

###########################
######## EXAMPLE 1 ########

grid1 = [[3,1,2,2],
         [1,4,4,5],
         [2,4,2,2],
         [2,4,2,2]]

def equalColAndRow(grid: List[List[int]]) -> int:
    row_ct = Counter(tuple(row) for row in grid)

    print(row_ct)
    # row_ct =  {(2, 4, 2, 2): 2, 
    #            (3, 1, 2, 2): 1, 
    #            (1, 4, 4, 5): 1 }

    for tup in zip(*grid):  #<- this '*' is a 'splate operator'. 
        print(tup)
    # (3, 1, 2, 2)
    # (1, 4, 4, 4)
    # (2, 4, 2, 2)
    # (2, 5, 2, 2)

equalColAndRow(grid1)

###########################
######## EXAMPLE 2 ########

grid2 = [["A","A","A","A"],
         ["B","B","B","B"],
         ["C","C","C","C"],
         ["D","D","D","D"]]

grid2_transposed = list(zip(*grid2))

print(grid2_transposed)

# grid2_transposed = 
#       [('A', 'B', 'C', 'D'), 
#        ('A', 'B', 'C', 'D'), 
#        ('A', 'B', 'C', 'D'), 
#        ('A', 'B', 'C', 'D')]