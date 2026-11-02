class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        starting_fruits = []
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    starting_fruits.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        def bfs(): 
            nonlocal time, fresh
            queue = deque(starting_fruits) 
            while queue and fresh > 0:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for cr, cc in directions:
                        nr = r + cr
                        nc = c + cc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            queue.append((nr, nc))
                            fresh -= 1
                time += 1
        bfs()

        return time if fresh == 0 else -1