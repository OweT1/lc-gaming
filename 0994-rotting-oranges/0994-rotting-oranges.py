class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, rotten = [], set()
        rows, cols = len(grid), len(grid[0])
        visited = [[0]*cols for _ in range(rows)]
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh.append((r,c))
                elif grid[r][c] == 2:
                    rotten.add((r,c))
        
        if len(fresh) == 0:
            return 0
        if len(rotten) == 0:
            return -1

        while rotten:
            new_rotten = set()
            has_visits = False
            for t_r, t_c in rotten:
                if not visited[t_r][t_c]:
                    has_visits = True
                    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    for d in directions:
                        n_r, n_c = t_r + d[0], t_c + d[1]
                        if (
                            n_r >= 0 and
                            n_r < rows and
                            n_c >= 0 and
                            n_c < cols and
                            not visited[n_r][n_c] and
                            grid[n_r][n_c] == 1
                        ):
                            new_rotten.add((n_r, n_c))
                    visited[t_r][t_c] = 1
            rotten = new_rotten
            if has_visits: # only add time if there were additional visits
                time += 1
        
        for r, c in fresh:
            if visited[r][c] == 0:
                return -1
        return time-1


        