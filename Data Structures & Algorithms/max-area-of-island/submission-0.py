class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        max_area = 0
        curr_area = 0
        def dfs(r, c):
            nonlocal curr_area, max_area
            if (r < 0 or r >= num_rows or 
                c < 0 or c >= num_cols or
                grid[r][c] == 0):
                return
            grid[r][c] = 0
            curr_area += 1
            max_area = max(max_area, curr_area) 
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1:
                    curr_area = 0
                    dfs(r, c)
        return max_area