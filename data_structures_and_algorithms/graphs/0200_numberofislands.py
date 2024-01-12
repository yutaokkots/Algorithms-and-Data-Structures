# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

import collections

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # Input: grid = [
        #     ["1","1","1","1","0"],
        #     ["1","1","0","1","0"],
        #     ["1","1","0","0","0"],
        #     ["0","0","0","0","0"]
        # ]
        #
        # how do we mark the island, "1", as visited?
        # Breadth-first-search / graph traversal algorithm
        #
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        # mark where we have visited
        visit = set()
        islands = 0

        # breadth first search is not recursive, it is cumulative
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
    

island_map_1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

sol = Solution()
answer = sol.numIslands(island_map_1)
print(answer)