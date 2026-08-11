class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        1. what makes a node valid: value of '1'
        2. directions: horizontal left/right/up/down
        3. need to find cell to start (loop thru)
        4. dfs
        5. visited set for island valid ones seen
        6. explore neighbor cells
        '''

        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        rows = range(len(grid))
        cols = range(len(grid[0]))

        num_islands = 0

        seen = set()

        def dfs(r, c):
            queue = collections.deque([(r,c)])
            
            while queue:
                r, c = queue.popleft()
                

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (0 <= nr < len(grid) and
                        0 <= nc < len(grid[0]) and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in seen):
                        seen.add((nr, nc))
                        queue.append((nr, nc))

        for r in rows:
            for c in cols:
                if grid[r][c] == '1' and (r, c) not in seen:
                    seen.add((r,c))
                    dfs(r, c)
                    num_islands += 1

        return num_islands
