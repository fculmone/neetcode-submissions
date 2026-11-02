class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        visited = set()
        island_count = 0

        def dfs(r, c):
            if ((r, c) in visited or 
                r < 0 or r >= num_rows or
                c < 0 or c >= num_cols or
                grid[r][c] == "0"):
                return
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(num_rows):
            for c in range(num_cols):
                if ((r, c) not in visited) and (grid[r][c] == "1"):
                    island_count += 1
                    dfs(r, c)
        return island_count