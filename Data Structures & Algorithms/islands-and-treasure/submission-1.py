
INF = 2147483647

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        NUM_ROWS, NUM_COLS = len(grid), len(grid[0])
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]
        queue = deque([])
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
        level = 0 
        while queue:
            level += 1
            for _ in range(len(queue)):
                r, c = queue.popleft() 
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (
                        0 <= nr < NUM_ROWS and
                        0 <= nc < NUM_COLS and
                        grid[nr][nc] == INF
                    ):
                        grid[nr][nc] = level
                        queue.append((nr, nc))


