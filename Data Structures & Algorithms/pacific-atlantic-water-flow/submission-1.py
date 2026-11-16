class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        can_reach_pacific = set()
        can_reach_atlantic = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        borders_pacific = []
        borders_atlantic = []
        flows_to_pacific = set()
        flows_to_atlantic = set()

        def dfs(r, c, flows_to):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or 
                (r, c) in flows_to 
            ):
                return
            flows_to.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    heights[r][c] <= heights[nr][nc]
                ):
                    dfs(nr, nc, flows_to)
        for r in range(ROWS):
            dfs(r, 0, flows_to_pacific)
            dfs(r, COLS - 1, flows_to_atlantic)
        for c in range(COLS):
            dfs(0, c, flows_to_pacific)
            dfs(ROWS - 1, c, flows_to_atlantic)

        return list(flows_to_pacific.intersection(flows_to_atlantic))