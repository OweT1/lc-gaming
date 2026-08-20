class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        distances = [[math.inf]*n for _ in range(n)]
        pq = [(grid[0][0], 0, 0)]

        res = grid[0][0]
        while pq:
            t, i, j = heapq.heappop(pq)
            res = max(res, t)
            distances[i][j] = res

            for dirctn in directions:
                new_i, new_j = i + dirctn[0], j + dirctn[1]

                if new_i == n-1 and new_j == n-1: return max(res, grid[n-1][n-1])
                if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n or distances[new_i][new_j] != math.inf: continue

                heapq.heappush(pq, (grid[new_i][new_j], new_i, new_j))

        return res
                
                
                
                
                
        