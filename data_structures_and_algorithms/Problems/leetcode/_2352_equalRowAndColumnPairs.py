"""2352. Equal Row and Column Pairs"""

"""
2352. Equal Row and Column Pairs
Medium


Medium

Topics
Companies

Hint
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

Constraints:
    n == grid.length == grid[i].length
    1 <= n <= 200
    1 <= grid[i][j] <= 10^5
"""
from typing import List
from collections import defaultdict

class Solution:
    """Solution for LC2352"""
    def equalPairs(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        hash_table_row = defaultdict(int)
        hash_table_col = defaultdict(int)

        for i in range(row):
            lst_idx = grid[i]
            str_r = "-".join([str(int_idx) for int_idx in lst_idx])
            hash_table_row[str_r] += 1
        for j in range(col):
            lst_col = []
            for i in range(row):
                lst_col.append(str(grid[i][j]))
            str_c = "-".join(lst_col)
            hash_table_col[str_c] += 1
        set_row = set(hash_table_row.keys())
        set_col = set(hash_table_col.keys())
        union = set_row & set_col

        answer = 0
        for shared in union:
            r_val = hash_table_row[shared] 
            c_val = hash_table_col[shared] 
            if (r_val > 0 and 
                    c_val > 0):
                answer += (r_val * c_val)

        return answer