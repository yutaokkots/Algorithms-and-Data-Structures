'''
200. Number of Islands
Medium



--
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 
--
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

'''
from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        # mark where we have visited
        visit = set()
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visit:
                    bfs(row, col)
                    islands += 1
        return islands
    

class Solution2:
    def numIslandsDFS1(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        
        visit = set()
        islands = 0

        def dfs(r, c):
            if grid[r][c] == "0" or (r,c) in visit:
                return
            visit.add((r, c))
            if 0 <= r + 1 < rows and 0 <= c < cols:
                dfs(r + 1, c)
            if 0 <= r - 1 < rows and 0 <= c < cols:
                dfs(r - 1, c)
            if 0 <= r < rows and 0 <= c + 1 < cols:
                dfs(r, c + 1)
            if 0 <= r < rows and 0 <= c - 1 < cols:
                dfs(r, c - 1)

        for row in range(rows):
            for col in range(cols):
                if (grid[row][col] == "1" and (row, col) not in visit):
                    dfs(row, col)
                    islands += 1

        return islands
    
    def numIslandsDFS1(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if ((r, c) in visited or grid[r][c] == "0"):
                return
            visited.add((r, c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row in range(rows) and 
                    col in range(cols) and 
                    (row,col) not in visited and
                    grid[row][col] == "1"):
                    dfs(row, col)

        for row in range(rows):
            for col in range(cols):
                if (grid[row][col] == "1" and (row, col) not in visited):
                    dfs(row, col)
                    islands += 1
        return islands
